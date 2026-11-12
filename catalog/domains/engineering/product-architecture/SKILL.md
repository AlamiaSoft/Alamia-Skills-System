---
name: product-architecture
description: >-
  Design or review system boundaries, modules, data flows, technology choices, integrations and deployment topology.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Product Architecture

## Purpose
Design or review system boundaries, modules, data flows, technology choices, integrations and deployment topology.

## Activation
Design or review system boundaries, modules, data flows, technology choices, integrations and deployment topology.

## Inputs
PRD; repository/stack evidence; scale assumptions; security constraints; integrations; operational requirements.

## Procedure
1. Inspect repository, runtime and deployment before proposing changes.
2. Define context boundaries, modules, ownership, APIs, domain model and data flows.
3. Design authentication, authorization, tenancy, trust boundaries and sensitive-data handling.
4. Choose persistence, queues, cache, storage and integration patterns based on requirements.
5. Specify consistency, idempotency, retries, failure modes, backups and recovery.
6. Compare options, document trade-offs and record material decisions as ADRs.

## Outputs
Architecture overview; context/component/data-flow diagrams; API contracts; data model; ADRs; threat boundaries; deployment topology.

## Quality checks
- [ ] Architecture is proportionate and supportable; decisions and trade-offs are documented.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Do not overengineer hypothetical scale or force a preferred stack. Do not pass unresolved tenant-isolation/data-integrity risks.
