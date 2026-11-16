# Public Publication Readiness Audit

**Status: PRELIMINARY — NOT CLEARED FOR PUBLICATION**  
**Reviewed:** 2026-11-16  
**Target:** GitHub Pages project site at `https://alamiasoft.github.io/Alamia-Skills-System/`  
**Repository visibility:** Private (verified after PR #14 merge).  
**Publication decision:** Do not change repository visibility until all blockers below are resolved and the owner explicitly approves.

## Scope and evidence

Reviewed the current README, package metadata, root and vendored license files, catalogue manifest, skill schema, architecture/specification documents, CLI installer, reconciler, CI workflows, selected tests, Git tree paths, relevant merged PR diffs, and branch/PR metadata.

A pattern scan was run across **180 changed-file patches from PRs #1–#14**. It found two matches, both the same deliberate fake fixture in `tests/test_skill_learning.py`: `API_KEY = "this-is-a-real-looking-secret-value"`. This is a test value used to verify the candidate validator's credential detection, not a live credential. No other checked private-key, GitHub/AWS/OpenAI token, credential-assignment, or private-network-IP patterns were found. This is a narrow diff scan, **not** a complete scan of every current file, all branch tips, tags, or Git history.

PR #12 was rebased onto the latest `main`, its exact `## Quality checks` heading was corrected, and all Python, Node 20 and Node 22 checks passed before merge.

PR #14 was merged as `290b7a22355014788ab6aba27f59c36bf8c63405`. The post-merge Python portability, universal skills/installer, and GitHub Pages portal build workflows all passed. The generated artifact uploaded successfully; the deploy job was skipped as intended.

## Confirmed repository facts

- The repository remains private; default branch is `main`.
- The canonical catalogue contains **44 skills across 9 collections**, including 24 Product Engineering skills.
- The static portal is merged. It is generated from the canonical manifest and publishes only an allow-listed `site/` artifact.
- The npm package declares Node.js >=18 and includes the CLI/catalog/distributable skill content; it does not package the Python lifecycle runtime.
- The root license and both current vendor license files declare MIT.
- The current vendor tree contains 161 Matt Pocock snapshot blobs and 11 agent-pm blobs.
- The repository has 18 branch refs at the time of review. PRs #2 and #3 are closed without merge; their work was superseded by later merged PRs #4 and #5. Two temporary rebase branches created during this remediation now point to `main` and contain no unique tip changes.
- Tag enumeration was not confirmed by the available repository endpoint; do not assume there are no tags.

## Vendor provenance verification

Compared current vendored Git blob SHAs against the immutable upstream commits:

| Dependency | Pinned commit | Upstream blobs | Vendored blobs | Exact matches | Modified | Local-only |
|---|---|---:|---:|---:|---:|---:|
| Matt Pocock skills | `24fe0ef7737efae15c87225755e9f6f5965e4888` (`v1.3.1`) | 159 | 161 | 131 | 28 | 2 |
| agent-pm | `76d1a82ac0401221a00ca218f4eda72e7d344c12` | 11 | 11 | 11 | 0 | 0 |

For Matt Pocock, all upstream blobs are present. The 28 modified blobs are documentation overlays (21 under `docs/engineering`, 7 under `docs/productivity`); the two local-only blobs are the chief-of-staff skill files. Preserve these overlays during any future refresh. Both upstream projects and their vendored copies declare MIT.

Before PR #15, `main` had lost `vendor/UPSTREAMS.json`, and `core/reconciler.py` could shallow-clone moving default branches when vendor directories were absent. PR #15 restored the verified provenance manifest and changed fallback restoration to clone and verify immutable commit SHAs. PR #15 merged as `f54e2a2ac6304e981e0ffb01fe5ead676b508dd3`; its post-merge Python, vendor-pinning, portal, Node 20 and Node 22 checks all passed.

## Remaining publication blockers

### P0 — Complete repository and Git-history secret scan

The connector review cannot enumerate every current file and historical blob/ref. On a trusted machine, clone the repository, fetch all refs and tags, then run a full working-tree and all-ref scan before changing visibility:

```bash
git clone https://github.com/AlamiaSoft/Alamia-Skills-System.git
cd Alamia-Skills-System
git fetch --all --tags --prune
gitleaks dir --redact --no-banner .
gitleaks git --log-opts="--all" --redact --no-banner .
```

Triage the known fake test fixture as a false positive if the scanner reports it. Review every other finding manually. Remove confirmed secrets and rotate them where necessary. Removing a secret from the current tree does not remove it from Git history.

### P1 — Branch and pull-request hygiene

Review all 17 branch tips, closed unmerged PR refs, temporary rebase branches, and any tags before making the repository public. The old closed PR branches #2 and #3 are not current release sources, but their diffs remain reachable. Decide which historical branches should be retained and ensure no private notes, accidental credentials, or unfinished material are exposed.

### P1 — Final third-party attribution review

The two current vendored dependencies and their MIT license files have been identified and blob-compared. Before publication, complete the all-ref review for other copied assets, embedded examples, screenshots, fonts, and third-party materials. Preserve upstream attribution and do not imply the root MIT license relicenses third-party content.

### P2 — Public deployment approval

The portal artifact build is green, but deployment remains gated by `PAGES_PUBLISH_ENABLED == 'true'`. Do not set this variable or change repository visibility until the P0/P1 checks are complete and the owner explicitly approves publication.

## Portal publication rules

- Build only from the selected `main` ref and its canonical manifest.
- Use the allow-listed generated `site/` artifact; never copy the repository root wholesale.
- Publish only manifest-registered skills and preserve declared licenses and attribution.
- Keep the portal static and read-only; no accounts, backend, marketplace, payment, or 360 Skills scope.
- Keep the source repository private until the audit is cleared and the owner approves publication.

## Exit criteria

- [ ] Full working-tree and all-ref secret scan completed; findings triaged and remediated.
- [ ] All branch/tag/open-PR exposure reviewed, including the known fake test fixture. Branch tips were inventoried, but a full all-ref secret scan is still required.
- [ ] Remaining third-party materials and attribution reviewed.
- [ ] Generated portal artifact reviewed for accidental source leakage.
- [ ] Owner explicitly approves repository visibility change and public Pages deployment.
