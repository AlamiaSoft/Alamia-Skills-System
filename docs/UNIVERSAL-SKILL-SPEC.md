# Universal Skill Specification

A skill is a reusable professional capability, not a prompt dump, workflow or autonomous agent.

Each distributable skill directory contains:
- `SKILL.md`: agent-facing instructions.
- `skill.json`: machine-readable metadata validated against `schemas/skill.schema.json`.
- Optional supporting references, scripts, examples or templates.

Required metadata: stable kebab-case `id`, `name`, specific `description`, primary `domain`, semantic `version`. Recommended metadata: `license`, `tags`, evidence-based `compatibility`, external `requires`, and operational `risk`.

Every SKILL.md must define purpose/activation, inputs, actionable procedure, outputs, quality checks and boundaries. State tool requirements and approval gates. Do not invent facts, metrics, citations, credentials or user data. Treat publishing, sending, spending, deleting and production changes as approval-gated.

Keep skills focused. Collections group skills; workflows compose them; role profiles recommend collections and workflows. Do not conflate these concepts. A skill is not verified merely because its Markdown parses.
