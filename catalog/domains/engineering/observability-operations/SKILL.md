---
name: observability-operations
description: >-
  Instrument and operate service health, logs, metrics, traces, alerts, incident response and product KPI dashboards.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Observability and Operations

## Purpose
Instrument and operate service health, logs, metrics, traces, alerts, incident response and product KPI dashboards.

## Activation
Instrument and operate service health, logs, metrics, traces, alerts, incident response and product KPI dashboards.

## Inputs
Critical journeys; service topology; owners; privacy rules; SLOs; business KPI definitions.

## Procedure
1. Identify critical services, dependencies, journeys and failure modes.
2. Define structured logs, metrics and traces while excluding secrets and unnecessary personal data.
3. Instrument availability, latency, errors, saturation, queue and dependency health.
4. Define product events and KPI formulas where relevant.
5. Build dashboards with definitions, filters, units and data freshness.
6. Set actionable alert thresholds, routing, owners and runbooks.
7. Generate representative events and verify calculations and alert delivery.

## Outputs
Telemetry/event taxonomy; KPI dictionary; dashboards; alert rules; runbooks; signal checks.

## Quality checks
- [ ] Signals are actionable and privacy-conscious; alerts have owners; KPI calculations reconcile.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Do not collect data without purpose or claim accuracy without validation. Avoid noisy alerts and sensitive logging.
