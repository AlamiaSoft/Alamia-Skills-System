---
name: staging-validation
description: >-
  Validate a release candidate in staging, verify production parity, run smoke tests and conduct UAT.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Staging Validation

## Purpose
Validate a release candidate in staging, verify production parity, run smoke tests and conduct UAT.

## Activation
Validate a release candidate in staging, verify production parity, run smoke tests and conduct UAT.

## Inputs
Release candidate SHA/version; staging access; config; acceptance criteria; test data; UAT owner.

## Procedure
1. Confirm staging is production-like with safe credentials/data.
2. Verify version, configuration, flags, integrations and migrations.
3. Run smoke tests and critical journeys including roles and tenant boundaries.
4. Verify jobs, queues, notifications, webhooks, analytics, logs and alerts.
5. Conduct UAT against written criteria and record tester/results.
6. Classify defects, retest fixes and repeat impacted checks.
7. Produce release recommendation and residual-risk list.

## Outputs
Staging record; smoke evidence; UAT sign-off; defect disposition; release candidate ID.

## Quality checks
- [ ] Version is traceable; critical flows/integrations pass; UAT sign-off is explicit.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Do not use production secrets or unapproved production data. Staging success does not authorize production.
