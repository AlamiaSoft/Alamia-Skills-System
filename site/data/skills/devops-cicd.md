---
name: devops-cicd
description: >-
  Build reproducible pipelines, containers, environments, infrastructure automation, secrets and rollback.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# DevOps and CI/CD

## Purpose
Build reproducible pipelines, containers, environments, infrastructure automation, secrets and rollback.

## Activation
Build reproducible pipelines, containers, environments, infrastructure automation, secrets and rollback.

## Inputs
Repository; stack; hosting target; environment matrix; release process; security requirements; access model.

## Procedure
1. Inspect current pipelines, deployment and environment differences.
2. Create reproducible build/test steps with pinned dependencies and traceable artifacts.
3. Automate lint, static analysis, tests, builds and security checks.
4. Configure containers, non-root execution, health checks and resource limits where relevant.
5. Separate config from code and use approved secret management.
6. Provision DNS, TLS, storage, databases, queues, backups and least privilege repeatably.
7. Define deployment strategy, migrations, rollback and recovery.

## Outputs
CI/CD workflows; environment matrix; container/infra config; secret plan; deployment and rollback runbooks.

## Quality checks
- [ ] Clean-checkout pipeline works; no secrets leak; artifacts map to commits; rollback is actionable.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Do not deploy or change production infrastructure without approval. Never weaken required CI gates.
