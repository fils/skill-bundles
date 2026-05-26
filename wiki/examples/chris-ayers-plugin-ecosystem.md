# Chris Ayers — Plugin Ecosystem: Skills, Plugins, and Marketplaces

**Source:** https://chris-ayers.com/posts/agent-skills-plugins-marketplace/
**Date Added:** 2026-05-26 (Iteration 11)
**Author:** Chris Ayers (@CodeBytes)
**Bundle Type:** Ecosystem Architecture · Plugin Distribution · Cross-Tool Compatibility
**Confidence:** 8/10

## Name & Origin

A comprehensive guide to the **three-layer agent extensibility ecosystem**: Skills (atomic capabilities), Plugins (bundled distributions), and Marketplaces (discovery and versioning). Focused on the GitHub Copilot ecosystem but applicable across Claude Code, Codex CLI, and Gemini CLI.

## Skills Included

- Standard SKILL.md creation and cross-tool placement (`.github/skills/`, `.claude/skills/`, `.agents/skills/`, `.gemini/skills/`)
- Plugin manifest authoring (`plugin.json`) bundling skills + agents + hooks + MCP + LSP
- Marketplace creation and plugin distribution
- Version pinning from external sources (GitHub refs, URL-based)

## Context Elements

- **Plugin Manifest Schema:** `plugin.json` with `name`, `version`, `author`, `license`, `keywords`, `agents[]`, `skills[]`, `hooks.json`, `.mcp.json`, `lsp.json` — a formal packaging format for skill bundles
- **Cross-Tool Compatibility Matrix:**

| Capability | Copilot CLI | VS Code | Claude Code | Codex CLI | Gemini CLI |
|------------|-------------|---------|-------------|-----------|------------|
| SKILL.md | ✓ | ✓ | ✓ | ✓ | ✓ |
| Plugin Manifest | `.github/` | same | `.claude-plugin/` | N/A | Extensions |
| Marketplace | ✓ | ✓ | ✓ | `$skill-installer` | `gemini extensions` |
| Hooks | ✓ | ✓ | ✓ | ✗ | ✗ |
| MCP Servers | ✓ | ✓ | ✓ | ✗ | ✓ |

- **Marketplace Architecture:** Git repositories with `marketplace.json` defining available plugins — default markets: `github/copilot-plugins`, `github/awesome-copilot`
- **Versioning Model:** External source references with `source.source=url`, `url`, `ref` for pinning to specific tags/commits
- **CLI Lifecycle:** `plugin marketplace browse → install → list → update → uninstall`

## How Context Elements Support Skills

The plugin ecosystem provides the **distribution and versioning layer** that pure SKILL.md lacks:

1. **Plugins as Skill Bundles:** A plugin IS a skill bundle — it packages multiple skills with optional agents, hooks, and MCP servers into a single installable unit with version metadata
2. **Version Pinning:** External source references with `ref: v2.0` implement the immutable versioning that [[owasp-agentic-skills-top-10]]'s AST07 (Update Drift) requires
3. **Cross-Tool SKILL.md Compatibility:** The fact that SKILL.md works identically across all five major tools validates the [[agent-skills-spec]]'s portability claim
4. **Marketplace as Governance Mechanim** : Marketplaces with `marketplace.json` provide the skill inventory that AST09 (No Governance) demands

## Key Insight: SKILL.md is the Universal Portable Unit

The most important finding is that **SKILL.md works identically across 5 major agent tools** (Copilot CLI, VS Code, Claude Code, Codex CLI, Gemini CLI). This is the strongest evidence yet that skills will become the portable unit of agent capability, with plugins and marketplaces being the distribution mechanism.

## Composition Notes

The three-layer model (Skills → Plugins → Marketplaces) parallels mature software distribution:

| Agent Layer | Software Analogy |
|-------------|-----------------|
| Skill (SKILL.md) | Python module / JS file |
| Plugin (plugin.json) | Python package / npm module |
| Marketplace (marketplace.json) | PyPI / npm registry |

This suggests skill bundles will follow the same maturation path as package management — lockfiles, signing, dependency resolution, and semantic versioning.

## Reproducibility

High — public blog post with complete code examples, CLI commands, and configuration files.

## Bundle Links
- [[agent-skills-spec]] — The SKILL.md standard that powers cross-tool compatibility
- [[github-cli-skill-management]] — Related CLI management patterns
- [[agensi-marketplace-landscape]] — Marketplace comparison from this iteration
- [[owasp-agentic-skills-top-10]] — Security requirements for marketplace governance (AST02, AST07, AST09)
