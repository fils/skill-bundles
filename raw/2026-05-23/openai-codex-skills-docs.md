# OpenAI Codex — Agent Skills Documentation

Source: https://developers.openai.com/codex/skills

Agent skills are task-specific capabilities that extend Codex by packaging instructions, resources, and scripts into reliable workflows. Based on the open agent skills standard (agentskills.io).

## Core Concepts
- **Skills vs. Plugins:** Skills are the authoring format; Plugins are the distribution unit
- **Progressive Disclosure:** Only name/description/path loaded initially; full SKILL.md on activation
- **Context Budget:** Capped at 2% of context window (~8,000 chars)

## Skill Structure
Directory with mandatory SKILL.md and optional:
- scripts/: Executable code
- references/: Documentation
- assets/: Templates/resources
- agents/openai.yaml: UI appearance and tool dependencies

## Context Budget: Discovery → Instructions → Resources (progressive)

## Skill Locations & Scopes
| Scope | Location |
| REPO | $CWD/.agents/skills |
| REPO | $REPO_ROOT/.agents/skills |
| USER | $HOME/.agents/skills |
| ADMIN | /etc/codex/skills |
| SYSTEM | Bundled by OpenAI |

## Advanced Configuration (openai.yaml)
```yaml
interface:
  display_name: "My Skill"
  brand_color: "#3B82F6"
policy:
  allow_implicit_invocation: false
dependencies:
  tools:
    - type: "mcp"
      value: "serverName"
```

## Context Elements Found
- **YAML configuration** for UI, invocation policy, tool dependencies
- **MCP dependency declarations** — skills declare external tool server requirements
- **Context budget management** — progressive disclosure pattern formalized
