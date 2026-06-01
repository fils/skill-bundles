# agentskill-sh/ags — `/learn` Command + Security Scoring Marketplace

**Extracted:** 2026-06-01
**Source:** https://github.com/agentskill-sh/ags
**License:** MIT | **Language:** TypeScript 92.8% / JavaScript 7.2% | **Stars:** 22 | **Forks:** 8
**Stats:** 100,000+ skills, 15+ platforms, 52 commits, 3 contributors (romainsimon, claude, github-actions[bot])

## What It Is

The `ags` (Agent Skills) repo is the official home for the **agentskill.sh** CLI and skills. It provides tooling to **search, install, manage, and rate** agent skills across 15+ AI coding platforms. It is, in effect, a **security-scored marketplace** with both a CLI and an in-agent `/learn` skill interface.

## Two-Layer Security Model

> After incidents like [OpenClaw](https://www.koi.ai/blog/openclaw-when-ai-skills-attack) showed how malicious skill files can compromise agents, vetting matters.

### Server-side (agentskill.sh)
Static analysis on every skill across **12 threat categories**:

1. Command injection
2. Data exfiltration
3. Credential harvesting
4. Prompt injection
5. Obfuscation
6. Sensitive file access
7. Persistence mechanisms
8. External calls
9. Reverse shells
10. Destructive commands
11. Social engineering
12. Supply chain attacks

- Each skill gets a **security score (0-100)**
- **110,000+ skills scanned, 100% coverage**
- Skills scoring **below 30** require explicit confirmation before installation
- Live dashboard: https://agentskill.sh/security

### Client-side (`/learn`)
Performs a second scan before writing files to the local skill directory.

## Distribution Components

| Component | Description |
|---|---|
| `ags` CLI | npm-published terminal tool — `ags search/install/list/update/remove/feedback` |
| `/learn` skill | In-agent search + install + context-aware recommendations |
| `review-skill` skill | Reviews SKILL.md files against best practices, scores 10 quality dimensions |

## Why It Matters for the Catalog

`ags` is a **marketplace-with-policy-as-code** for skill bundles. It complements:

- **OWASP Agentic Skills Top 10** (catalog): Defines *what* bad skills do
- **Agentic Trust Framework / CSA** (catalog): Defines *maturity levels* for trust
- **Mondoo Security Skills** (catalog): Bundles security *scanners* as skills
- **PurpleBox Supply Chain** (catalog): Classifies attack vectors

`ags` provides the *infrastructure* — a registry that enforces the rules those frameworks define.

## OpenClaw Incident Reference

The README directly cites the [Koi AI blog post on OpenClaw](https://www.koi.ai/blog/openclaw-when-ai-skills-attack) — the same incident that motivated the **Nemoclaw security scanner** and **OWASP AST10** entries in our catalog. Three independent projects converging on the same threat model is strong signal that the threat taxonomy is now well-defined.

## Composition Notes

- **Versioning:** Every installed skill is tagged with a content SHA. `/learn update` shows diffs — no silent breakage.
- **Feedback loop:** Agents auto-rate skills 1-5 with comments after use. Best skills surface, broken ones get community-flagged.
- **Cross-platform install paths:** Different agents get different skill directories (`.claude/skills/`, `.codex/skills/`, etc.) — handled by the CLI.
- **Plugin marketplace variant:** Claude Code only — `/plugin marketplace add https://agentskill.sh/marketplace.json` — but the plugin installs *only* `/learn`, not all skills.
- **Quality scoring:** `review-skill` scores 10 quality dimensions — a separate axis from the 12-category security scoring (the two are independent).

## Bundle Density

This is one of the most bundle-dense examples in the catalog:
- Skills: `ags` CLI + `/learn` skill + `review-skill` skill
- Context elements: 12-category threat taxonomy, 0-100 security score, 1-5 quality score, 10 quality dimensions, content-SHA versioning
- Distribution: npm CLI, in-agent slash command, Claude Code plugin marketplace, JSON output mode
- Telemetry: agents auto-rate, 110k+ skills scanned, security dashboard

## Reproducibility Assessment

**High.** Open-source CLI, public GitHub repo, npm package, security dashboard accessible without auth. Threat taxonomy is published (12 categories listed in README).
