---
type: Concept
title: OKF Knowledge Bundle — Format Rules for this Wiki
description: Local summary of Open Knowledge Format (OKF) v0.1 rules used by the skill-bundles wiki for agents and humans.
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
tags: [okf, format, conformance, agent-workflow]
timestamp: 2026-07-16T00:00:00Z
date: 2026-07-16
---

# OKF Knowledge Bundle — Format Rules for this Wiki

This repository's `wiki/` directory is an **Open Knowledge Format (OKF) v0.1** Knowledge Bundle.

**Authoritative spec:** [OKF SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)

The daily research *workflow* is inspired by Karpathy-style LLM knowledge bases (compound daily notes, agent ownership of the wiki). The **document format** is OKF — not Obsidian, not bare `[[wikilink]]` markup.

## Bundle root

- Bundle root: `wiki/`
- Concept ID: path under `wiki/` without `.md` (e.g. `examples/skill0-skill-internalization`)
- Outside the bundle: `raw/`, `scripts/`, `PLAN.md`, `resources/`

## Required frontmatter (every concept)

Every non-reserved `.md` file under `wiki/` must start with YAML frontmatter including:

```yaml
---
type: Skill Bundle Example   # required
title: Human-readable title  # recommended
description: One sentence    # recommended
resource: https://...        # optional canonical URI
tags: [optional]
timestamp: 2026-07-16T00:00:00Z
# plus any producer extensions
---
```

### Types used in this bundle

| `type` | Directory / file |
|--------|------------------|
| `Skill Bundle Example` | `examples/` |
| `Concept` | `concepts/` |
| `Paper` | `papers/` |
| `Tool` | `tools/` |
| `Daily Digest` | `daily-digests/` |
| `Q&A` | `qa/` |
| `Publication` | `skill-bundles.md` |
| `Metrics` | `metrics.md` |

## Reserved filenames (OKF §3.1)

| File | Role |
|------|------|
| `index.md` | Progressive disclosure listing (no concept `type`; root may have `okf_version` only) |
| `log.md` | Chronological update history |

## Cross-linking (OKF §5)

**Use relative markdown links** so links work on GitHub and in OKF consumers:

```markdown
[SkillOpt](../examples/skillopt-trainable-skill-parameters.md)
```

**Do not use:**

```markdown
[[skillopt-trainable-skill-parameters]]
```

Absolute bundle-relative paths starting with `/` are OKF-legal when the bundle is the publish root; in this monorepo they break GitHub navigation, so this project standardizes on **relative** links (§5.2).

## Citations (OKF §8)

Prefer a trailing `# Citations` section for external sources that support claims.

## Conformance gate

```bash
python3 scripts/okf-lint.py
```

Hard failures: missing frontmatter, missing `type`, residual `[[wikilinks]]`.

Use only `okf-lint.py`. Dated `scripts/wikilink-lint-*.py` files are legacy and must not drive the daily loop.

## Related

- Bundle entry: [index](../index.md)
- Primary publication: [Skill Bundles catalog](../skill-bundles.md)
- Agent workflow contract: `PLAN.md` (repo root, outside bundle)

# Citations

[1] [Open Knowledge Format (OKF) SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
