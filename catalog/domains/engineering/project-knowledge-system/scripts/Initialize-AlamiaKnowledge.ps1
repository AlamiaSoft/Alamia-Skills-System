#requires -Version 5.1
<#
.SYNOPSIS
  Initialize the Alamia AI Project Knowledge System.
.DESCRIPTION
  Creates a durable .ai/ knowledge architecture and .agents/AGENTS.md.
  Safe to re-run: existing files are preserved and only missing files are created.
.PARAMETER ProjectRoot
  Target project root. Defaults to the current working directory.
#>
[CmdletBinding()]
param(
    [string]$ProjectRoot = (Get-Location).Path
)

$ErrorActionPreference = "Stop"
$root = (Resolve-Path -LiteralPath $ProjectRoot).Path
Write-Host "Initializing Alamia Project Knowledge System in $root" -ForegroundColor Green

$directories = @(
    ".ai/permanent/architecture",
    ".ai/permanent/adr",
    ".ai/permanent/glossary",
    ".ai/permanent/standards",
    ".ai/transient/sprint",
    ".ai/transient/handoffs",
    ".ai/transient/backlog",
    ".ai/history",
    ".ai/indexes",
    ".ai/lessons",
    ".agents"
)

foreach ($relative in $directories) {
    $path = Join-Path $root $relative
    if (-not (Test-Path -LiteralPath $path)) {
        New-Item -ItemType Directory -Force -Path $path | Out-Null
        Write-Host "Created directory: $relative" -ForegroundColor DarkGray
    }
}

$files = [ordered]@{}

$files[".ai/README.md"] = @'
# AI Project Knowledge Base

This is the canonical, repository-local knowledge base for this project. It preserves intent, decisions, constraints and working context across agents and sessions.

## Agent bootstrap read order

A new agent session must read these documents before inspecting unrelated source code:

1. This index.
2. transient/sprint/00-current-state.md.
3. permanent/architecture/01-system-architecture.md.
4. indexes/repository.md.
5. permanent/standards/01-coding-standards.md.
6. Relevant ADRs, glossary entries, backlog items and latest handoff.
7. Then inspect source code and tests relevant to the assigned task.

If a listed file is still a template, populate it from repository evidence. Do not invent missing facts.

## Knowledge model

### Permanent knowledge
- permanent/architecture/: system boundaries, invariants and design intent.
- permanent/adr/: accepted, rejected and superseded architecture decisions.
- permanent/glossary/: canonical domain terminology.
- permanent/standards/: coding, testing, security and documentation conventions.

### Transient knowledge
- transient/sprint/: current objectives, progress and blockers.
- transient/handoffs/: session-to-session deltas and next actions.
- transient/backlog/: prioritized unresolved work.

### History and indexes
- history/: dated evolution records.
- indexes/repository.md: maps concepts to source locations and ADRs.
- indexes/dependency-map.md: component/dependency map, preferably Mermaid.
- lessons/: debugging outcomes, operational lessons and failed experiments.

## Maintenance rules
- Update knowledge when implementation changes architecture, data, APIs, workflows, security or operations.
- Document intent, invariants, trade-offs and failure modes; do not duplicate source code.
- Keep current-state and handoff files concise; link to durable records.
- Never store credentials, tokens or private keys here.
- Preserve accepted decisions; supersede them through a new or amended ADR.
- Treat unknowns as TODO/unknown, not as facts.
'@

$files[".agents/AGENTS.md"] = @'
# AI Workspace Instructions

These instructions apply to AI agents working in this repository.

## 1. Mandatory bootstrap sequence
When entering a fresh conversation without complete project context:
1. Read .ai/README.md.
2. Read .ai/transient/sprint/00-current-state.md.
3. Read .ai/permanent/architecture/01-system-architecture.md.
4. Read .ai/indexes/repository.md.
5. Read .ai/permanent/standards/01-coding-standards.md.
6. Read relevant ADRs, glossary entries, backlog items and latest handoff.
7. Then inspect source code and tests relevant to the assigned task.

Do not reverse-engineer the repository before checking canonical project knowledge. If a document is missing or stale, report and reconcile it using repository evidence.

## 2. Knowledge ownership
- .ai/ is the canonical project knowledge base.
- The implementing agent is responsible for ensuring relevant knowledge is updated.
- A designated Knowledge Manager may review or perform the documentation pass, but delegation does not remove accountability.
- Record architectural decisions as ADRs; do not silently rewrite accepted decisions.
- Document intent, invariants, trade-offs and failure modes—not line-by-line source summaries.

## 3. Engineering and safety
- Inspect Git status and project conventions before changing files.
- Keep changes scoped and preserve unrelated work.
- Never commit secrets, credentials or private keys.
- Add/update tests for behavior changes and report only checks actually run.
- Obtain explicit human approval before production deployment, destructive data operations, publishing, spending or other consequential external actions.
- Never claim a task or quality gate passed without observed evidence.

## 4. Session handoff
Before ending substantial work, update current state and create a handoff covering completed work, changed areas, decisions, tests/evidence, blockers, uncommitted work and exact next actions.
'@

$files[".ai/permanent/architecture/01-system-architecture.md"] = @'
# System Architecture
Status: TODO — populate from verified project evidence.

## Purpose and system context
- Product purpose:
- Primary users:
- Core capabilities:

## System boundaries
- In scope:
- Out of scope:
- External systems:

## Runtime and deployment topology
- Applications/services:
- Environments:
- Hosting/infrastructure:

## Components and responsibilities
| Component | Responsibility | Owns data | Interfaces |
|---|---|---|---|

## Data flows and trust boundaries
- Authentication and authorization:
- Tenant/data isolation:
- Sensitive data:
- External integrations:

## Architectural invariants
- TODO

## Constraints, trade-offs, failure modes and recovery
- TODO

## Related ADRs
- TODO
'@

$files[".ai/indexes/repository.md"] = @'
# Repository Index
Status: TODO — map concepts to actual paths; do not guess.

| Concept / capability | Source paths | Tests | Relevant docs / ADRs | Owner |
|---|---|---|---|---|
| Application entry points | TODO | TODO | TODO | TODO |
| Domain/business logic | TODO | TODO | TODO | TODO |
| Persistence and migrations | TODO | TODO | TODO | TODO |
| API / integrations | TODO | TODO | TODO | TODO |
| Frontend / UI | TODO | TODO | TODO | TODO |
| Background jobs | TODO | TODO | TODO | TODO |
| Infrastructure / deployment | TODO | TODO | TODO | TODO |

## Navigation notes
- TODO
'@

$files[".ai/permanent/standards/01-coding-standards.md"] = @'
# Coding and Engineering Standards
Status: TODO — reconcile with existing linters, formatters, CI and team conventions.

## General
- Follow established repository conventions.
- Prefer simple, explicit and maintainable changes.
- Keep responsibilities cohesive and boundaries clear.
- Validate untrusted input at system boundaries.
- Never hardcode secrets.

## Testing
- Required test commands:
- Unit/feature/integration/E2E expectations:
- Test data and fixture conventions:

## Security
- Authentication/authorization requirements:
- Tenant isolation requirements:
- Secret handling:
- Dependency and vulnerability checks:

## Code review
- Branch and PR conventions:
- Required approvals:
- Required CI checks:
- Definition of Done:

## Documentation
- Architecture/API/operations documentation update rules:
- ADR requirements:
'@

$files[".ai/transient/sprint/00-current-state.md"] = @'
# Current Project State
Last updated: TODO | Updated by: TODO

## Current objective
- TODO

## Active scope
- TODO

## Progress
- Completed:
- In progress:
- Blocked:

## Decisions made
- TODO

## Verification
- Commands actually run:
- Results:
- Checks not run / unavailable:

## Risks and dependencies
- TODO

## Next actions
1. TODO

## Repository state
- Branch:
- Commit:
- Working tree:
'@

$files[".ai/permanent/adr/README.md"] = @'
# Architecture Decision Records

Store one decision per ADR using 0000-template.md.

| ADR | Title | Status | Date |
|---|---|---|---|
| TODO | TODO | proposed / accepted / rejected / superseded | TODO |
'@

$files[".ai/permanent/adr/0000-template.md"] = @'
# ADR-NNNN: Decision title
- Status: proposed
- Date: YYYY-MM-DD
- Decision owners:
- Supersedes / superseded by:

## Context
Problem, constraints and forces requiring a decision.

## Decision
What are we choosing?

## Alternatives considered
- Option and trade-off:
- Option and trade-off:

## Consequences
- Positive:
- Negative:
- Operational impact:
- Security/data impact:

## Validation and revisit conditions
Evidence that validates this decision and conditions that would cause it to be revisited.
'@

$files[".ai/permanent/glossary/README.md"] = @'
# Project Glossary

Define domain-specific terms, acronyms and state names consistently.

| Term | Definition | Avoid confusing with | Related concepts |
|---|---|---|---|
| TODO | TODO | TODO | TODO |
'@

$files[".ai/transient/handoffs/README.md"] = @'
# Session Handoffs

For substantial work sessions record:
- Objective and outcome.
- Changed files/modules and key decisions.
- Tests/checks actually run and results.
- Blockers, risks and uncommitted work.
- Exact next actions and relevant issue/PR links.
'@

$files[".ai/transient/backlog/README.md"] = @'
# Project Backlog Notes

Keep this as an index or concise snapshot, not a replacement for the issue tracker.

| Priority | Item | Rationale | Dependencies | Status | Tracking link |
|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO |
'@

$files[".ai/history/README.md"] = @'
# Project History

Record dated, material changes to architecture, boundaries, integrations and operating model. Link to commits, ADRs, issues or releases. Do not duplicate the full changelog.
'@

$files[".ai/indexes/dependency-map.md"] = @'
# Component and Dependency Map
Status: TODO — generate from verified architecture and repository evidence.

Use Mermaid when useful. Replace this illustrative graph with actual components and dependencies, marking external systems and trust boundaries.

    flowchart TD
      User --> Application
      Application --> PrimaryDataStore
'@

$files[".ai/lessons/README.md"] = @'
# Engineering Lessons

Record non-obvious debugging outcomes, operational lessons, failed experiments and prevention guidance.

Each entry should state context/symptom, confirmed or suspected root cause, resolution and verification evidence, prevention/detection improvement, and relevant commit/issue/incident.
'@

$files[".ai/transient/repository-health.md"] = @'
# Repository and Knowledge Health
Last reviewed: TODO

## Documentation coverage
- Architecture:
- Repository map:
- Coding/testing standards:
- ADR index:
- API/integration docs:

## Drift and gaps
- TODO

## Quality and delivery signals
- CI status:
- Test status:
- Security findings:
- Dependency freshness:

## Actions
- TODO
'@

foreach ($relative in $files.Keys) {
    $path = Join-Path $root $relative
    if (-not (Test-Path -LiteralPath $path)) {
        $parent = Split-Path -Parent $path
        if (-not (Test-Path -LiteralPath $parent)) {
            New-Item -ItemType Directory -Force -Path $parent | Out-Null
        }
        Set-Content -LiteralPath $path -Value $files[$relative] -Encoding UTF8
        Write-Host "Created file: $relative" -ForegroundColor Gray
    }
    else {
        Write-Host "Preserved existing file: $relative" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Alamia Project Knowledge System is ready." -ForegroundColor Green
Write-Host "Review .ai/README.md and populate TODO templates from verified project evidence." -ForegroundColor Yellow
