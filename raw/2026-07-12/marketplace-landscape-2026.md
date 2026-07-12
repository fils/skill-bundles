# AI Agent Skills Marketplace Landscape 2026

**Source:** https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026
**Date:** 2026-07-12
**Signal:** 8/10

## Overview

The agent skills ecosystem grew from one registry in December 2025 to **eight major marketplaces** by Q2 2026. This is a comprehensive comparison of all major skill marketplaces.

## Eight Major Marketplaces (April 2026)

| Marketplace | Skills Listed | Curation | Security Review | Creator Payments | MCP Live Access |
|---|---|---|---|---|---|
| **Skills.sh** | ~2,000 | Community submissions | None | No | No |
| **SkillsMP** | 800,000+ | Scraped from GitHub, 2+ stars | None | No | No |
| **LobeHub** | 169,000+ | Scraped | None | No | No |
| **ClaudeSkills.info** | 658 | Community + official | None | No | No |
| **MCP Market** | ~500 | Submission-based | None | No | Partial |
| **Anthropic official** | ~20 | Manual, Anthropic-verified | Internal audit | No | No |
| **Plugin marketplaces (GitHub)** | 2,500+ registries | Per-owner | None | No | No |
| **Agensi** | 200+ | Manual + automated | 8-point scan | Yes, 70/30 split | N/A (curl install) |

## Key Insights

### Catalog Size is Misleading
- SkillsMP's 800,000 = indexed public GitHub repos with no quality filter beyond "has 2 stars"
- Many are abandoned experiments, half-finished tests, or duplicates
- The catalog size that matters: how many skills work well enough that developers use them repeatedly

### Security Problem
- Security audit of 22,511 skills across skills.sh, ClawHub, GitHub, and Tessl found **140,963 issues** (6.3 issues per skill on average)
- Snyk's ToxicSkills research found **prompt injection in 36%** of skills tested
- Large catalogs compound security risk

### MCP-Based Access Shift
- Most marketplaces still work like npm: install, live on disk, update manually
- MCP-based access: agent connects once, searches live catalog, loads skills on demand, auto-sees new skills
- Predicted to become default within 12 months

### Predictions for Q4 2026
1. **Payments become table stakes** — at least 2 free-only platforms will add paid tiers
2. **Security scanning becomes a selling point** — post-ToxicSkills and ClawHavoc
3. **Consolidation starts** — 8 marketplaces → 3-4 dominant platforms within a year

## Relevance to Skill Bundles

This is the definitive marketplace landscape data:
1. **Marketplace ecosystem map** — 8 marketplaces with different curation/security/payment models
2. **Security quantification** — 6.3 issues per skill, 36% prompt injection rate
3. **MCP-based delivery** — emerging alternative to download-based skill distribution
4. **Creator economy** — Agensi's 70/30 revenue split is the first creator payment model
5. **Consolidation prediction** — market maturation trajectory

Updates and expands on the marketplace data from [[clawhavoc-marketplace-attack]] and [[sok-agentic-skills-beyond-tool-use]].

## Key Quotes

> "The agent skills ecosystem grew from one registry in December 2025 to eight major marketplaces by Q2 2026"

> "A security audit of 22,511 skills across skills.sh, ClawHub, GitHub, and Tessl found 140,963 issues. That's 6.3 issues per skill on average."

> "Snyk's ToxicSkills research found prompt injection in 36% of skills tested"

> "MCP-based access changes that. Your agent connects to a marketplace's MCP server once, and from then on it can search the full live catalog, load skills on demand, and automatically see new skills as they publish."

## Links
- Article: https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026
- Agensi: https://www.agensi.io/skills
