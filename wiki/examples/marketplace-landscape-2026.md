---
type: Skill Bundle Example
title: AI Agent Skills Marketplace Landscape 2026
description: '- **Source:** Agensi.io comprehensive comparison (April 2026) - **Coverage:** 8 major marketplaces, Q2 2026 snapshot'
resource: https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026
timestamp: '2026-07-12T00:00:00Z'
date: 2026-07-12
source: https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026
signal: 8
context_elements:
- Marketplace governance
- Security scanning
- Creator payments
- MCP-based access
- Curation models
---

# AI Agent Skills Marketplace Landscape 2026

## Origin

- **Source:** Agensi.io comprehensive comparison (April 2026)
- **Coverage:** 8 major marketplaces, Q2 2026 snapshot

## Skills Included

This is a **marketplace ecosystem map**, not a single skill bundle. It documents the distribution, curation, and governance models of the entire agent skills marketplace ecosystem.

## Eight Major Marketplaces

| Marketplace | Skills Listed | Curation | Security Review | Creator Payments | MCP Live Access |
|---|---|---|---|---|---|
| Skills.sh | ~2,000 | Community submissions | None | No | No |
| SkillsMP | 800,000+ | Scraped from GitHub, 2+ stars | None | No | No |
| LobeHub | 169,000+ | Scraped | None | No | No |
| ClaudeSkills.info | 658 | Community + official | None | No | No |
| MCP Market | ~500 | Submission-based | None | No | Partial |
| Anthropic official | ~20 | Manual, Anthropic-verified | Internal audit | No | No |
| Plugin marketplaces (GitHub) | 2,500+ registries | Per-owner | None | No | No |
| Agensi | 200+ | Manual + automated | 8-point scan | Yes, 70/30 split | N/A (curl install) |

## Context Elements

### Security Quantification
- 22,511 skills audited across skills.sh, ClawHub, GitHub, Tessl → **140,963 issues** (6.3/skill)
- Snyk's ToxicSkills: **prompt injection in 36%** of skills tested
- Only Agensi has automated security scanning (8-point checklist)

### MCP-Based Access Shift
- Traditional: install, live on disk, update manually (npm model)
- MCP-based: agent connects once, searches live catalog, loads on demand, auto-sees new skills
- Predicted to become default within 12 months

### Creator Economy
- Agensi: first marketplace with creator payments (70/30 revenue split)
- Predicted: at least 2 free-only platforms will add paid tiers by Q4 2026

## Composition Notes

### Key Patterns
1. **Catalog size is misleading** — SkillsMP's 800K = scraped GitHub repos with 2+ stars, many abandoned
2. **Security is the critical gap** — only 1/8 marketplaces has automated scanning
3. **Consolidation predicted** — 8 marketplaces → 3-4 dominant within a year
4. **Curation spectrum** — from no filter (SkillsMP, LobeHub) to manual+automated (Agensi) to Anthropic-verified

### Agensi's 8-Point Security Scan
1. Prompt injection
2. Data exfiltration
3. Secret detection
4. Dangerous commands
5. Obfuscation
6. External fetches
7. Credential access
8. Privilege escalation

## Reproducibility

- Marketplace data as of April 2026
- Security audit: TheNewStack/Snyk ToxicSkills research

## Connections

- Updates marketplace data from [clawhavoc marketplace attack](clawhavoc-marketplace-attack.md) (1,184 malicious skills)
- Expands on [sok agentic skills beyond tool use](../papers/sok-agentic-skills-beyond-tool-use.md)'s marketplace risk findings (13-26% vulnerability rate)
- 6.3 issues/skill and 36% prompt injection rate validate [skillsieve malicious skill detection](skillsieve-malicious-skill-detection.md)'s motivation
- MCP-based access connects to [orca cognitive runtime](orca-cognitive-runtime.md)'s MCP server support

