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
8. **Verify the resulting plan.** After creating or editing issues, retrieve the created records and confirm titles, bodies, links, dependencies, and labels. If a machine-readable DAG is used, validate references, missing nodes, cycles, and dependency ordering. Report any operation that failed; never claim an issue or relationship exists without verifying it.

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
- **Verification** (specific commands, tests, reviews, or evidence required)
- **Learning capture** (finding, evidence, confidence, reusable candidate, approval/promotion status; or explain why none)
- **Completion evidence** (commit/PR, test results, review findings, follow-up issue links)
- **Definition of done**

For an Epic, use outcome-level scope, risks, acceptance criteria, child issues, DAG summary, and final verification gates.

### 6. Task completion and learning loop

When a task is completed:

1. Verify acceptance criteria and run the required checks.
2. Record actual result versus estimate and identify unexpected discoveries.
3. Capture evidence and confidence for each reusable lesson.
4. Create/update a learning candidate when the lesson is reusable; never auto-promote unvalidated knowledge.
5. Link the learning candidate or approved skill update from the task when possible.
6. Update issue/PR status and DAG readiness only after verifying the actual GitHub/CI state.
7. Select the next unblocked task in the agreed priority order.

Do this after every task, even when several tasks are completed in one session. Session-end summaries consolidate the work; they do not replace task-level learning.

## Definition of a successful plan

A plan is ready for execution when every task is at most one working day, multi-day outcomes have daily-goal subtasks, dependencies form a valid DAG, each task has testable acceptance and verification requirements, learning capture is included in completion criteria, and the next eligible task is unambiguous.
