# Public Publication Readiness Audit

**Status: PRELIMINARY — NOT CLEARED FOR PUBLICATION**  
**Reviewed:** 2026-11-16  
**Target:** GitHub Pages project site at `https://alamiasoft.github.io/Alamia-Skills-System/`  
**Repository visibility:** Private (verified after PR #12 merge).  
**Publication decision:** Do not change repository visibility until all blockers below are resolved and the owner explicitly approves.

## Scope and evidence

Inspected the current `main` README, package metadata, root license, collection manifest, skill schema, architecture/specification documents, CLI installer, reconciler, CI workflow definitions, selected tests, and relevant merged PR diffs (#1, #4–#13). Also inspected the current portal implementation branch and the open PR #14.

A pattern scan was run against 124 changed-file patches from PRs #8 and #10–#13. It found no matches for the checked private-key, common GitHub/AWS/OpenAI token, credential-assignment, email-address, or private-network-IP patterns. This is a narrow scan of reviewed diffs, **not** a complete scan of all current files, all branches, tags, or Git history.

PR #12 was rebased onto the latest `main`, its missing exact `## Quality checks` heading was corrected, and all Python, Node 20 and Node 22 checks passed before it was merged. Merge commit: `9d37670722146a250692ffd720c4338cbff46e7b`.

## Confirmed repository facts

- The repository is private; default branch is `main`.
- The current catalogue contains **44 skills across 9 collections**, including 24 in Product Engineering after PR #12.
- The root license is MIT. It does not automatically override licenses or attribution requirements for vendored third-party material.
- The repository includes a Python project lifecycle runtime, portable skill library, npm installer, collection manifest, schemas, workflows and role profiles.
- The npm package declares Node.js >=18 and includes the CLI/catalog/distributable skill content; it does not package the Python lifecycle runtime.
- The existing Alamia Fluid Design examples are skill reference demos, not the full portal.
- PR #12 is merged and included in the current catalogue. PR #14 is the portal implementation and remains a separate draft until its build and artifact checks pass.

## Findings and publication blockers

### P0 — Complete repository and Git-history secret scan

The connector review cannot enumerate every current file and historical blob/ref. On a trusted machine, clone the repository, fetch all refs and tags, then run a full working-tree and all-ref scan before changing visibility:

```bash
git clone https://github.com/AlamiaSoft/Alamia-Skills-System.git
cd Alamia-Skills-System
git fetch --all --tags --prune
gitleaks dir --redact --no-banner .
gitleaks git --log-opts="--all" --redact --no-banner .
```

Review findings manually. Remove confirmed secrets and rotate them where necessary. Removing a secret from the current tree does not remove it from Git history.

### P1 — Upstream pinning and provenance consistency

`core/reconciler.py` can clone the Matt Pocock skills repository and AlamiaSoft/agent-pm when vendor directories are missing. The clone commands use shallow clones without checking out a recorded immutable commit. This conflicts with the pinned-provenance approach. The merged PR #5 patch introduced `vendor/UPSTREAMS.json`, but fetching that exact path from current `main` returned 404 in this review. Confirm whether the manifest is absent, relocated, or inaccessible; reconcile the provenance record and clone behavior before publication.

### P1 — Third-party license and attribution audit

The repository history documents vendored snapshots from Matt Pocock's skills repository and AlamiaSoft/agent-pm, with MIT licenses claimed in the provenance record. Verify the actual current tracked files, upstream license texts, notices, local overlays, and attribution obligations across all refs. Do not imply the root MIT license relicenses third-party content.

### P2 — Branch and pull-request hygiene

The repository has multiple historical feature/Codex branches. Review all branch/tag refs and remaining open PR contents for secrets, private notes, licensing, and unfinished material before making the entire repository public. PR #12 is now merged; do not delete historical branches without an explicit retention decision.

### P2 — Portal build and artifact review

The portal build must be green on PR #14. Inspect the generated `site/` artifact to ensure it contains only catalogue-registered skills, approved metadata/instructions, agent indexes and portal assets. It must not publish tests, vendor snapshots, private planning notes, runtime internals, or arbitrary repository files.

## Resolved items

- Product Engineering README count is synchronized at 24 skills after PR #12.
- `domains/domains.json` is being aligned with the nine collection identifiers in the portal implementation.
- PR #12 catalogue metadata and exact quality-check heading failures are fixed; its CI passed and the PR is merged.

## Portal publication rules

- Build only from the selected `main` ref and its canonical manifest.
- Use an allow-listed generated `site/` artifact; never copy the repository root wholesale.
- Publish only manifest-registered skills and preserve declared licenses and attribution.
- Keep the portal static and read-only; no accounts, backend, marketplace, payment, or 360 Skills scope.
- Keep repository visibility private until P0 and P1 findings are resolved and the owner approves publication.

## Exit criteria

- [ ] Full working-tree and all-ref secret scan completed; findings triaged and remediated.
- [ ] All branch/tag/open-PR exposure reviewed.
- [ ] Vendored files, licenses and provenance verified; unpinned clone behavior corrected.
- [ ] Portal generator and artifact tests pass on PR #14.
- [ ] Generated artifact reviewed for accidental source leakage.
- [ ] Owner explicitly approves repository visibility change.
