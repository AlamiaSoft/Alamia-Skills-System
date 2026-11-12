---
name: security-hardening
description: >-
  Threat-model, audit and harden applications, APIs, dependencies, containers and infrastructure.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Security Hardening

## Purpose
Threat-model, audit and harden applications, APIs, dependencies, containers and infrastructure.

## Activation
Threat-model, audit and harden applications, APIs, dependencies, containers and infrastructure.

## Inputs
Architecture; data classification; auth model; deployment config; dependencies; threat context; scanners.

## Procedure
1. Identify assets, trust boundaries, actors, attack surfaces and abuse cases.
2. Review auth, sessions, object access and tenant isolation.
3. Test validation, encoding, injection, XSS, CSRF, SSRF, uploads and rate limits.
4. Inspect secrets, environment config, logs, sensitive data and encryption.
5. Scan source, dependencies, containers and infrastructure; triage findings with evidence.
6. Verify remediation with negative tests and assign residual risks.
7. Review backup, retention, deletion and incident response.

## Outputs
Threat model; security report; scan evidence; prioritized findings; remediation proof; residual-risk register.

## Quality checks
- [ ] Critical/high findings are fixed or formally accepted; access boundaries and negative paths are tested.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Do not claim certification from a scanner. Never test outside authorized scope or change production controls without approval.
