---
name: production-deployment
description: >-
  Prepare or execute an explicitly approved production release, rollback or hotfix.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Production Deployment

## Purpose
Prepare or execute an explicitly approved production release, rollback or hotfix.

## Activation
Prepare or execute an explicitly approved production release, rollback or hotfix.

## Inputs
Approval; release candidate; commit/version; runbook; approved credentials; backup status; rollback plan; approver.

## Procedure
1. Confirm explicit approval covers exact action, scope and time.
2. Verify target, artifact provenance, changes, migrations, flags and dependencies.
3. Confirm backup/recovery, monitoring, incident contacts and rollback criteria.
4. Execute approved deployment and capture evidence.
5. Run production smoke tests and verify health, critical workflows and integrations.
6. Monitor errors, latency, queues and business signals for agreed window.
7. Halt or rollback if criteria fail; record incident and release details.

## Outputs
Production release log; deployed SHA/version; approval; smoke evidence; monitoring result; rollback/incident record.

## Quality checks
- [ ] Approval matches artifact; post-deploy checks pass; rollback is actionable; operator accepts handoff.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Never infer approval from preparation/testing requests. Never expose credentials or bypass change controls.
