# Agent Skills Specification - agentskills.io

**Source:** https://agentskills.io/specification (accessed 2026-07-05)
**Type:** Official specification for Agent Skills open standard

## Key Points
- Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.
- A skill is a directory containing at minimum a `SKILL.md` file with YAML frontmatter (name, description) + Markdown instructions.
- Skills can bundle scripts, reference materials, templates, and other resources in subdirectories (references/, scripts/, assets/).
- Open standard originally from Anthropic, now adopted by GitHub Copilot, Claude Code, Cursor, etc.
- Progressive disclosure: agents load only relevant context when needed.
- Cross-agent compatibility: works in VS Code, Claude Code, Codex CLI, Gemini CLI, etc.

## Composition Notes
- Skills often include formal context elements: instruction templates, validation rules (implicit), resource files.
- Ecosystem supports .github/skills/, .claude/skills/, .agents/skills/ locations.
- Specification emphasizes metadata for discoverability and when to activate the skill.

**Relevance to Skill Bundles:** Core definition of the skill packaging format that many bundles build upon. Provides the base layer for adding SHACL/SSSOM/validation layers in advanced bundles.