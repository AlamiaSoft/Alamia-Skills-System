---
name: project-knowledge-system
description: >-
  Initialize, maintain and reconcile a durable AI project knowledge base using
  .ai/ and .agents/ conventions. Use before substantial work on a new project,
  when onboarding an agent, or when project context, architecture or handoffs drift.
license: MIT
metadata:
  type: project-foundation
  category: engineering
  version: "1.0.0"
---

# Project Knowledge System

## Purpose
Create a repository-local knowledge system that preserves intent, decisions, constraints and working context across agents and sessions. This skill manages .ai/ and .agents/AGENTS.md. It complements source documentation, Git history, issue tracking and the existing Alamia .alamia lifecycle runtime. If an equivalent knowledge system already exists, map and adopt it instead of creating a competing structure.

## Activation
Use before substantial work on a new project, when onboarding an agent, after material architecture/data/API/workflow/deployment changes, at sprint/session boundaries, or when knowledge is stale or contradictory.

## Inputs
Project root, repository state, existing docs and agent instructions, stack/test/deployment conventions, and team knowledge ownership rules.

## Procedure

### 1. Inspect before scaffolding
- Confirm project root and inspect Git status.
- Look for .ai/, .agents/, AGENTS.md, CLAUDE.md, README, architecture docs and .alamia metadata.
- Identify the canonical existing knowledge system.
- Never overwrite or rename project-owned instructions or knowledge.
- If an equivalent exists, map it and recommend additive improvements only.

### 2. Initialize
Use the bundled PowerShell script at scripts/Initialize-AlamiaKnowledge.ps1 from the target project root, or pass -ProjectRoot. It is idempotent: missing directories/files are created; existing files are preserved.

Expected structure:
- .ai/README.md: canonical index and agent bootstrap read order.
- .ai/permanent/architecture/: system boundaries, invariants and design intent.
- .ai/permanent/adr/: accepted, rejected and superseded decisions plus index.
- .ai/permanent/glossary/: canonical domain terms.
- .ai/permanent/standards/: coding, testing, security and documentation conventions.
- .ai/transient/sprint/: current objectives, work and project state.
- .ai/transient/handoffs/: session deltas, decisions and next actions.
- .ai/transient/backlog/: unresolved work and priorities.
- .ai/history/: dated project evolution records.
- .ai/indexes/: repository concept map and dependency/component map.
- .ai/lessons/: debugging outcomes, operational lessons and failed experiments.
- .agents/AGENTS.md: shared agent bootstrap sequence and knowledge ownership rules.

Permanent knowledge holds durable intent, invariants, decisions and standards. Transient knowledge holds current sprint, blockers and handoffs. History preserves dated changes without polluting current-state summaries.

### 3. Bootstrap and populate
Fresh-session read order:
1. .ai/README.md
2. .ai/transient/sprint/00-current-state.md
3. .ai/permanent/architecture/01-system-architecture.md
4. .ai/indexes/repository.md
5. .ai/permanent/standards/01-coding-standards.md
6. Relevant ADRs, glossary entries, backlog items and latest handoff.
7. Source code and tests relevant to the assigned task.

Populate templates only from verified evidence. Mark unknowns as TODO/unknown. For new projects, fill overview, initial architecture, standards and current-state files as decisions are made.

### 4. Maintain during development
When changes affect architecture, data models, APIs, workflows, security, integrations, deployment or operations:
- Update relevant permanent documents or ADRs.
- Update repository/dependency indexes when structure or ownership changes.
- Update glossary when domain language changes.
- Record temporary work and blockers in transient files.
- Add dated history for material architectural changes.
- Record non-obvious debugging outcomes and failed experiments in lessons.
- Document intent, invariants, trade-offs, constraints and failure modes, not duplicate source listings.

The implementing agent remains accountable for documentation. A Knowledge Manager may review or own the final pass, but delegation does not remove accountability.

### 5. Session and sprint handoff
Before ending substantial work:
- Update current-state.
- Create/update a handoff with completed work, changed areas, decisions, exact test evidence, blockers and next actions.
- Update backlog priorities and link issues/PRs.
- Record branch/commit and uncommitted changes accurately.
- Keep current-state concise and link to detailed records.

### 6. Reconcile and prevent drift
Compare documented architecture and repository maps with actual code, migrations, tests and deployment configuration. Report stale docs, contradictions, undocumented high-risk behavior, stale handoffs and knowledge gaps. Do not silently rewrite accepted decisions; propose an ADR amendment or superseding decision.

## Outputs
Initialized/reconciled .ai/ and .agents/; consistent bootstrap instructions; populated overview, architecture, repository map, standards and current-state; ADR/glossary/dependency/history/lessons/handoff records as applicable; and a knowledge-health report.

## Quality checks
- [ ] Existing project knowledge inspected before changes.
- [ ] Existing files preserved; scaffolding is additive and idempotent.
- [ ] Bootstrap order is consistent between README and AGENTS.md.
- [ ] Permanent, transient and historical knowledge are separated.
- [ ] Templates use placeholders rather than invented facts.
- [ ] Architecture and repository indexes reflect actual project evidence.
- [ ] Handoffs include evidence, blockers and next actions.
- [ ] Material code changes have corresponding knowledge updates.

## Boundaries
Never overwrite existing knowledge by default. Never treat empty templates as completed docs. Never store credentials, tokens or private keys in .ai/. Do not copy large source files into the knowledge base. Do not replace existing docs or lifecycle runtime without an explicit migration plan. Archive stale transient material instead of allowing current-state files to grow indefinitely.
