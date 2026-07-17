---
type: Tool
title: AI Agent Skill Marketplace Landscape (2026)
description: The agent skill marketplace ecosystem as of April 2026, based on Agensi's comprehensive comparison.
resource: https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026
timestamp: '2026-05-26T00:00:00Z'
date: '2026-05-26'
---

# AI Agent Skill Marketplace Landscape (2026)

**Source:** https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026
**Date Added:** 2026-05-26 (Iteration 11)
**Confidence:** 8/10

## Overview

The agent skill marketplace ecosystem as of April 2026, based on Agensi's comprehensive comparison. Eight major marketplaces operate with varying curation, security, and creator payment models.

## Marketplace Comparison

| Marketplace | Skills | Curation | Security | Creator Pay | MCP Live |
|-------------|--------|----------|----------|-------------|----------|
| Skills.sh | ~2,000 | Community | None | No | No |
| SkillsMP | 800,000+ | Scraped (2+ stars) | None | No | No |
| LobeHub | 169,000+ | Scraped | None | No | No |
| ClaudeSkills.info | 658 | Community | None | No | No |
| MCP Market | ~500 | Submissions | None | No | Partial |
| Anthropic official | ~20 | Manual | Internal | No | No |
| Plugin marketplaces | 2,500+ | Per-owner | None | No | No |
| **Agensi** | **200+** | **Manual + auto** | **8-point scan** | **80/20** | **N/A** |

## Agensi's 8-Point Security Scan
1. Prompt injection
2. Data exfiltration
3. Secret detection
4. Dangerous commands
5. Obfuscation
6. External fetches
7. Credential access
8. Privilege escalation

## Key Statistics
- SkillsMP's 800k is misleading — mostly abandoned experiments and duplicates
- 6.3 issues per skill on average across large catalogs (22,511 skills audited → 140,963 issues)
- 36% tested positive for prompt injection (Snyk ToxicSkills)

## Trends (to Q4 2026)
1. Payments become table stakes (only 1 marketplace has creator payments today)
2. Security scanning becomes a differentiator post-ToxicSkills and ClawHavoc
3. Consolidation: 8 → 3-4 dominant platforms expected

## Recommendation
Use TWO marketplaces: free browsing (ClaudeSkills.info or skills.sh) + vetted paid (Agensi). Skip massive scraped catalogs without auditing each skill.

## Related
- [chris ayers plugin ecosystem](../examples/chris-ayers-plugin-ecosystem.md) — Complementary view of plugin/marketplace architecture
- [owasp agentic skills top 10](../examples/owasp-agentic-skills-top-10.md) — Security requirements for marketplace governance
- [purplebox supply chain security](../examples/purplebox-supply-chain-security.md) — Supply chain risks in markets (12% infection rate)
