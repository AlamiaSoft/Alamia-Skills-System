---
name: session-end
description: >-
  Use this skill when the developer says "end session", "wrap up", or "handoff".
  Prepares the project for clean continuation, records decisions, and updates the project's memory/handoff system.
---

# Session End Lifecycle Orchestrator

The `session-end` skill prepares the codebase for clean continuation into the next session.

## Operational Workflow

1. **Verify State & Working Tree**:
   - Inspect `git status` and `git diff --stat` to identify all files modified or added during the session.
   - Note whether tests are passing or if there are broken/incomplete changes that need documentation.

2. **Discover Project Memory Pattern**:
   - Inspect `.alamia/project.json` for `memory.handoff_dir` and `memory.latest_handoff_file`.
   - If sequential handoffs exist (e.g., `07-session-handoff-...md`):
     - Determine the next sequential index (e.g. `08-session-handoff-...md`).
     - Adopt the exact structure, headers, and metadata conventions of previous handoffs in that directory.
   - If worklogs exist (`CHANGELOG.md`, `TODO.md`):
     - Update the relevant sections with completed work and next tasks.
   - If no memory convention exists:
     - Create a clean handoff in `docs/handoffs/` or output a comprehensive session summary.

3. **Capture Session Handoff Contents**:
   The handoff must record:
   - **Objectives Achieved:** Concrete achievements, bug fixes, or features implemented.
   - **Verification Artifacts:** Tests executed, logs inspected, or live behavior observed.
   - **Pending Work / Next Session Objectives:** Clear, actionable items for the next session.

4. **Governed Learning Review (Never Auto-Promote)**:
   - Review the session for reusable techniques, verified project conventions, root-cause findings, and failed approaches that are worth preserving.
   - Search existing approved skills and pending candidates before proposing anything new. Prefer improving an existing skill over creating a near-duplicate.
   - Capture a candidate under `.alamia/learning/candidates/<slug>/` with `candidate.json` and `SKILL.md`, using `templates/skill-candidate-template/` as the schema/example when available.
   - Record concrete evidence, exact verification commands/results, scope (`shared` or `project`), prerequisites, limitations, and source session. Distinguish observed facts from hypotheses.
   - Never include secrets, credentials, private user data, or copied proprietary material. If uncertain, omit the material and flag it for human review.
   - Validate the candidate with `python scripts/validate_skill_candidate.py <candidate-dir> --project-root <project-root>` when the validator is available.
   - A candidate is not an approved skill. Do not edit the approved catalog, change policy, or promote candidates automatically. Promotion requires explicit human approval and review of evidence.
   - If no reusable lesson meets this bar, record no candidate; do not manufacture one.

5. **Git Hygiene (Do Not Auto-Push)**:
   - Report staged and unstaged changes.
   - Only stage and commit if the developer explicitly asks. Never auto-push without confirmation.

6. **Present Next-Session Handoff Summary**:
   - Deliver a concise closing summary and confirm that all state has been safely captured.
