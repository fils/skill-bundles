# Agent Skills, Plugins, and Marketplace: Complete Guide

**Source:** https://chris-ayers.com/posts/agent-skills-plugins-marketplace/
**Author:** Chris Ayers (@CodeBytes)
**Fetched:** 2026-05-26

## 3-Layer Ecosystem (Copilot-centric)

### 1. Agent Skills
Standard SKILL.md folders in `.github/skills/`, `.claude/skills/`, `.agents/skills/`, `.gemini/skills/`.

### 2. Plugins
Distributable packages bundling: Custom Agents + Skills + Hooks + MCP Servers + LSP Servers.
```json
{
  "name": "document-tools",
  "version": "1.0.0",
  "agents": ["./agents/data-analyst.agent.md"],
  "skills": ["./skills/csv-analysis/"]
}
```

### 3. Marketplaces
Git repos with `marketplace.json`. Default: `github/copilot-plugins`, `github/awesome-copilot`.

## Cross-Tool Compatibility Matrix
| Capability | Copilot CLI | VS Code | Claude Code | Codex CLI | Gemini CLI |
|------------|-------------|---------|-------------|-----------|------------|
| SKILL.md | Yes | Yes | Yes | Yes | Yes |
| Custom Agents | Yes | Yes | Yes | Partial | Partial |
| Plugin Manifest | `.github/` | same | `.claude-plugin/` | N/A | Extensions |
| Marketplace | Yes | Yes | Yes | `$skill-installer` | `gemini extensions` |
| Hooks | Yes | Yes | Yes | No | No |
| MCP Servers | Yes | Yes | Yes | No | Yes |
| LSP Servers | Yes | Yes | Yes | No | No |

## Key Insight
SKILL.md is the MOST portable — works identically across all five tools. Maximize compatibility by including both `.github/plugin.json` and `.claude-plugin/plugin.json`.

## Versioning with External Sources
```json
{
  "name": "external-tool",
  "version": "2.0.0",
  "source": { "source": "url", "url": "https://github.com/org/tool-plugin", "ref": "v2.0" }
}
```

## CLI Commands
```bash
copilot plugin marketplace list
copilot plugin marketplace browse awesome-copilot
copilot plugin install dev-toolkit@awesome-copilot
copilot plugin update my-plugin
copilot plugin uninstall my-plugin
```
