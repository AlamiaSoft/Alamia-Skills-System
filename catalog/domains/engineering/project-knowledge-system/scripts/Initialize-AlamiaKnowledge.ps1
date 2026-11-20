#requires -Version 5.1
<#
.SYNOPSIS
  Initialize the Alamia unified project knowledge system.
.DESCRIPTION
  Creates a docs/-canonical knowledge structure and concise .agents/AGENTS.md.
  Safe to re-run: existing files are preserved; only missing files are created.
  This initializer does NOT migrate or delete legacy .ai/ content. Use the
  project-knowledge-system migration workflow to audit and physically migrate it.
.PARAMETER ProjectRoot
  Target project root. Defaults to the current working directory.
#>
[CmdletBinding()]
param([string]$ProjectRoot = (Get-Location).Path)

$ErrorActionPreference = "Stop"
$root = (Resolve-Path -LiteralPath $ProjectRoot).Path

$directories = @(
    "docs/permanent/product",
    "docs/permanent/architecture",
    "docs/permanent/adr",
    "docs/permanent/glossary",
    "docs/permanent/standards",
    "docs/transient/sprint",
    "docs/transient/handoffs",
    "docs/transient/backlog",
    "docs/history",
    "docs/lessons",
    "docs/indexes",
    "docs/research",
    "docs/assets",
    ".agents",
    "scripts"
)
foreach ($relative in $directories) {
    $path = Join-Path $root $relative
    if (-not (Test-Path -LiteralPath $path)) {
        New-Item -ItemType Directory -Force -Path $path | Out-Null
        Write-Host "[CREATED] $relative" -ForegroundColor DarkGray
    }
}

$files = [ordered]@{}
$files["docs/README.md"] = @'
# Project Knowledge Base

This repository uses one canonical project knowledge tree: docs/. These exact Markdown files are read by AI agents and by humans through the repository or optional browser viewer. Do not create a parallel .ai/ knowledge base.

## Agent bootstrap read order
1. This index.
2. transient/sprint/00-current-state.md, if present.
3. Product and system architecture documents.
4. Relevant ADRs, standards, glossary and security constraints.
5. indexes/repository.md.
6. Latest relevant handoff.
7. Source code and tests relevant to the task.

## Knowledge structure
- permanent/product/: product vision, requirements and domain intent.
- permanent/architecture/: system boundaries, invariants and design.
- permanent/adr/: architecture decision records.
- permanent/glossary/: canonical terminology.
- permanent/standards/: engineering, security and testing standards.
- transient/sprint/: current objectives and blockers.
- transient/handoffs/: dated session handoffs.
- transient/backlog/: working backlog snapshots.
- history/: dated evolution records.
- lessons/: debugging and operational lessons.
- indexes/: repository and dependency maps.
- research/: sourced research with date and confidence.

Update canonical docs when implementation changes intent, architecture, data, APIs, workflows, security or operations. Preserve accepted decisions through ADR amendments or superseding ADRs. Mark unknowns as TODO; never invent facts.
'@

$files[".agents/AGENTS.md"] = @'
# Agent Instructions

## Canonical project knowledge
- docs/ is the single source of truth for project knowledge shared by humans and AI agents.
- Start with docs/README.md, then follow its bootstrap read order before substantial work.
- Do not create or maintain a parallel .ai/ knowledge base.
- Keep this file concise; put substantive project knowledge in docs/ and link to it.

## Engineering discipline
- Inspect Git status and repository conventions before editing.
- Preserve unrelated work and existing knowledge.
- Update docs/ADRs when material behavior, architecture, data, APIs, security or operations change.
- Record substantial session outcomes and exact next actions in docs/transient/handoffs/.
- Never store secrets in project documentation.
- Obtain approval for destructive or consequential external actions.
- Report only tests and checks actually run.
'@

$files["docs/permanent/architecture/01-system-architecture.md"] = @'
# System Architecture
Status: TODO — populate from verified repository evidence.

## Purpose and system context
- Product purpose:
- Primary users:
- Core capabilities:

## System boundaries and components
- In scope:
- Out of scope:
- Components and responsibilities:

## Runtime, deployment and integrations
- Runtime topology:
- Environments:
- External systems:

## Data flows and trust boundaries
- Authentication and authorization:
- Tenant/data isolation:
- Sensitive data:
- Integration boundaries:

## Architectural invariants
- TODO

## Constraints, trade-offs and failure modes
- TODO

## Related ADRs
- TODO
'@

$files["docs/transient/sprint/00-current-state.md"] = @'
# Current Project State
Last updated: TODO

## Current objective
- TODO

## Active work and progress
- Completed:
- In progress:
- Blocked:

## Decisions and risks
- TODO

## Verification
- Commands actually run:
- Results:
- Checks not run:

## Next actions
1. TODO

## Repository state
- Branch:
- Commit:
- Working tree:
'@

$files["docs/indexes/repository.md"] = @'
# Repository Concept-to-Code Index
Status: TODO — populate from actual repository evidence.

| Concept / capability | Source paths | Tests | Related docs / ADRs |
|---|---|---|---|
| Application entry points | TODO | TODO | TODO |
| Domain/business logic | TODO | TODO | TODO |
| Persistence and migrations | TODO | TODO | TODO |
| API and integrations | TODO | TODO | TODO |
| Frontend/UI | TODO | TODO | TODO |
| Jobs and operations | TODO | TODO | TODO |
'@

foreach ($relative in $files.Keys) {
    $path = Join-Path $root $relative
    if (-not (Test-Path -LiteralPath $path)) {
        $parent = Split-Path -Parent $path
        if (-not (Test-Path -LiteralPath $parent)) {
            New-Item -ItemType Directory -Force -Path $parent | Out-Null
        }
        Set-Content -LiteralPath $path -Value $files[$relative] -Encoding UTF8
        Write-Host "[CREATED] $relative" -ForegroundColor Gray
    }
    else {
        Write-Host "[PRESERVED] $relative" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "[SUCCESS] Unified docs/ knowledge structure initialized." -ForegroundColor Green
if (Test-Path -LiteralPath (Join-Path $root ".ai")) {
    Write-Host "[NOTICE] Legacy .ai/ content detected. It was NOT changed. Audit and migrate it using the project-knowledge-system skill." -ForegroundColor Yellow
}
