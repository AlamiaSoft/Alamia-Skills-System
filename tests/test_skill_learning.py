import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from validate_skill_candidate import validate_candidate


def write_candidate(root: Path, slug="sample-skill", **overrides):
    candidate = root / slug
    candidate.mkdir(parents=True, exist_ok=True)
    metadata = {
        "id": slug,
        "title": "Verified Example Skill",
        "scope": "project",
        "status": "candidate",
        "summary": "A repeatable and evidence-backed technique for solving a specific engineering problem.",
        "prerequisites": ["A configured test environment"],
        "steps": ["Run the focused check", "Inspect the recorded result"],
        "evidence": ["commit abc123 and test output"],
        "validation": {"commands": ["python -m unittest"], "results": "Executed locally; sample result recorded."},
        "known_limitations": ["Only validated for the stated project stack"],
        "sensitive_data_reviewed": True,
        "source_session": "session-2026-10-15",
        "approval": {"status": "not-reviewed", "approved_by": None, "approved_at": None},
    }
    metadata.update(overrides)
    (candidate / "candidate.json").write_text(json.dumps(metadata), encoding="utf-8")
    (candidate / "SKILL.md").write_text(
        "---\nname: sample-skill\ndescription: A sample verified skill.\n---\n\n"
        "# Sample Skill\n\n## Steps\n1. Run a focused check.\n",
        encoding="utf-8",
    )
    return candidate


class SkillCandidateValidationTests(unittest.TestCase):
    def test_valid_candidate_passes_structure_checks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = write_candidate(root)
            self.assertEqual(validate_candidate(candidate, root), [])

    def test_missing_evidence_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = write_candidate(root, evidence=[])
            self.assertTrue(any("evidence" in e for e in validate_candidate(candidate, root)))

    def test_candidate_cannot_mark_itself_approved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = write_candidate(root, status="approved")
            self.assertTrue(any("must remain 'candidate'" in e for e in validate_candidate(candidate, root)))

    def test_duplicate_candidate_title_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_candidate(root, "one")
            second = write_candidate(root, "two", title="verified-example skill")
            self.assertTrue(any("Duplicate candidate title" in e for e in validate_candidate(second, root)))

    def test_existing_nested_skill_duplicate_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = write_candidate(root)
            existing = root / ".agents" / "skills" / "engineering" / "sample-skill"
            existing.mkdir(parents=True)
            (existing / "SKILL.md").write_text(
                "---\nname: sample-skill\ndescription: Existing skill.\n---\n\n# Existing\n\n## Steps\n",
                encoding="utf-8",
            )
            self.assertTrue(any("existing project skill" in e for e in validate_candidate(candidate, root)))

    def test_obvious_secret_material_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = write_candidate(root)
            skill = candidate / "SKILL.md"
            skill.write_text(skill.read_text(encoding="utf-8") + '\nAPI_KEY = "this-is-a-real-looking-secret-value"\n', encoding="utf-8")
            self.assertTrue(any("credential" in e for e in validate_candidate(candidate, root)))


if __name__ == "__main__":
    unittest.main()
