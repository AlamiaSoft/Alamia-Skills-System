---
name: dag-task-planning
description: >-
  Use when turning a feature, product goal, bug-fix program, or repository backlog into
  GitHub Epics, agent-executable tasks, daily-goal subtasks, dependency DAGs, or an
  ordered implementation plan. Enforces a maximum one-working-day task size and
  captures governed learning after every completed task.
---

# DAG-Driven Task Planning

## Purpose

Convert desired outcomes into a dependency-aware, GitHub-backed plan that a developer agent can pick up, finish, verify, and hand off without rediscovering the whole project. Design the plan to show meaningful, verifiable progress every working day.

## Mandatory rules

1. **Maximum task size: one working day.** Every implementation task must be reasonably finishable within one working day by one capable developer/agent, including implementation, required tests, and task-level evidence. Estimate effort before creating the issue.
2. **Split multi-day work into daily goals.** If a task or feature is expected to take longer than one working day, create a parent feature/Epic and decompose it into ordered, independently verifiable child tasks. Each child task has a concrete daily goal, a useful outcome, and a clear contribution to the parent outcome. Avoid artificial splits that produce no independently meaningful progress.
3. **GitHub is the work-item source of truth.** Use repository issues for Epics, tasks, dependencies, acceptance criteria, and status. Reuse existing issue conventions and labels when present; do not invent labels or milestones without checking the repository. If native parent/sub-issue or blocking relationships are unavailable, encode relationships using explicit issue references and a machine-readable DAG where the repository already supports one.
4. **DAGs must be valid.** Identify prerequisites, parallelizable work, integration points, and final acceptance gates. Ensure the graph is acyclic, every task contributes to a parent outcome, and no task is marked ready while a required dependency is unresolved.
5. **Tasks must be agent-executable.** Each issue includes one outcome, bounded in-scope/out-of-scope boundaries, relevant context, dependencies, testable acceptance criteria, verification commands or procedures, risks, and a definition of done. Link known files, ADRs, skills, and prior issues when verified. Do not fabricate paths, test commands, labels, or repository state.
6. **Preserve the user's priority order and approval boundaries.** Do not silently reorder agreed work. Security-sensitive, financial/accounting, destructive, production, or externally consequential actions require the project's existing approval gates. Planning or issue creation does not authorize code changes, deployment, or merging.
7. **Capture learning after each task, not only at session end.** Every task's definition of done includes a learning review. Record relevant discoveries with evidence and confidence; distinguish facts from hypotheses; create a governed learning candidate for reusable knowledge; check duplicates, scope, safety, and portability; and follow the repository's approval process before promoting a candidate into an approved skill. A task may record that no reusable learning was found.
8. **Plan verification and CI/CD as part of the DAG.** For every task, decide during planning which automated checks, tests, and human decisions are needed to establish its acceptance criteria. Add or identify the CI workflow and required status checks where the repository supports them. Put test-writing and CI setup tasks in the DAG when they are prerequisites; do not leave them as vague follow-up work. Reuse existing workflows and test commands, and never invent a workflow, command, or status check that has not been verified.
9. **Use risk-proportionate test gates.** Choose checks based on change type and impact: formatting/lint/static analysis, unit tests, integration/contract tests, migrations/schema checks, security checks, end-to-end tests, concurrency/retry/failure-injection tests, and supported-database certification as applicable. Financial/accounting, tenant isolation, authorization, idempotency, concurrency, destructive operations, and production changes require explicit negative/failure-path coverage where relevant. Do not require every test category for every task; document why a category is applicable or not applicable.
10. **Separate automated evidence from human judgment.** CI can establish repeatable technical evidence, not approve architecture, business semantics, security exceptions, financial correctness, or production risk by itself. Define which gates are machine-enforced and which require an explicit human decision. Passing CI does not authorize merge, deployment, closing an Epic, or starting a dependent task unless the project's policy says so.
11. **Verify the resulting plan.** After creating or editing issues, retrieve the created records and confirm titles, bodies, links, dependencies, labels, and referenced workflows/checks. If a machine-readable DAG is used, validate references, missing nodes, cycles, and dependency ordering. Report any operation that failed; never claim an issue, relationship, workflow, or check exists without verifying it.

## Workflow

### 1. Discover before planning

- Confirm repository, default branch, existing backlog, labels, milestones, templates, planning files, architecture/ADR documents, and current priority order.
- Read relevant existing issues and avoid duplicate work.
- Separate verified repository facts from assumptions and decisions that need the owner.
- Ask a concise question only if a missing decision materially blocks safe planning; otherwise record the assumption explicitly.

### 2. Define the outcome and Epic

Create an Epic or equivalent parent issue for each coherent outcome that spans multiple tasks. Include:

- Problem / intended outcome and why it matters.
- Scope and non-goals.
- Observable Epic-level acceptance criteria.
- Child task list and dependency overview.
- Risks, external decisions, and release/security gates.
- Links to relevant existing issues and design decisions.

For a truly single-day change, do not create a ceremonial Epic unless repository conventions require one.

### 3. Estimate and decompose

- Estimate each task in focused working hours, including coding, tests, review-ready evidence, and expected learning capture.
- Target a small task that can finish in one day; if estimated effort or uncertainty makes that unlikely, split it.
- For multi-day features, create a sequence of daily-goal tasks. Each daily goal should end in a verifiable artifact: a tested vertical slice, merged-safe code change, passing regression test, validated interface, documented decision, or another meaningful increment.
- Keep discovery/spikes bounded to one day and require a decision/evidence output, not open-ended research.
- Prefer independently reviewable changes and one focused PR per task where practical.
- Identify tasks that can safely run in parallel, but make integration and validation tasks explicit.

### 4. Build and validate the DAG

- Represent each task as a node with stable issue number/URL, estimated effort, daily goal, dependencies, acceptance criteria, and status.
- Add dependency edges only when a real prerequisite exists. Avoid serializing independent work unnecessarily.
- Include explicit integration, security/accounting review, end-to-end verification, and release gates where appropriate.
- Define a verification matrix for the Epic: task/acceptance criterion → test type or review → command/workflow → expected evidence → blocking or advisory status.
- Inspect existing GitHub Actions/workflows and branch-protection/required-check conventions when accessible. Reuse them; propose new CI jobs only for a demonstrated gap. If permissions prevent inspection, state that the check configuration remains unverified.
- Make CI enablement, flaky-test repair, test fixtures, test-environment provisioning, or supported-database validation explicit DAG tasks when they are needed to make acceptance verifiable.
- Ensure each PR's required checks are knowable before implementation starts. For a task that changes behavior, require the relevant regression test in the same task unless a documented dependency makes a separate test task necessary.
- Validate that there are no cycles, dangling dependencies, missing prerequisites, or child tasks that do not contribute to the Epic.
- Preserve an existing canonical DAG format. If none exists, GitHub issue links are sufficient for a small plan; create a machine-readable DAG only when it materially helps automation and define which source is canonical.

### 5. Use this issue structure

For a task issue, include:

- **Objective / daily goal**
- **Estimate** (focused working time; no task exceeds one working day)
- **Context and constraints**
- **Dependencies** (blocked by / blocks / parent Epic)
- **Scope** (included and excluded)
- **Acceptance criteria** (observable checkboxes)
- **Test strategy** (applicable test layers, important positive/negative/failure-path cases, and why omitted layers are not applicable)
- **CI/CD gates** (verified workflow/check names, blocking vs advisory, required environment/database, and what evidence to attach; mark unknown configuration as unverified rather than guessing)
- **Verification** (exact commands, working directory, prerequisites, expected result, and required CI run/link; distinguish locally run checks from CI results)
- **Learning capture** (finding, evidence, confidence, reusable candidate, approval/promotion status; or explain why none)
- **Completion evidence** (commit/PR, test results, review findings, follow-up issue links)
- **Definition of done**

For an Epic, use outcome-level scope, risks, acceptance criteria, child issues, DAG summary, and final verification gates.

### 6. Task completion and learning loop

When a task is completed:

1. Verify each acceptance criterion against its planned evidence; run relevant local checks and inspect the actual PR CI status.
2. Report exact commands, working directories, results, failed attempts, CI run links, and any skipped checks with reasons. A command written in an issue is a plan, not proof it ran.
3. Do not call a PR review-ready while required checks are pending/failing, required evidence is missing, or a known failure-path test has not been addressed. If a check cannot run, mark the criterion blocked/not verified and state the decision needed.
4. Record actual result versus estimate and identify unexpected discoveries.
5. Capture evidence and confidence for each reusable lesson.
6. Create/update a learning candidate when the lesson is reusable; never auto-promote unvalidated knowledge.
7. Link the learning candidate or approved skill update from the task when possible.
8. Update issue/PR status and DAG readiness only after verifying the actual GitHub/CI state.
9. Select the next unblocked task in the agreed priority order only after the task's required gates and approval boundaries are satisfied.

Do this after every task, even when several tasks are completed in one session. Session-end summaries consolidate the work; they do not replace task-level learning.

## Definition of a successful plan

A plan is ready for execution when every task is at most one working day, multi-day outcomes have daily-goal subtasks, dependencies form a valid DAG, each task has testable acceptance criteria plus a risk-proportionate test strategy and verification evidence, applicable CI/CD gates are identified or explicitly marked unverified, learning capture is included in completion criteria, and the next eligible task is unambiguous. A PR is review-ready only when its required checks and evidence are available; human review remains focused on design, correctness, trade-offs, security, and decisions that automation cannot settle.
