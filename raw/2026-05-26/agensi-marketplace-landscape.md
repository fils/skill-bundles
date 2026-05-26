# AI Agent Skill Marketplace Landscape (April 2026)

**Source:** https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026
**Fetched:** 2026-05-26

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

## What the Numbers Hide
- SkillsMP's 800k is misleading — mostly abandoned experiments and duplicates
- Real catalog size = how many skills are actually used
- 6.3 issues per skill on average across large catalogs
- 36% tested positive for prompt injection (Snyk ToxicSkills)

## Recommendation
Use TWO marketplaces: free browsing (ClaudeSkills.info or skills.sh) + vetted paid (Agensi). Skip massive scraped catalogs.

## Trends (next 6 months to Q4 2026)
1. Payments become table stakes
2. Security scanning becomes selling point (post-ToxicSkills, ClawHavoc)
3. Consolidation: 8 → 3-4 dominant platforms
