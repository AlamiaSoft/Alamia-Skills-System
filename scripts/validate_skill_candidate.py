#!/usr/bin/env python3
"""Validate a proposed Alamia skill without promoting it into the approved catalog."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = {
    "id", "title", "scope", "status", "summary", "prerequisites", "steps",
    "evidence", "validation", "known_limitations", "sensitive_data_reviewed",
    "source_session",
}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----", re.I),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(r"(?i)(?:api[_-]?key|password|secret|access[_-]?token)\s*[:=]\s*[\"'][^\"'\n]{8,}[\"']"),
]


def _normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def _load_json(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"Cannot read valid JSON from {path.name}: {exc}"
    if not isinstance(value, dict):
        return None, f"{path.name} must contain a JSON object."
    return value, None


def validate_candidate(candidate_dir: Path, project_root: Path | None = None) -> list[str]:
    """Return validation errors. A successful result never means approval."""
    candidate_dir = candidate_dir.resolve()
    project_root = (project_root or Path.cwd()).resolve()
    errors: list[str] = []

    if not candidate_dir.is_dir():
        return [f"Candidate directory does not exist: {candidate_dir}"]

    metadata_path = candidate_dir / "candidate.json"
    metadata, error = _load_json(metadata_path)
    if error:
        return [error]
    assert metadata is not None

    missing = sorted(REQUIRED_FIELDS - set(metadata))
    if missing:
        errors.append("Missing required metadata fields: " + ", ".join(missing))

    if metadata.get("scope") not in {"shared", "project"}:
        errors.append("scope must be either 'shared' or 'project'.")
    if metadata.get("status") != "candidate":
        errors.append("status must remain 'candidate'; this validator never approves or promotes skills.")
    if metadata.get("sensitive_data_reviewed") is not True:
        errors.append("sensitive_data_reviewed must be true before review can proceed.")
    if not isinstance(metadata.get("id"), str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata.get("id", "")):
        errors.append("id must be a lowercase hyphenated slug.")
    if not isinstance(metadata.get("title"), str) or not metadata.get("title", "").strip():
        errors.append("title must be a non-empty string.")
    for field in ("prerequisites", "steps", "evidence", "known_limitations"):
        value = metadata.get(field)
        if not isinstance(value, list) or not value or any(not isinstance(item, str) or not item.strip() for item in value):
            errors.append(f"{field} must be a non-empty list of non-empty strings.")
    if not isinstance(metadata.get("summary"), str) or len(metadata.get("summary", "").strip()) < 20:
        errors.append("summary must explain the reusable lesson in at least 20 characters.")
    validation = metadata.get("validation")
    if not isinstance(validation, dict) or not isinstance(validation.get("commands"), list) or not validation["commands"] or not isinstance(validation.get("results"), str) or not validation["results"].strip():
        errors.append("validation must include a non-empty commands list and recorded results.")
    if not isinstance(metadata.get("source_session"), str) or not metadata.get("source_session", "").strip():
        errors.append("source_session must identify the originating task/session.")

    skill_path = candidate_dir / "SKILL.md"
    if not skill_path.is_file():
        errors.append("SKILL.md is required.")
        skill_text = ""
    else:
        skill_text = skill_path.read_text(encoding="utf-8")
        frontmatter = re.match(r"^---\s*\n([\s\S]*?)\n---\s*\n", skill_text)
        if not frontmatter:
            errors.append("SKILL.md must start with YAML frontmatter.")
        else:
            header = frontmatter.group(1)
            if not re.search(r"(?m)^name:\s*\S+", header):
                errors.append("SKILL.md frontmatter must define name.")
            if not re.search(r"(?m)^description:\s*\S+", header):
                errors.append("SKILL.md frontmatter must define description.")
        if len(re.findall(r"(?m)^#{1,3}\s+\S+", skill_text)) < 2:
            errors.append("SKILL.md must contain a title and at least one substantive section.")

    all_text = skill_text + "\n" + (metadata_path.read_text(encoding="utf-8") if metadata_path.exists() else "")
    if any(pattern.search(all_text) for pattern in SECRET_PATTERNS):
        errors.append("Possible credential/private-key material detected; remove it and re-review manually.")

    # Duplicate checks include sibling candidates and existing top-level project skills.
    candidate_root = candidate_dir.parent
    candidate_id = metadata.get("id")
    candidate_title = _normalized(metadata.get("title", "")) if isinstance(metadata.get("title"), str) else ""
    for sibling in candidate_root.iterdir() if candidate_root.is_dir() else []:
        if not sibling.is_dir() or sibling.resolve() == candidate_dir:
            continue
        sibling_meta, sibling_error = _load_json(sibling / "candidate.json")
        if sibling_error or sibling_meta is None:
            continue
        if sibling_meta.get("id") == candidate_id:
            errors.append(f"Duplicate candidate id found in {sibling.name}.")
        if candidate_title and _normalized(str(sibling_meta.get("title", ""))) == candidate_title:
            errors.append(f"Duplicate candidate title found in {sibling.name}.")

    approved_skills = project_root / ".agents" / "skills"
    if approved_skills.is_dir():
        for skill_file in approved_skills.glob("*/SKILL.md"):
            if skill_file.resolve() == skill_path.resolve() if skill_path.exists() else False:
                continue
            try:
                text = skill_file.read_text(encoding="utf-8")
            except OSError:
                continue
            name_match = re.search(r"(?m)^name:\s*(.+?)\s*$", text)
            if candidate_title and name_match and _normalized(name_match.group(1)) == candidate_title:
                errors.append(f"Candidate duplicates an existing project skill: {skill_file.parent.name}.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate_dir", type=Path, help="Directory containing candidate.json and SKILL.md")
    parser.add_argument("--project-root", type=Path, default=Path.cwd(), help="Target project root for duplicate checks")
    args = parser.parse_args()
    errors = validate_candidate(args.candidate_dir, args.project_root)
    if errors:
        print("Candidate validation: ACTION REQUIRED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Candidate validation: STRUCTURE PASSED")
    print("This is not approval. Human review and explicit promotion are still required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
