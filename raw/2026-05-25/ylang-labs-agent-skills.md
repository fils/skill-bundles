# Ylang Labs — Agent Skills: Portable Format for Teaching AI Agents

**Source:** https://ylanglabs.com/blogs/agent-skills
**Date:** 2026-05-25
**Signal:** 8/10

## Key Insight
Skills = "recipes" (procedural knowledge), MCP = "kitchen" (tools/data). This metaphor clarifies the composition relationship.

## Three-Level Loading (Progressive Disclosure)
| Level | Content | Tokens |
|---|---|---|
| 1. Metadata | Name + Description | ~100 |
| 2. Instructions | SKILL.md body | <5000 |
| 3. Resources | Scripts + References | Variable |

## Comparison Matrix (Skills vs System Prompts vs MCP)
| Feature | Skills | System Prompts | MCP Servers |
|---|---|---|---|
| Provides | Procedural how-to | Momentary instructions | Tool/data access |
| Persistence | Cross-conversation | Single session | Continuous |
| Portability | High (open standard) | Low (product-specific) | High (open standard) |
| Idle Cost | ~100 tokens | High (full prompt) | Minimal |

## Distribution Patterns
- Direct installation (.claude/skills/, .cursor/skills/)
- Plugin marketplaces (git-based, version pinning)
- Community directories (skills.sh by Vercel Labs)

## Bundle Context Elements
Includes YAML frontmatter schema, scripts/ directory pattern, references/ pattern, assets/ templates. Strong example of the minimal bundle structure.
