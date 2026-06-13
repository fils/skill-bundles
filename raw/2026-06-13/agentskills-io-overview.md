# Agent Skills Overview

**Source:** https://agentskills.io/home
**Date ingested:** 2026-06-13
**Category:** Specification / Standard

## Key Points

- Lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.
- Core: folder with required `SKILL.md` (name, description, instructions) + optional scripts/, references/, assets/.
- Progressive disclosure: Discovery (name+desc), Activation (full SKILL.md), Execution.
- Supported by Claude, Cursor, VS Code Copilot, Gemini CLI, OpenHands, and 20+ others.
- Originally from Anthropic, now open standard.
- GitHub org: https://github.com/agentskills/agentskills

## Relevance to Skill Bundles

This is the foundational standard for portable, version-controlled agent skills. Bundles would combine multiple SKILL.md + shared context artifacts (validation rules, mappings, vocabularies) for domain-specific agent teams.