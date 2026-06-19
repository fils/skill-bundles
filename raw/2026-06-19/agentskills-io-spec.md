# agentskills.io — Official Agent Skills Specification & Overview

**Source**: https://agentskills.io/home (2026-06-19)
**Type**: Core Specification + Ecosystem Hub

## Key Concepts
- Lightweight open format: folder with required SKILL.md (YAML frontmatter: name, description + instructions) + optional scripts/, references/, assets/.
- Progressive disclosure: Discovery (name+desc) → Activation (full SKILL.md) → Execution (scripts/references as needed).
- Cross-product portability: Claude Code, OpenAI Codex, GitHub Copilot/VS Code, Gemini CLI, Cursor, and 20+ others.

## Context Elements
- Official specification (agentskills.io/specification).
- llms.txt for LLM-friendly discovery.
- Client showcase and quickstart guides.
- Community Discord + GitHub org (agentskills/agentskills).

## Relevance to Skill Bundles
Defines the canonical packaging standard that most "agent skills" repos implement. Any bundle discussion must reference this spec for interoperability, metadata, and resource discovery rules.

**Signal**: 9/10 — foundational reference for all skill bundle work.
