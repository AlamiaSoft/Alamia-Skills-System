---
name: product-release-management
description: >-
  Version releases, prepare release notes, manage feature flags, rollout, deprecation and post-release verification.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Product Release Management

## Purpose
Version releases, prepare release notes, manage feature flags, rollout, deprecation and post-release verification.

## Activation
Version releases, prepare release notes, manage feature flags, rollout, deprecation and post-release verification.

## Inputs
Approved scope; merged changes; commit range; issue/PR refs; test evidence; migration notes; release owner.

## Procedure
1. Confirm release scope from commit and issue evidence.
2. Apply repository-approved versioning and update release metadata.
3. Prepare user-facing notes and technical changelog with breaking changes/migrations.
4. Review flags, rollout cohorts, compatibility and deprecation timelines.
5. Confirm QA/security/UAT approvals and operational readiness.
6. Coordinate approval and deployment with authorized owner.
7. Verify health, capture feedback/incidents and close release record.

## Outputs
Versioned release record; changelog; rollout plan; deprecation notices; post-release verification.

## Quality checks
- [ ] Notes match actual changes; breaking impacts disclosed; approvals and deployed version traceable.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Do not publish or promise availability/timelines without authorization. Do not omit breaking changes.
