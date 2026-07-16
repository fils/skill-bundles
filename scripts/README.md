# Scripts

Helper tools for the skill-bundles research wiki (OKF v0.1 Knowledge Bundle under `wiki/`).

**Spec:** https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md  
**Local format rules:** `wiki/concepts/okf-knowledge-bundle.md`  
**Agent workflow:** repo-root `PLAN.md`

## OKF tooling (current — use these)

| Script | Purpose |
|--------|---------|
| `okf-lint.py` | **Primary daily gate.** OKF §9 conformance + soft graph checks (catalog links, inbound degree, index completeness). |
| `convert-to-okf.py` | One-shot / re-run migration helper (frontmatter, relative MD links, index generation). |
| `link-catalog-and-digests.py` | Link primary catalog bullets, regenerate indexes, digest→example links, Q&A cross-links. |

```bash
# From repo root — Hermes / daily agent should run this only
python3 scripts/okf-lint.py
python3 scripts/okf-lint.py --strict   # also fail on soft issues
python3 scripts/convert-to-okf.py --dry-run
python3 scripts/convert-to-okf.py
python3 scripts/link-catalog-and-digests.py   # after bulk catalog/digest link repairs
```

## Legacy (do not use in daily loop)

| Script | Purpose |
|--------|---------|
| `wikilink-lint.py` | Deprecated; **delegates to** `okf-lint.py`. |
| `wikilink-lint-2026-*.py` | Dated historical Obsidian-era copies. **Ignore.** |
| `wiki-integrity-check.py` | Pre-OKF orphan analysis (stem-based). Optional research only. |
| `phase0_update_meta.py`, `update-metrics-*.py` | Ad-hoc metrics helpers. |

**Hard rule for agents:** use **relative markdown links** only; never reintroduce `[[wikilink]]` syntax; never treat dated wikilink linters as the gate.
