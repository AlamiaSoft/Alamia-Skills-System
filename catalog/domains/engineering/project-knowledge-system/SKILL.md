---
name: project-knowledge-system
description: >-
  Initialize, maintain, audit and migrate a durable repository-local knowledge
  base shared by human developers and AI agents. Uses docs/ as the single
  canonical Markdown source and .agents/ as a concise bootstrap layer.
license: MIT
metadata:
  type: project-foundation
  category: engineering
  version: "2.0.0"
---

# Project Knowledge System

## Purpose

Create and maintain one repository-local knowledge system that preserves product intent, decisions, constraints, architecture and working context across developers, tools and AI sessions.

**Canonical knowledge lives physically in docs/.** Humans browse those Markdown files directly or through the optional browser viewer; AI agents read the exact same files. .agents/AGENTS.md (or an existing root agent instruction file) contains only concise operating rules and links to canonical docs. It is not a second knowledge base.

This skill complements source documentation, Git history, issue tracking and the Alamia lifecycle runtime. If a repository already has a useful documentation structure, reconcile and adopt it rather than replacing it with generic templates.

## Activation

Use before substantial work on a new project; when onboarding an agent; after material architecture, data, API, workflow, security, integration, deployment or operations changes; at sprint/session boundaries; or when documentation is stale, contradictory, duplicated or split across .ai/, docs/ and agent instruction files.

## Inputs

Project root, Git status/history, existing docs and agent instructions, source code/tests/migrations/configuration, stack/test/deployment conventions, and team knowledge ownership rules.

## Canonical structure

Use docs/ with lifecycle and domain groupings appropriate to the project:
- docs/README.md: master index and bootstrap read order.
- docs/permanent/product/: product vision, requirements and domain intent.
- docs/permanent/architecture/: system boundaries, invariants and design.
- docs/permanent/adr/: accepted, rejected and superseded decisions.
- docs/permanent/glossary/: canonical terminology.
- docs/permanent/standards/: coding, testing, security and documentation standards.
- docs/transient/sprint/: current objectives, progress and blockers.
- docs/transient/handoffs/: dated session handoffs.
- docs/transient/backlog/: working backlog snapshots, not a replacement for issue tracking.
- docs/history/: dated material evolution records.
- docs/lessons/: debugging outcomes and operational lessons.
- docs/indexes/: repository and dependency maps.
- docs/research/: sourced research with dates and confidence.

Projects may add domain-specific folders such as api/, integrations/, operations/, security/ or ux/. Preserve a meaningful existing taxonomy where clearer.

## Procedure

### 1. Inspect before scaffolding
- Confirm project root and inspect Git status; do not disturb user changes.
- Inventory docs/, legacy .ai/, .agents/, root AGENTS.md/CLAUDE.md, README and module-level docs.
- Inspect actual source code, tests, migrations, CI and deployment configuration before documenting architecture.
- Identify canonical/non-canonical knowledge, duplicates, conflicts, stale material, generated files and references.
- If an equivalent knowledge system exists, map and adopt it. Never create a competing tree.

### 2. Initialize safely
- Create missing directories/files under docs/; preserve existing content.
- Use the bundled PowerShell initializer only as a safe initializer. It creates the canonical docs/ layout, not a new .ai/ tree.
- Create/update a concise .agents/AGENTS.md that directs agents to docs/README.md and explains ownership, safety and handoff rules.
- Create a master index with links to real documents and a bootstrap sequence.
- Populate templates only from verified evidence. Mark missing information TODO/unknown.
- Do not replace existing docs or lifecycle runtime without an explicit plan.

### 3. Bootstrap and populate

Fresh-session read order:
1. docs/README.md
2. docs/transient/sprint/00-current-state.md, if present
3. Product and system architecture docs
4. Relevant ADRs, standards, glossary and security constraints
5. docs/indexes/repository.md
6. Latest relevant handoff
7. Source code and tests relevant to the task

Populate product overview, architecture, standards, repository map and current state from repository evidence. Record invariants, interfaces, ownership, trust boundaries, trade-offs, constraints and failure modes—not line-by-line source listings.

### 4. Migrate legacy knowledge physically

When project knowledge exists in .ai/ or elsewhere, do not merely configure the viewer to read that location. Physically move/reconcile actual Markdown knowledge into docs/, so one physical canonical file serves both AI and human readers.

1. Run a full audit and create a source-to-destination manifest with hashes, classification, rationale and link impact.
2. Classify each item as permanent, transient, history, lesson, index, research, non-knowledge config/tooling, generated output or out of scope.
3. Compare duplicate candidates by content and meaning. Preserve unique material, provenance, decisions, dates and evidence.
4. Flag contradictory decisions/specifications; do not resolve by guessing. Retain both versions or record the unresolved conflict until an owner decides.
5. Physically move files into the agreed docs/ structure, using Git-aware renames where possible. Update relative links, asset references, scripts, tests, viewer configuration and bootstrap instructions.
6. Keep .agents/AGENTS.md concise; move substantive knowledge from agent instruction files into canonical docs and link to it.
7. Do not move executable tooling, runtime config, credentials, secrets, vendor files or unrelated source code into docs.
8. Do not leave .ai/ as a parallel knowledge silo after successful migration. Preserve non-knowledge tooling/configuration and account for every source file.
9. Record old path -> new path, hashes, actions, conflicts and validation in a migration report under docs/history/ or another agreed location.
10. Regenerate the browser index from canonical Markdown and validate links.

**Approval and safety:** Audit and planning are read-only. General authorization to migrate permits safe moves that preserve content, but not destructive consolidation. Obtain explicit approval before overwriting, deleting unique/conflicting material, lossy merging or irreversible cleanup. If uncertain, retain the source and report the blocker. Keep a pre-migration commit and rollback path. Migration must be idempotent.

### 5. Maintain during development
When changes affect architecture, data models, APIs, workflows, security, integrations, deployment or operations:
- Update relevant permanent docs or ADRs.
- Update repository/dependency indexes when structure or ownership changes.
- Update glossary when domain language changes.
- Record temporary work/blockers in transient docs.
- Add dated history for material architectural changes.
- Record non-obvious debugging outcomes and failed experiments in lessons.
- Run docs sync if the viewer is present.
- The implementing agent remains accountable for documentation.

### 6. Session and sprint handoff
Before ending substantial work:
- Update current-state with still-active objectives and blockers.
- Create/update a dated handoff with completed work, changed areas, decisions, exact test evidence, blockers and next actions.
- Update backlog priorities and link issues/PRs.
- Record branch/commit and uncommitted changes accurately.
- Keep current-state concise and link to detailed records.

### 7. Reconcile and prevent drift
Compare documented architecture and repository maps with actual code, migrations, tests and deployment configuration. Report stale docs, contradictions, undocumented high-risk behavior, stale handoffs and knowledge gaps. Do not silently rewrite accepted decisions; propose an ADR amendment or superseding decision.

## Outputs

Unified docs/ knowledge tree; concise .agents/AGENTS.md; populated product/architecture/repository/standards/current-state docs; ADR/glossary/history/lessons/handoff records as applicable; migration manifest/report; generated browser index; and knowledge-health report.

## Quality checks
- [ ] docs/ is the single canonical knowledge location.
- [ ] AI bootstrap and human viewer use the same physical Markdown files.
- [ ] Legacy knowledge inventory is complete and every file accounted for.
- [ ] Permanent, transient, historical, research and non-knowledge files are classified.
- [ ] Existing knowledge and provenance are preserved; conflicts explicit.
- [ ] No unapproved overwrite, lossy merge or deletion.
- [ ] Bootstrap order is consistent between README and AGENTS.md.
- [ ] Architecture and repository indexes reflect actual evidence.
- [ ] Handoffs include evidence, blockers and next actions.
- [ ] Material code changes have corresponding knowledge updates.
- [ ] Browser index is regenerated from canonical docs and links validate.
- [ ] Migration is idempotent and rollback is available.

## Boundaries

Never maintain parallel .ai/ and docs/ knowledge bases. Never overwrite existing knowledge by default. Never treat empty templates as completed docs. Never store credentials/tokens/private keys in project knowledge. Do not copy large source files into the knowledge base. Do not silently resolve conflicting decisions. Archive stale transient material instead of allowing current-state files to grow indefinitely.
