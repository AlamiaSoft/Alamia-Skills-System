---
name: ai-integration-engineering
description: >-
  Add LLMs, agents, MCP tools, retrieval and AI workflows with evaluation, safety and cost controls.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# AI Integration Engineering

## Purpose
Add LLMs, agents, MCP tools, retrieval and AI workflows with evaluation, safety and cost controls.

## Activation
Add LLMs, agents, MCP tools, retrieval and AI workflows with evaluation, safety and cost controls.

## Inputs
User outcome; data classification; provider/model constraints; latency/cost budget; tool contracts; evaluation data.

## Procedure
1. Confirm AI is justified over deterministic software.
2. Select provider/model abstraction and fallback based on quality, latency, privacy and cost.
3. Version prompts, schemas, tool permissions and context contracts.
4. Treat model/retrieved output as untrusted; validate outputs and authorize tools server-side.
5. Protect tenant boundaries, secrets and sensitive data.
6. Evaluate quality, safety, prompt injection and tool misuse.
7. Instrument cost, latency and failures; add quotas and graceful fallback.

## Outputs
AI design; provider/tool contracts; evaluation cases/results; safety controls; usage budgets; metrics.

## Quality checks
- [ ] Outputs are validated; tools are least-privilege; cost/latency and failure behavior are measurable.
- [ ] Work is traceable to the requested scope and project standards.
- [ ] Relevant project knowledge and documentation are updated.

## Boundaries
Never expose secrets or trust model-generated authorization. Do not add AI where simpler logic is safer.
