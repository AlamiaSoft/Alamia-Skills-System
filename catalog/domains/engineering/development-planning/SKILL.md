---
name: development-planning
description: >-
  Decompose requirements into dependency-aware implementation slices, tasks, milestones and delivery gates.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Development Planning

## Purpose
Decompose requirements into dependency-aware implementation slices, tasks, milestones and delivery gates.

## Activation
Decompose requirements into dependency-aware implementation slices, tasks, milestones and delivery gates.

## Inputs
Approved PRD; architecture; designs; team capacity; repository state; release constraints.

## Procedure
1. Inspect issues, branches, CI and conventions before creating a parallel plan.
2. Break scope into small vertical slices with verifiable value.
3. Model dependencies, critical path and external blockers.
4. Give each task an outcome, acceptance criteria, owner, dependencies and verification.
5. Surface risky work early: migrations, auth, tenancy, integrations and infrastructure.
6. Set milestones and contingencies without presenting uncertain estimates as commitments.

## Outputs
Prioritized backlog; dependency graph; milestone plan; task acceptance criteria; risk register; Definition of Ready.

## Quality checks
- [ ] Tasks are actionable and verifiable; dependencies and blockers are explicit; plan maps to scope.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Do not manufacture ticket volume or false precision. Do not silently expand scope.
