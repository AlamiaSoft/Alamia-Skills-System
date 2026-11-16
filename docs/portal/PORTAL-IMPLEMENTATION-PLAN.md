# GitHub Pages Portal — Implementation Plan

## Goal

Create a public, static showcase and documentation portal for Alamia Skills System that serves both people and AI agents. This is the Alamia Skills System portal only. 360 Skills, marketplace features, accounts, payments and hosted execution are out of scope.

## URL

Project Pages URL: `https://alamiasoft.github.io/Alamia-Skills-System/`

The repository is currently private. Build and validate the site on a feature branch first. Public Pages availability depends on the organization's GitHub plan and repository visibility. Do not change repository visibility until `PUBLICATION-READINESS-AUDIT.md` is cleared and the owner approves.

## Human-facing experience

- Overview: what Alamia Skills System is and who it helps.
- Explore: searchable/filterable skill catalogue driven by `catalog/collections.json` and each skill's `skill.json`.
- Skill detail: purpose, description, domain, version, compatibility, requirements, risk, license, agent instructions and raw source links.
- Collections: installable collection contents and CLI commands.
- Workflows and role profiles: explain compositions and recommendations without claiming they are automated execution engines.
- Getting started: prerequisites, install commands, repository links and contribution path.
- Architecture and governance: canonical sources, skill contract, validation and approval boundaries.

## Agent-facing resources

Generate from the same canonical repository data:
- `llms.txt` — concise orientation and links to machine-readable resources.
- `agents.json` — stable entry point describing catalogue, collections and resource URLs.
- `data/catalog.json` — normalized catalogue and collection metadata.
- `data/skills/<id>.json` and `data/skills/<id>.md` — metadata and agent instructions for each published skill.
- A sitemap and stable per-skill pages at `skills/<id>/`, plus raw Markdown and JSON resources.

Do not manually duplicate skill metadata in site source. Do not publish unregistered candidate skills or unmerged PR content.

## Technical approach

- Static HTML, CSS and vanilla JavaScript; no server-side runtime.
- A Python standard-library build script reads the canonical manifest, validates referenced skill files and generates a curated `site/` artifact.
- GitHub Actions runs the build and validation on pull requests. Deployment occurs only from `main` after the repository has been approved for public publication and Pages is enabled.
- Keep the artifact allow-listed. Do not copy the whole repository into the Pages artifact.
- Use relative URLs so the project Pages path works.
- Test keyboard navigation, responsive layout, direct skill links, search/filter behavior, raw Markdown/JSON access and 404 handling.

## Release sequence

1. Complete and clear the publication audit.
2. Resolve P1 catalogue/provenance/license issues.
3. Build the portal and validate generated artifact in CI.
4. Review the artifact for accidental source leakage.
5. Owner approves repository public visibility.
6. Enable Pages with GitHub Actions and verify the project URL.
7. Update personal portfolio and GitHub profile.
8. Publish LinkedIn announcement only after the portal is accessible.
