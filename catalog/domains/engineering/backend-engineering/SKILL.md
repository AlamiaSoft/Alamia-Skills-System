---
name: backend-engineering
description: >-
  Implement and review backend services, APIs, domain logic, auth, jobs and integrations.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Backend Engineering

## Purpose
Implement and review backend services, APIs, domain logic, auth, jobs and integrations.

## Activation
Implement and review backend services, APIs, domain logic, auth, jobs and integrations.

## Inputs
API/spec contracts; architecture; domain rules; coding standards; test profile; security constraints.

## Procedure
1. Inspect framework patterns, middleware, validation and error conventions.
2. Keep transport/controllers thin and domain behavior cohesive.
3. Validate untrusted input and enforce server-side object/action authorization.
4. Use transactions, constraints, idempotency and concurrency controls for state changes.
5. Add safe retries, timeouts, rate limits and observability for external calls/jobs.
6. Test success, invalid input, denied access and failure paths; update API docs and ADRs.

## Outputs
Reviewed backend changes; API behavior; migrations; tests; error/observability behavior; updated docs.

## Quality checks
- [ ] Contracts and authorization are tested; errors are predictable; state changes are safe under retries.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Never trust client authorization, expose secrets or bypass domain invariants. Plan API compatibility changes.
