---
name: product-analytics-growth-seo
description: Audit and improve product measurement, acquisition, engagement, retention, monetization visibility, operational observability and SEO for websites, apps, PWAs and SaaS products.
license: MIT
metadata:
  domain: growth
  version: "1.0.0"
---

# Product Analytics, Growth & SEO

## Purpose and activation

Use this skill when a project owner needs to understand product performance, define meaningful KPIs, instrument user journeys, establish analytics and operational reporting, improve organic search visibility, or build an owner-facing growth dashboard.

This capability is project-agnostic. Adapt recommendations to the product type, business model, audience, lifecycle stage, technical stack, privacy obligations, budget and existing infrastructure. Do not assume a particular analytics vendor, cloud provider, framework, database or monetization model.

## Inputs

Gather what is available; identify material gaps rather than inventing answers.

- Product/project description, audience, value proposition and lifecycle stage
- Business model, primary outcomes, conversion goals and monetization plans
- Application types and surfaces: website, mobile app, PWA, SaaS, API or marketplace
- Architecture, stack, hosting, data stores and existing admin/analytics systems
- Existing analytics properties, event specifications, tag managers and search tools
- User journeys, acquisition channels, onboarding and retention mechanisms
- Existing traffic, event, revenue, support, infrastructure and SEO data
- Privacy, consent, data residency, security and retention requirements
- Budget, preferred tools, access constraints and implementation permissions

## Procedure

### 1. Discover the product and define outcomes

1. Inspect the repository, deployed product (when access is authorized), documentation, existing dashboards and analytics configuration.
2. Map the primary user journeys from acquisition through activation, core value, repeat use and conversion/monetization where applicable.
3. Identify the product's north-star outcome and a small set of supporting input metrics.
4. Separate product, marketing, commercial and operational measurement needs.
5. Distinguish existing capabilities from planned, unavailable or unverified capabilities.

### 2. Define a useful KPI framework

For each KPI, document its business question, precise definition, formula, unit, segmentation, time window, source of truth, owner, refresh cadence, caveats and target (only when a target is approved).

Consider relevant measures rather than blindly implementing every category:

- Acquisition: users/visitors, sessions, source/medium, campaign attribution, landing pages, geography and device mix.
- Activation: sign-ups or first-use events, onboarding completion, time to first value and activation rate.
- Engagement: active users, key actions, frequency, depth, feature adoption and task completion.
- Retention: cohort-based D1/D7/D30 or product-appropriate retention, returning users, churn and reactivation.
- Conversion: funnel progression, drop-off, lead or trial conversion, purchase/subscription conversion and abandonment.
- Revenue: gross/net revenue, ARPU/ARPPU, MRR/ARR where applicable, refunds, cancellations and sponsorship/advertising revenue where relevant.
- Referral and virality: shares, invites, referred visits, referral activation and resulting conversion.
- SEO: impressions, clicks, CTR, average position, indexed pages, organic landing-page sessions and organic conversions.
- Reliability and operations: availability, latency, error rates, failed jobs, API usage, quota/cost, deployment health and data-pipeline freshness.
- Installation/platform adoption: install prompt views/acceptance and app launches in installed/standalone contexts where measurable.

Do not recommend irrelevant metrics merely because they are common SaaS KPIs. Distinguish unique people, anonymous identifiers, accounts, sessions, devices, installs and page views. Define denominators and time zones explicitly.

### 3. Design the measurement plan

1. Map business questions and KPIs to observable events and properties.
2. Define a consistent event taxonomy: event name, trigger, required properties, optional properties, identity rules, deduplication key, consent category and owning surface.
3. Specify lifecycle events, core-value events, conversion events and operational events separately.
4. Define anonymous-to-authenticated identity resolution and account-linking behavior without losing historical attribution or creating duplicate people.
5. Include event versioning, schema validation, timestamps (prefer UTC storage), environment separation and idempotency.
6. Avoid collecting sensitive data or sending emails, credentials, raw user content or direct identifiers to third-party analytics unless explicitly justified, lawful and approved.
7. Define consent behavior, opt-out handling, retention periods, deletion/export processes and access controls appropriate to the jurisdiction and product.
8. Identify metrics that require first-party authoritative records rather than analytics-platform estimates.

### 4. Select tools and integrations

Evaluate existing tools first. Recommend the smallest practical stack that meets requirements and budget.

Possible categories include:

- Product/web analytics: GA4, privacy-focused analytics, self-hosted analytics or existing product telemetry.
- Search performance: Google Search Console, Bing Webmaster Tools and relevant search-provider equivalents.
- Edge/hosting analytics: Cloudflare Web Analytics, platform metrics or hosting-provider telemetry.
- Performance: real-user monitoring, Core Web Vitals, synthetic checks and PageSpeed/Lighthouse.
- Error monitoring: application error tracking and structured logs.
- Business data: first-party database, warehouse or existing reporting layer.
- Dashboards: existing admin console, BI tool or lightweight reporting interface.

For each proposed integration, state what it measures, what it cannot measure, pricing/limits to verify, privacy implications, required access, data ownership and setup steps. Never claim an integration is configured or data is available without verifying it. Do not create accounts, change production settings, transmit data or publish credentials without approval.

### 5. Establish sources of truth and data quality

1. Identify the authoritative system for each metric.
2. Use first-party records for transactions, subscriptions, entitlements, gameplay, orders or other business-critical facts.
3. Treat third-party analytics as behavioral/attribution reporting, not automatically authoritative financial or operational ledgers.
4. Document expected discrepancies between tools (consent, blockers, sampling, attribution, time zones, identity and ad blockers).
5. Add validation for missing/duplicate events, impossible sequences, schema drift, bot traffic and stale integrations.
6. Provide data freshness and coverage indicators on dashboards.
7. Prevent internal/admin traffic and automated monitoring from distorting user metrics where practical.

### 6. Design owner-facing reporting

Propose a role-appropriate dashboard with:

- Executive overview: north-star KPI, acquisition, activation, retention and business outcomes.
- Funnel and cohort analysis: conversion steps, drop-offs and retention cohorts.
- Acquisition and SEO: channels, campaigns, search queries, landing pages and organic outcomes.
- Monetization: only the revenue streams and conversion models the project actually uses.
- Product usage: key features, workflows and adoption.
- Operations: uptime, latency, errors, scheduled tasks, resource consumption and integration health.
- Data quality: last successful sync, event volume, missing data and tracking status.

For each card/chart, provide its definition, source, time range, filters and drill-down. Clearly label estimates, delayed data, unavailable integrations and illustrative placeholders. Never fabricate counts or populate a live dashboard with invented demo values.

### 7. Audit and improve SEO where applicable

1. Determine whether public, indexable search traffic is relevant to the product. Do not apply public SEO assumptions to private apps, authenticated dashboards or API-only services.
2. Inspect crawlability, indexability, robots directives, XML sitemaps, canonical URLs, redirects, status codes, metadata, heading structure, internal links, structured data, duplicate/thin pages, mobile usability and performance.
3. Review search intent, audience needs, landing-page relevance, information architecture and content quality.
4. Recommend useful, original pages and content only where they serve real search intent and product value.
5. Configure or recommend search-engine tools such as Search Console and Bing Webmaster Tools where relevant.
6. Verify ownership, sitemap submission, indexing and search reporting only when access and evidence are available.
7. Avoid doorway pages, scaled low-value AI content, keyword stuffing, fabricated reviews/claims and misleading structured data.
8. Protect private routes, admin pages, API endpoints and sensitive data from indexing.

### 8. Prioritize implementation

Create a backlog ranked by impact, confidence, effort, dependency, risk and time-to-value. Separate:
- Measurement gaps that prevent decisions
- Low-cost configuration tasks
- Instrumentation/code changes
- Dashboard/reporting work
- SEO fixes and content opportunities
- Longer-term experimentation and optimization

Prefer incremental implementation. Reuse the project's stack and existing infrastructure. Do not introduce a warehouse, tag manager, BI platform or paid vendor without a demonstrated need.

## Outputs

Produce an evidence-based package adapted to project scope:

1. Product and measurement discovery summary.
2. KPI dictionary with definitions, formulas, sources, segmentation and cadence.
3. User journey/funnel map.
4. Event tracking plan and event/property schema.
5. Analytics and integration architecture with tool comparison and cost/privacy notes.
6. Source-of-truth and data-quality plan.
7. Owner dashboard information architecture and metric specifications.
8. SEO audit and prioritized technical/content recommendations, when applicable.
9. Implementation backlog with acceptance criteria and dependencies.
10. Validation report distinguishing implemented, configured, verified, unavailable and proposed work.

Use repository-appropriate paths and formats. If the caller requests machine-readable output, provide structured JSON/CSV alongside human-readable documentation.

## Quality checks

- Every KPI answers a real business question and has an unambiguous definition and denominator.
- Every event has a clear trigger, properties, identity and deduplication behavior.
- Metrics distinguish users, accounts, sessions, devices, installations and events.
- First-party authoritative records are identified for business-critical measures.
- Privacy, consent, minimization, access and retention are addressed.
- Tool capabilities and limitations are represented accurately.
- Dashboard figures are traceable to documented sources and definitions.
- SEO recommendations are relevant to indexable public surfaces and supported by evidence.
- Observed facts, hypotheses, estimates and recommendations are clearly distinguished.
- Implementation is tested in a non-production environment before production rollout.
- No fabricated data, rankings, traffic, conversions, revenue, testimonials or performance claims appear.

## Boundaries

- Do not invent KPIs, targets, traffic, installs, users, revenue or analytics results.
- Do not claim tracking, integrations, SEO indexing or dashboards are live without verification.
- Do not treat analytics-platform counts as exact or complete user counts.
- Do not collect unnecessary personal or sensitive information.
- Do not expose secrets, credentials, tokens or raw personal data in events, logs or reports.
- Do not change production analytics, DNS, tags, consent settings, billing or deployment configuration without explicit approval.
- Do not publish content, create paid accounts, purchase services or enable advertising without approval.
- Do not promise search rankings, traffic growth, conversion lifts or revenue outcomes.
- Do not force a SaaS metric framework onto products whose business model does not support it.
- Clearly state access limitations and missing evidence; provide a useful plan without pretending unavailable work was completed.
