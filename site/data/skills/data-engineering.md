---
name: data-engineering
description: >-
  Design schemas, migrations, relationships, indexing, imports, retention, backup and data integrity controls.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Data Engineering

## Purpose
Design schemas, migrations, relationships, indexing, imports, retention, backup and data integrity controls.

## Activation
Design schemas, migrations, relationships, indexing, imports, retention, backup and data integrity controls.

## Inputs
Domain model; query patterns; volume assumptions; existing schema; migration constraints; recovery needs.

## Procedure
1. Inspect schema, migration history, ownership and access patterns.
2. Define entities, constraints, lifecycle and tenant scoping.
3. Design forward-safe migrations and rollback for production data volume.
4. Add indexes from query evidence and verify query plans.
5. Protect integrity with constraints, transactions and idempotent imports.
6. Define retention, deletion, archival, backup and restore; test fresh install and upgrade paths.

## Outputs
ERD/schema notes; migration plan; constraints/indexes; retention rules; backup/restore evidence; tests.

## Quality checks
- [ ] No unscoped tenant queries; migrations preserve data; integrity and recovery are tested.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
No destructive production migrations without explicit approval and verified backups. Do not add indexes blindly.
