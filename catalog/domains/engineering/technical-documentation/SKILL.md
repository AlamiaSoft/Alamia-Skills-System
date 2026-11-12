---
name: technical-documentation
description: >-
  Create and maintain architecture, API, setup, deployment, operations, troubleshooting and onboarding documentation.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Technical Documentation

## Purpose
Create and maintain architecture, API, setup, deployment, operations, troubleshooting and onboarding documentation.

## Activation
Create and maintain architecture, API, setup, deployment, operations, troubleshooting and onboarding documentation.

## Inputs
Actual code/config; ADRs; API schemas; test/deploy commands; owners; audience.

## Procedure
1. Identify audience, task and authoritative source.
2. Document purpose, boundaries, invariants, decisions, trade-offs and failure modes.
3. Provide reproducible setup, config, migration, test and deployment instructions.
4. Document API/auth/error contracts and integrations.
5. Create backup/restore, alert, incident and rollback runbooks.
6. Link docs to source, ADRs, issues and releases; remove stale contradictions.
7. Validate commands/examples in a clean environment where practical.

## Outputs
Updated docs; architecture/API references; setup guide; runbooks; changelog notes; gap list.

## Quality checks
- [ ] Instructions are accurate, runnable and discoverable; docs describe intent rather than duplicating code.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Do not invent commands or architecture. Never include secrets or customer data.
