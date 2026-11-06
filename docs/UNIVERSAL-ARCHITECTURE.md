# Universal Skills Architecture

- **Core runtime:** existing project discovery, lifecycle orchestration, reconciliation and validation; domain-neutral.
- **Canonical skill library:** portable capabilities grouped by professional domain.
- **Collections:** installable sets (engineering, SEO, content, marketing, video, research, business).
- **Workflows:** ordered compositions with explicit handoffs and completion criteria.
- **Role profiles:** recommended collections/workflows for professional roles.
- **Distribution:** dependency-free npm CLI installs selected skills to `.agents/skills/<id>/`.
- **Future commercial services:** storefront, entitlement, hosted education and execution remain separate.

Existing `core/`, `lifecycle/` and first-party `skills/` paths stay stable for backwards compatibility. New domain skills live under `catalog/domains/<domain>/<skill-id>/`. `catalog/collections.json` is the installer source of truth. The npm package bundles the installer and distributable content, not the Python lifecycle runtime or vendor repositories.
