# agentskill-sh/ags — `/learn` Command + Security Scoring Marketplace

**Source:** https://github.com/agentskill-sh/ags
**Date Added:** 2026-06-01 (Iteration 13)
**License:** MIT | **Language:** TypeScript 92.8% / JavaScript 7.2% | **Stars:** 22 | **Forks:** 8
**Stats:** 100,000+ skills, 15+ platforms, 52 commits, 3 contributors
**Bundle Type:** Marketplace · Security Scoring · In-Agent Discovery · Versioned Distribution
**Confidence:** 9/10

## Name & Origin

The `ags` (Agent Skills) repo is the official home for the **agentskill.sh** CLI and skills. It provides tooling to **search, install, manage, and rate** agent skills across 15+ AI coding platforms. It is, in effect, a **security-scored marketplace** with both a CLI and an in-agent `/learn` skill interface.

> After incidents like [OpenClaw](https://www.koi.ai/blog/openclaw-when-ai-skills-attack) showed how malicious skill files can compromise agents, vetting matters.

## Skills Included (3 skills + 1 CLI)

| Component | Description |
|---|---|
| `ags` CLI | npm-published terminal tool — `ags search/install/list/update/remove/feedback` |
| `/learn` skill | In-agent search + install + context-aware recommendations |
| `review-skill` skill | Reviews SKILL.md files, scores 10 quality dimensions |

## Context Elements (12-Category Threat Taxonomy)

`agentskill.sh` runs server-side static analysis on every skill across **12 threat categories**:

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

## How Context Elements Support Skills

`ags` is a **marketplace-with-policy-as-code** for skill bundles. The 12-category threat taxonomy is a *security specification* — a kind of SHACL for skill files. Every install path is gated by both server-side (the registry score) and client-side (the `/learn` second scan) checks, which is a defense-in-depth composition.

The **content SHA tagging** is essentially **Merkle-root provenance** for installed skills — the same provenance pattern that [[nvidia-verified-agent-skills]] uses with OpenSSF signing. Two independent implementations of the same underlying pattern (immutable identifier for a skill version).

## Composition Notes

- **Two-layer security model:** Server (registry) + Client (`/learn`) — defense in depth
- **Versioning:** Every installed skill tagged with content SHA. `/learn update` shows diffs — no silent breakage.
- **Feedback loop:** Agents auto-rate skills 1-5 with comments after use. Best skills surface, broken ones get community-flagged.
- **Cross-platform install paths:** Different agents get different skill directories (`.claude/skills/`, `.codex/skills/`, etc.) — handled by the CLI.
- **Plugin marketplace variant:** Claude Code only — `/plugin marketplace add https://agentskill.sh/marketplace.json` — but the plugin installs *only* `/learn`, not all skills.
- **Quality scoring:** `review-skill` scores 10 quality dimensions — separate from the 12-category security scoring (the two are independent axes).

## Bundle Density

One of the most bundle-dense examples in the catalog:
- **Skills:** `ags` CLI + `/learn` skill + `review-skill` skill
- **Context elements:** 12-category threat taxonomy, 0-100 security score, 1-5 quality score, 10 quality dimensions, content-SHA versioning
- **Distribution:** npm CLI, in-agent slash command, Claude Code plugin marketplace, JSON output mode
- **Telemetry:** agents auto-rate, 110k+ skills scanned, security dashboard

## Convergence Signal

The README directly cites the Koi AI blog post on OpenClaw — the same incident that motivated the [[nemoclaw-security-scanner]] and [[owasp-agentic-skills-top-10]] entries in our catalog. **Three independent projects converging on the same threat model** is strong signal that the threat taxonomy is now well-defined.

## Reproducibility

**High.** Open-source CLI, public GitHub repo, npm package, security dashboard accessible without auth. Threat taxonomy is published (12 categories listed in README).

## Bundle Links
- [[nemoclaw-security-scanner]] — Convergent security scanner (same OpenClaw threat model)
- [[owasp-agentic-skills-top-10]] — Defines 10-class vulnerability taxonomy
- [[agentic-trust-framework-csa]] — 4-level Zero Trust maturity model
- [[purplebox-supply-chain-security]] — 6-vector attack taxonomy
- [[nvidia-verified-agent-skills]] — OpenSSF signing (another provenance implementation)
- [[mondoo-agent-skills-security]] — Security skills-as-scanners pattern
- [[skill-validator-cli]] — Local/pre-commit validation
- [[validate-skill-github-action]] — CI/CD structural validation
