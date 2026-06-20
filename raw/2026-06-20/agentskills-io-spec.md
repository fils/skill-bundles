# agentskills.io — Official Agent Skills Specification & Overview

**Source:** https://agentskills.io/home
**Date ingested:** 2026-06-20
**Signal rating:** 10/10 (canonical spec + progressive disclosure model)

## Key Ideas
- Lightweight open format: folder + required SKILL.md (name + description + instructions)
- Optional: scripts/, references/, assets/
- Progressive disclosure: Discovery (name+desc) → Activation (full SKILL.md) → Execution
- Cross-product: works with Claude Code, Cursor, GitHub Copilot, VS Code, Gemini CLI, OpenAI Codex, 40+ tools
- Originally developed by Anthropic, now open standard (GitHub: agentskills/agentskills)

## Context Elements
- SKILL.md frontmatter (YAML: name, description)
- Progressive disclosure as the core architectural pattern
- Resource directories and extensions defined in spec

## Quotes
> "Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows."

> "Agents load skills in three stages: Discovery, Activation, Execution. This minimizes context footprint while supporting many skills."

## Composition Notes
The specification itself is the foundational **context artifact** that enables all skill bundles. It defines the portable packaging format that pairs skills with optional validation (frontmatter), scripts, and references.

## Reproducibility
Open spec at https://agentskills.io/specification. Quickstart available.