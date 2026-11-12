---
name: product-engineering
description: >-
  Orchestrate end-to-end professional software product development from discovery
  through specification, architecture, design, implementation, QA, security,
  staging, production release, observability and ongoing maintenance.
license: MIT
metadata:
  type: lifecycle-orchestrator
  category: engineering
  version: "1.0.0"
---

# Product Engineering

## Purpose
Deliver a working, maintainable, secure and operable software product—not merely a codebase or demo. Coordinate the full lifecycle, invoke specialist capabilities where available, and require evidence at each material quality gate. This skill is an orchestrator and playbook, not an autonomous permission grant.

## Activation
Use for greenfield products, major features, brownfield production-readiness work, releases and lifecycle remediation. Support:
- **Greenfield:** establish project knowledge first, then begin discovery.
- **Brownfield:** inspect existing artifacts, assess maturity and resume at the earliest incomplete or failed gate. Preserve sound work; do not force a rewrite.

## Inputs
Discover or collect product intent, target users, repository and current deployment, stack preferences, constraints, integrations, data sensitivity, compliance needs, delivery scope, owners and approval boundaries. Ask only for decisions that cannot safely be inferred and materially affect scope, cost, architecture, security or delivery.

## Non-negotiable operating rules
1. Evidence over declarations: artifacts and observed checks determine gate status.
2. Build incrementally in vertical slices; avoid speculative abstractions.
3. Security, privacy, accessibility and operability are design inputs.
4. Maintain project knowledge throughout the lifecycle.
5. Adapt to the actual stack and reuse existing tools before adding dependencies.
6. Consequential actions require explicit human approval.
7. Report passed, failed, blocked, not-run and advisory checks distinctly.
8. A build or happy-path demo is not proof of production readiness.

## Lifecycle procedure

### 0. Project foundation and knowledge
Invoke Project Knowledge System before substantial work. Inspect existing docs and agent instructions, initialize or reconcile the .ai/ and .agents/ structure, read the project bootstrap sequence, capture current Git state and record initial intent, constraints and decisions.
**Artifacts:** project overview, current state, architecture baseline, repository map, coding standards and initial handoff.
**Gate:** project knowledge exists or an equivalent is mapped; existing files are preserved; project ownership and Git state are understood.

### 1. Product discovery
Define the problem, users, jobs-to-be-done, alternatives, value proposition and business objective. Separate evidence from assumptions; identify the riskiest assumptions. Assess feasibility, market evidence, integration dependencies, regulation, operational burden and cost drivers. Define a narrow MVP, non-goals and validation experiments.
**Artifacts:** discovery brief, personas/use cases, assumptions and risks register, MVP boundary, product outcome hypotheses.
**Gate:** problem, target user, value hypothesis and MVP are clear enough to specify. Do not present assumptions as validated demand.

### 2. Product specification
Create a PRD, user journeys, functional requirements, user stories and observable acceptance criteria. Define non-functional requirements: security, privacy, accessibility, performance, availability, recovery, localization and compatibility. Specify roles, permissions, tenant boundaries, data ownership, audit requirements, integrations, retries, idempotency, retention, analytics events and product KPIs. Prioritize and trace requirements to implementation and tests.
**Artifacts:** PRD, acceptance criteria, prioritized backlog, requirements traceability, KPI/event specification.
**Gate:** critical workflows are testable; unresolved decisions are visible.

### 3. Architecture and technical design
Inspect the repository and stack first. Choose the simplest architecture that meets requirements and credible growth needs. Define system boundaries, modules, domain model, data flows, APIs, integrations, authentication, authorization, tenant isolation, secrets and trust boundaries. Design schemas, constraints, indexes, transactions, migrations, jobs, queues, cache, storage, backups and recovery as needed. Document deployment topology, failure modes, trade-offs and ADRs. Define architecture-specific test and security strategies.
**Artifacts:** architecture overview, component/data-flow diagrams, API contracts, data model, threat model, ADRs, deployment topology.
**Gate:** critical architectural risks and data/security boundaries have been reviewed.

### 4. UX/UI engineering
Map journeys, navigation and information architecture. Define design tokens, reusable components, responsive layouts and accessibility behavior. Specify loading, empty, error, permission-denied, offline and success states. Validate keyboard and assistive-technology use, mobile/tablet/desktop behavior and realistic content.
**Artifacts:** user flows, wireframes/prototypes, design system, screen specs and accessibility notes.
**Gate:** critical journeys are coherent and approved; implementation has enough detail to avoid guesswork.

### 5. Engineering planning and governance
Break work into dependency-aware vertical slices. Establish repository conventions, branching, PR review, ownership, Definition of Ready/Done, test strategy, security checks, CI requirements and human approval gates. Assign owners and track decisions/risks in the team's system of record. Keep ceremony proportional.
**Artifacts:** implementation plan, task backlog, dependency map, engineering standards and gate matrix.
**Gate:** every planned slice has acceptance criteria, dependencies and a verification approach.

### 6. Implementation workstreams
Coordinate these workstreams according to product needs:
- **Backend:** domain logic, APIs, validation, authorization, transactions, jobs, notifications and integrations.
- **Frontend:** responsive UI, state management, forms, client validation, API integration and accessibility.
- **Data:** schemas, migrations, relationships, constraints, indexes, seed data, retention and migration safety.
- **AI/integrations:** provider abstraction, model/tool selection, prompt and tool contracts, structured outputs, evaluation, cost/usage limits, privacy and graceful fallback.
- **Cross-cutting:** error handling, auditability, feature flags, configuration, localization and maintainability.
Implement thin vertical slices, follow project conventions, add tests with behavior, avoid hardcoded secrets, enforce server-side authorization, use safe migrations, review diffs and update knowledge/docs when behavior changes.
**Artifacts:** working increments, reviewed code, migrations, tests, updated docs and traceable commits/PRs.
**Gate:** each slice meets acceptance criteria and has appropriate tests and review evidence.

### 7. Quality assurance
Run proportionate unit, feature, integration, contract, E2E, regression, browser/device, accessibility and localization tests. Test critical journeys, role/permission matrices, tenant isolation, edge cases, invalid input, retries, duplicates and failure recovery. Validate migration/upgrade paths and backup restore for material data changes. Record exact commands, environment, counts, failures and skipped tests. Triage by severity.
**Artifacts:** test plan, execution report, defect register and acceptance evidence.
**Gate:** blocking acceptance tests pass; critical/high defects are resolved or explicitly risk-accepted by the authorized owner.

### 8. Security and privacy hardening
Threat-model trust boundaries and abuse cases. Review authentication, sessions, authorization, object-level access, tenant isolation, validation, encoding, CSRF, XSS, injection, SSRF, uploads, rate limiting, secrets, logs and sensitive data. Scan dependencies, containers, source and infrastructure. Review encryption, retention, deletion, backups and privacy obligations. Verify findings and negative paths; document residual risk.
**Artifacts:** threat model, security report, scan results, remediation evidence and residual-risk register.
**Gate:** no unresolved critical/high finding without documented approval from the accountable owner. This skill does not certify legal or regulatory compliance.

### 9. Performance and reliability
Profile before optimizing. Establish workload assumptions and measure key latency, database and frontend paths. Inspect N+1 queries, indexing, payload size, caching, concurrency, queues, resource limits and graceful degradation. Validate timeouts, retries, circuit breakers and idempotency. Define suitable service-level objectives and capacity thresholds.
**Artifacts:** baseline, load/profile results, bottleneck analysis and reliability risks.
**Gate:** critical paths meet agreed targets or have an approved remediation plan.

### 10. CI/CD and infrastructure readiness
Make development, test, staging and production configuration reproducible. Containerize where useful; pin and scan dependencies/images. Automate lint, static analysis, tests, builds and security checks. Manage secrets safely. Use infrastructure as code or repeatable provisioning where practical. Configure DNS, TLS, storage, databases, queues, backups, network boundaries, health checks, deployment strategy, rollback and recovery.
**Artifacts:** CI/CD workflows, deployment config, environment matrix, provisioning/runbook, backup and rollback procedures.
**Gate:** pipeline is reproducible; deployment and rollback paths are understood and tested proportionate to risk.

### 11. Staging and UAT
Deploy a release candidate to production-like staging. Verify configuration parity without exposing production secrets/data. Run migrations, smoke tests, critical E2E flows and integration checks. Verify analytics, logs, alerts, email/webhooks and background jobs. Conduct UAT against agreed criteria; record defects, retest fixes and capture designated-owner sign-off.
**Artifacts:** staging release record, smoke-test report, UAT evidence and defect disposition.
**Gate:** UAT and blocking staging checks are signed off; no unapproved critical/high defect remains.

### 12. Production release
Present exact version/commit, release scope, risks, approvals and rollback plan. Obtain explicit human approval before production deployment. Confirm backup/recovery and migration compatibility. Deploy using an appropriate rolling, blue/green, canary or controlled-maintenance strategy. Run production smoke tests and verify health, critical journeys and integrations. Monitor; halt or roll back if criteria fail. Record release metadata and exceptions.
**Artifacts:** approved release record, deployment log, production verification and changelog.
**Gate:** production deployment is explicitly approved and verified. Approval to prepare or test a release is not deployment approval.

### 13. Observability and product analytics
Instrument structured logs, metrics, traces and error reporting as appropriate. Track uptime, latency, error rates, queue health, resource saturation and dependency failures. Track relevant product events, funnels, activation, retention, conversion and revenue. Provide owner/admin dashboards with clear definitions, date ranges, segmentation and freshness. Define alerts, escalation owners and runbooks. Minimize personal data and verify signals against actual behavior.
**Artifacts:** telemetry/event taxonomy, KPI definitions, dashboards, alert rules and runbooks.
**Gate:** owners can detect material failures and understand product health through verified signals.

### 14. Documentation and handover
Maintain setup, architecture, API, configuration, deployment and troubleshooting docs. Document backup/restore, incident response and rollback. Provide onboarding and ownership boundaries. Update repository maps, ADRs, glossary and current-state handoff. Document intent, invariants, trade-offs and failure modes rather than duplicating source code.
**Gate:** another competent engineer/operator can build, deploy, troubleshoot and maintain the product using documentation and authorized access.

### 15. Release management and maintenance
Version releases and publish accurate changelogs. Manage feature flags, staged rollout and deprecation. Triage production issues and feedback by impact. Patch vulnerabilities and update dependencies deliberately. Monitor technical debt, reliability, cost, usage and KPIs. Feed lessons into ADRs, standards, backlog and discovery; rerun affected gates after material changes.
**Artifacts:** release notes, maintenance backlog, incident/postmortem records and improvement roadmap.
**Gate:** ownership, support path, maintenance cadence and next priorities are explicit.

## Lifecycle state and gate management
For each phase record status (not started, in progress, blocked, passed, accepted exception), owner, timestamp, required artifacts, verification evidence, unresolved risks, approver and next eligible phase. A document's existence does not prove a gate passed. A failed blocking gate prevents dependent work unless the accountable human owner records an explicit scoped exception.

## Brownfield assessment
1. Bootstrap/reconcile project knowledge.
2. Inspect Git state, architecture, docs, tests, CI, environments and release state.
3. Map actual maturity against the lifecycle phases.
4. Identify earliest missing/failed gate and highest-risk gaps.
5. Produce a prioritized remediation plan that preserves sound work.
6. Resume at the appropriate phase; do not redo completed work without cause.

## Outputs
Provide lifecycle assessment/current phase, prioritized plan, dependency map, quality-gate matrix, evidence-backed status, blockers, risks, approvals required and next action/owner.

## Quality checks
- [ ] Project knowledge is initialized or an equivalent is mapped.
- [ ] Scope and acceptance criteria are explicit.
- [ ] Architecture, data ownership and security boundaries are documented.
- [ ] Implementation is tested and reviewed incrementally.
- [ ] QA, security and performance checks have evidence.
- [ ] CI/CD, staging, rollback and production approval gates exist.
- [ ] Observability, product analytics and operational ownership are covered.
- [ ] Documentation and handoff support ongoing maintenance.
- [ ] Status claims match observed evidence.

## Boundaries
Do not invent validation, test results, security assurance, performance metrics or approvals. Do not deploy, merge, publish, spend, delete data or perform irreversible actions without explicit authorization. Do not force a stack or process that is not justified by project context. Obtain specialist legal, regulatory, accessibility or security review where product risk requires it.
