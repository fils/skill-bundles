# Agent Skills Specification (agentskills.io)

**Source:** https://agentskills.io/ and https://agentskills.io/specification (extracted 2026-06-18)
**Date ingested:** 2026-06-18
**Signal:** Core standard definition — high (defines the portable SKILL.md format with YAML frontmatter + instructions)

## Key Ideas
- Lightweight, open format for extending AI agents with specialized knowledge/workflows.
- A skill = folder with required `SKILL.md` (YAML frontmatter: name, description; + Markdown instructions) + optional scripts/, references/, assets/.
- Progressive disclosure: agents discover by name/desc, activate full content on match, execute with optional code/resources.
- Originally from Anthropic, now open standard supported across Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, VS Code, and 40+ clients.
- Cross-product reuse via version-controlled folders.

## Quotes
- "Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows."
- "Skills package procedural knowledge and context into portable, version-controlled folders that agents load on demand."

## Relevance to Skill Bundles
Provides the foundational packaging mechanism (SKILL.md + resources). Context elements (validation, mapping) can be bundled inside the skill folder or referenced. No built-in SHACL/SSSOM, but extensible.

## Composition Notes
Skills are composable by loading multiple; meta-skills (e.g. using-agent-skills) orchestrate.