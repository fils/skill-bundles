# OpenAI Codex Developer Skills Specification

**Source:** https://developers.openai.com/codex/skills
**Date Accessed:** 2026-05-24
**Author:** OpenAI Developer Docs

---

## Key Ideas
- Agent skills extend Codex by packaging instructions, resources, and scripts
- Based on the open agent skills standard (agentskills.io)
- Skills vs. Plugins: Skills are the authoring format, Plugins are the distribution unit for packaging
- Progressive Disclosure: Initially only name/description/path loaded (~100 tokens), full SKILL.md loaded when activated
- Context Budget: Initial skill list capped at 2% of context window (~8,000 chars)

## Skill Structure
- SKILL.md (required): metadata + instructions
- scripts/: executable code
- references/: documentation
- assets/: templates/resources
- agents/openai.yaml: UI appearance and dependencies

## Advanced Configuration (openai.yaml)
- Interface customization (display_name, brand_color)
- Policy: allow_implicit_invocation toggle
- Dependencies: MCP server connections with URLs

## Storage Locations (Search Hierarchy)
| Scope | Location |
| REPO | $CWD/.agents/skills |
| REPO | $REPO_ROOT/.agents/skills |
| USER | $HOME/.agents/skills |
| ADMIN | /etc/codex/skills |
| SYSTEM | Bundled by OpenAI |

## Bundle Context Elements
- **YAML Configuration:** openai.yaml for UI and dependency declaration
- **MCP Dependencies:** Skills can declare MCP tool dependencies
- **Skill Specification:** Based on agentskills.io standard

## Reproducibility
- High: Official OpenAI documentation, well-structured
- Confidence: 9/10
