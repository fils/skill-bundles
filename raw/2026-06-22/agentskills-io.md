# agentskills.io — Official Agent Skills Specification & Overview

**Source**: https://agentskills.io/
**Date ingested**: 2026-06-22
**Signal rating**: 9/10 — Foundational specification defining the open standard for skill bundles.

## Key Ideas
- Lightweight open format: folder with required SKILL.md (YAML frontmatter + instructions) + optional scripts/, references/, assets/.
- Progressive disclosure: Discovery (name+desc) → Activation (full SKILL.md) → Execution.
- Portable across 20+ agents (Claude, Cursor, GitHub Copilot, Codex, Gemini CLI, VS Code, etc.).
- Originally from Anthropic, now community-driven (GitHub: agentskills/agentskills, Discord).

## Quotes & Excerpts
- "A skill is a folder containing a required `SKILL.md` file with metadata (`name`, `description`) and task instructions, plus optional scripts, references, templates, and resources."
- "Skills package procedural knowledge and context into portable, version-controlled folders."

## Composition Notes
- Context elements explicitly supported: references/ (vocabularies, docs), scripts/ (executable rules), templates/assets (taxonomies/examples).
- No SHACL/SSSOM in core spec but extensible.

## Reproducibility
High — open standard, quickstart, specification, llms.txt available.