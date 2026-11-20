---
name: product-maintenance
description: >-
  Triage production defects, maintain dependencies, patch vulnerabilities and prioritize technical debt.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Product Maintenance

## Purpose
Triage production defects, maintain dependencies, patch vulnerabilities and prioritize technical debt.

## Activation
Triage production defects, maintain dependencies, patch vulnerabilities and prioritize technical debt.

## Inputs
Incidents/customer reports; telemetry; dependency inventory; support commitments; backlog; release; owners.

## Procedure
1. Classify impact, severity, frequency, security and data-integrity risk.
2. Reproduce with logs/traces/tests; distinguish symptom from root cause.
3. Choose hotfix versus planned remediation and define rollback/mitigation.
4. Assess dependency updates and advisories for compatibility/regression risk.
5. Prioritize technical debt by measurable delivery or operational cost.
6. Add regression tests and update runbooks, ADRs, lessons and project knowledge.
7. Feed KPI/support evidence into discovery and backlog.

## Outputs
Triage record; remediation plan; regression tests; patch evidence; postmortem; maintenance backlog.

## Quality checks
- [ ] Ownership and severity are explicit; root cause is addressed; regression and release gates followed.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Do not close without verification or defer critical security/data risks silently. Do not upgrade blindly.
