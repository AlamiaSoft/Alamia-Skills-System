# Skill candidate template

Create a candidate in `.alamia/learning/candidates/<slug>/`. Copy `candidate.json` and `SKILL.md` below, replacing every placeholder. Keep the status as `candidate`.

Validation command:

```bash
python scripts/validate_skill_candidate.py .alamia/learning/candidates/<slug> --project-root .
```

Passing validation only checks structure, duplicates, and obvious secret patterns. It does not establish technical correctness, approve the skill, or publish it.
