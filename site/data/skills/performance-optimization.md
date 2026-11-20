---
name: performance-optimization
description: >-
  Investigate latency, throughput, resource use, database behavior and scale readiness.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Performance Optimization

## Purpose
Investigate latency, throughput, resource use, database behavior and scale readiness.

## Activation
Investigate latency, throughput, resource use, database behavior and scale readiness.

## Inputs
Performance targets; workload assumptions; telemetry; representative data; environment; critical journeys.

## Procedure
1. Define user-visible objectives and representative workloads.
2. Establish baseline with profiling, traces, query plans and frontend measurements.
3. Locate bottlenecks before changing code; inspect N+1, payloads, indexes, cache and rendering.
4. Test concurrency, queues, pools, memory, CPU and external limits.
5. Optimize the smallest bottleneck and remeasure under the same workload.
6. Test degradation, timeouts, backpressure and resource exhaustion.
7. Document capacity assumptions and thresholds.

## Outputs
Baseline/post-change measurements; bottleneck analysis; optimization diff; load report; capacity notes.

## Quality checks
- [ ] Measurements are reproducible and improvement does not regress correctness/security.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Do not optimize by intuition or present synthetic results as production facts. Protect tenant isolation in caches.
