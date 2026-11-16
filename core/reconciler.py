"""
Idempotent Reconciler for Alamia-Skills-System.
Takes the discovered state, creates/updates .alamia/project.json,
and reconciles lifecycle skills in .agents/skills without destructive overwrites.
"""
from pathlib import Path
from typing import Any, Dict
import json
import re
import shutil
import subprocess
import sys


def _load_vendor_dependency(system_root: Path, name: str) -> Dict[str, Any] | None:
    """Load a pinned vendor entry; never infer a moving branch or tag."""
    manifest_path = system_root / "vendor" / "UPSTREAMS.json"
    if not manifest_path.is_file():
        return None
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1:
        raise ValueError("Unsupported vendor provenance manifest schema.")
    dependencies = manifest.get("dependencies", [])
    if not isinstance(dependencies, list):
        raise ValueError("Vendor provenance dependencies must be a list.")
    dependency = next(
        (item for item in dependencies if isinstance(item, dict) and item.get("name") == name),
        None,
    )
    if dependency is None:
        return None
    commit_sha = dependency.get("commit_sha", "")
    source = dependency.get("source", "")
    if not re.fullmatch(r"[0-9a-f]{40}", commit_sha, flags=re.IGNORECASE):
        raise ValueError(f"Vendor dependency {name!r} has no immutable 40-character commit SHA.")
    if not isinstance(source, str) or not source.startswith("https://github.com/"):
        raise ValueError(f"Vendor dependency {name!r} has an invalid GitHub source URL.")
    return dependency


def _clone_pinned_repository(source: str, target: Path, commit_sha: str) -> None:
    """Clone and verify one immutable commit; clean up incomplete clones on failure."""
    if not re.fullmatch(r"[0-9a-f]{40}", commit_sha, flags=re.IGNORECASE):
        raise ValueError("Refusing to clone a vendor repository without an immutable commit SHA.")
    if target.exists():
        raise FileExistsError(f"Vendor target already exists and will not be overwritten: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            ["git", "clone", "--no-checkout", source, str(target)],
            check=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(
            ["git", "-C", str(target), "fetch", "--depth", "1", "origin", commit_sha],
            check=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(
            ["git", "-C", str(target), "checkout", "--detach", commit_sha],
            check=True,
            capture_output=True,
            text=True,
        )
        actual_sha = subprocess.run(
            ["git", "-C", str(target), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        if actual_sha.lower() != commit_sha.lower():
            raise RuntimeError(
                f"Vendor checkout SHA mismatch: expected {commit_sha}, got {actual_sha}."
            )
    except Exception:
        shutil.rmtree(target, ignore_errors=True)
        raise

try:
    from .engine import ProjectStateEngine, CORE_LIFECYCLE_GROUPS
except ImportError:
    from pathlib import Path
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from engine import ProjectStateEngine, CORE_LIFECYCLE_GROUPS


class ProjectReconciler:
    """Reconciles the project's Alamia configuration and lifecycle skills."""

    def __init__(self, project_root: Path = None):
        self.project_root = (project_root or Path.cwd()).resolve()
        self.engine = ProjectStateEngine(self.project_root)
        self.system_root = Path(__file__).resolve().parent.parent

    def reconcile(self) -> Dict[str, Any]:
        """Perform idempotent reconciliation."""
        state = self.engine.inspect()
        actions_taken = []

        # 1. Ensure .alamia/ directory and write .alamia/project.json
        alamia_dir = self.project_root / ".alamia"
        alamia_dir.mkdir(exist_ok=True)
        config_path = alamia_dir / "project.json"

        profile = {
            "schema_version": 1,
            "system_version": "0.2.0",
            "project_name": state["project_name"],
            "stack": state["stack"],
            "testing": state["testing"],
            "memory": {
                "has_memory_system": state["memory"]["has_memory_system"],
                "handoff_dir": state["memory"]["handoff_dir"],
                "architecture_dir": state["memory"]["architecture_dir"],
                "worklogs": state["memory"]["worklogs"],
                "latest_handoff_file": (
                    state["memory"]["latest_handoff"]["file"]
                    if state["memory"]["latest_handoff"]
                    else None
                ),
            },
            "lifecycle": {
                "groups": CORE_LIFECYCLE_GROUPS,
            },
        }

        # Check if profile changed or is new
        existing_profile_str = config_path.read_text(encoding="utf-8") if config_path.exists() else None
        existing_profile = {}
        profile_needs_backup = False
        if existing_profile_str:
            try:
                parsed = json.loads(existing_profile_str)
                if isinstance(parsed, dict):
                    existing_profile = parsed
                else:
                    profile_needs_backup = True
                    actions_taken.append("Notice: existing .alamia/project.json was not an object; preserving it before repair.")
            except json.JSONDecodeError:
                profile_needs_backup = True
                actions_taken.append("Notice: existing .alamia/project.json was invalid JSON; preserving it before repair.")

        # Preserve user-owned top-level and nested keys. Refresh only fields owned by discovery.
        merged_profile = dict(existing_profile)
        for key, value in profile.items():
            if isinstance(value, dict) and isinstance(existing_profile.get(key), dict):
                merged_profile[key] = {**existing_profile[key], **value}
            else:
                merged_profile[key] = value
        new_profile_str = json.dumps(merged_profile, indent=2)

        if existing_profile_str != new_profile_str:
            if existing_profile_str and profile_needs_backup:
                backup_path = config_path.with_suffix(".json.bak")
                if not backup_path.exists():
                    backup_path.write_text(existing_profile_str, encoding="utf-8")
                    actions_taken.append("Preserved the previous project profile at .alamia/project.json.bak.")
            config_path.write_text(new_profile_str, encoding="utf-8")
            actions_taken.append("Updated .alamia/project.json while preserving user-managed settings.")
        else:
            actions_taken.append(".alamia/project.json is already up to date.")

        # 2. Reconcile Lifecycle Skills in .agents/skills/
        agents_skills_dir = self.project_root / ".agents" / "skills"
        agents_skills_dir.mkdir(parents=True, exist_ok=True)

        lifecycle_source_dir = self.system_root / "lifecycle"
        for group in CORE_LIFECYCLE_GROUPS:
            target_group_dir = agents_skills_dir / group
            target_skill_file = target_group_dir / "SKILL.md"
            source_skill_file = lifecycle_source_dir / group / "SKILL.md"

            if not target_skill_file.exists():
                target_group_dir.mkdir(parents=True, exist_ok=True)
                if source_skill_file.exists():
                    shutil.copy2(source_skill_file, target_skill_file)
                    actions_taken.append(f"Scaffolded lifecycle skill: {group}")
                else:
                    # Fallback default if not yet copied to lifecycle dir
                    target_skill_file.write_text(
                        f"---\nname: {group}\ndescription: Universal {group} lifecycle capability.\n---\n\n# {group.title()} Lifecycle\n",
                        encoding="utf-8"
                    )
                    actions_taken.append(f"Created fallback lifecycle skill: {group}")
            else:
                actions_taken.append(f"Preserved existing lifecycle skill: {group}")

        # 3. Reconcile .agents/skills.json to expose atomic skills & agent-pm
        vendor_repo_dir = self.system_root / "vendor" / "mattpocock-skills"
        vendor_skills_dir = vendor_repo_dir / "skills"

        # Missing vendor snapshots may be restored only from immutable provenance pins.
        if not vendor_skills_dir.exists():
            try:
                dependency = _load_vendor_dependency(self.system_root, "mattpocock-skills")
                if dependency is None:
                    raise RuntimeError("vendor/UPSTREAMS.json has no mattpocock-skills pin.")
                _clone_pinned_repository(
                    dependency["source"], vendor_repo_dir, dependency["commit_sha"]
                )
                actions_taken.append(
                    f"Restored Matt Pocock skills at pinned commit {dependency['commit_sha']}."
                )
            except Exception as e:
                actions_taken.append(
                    f"Notice: Could not restore pinned Matt Pocock skills ({e}). Skipping vendor registration."
                )

        # agent-pm is restored from its immutable pin; unpinned sibling copies are not trusted.
        vendor_pm_dir = self.system_root / "vendor" / "agent-pm"
        if not vendor_pm_dir.exists():
            try:
                dependency = _load_vendor_dependency(self.system_root, "agent-pm")
                if dependency is None:
                    raise RuntimeError("vendor/UPSTREAMS.json has no agent-pm pin.")
                _clone_pinned_repository(
                    dependency["source"], vendor_pm_dir, dependency["commit_sha"]
                )
                actions_taken.append(
                    f"Restored agent-pm at pinned commit {dependency['commit_sha']}."
                )
            except Exception as e:
                actions_taken.append(
                    f"Notice: Could not restore pinned agent-pm ({e}). Skipping agent-pm registration."
                )

        skills_config_path = self.project_root / ".agents" / "skills.json"
        skill_entries = []

        if vendor_skills_dir.exists():
            try:
                rel_vendor_path = str(vendor_skills_dir.relative_to(self.project_root)).replace("\\", "/")
            except ValueError:
                rel_vendor_path = str(vendor_skills_dir).replace("\\", "/")
            skill_entries.append({"path": f"{rel_vendor_path}/engineering"})
            skill_entries.append({"path": f"{rel_vendor_path}/productivity"})

        # Register agent-pm from vendor/agent-pm
        vendor_pm_skills_dir = vendor_pm_dir / ".agents" / "skills"
        if vendor_pm_skills_dir.exists():
            try:
                rel_pm_path = str(vendor_pm_skills_dir.relative_to(self.project_root)).replace("\\", "/")
            except ValueError:
                rel_pm_path = str(vendor_pm_skills_dir).replace("\\", "/")
            skill_entries.append({"path": f"{rel_pm_path}/agent-pm"})

        # Register the Alamia DAG planning skill for issue/task decomposition and daily-goal planning.
        dag_skill_dir = self.system_root / "skills" / "dag-task-planning"
        if (dag_skill_dir / "SKILL.md").exists():
            try:
                rel_dag_skill_path = str(dag_skill_dir.relative_to(self.project_root)).replace("\\", "/")
            except ValueError:
                rel_dag_skill_path = str(dag_skill_dir).replace("\\", "/")
            skill_entries.append({"path": rel_dag_skill_path})

        # Register reusable operational tooling guidance as a first-party atomic skill.
        tooling_skill_dir = self.system_root / "skills" / "persistent-operational-tooling"
        if (tooling_skill_dir / "SKILL.md").exists():
            try:
                rel_tooling_skill_path = str(tooling_skill_dir.relative_to(self.project_root)).replace("\\", "/")
            except ValueError:
                rel_tooling_skill_path = str(tooling_skill_dir).replace("\\", "/")
            skill_entries.append({"path": rel_tooling_skill_path})

        # Register the first-party cross-cutting engineering discipline skill.
        discipline_skill_dir = self.system_root / "skills" / "engineering-discipline"
        if (discipline_skill_dir / "SKILL.md").exists():
            try:
                rel_discipline_path = str(discipline_skill_dir.relative_to(self.project_root)).replace("\\", "/")
            except ValueError:
                rel_discipline_path = str(discipline_skill_dir).replace("\\", "/")
            skill_entries.append({"path": rel_discipline_path})

        if skill_entries:
            existing_cfg_str = skills_config_path.read_text(encoding="utf-8") if skills_config_path.exists() else None
            existing_cfg = {}
            if existing_cfg_str:
                try:
                    parsed = json.loads(existing_cfg_str)
                    if isinstance(parsed, dict):
                        existing_cfg = parsed
                except json.JSONDecodeError:
                    backup_path = skills_config_path.with_suffix(".json.bak")
                    if not backup_path.exists():
                        backup_path.write_text(existing_cfg_str, encoding="utf-8")
                        actions_taken.append("Preserved invalid .agents/skills.json at .agents/skills.json.bak.")
            existing_entries = existing_cfg.get("entries", [])
            if not isinstance(existing_entries, list):
                existing_entries = []
            merged_entries = list(existing_entries)
            known_paths = {
                item.get("path") for item in merged_entries
                if isinstance(item, dict) and isinstance(item.get("path"), str)
            }
            for entry in skill_entries:
                if entry["path"] not in known_paths:
                    merged_entries.append(entry)
                    known_paths.add(entry["path"])
            skills_cfg = {**existing_cfg, "entries": merged_entries}
            new_cfg_str = json.dumps(skills_cfg, indent=2)

            if existing_cfg_str != new_cfg_str:
                skills_config_path.write_text(new_cfg_str, encoding="utf-8")
                actions_taken.append("Merged Alamia skill registrations without removing existing entries.")
            else:
                actions_taken.append(".agents/skills.json is already up to date.")

        # Re-inspect to get final state
        final_state = self.engine.inspect()

        return {
            "initial_case": state["case_classification"],
            "final_case": final_state["case_classification"],
            "actions_taken": actions_taken,
            "profile": profile,
            "git": final_state["git"],
            "memory": final_state["memory"],
            "testing": final_state["testing"],
        }

    def format_report(self, result: Dict[str, Any]) -> str:
        """Format a concise, beautiful markdown report for the developer."""
        prof = result["profile"]
        git = result["git"]
        mem = result["memory"]
        test = result["testing"]
        case = result["final_case"]

        lines = [
            f"# Alamia-Skills-System: Bootstrap & Reconciliation Report",
            f"",
            f"**Project:** `{prof['project_name']}` | **Status:** `{case['case']}` ({case['description']})",
            f"",
            f"---",
            f"",
            f"## 1. Discovered Stack & Environment",
            f"- **Primary Language:** `{prof['stack']['primary_language']}` (All: `{', '.join(prof['stack']['languages']) or 'None'}`)",
            f"- **Frameworks:** `{', '.join(prof['stack']['frameworks']) or 'None detected'}`",
            f"- **Package Manager:** `{', '.join(prof['stack']['package_managers']) or 'None detected'}`",
            f"- **Containers:** `{', '.join(prof['stack']['containers']) or 'None'}`",
            f"",
            f"## 2. Testing Configuration",
            f"- **Test Runner:** `{test['runner']}`",
            f"- **Test Command:** `{test['command'] or 'None'}`",
            f"- **Test Dirs:** `{', '.join(test['test_dirs']) or 'None'}`",
            f"",
            f"## 3. Project Memory & Continuity",
        ]

        if mem["has_memory_system"]:
            lines.append(f"- **Handoff Directory:** `{mem['handoff_dir'] or 'None'}`")
            lines.append(f"- **Architecture Directory:** `{mem['architecture_dir'] or 'None'}`")
            if mem.get("latest_handoff"):
                lh = mem["latest_handoff"]
                lines.append(f"- **Latest Handoff:** [{lh['file']}](file:///{self.project_root}/{lh['file']})")
                lines.append(f"  *Title:* **{lh['title']}**")
                if lh.get("pending_items"):
                    lines.append(f"  *Active Pending Objectives:*")
                    for it in lh["pending_items"]:
                        lines.append(f"    - {it}")
        else:
            lines.append("- *No existing session memory detected. Standard lightweight defaults ready.*")

        lines.extend([
            f"",
            f"## 4. Git & Working Tree",
            f"- **Branch:** `{git['branch']}`",
            f"- **Commit:** `{git['latest_commit']}`",
            f"- **Dirty Working Tree:** `{'Yes (' + str(git['uncommitted_lines']) + ' files modified/untracked)' if git['is_dirty'] else 'Clean'}`",
            f"",
            f"## 5. Lifecycle Capabilities Reconciled",
            f"- Available lifecycle commands: `{', '.join(prof['lifecycle']['groups'])}`",
            f"",
            f"## 6. Actions Taken",
        ])
        for act in result["actions_taken"]:
            lines.append(f"- {act}")

        lines.extend([
            f"",
            f"---",
            f"**Ready.** You can now say `implement`, `qa`, `architecture-review`, or `session-end`.",
        ])

        return "\n".join(lines)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    reconciler = ProjectReconciler()
    res = reconciler.reconcile()
    print(reconciler.format_report(res))
