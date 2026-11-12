# Alamia Skills System

> **A universal, portable capability system for AI agents — across engineering, SEO, content, marketing, video, research and business operations.**

Alamia Skills provides reusable professional capabilities, curated installable collections, composable workflows and role profiles. The existing lifecycle runtime remains available for project-aware software engineering; the skill library is no longer limited to developers.

## Install collections

Requires Node.js 18 or newer.

```bash
npx alamia-skills-install --seo
npx alamia-skills-install --growth
npx alamia-skills-install --content
npx alamia-skills-install --marketing
npx alamia-skills-install --video
npx alamia-skills-install --research
npx alamia-skills-install --business
npx alamia-skills-install --engineering
npx alamia-skills-install --all
```

Additional options: `--list`, `--dry-run`, `--target ../project`, and `--force`. Skills install into `.agents/skills/<skill-id>/`. Existing skill directories are preserved unless `--force` is specified.

**Publication note:** this repository contains the npm package source and CLI. The public `npx` command becomes available after the package is published to npm. Validate locally with `npm test` and `npm pack` until publication.

## Collections

| Collection | Capabilities |
|---|---|
| Engineering | DAG task planning, engineering discipline, operational tooling |
| SEO | Keyword intent mapping, technical SEO audit, content optimization |
| Growth | Product analytics, KPI frameworks, event tracking, owner dashboards, SEO and growth measurement |
| Content | Editorial briefs, evidence-led articles, repurposing |
| Marketing | Campaign strategy, email campaigns, landing-page reviews |
| Video | Script development, short-form repurposing |
| Research | Research plans, source synthesis |
| Business | SOP builder, meeting-to-execution |

The canonical manifest is `catalog/collections.json`.

## Architecture

- `core/`: existing project discovery, state engine and non-destructive reconciler.
- `lifecycle/`: bootstrap, implement, QA, architecture review and session-end orchestration.
- `skills/`: existing first-party skills, retained at their current paths.
- `catalog/domains/`: independently installable domain skills.
- `catalog/collections.json`: source of truth for collection membership and CLI installation.
- `workflows/`: examples composing skills into processes (specifications, not an automated runner).
- `profiles/`: recommended collections/workflows for professional roles.
- `domains/`: canonical domain taxonomy.
- `schemas/`: machine-readable skill metadata contract.

See [Universal Architecture](docs/UNIVERSAL-ARCHITECTURE.md) and [Universal Skill Specification](docs/UNIVERSAL-SKILL-SPEC.md).

## Universal skill contract

Each distributable skill contains `SKILL.md` (purpose, activation, inputs, procedure, outputs, quality checks and boundaries) and `skill.json` (stable ID, domain, version, compatibility, dependencies, tags and risk). Optional supporting assets may be included.

Skills describe capabilities; workflows compose capabilities; role profiles recommend collections and workflows. Keep these concepts distinct.

## Existing engineering lifecycle

The project-aware Python runtime remains intact and reconciles lifecycle skills without overwriting project-owned files:

```text
bootstrap → implement → qa → architecture-review → session-end
```

Run `python Alamia-Skills-System/core/reconciler.py` from a target project containing this system. The runtime and vendored integrations are separate from the lightweight npm installer.

## Validation

```bash
python tests/test_portability.py
python -m unittest tests.test_catalog
npm test
npm pack --dry-run
```

GitHub Actions runs Python regression tests, catalog validation, Node installer tests, npm package-content checks and a packed-package CLI smoke test.

## Future services

The local format and installer do not depend on accounts, payment providers or hosted services. Storefront, lifetime entitlements, referral rewards, hosted education and hosted execution remain separate future layers.

## License and attribution

Alamia first-party system and skills are MIT unless stated otherwise. Bundled third-party materials retain their original licenses and attribution in their vendor directories.
