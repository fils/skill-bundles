# agentskills.io Overview

**Source:** https://agentskills.io/home
**Date ingested:** 2026-06-12
**Type:** Official specification site for Agent Skills open standard

## Key Ideas
- Lightweight open format for extending AI agents with specialized knowledge/workflows
- Core: folder with SKILL.md (metadata + instructions) + optional scripts/references/assets
- Progressive disclosure: Discovery (name/desc only) → Activation (full SKILL.md) → Execution
- Supported by many clients: Claude, GitHub Copilot, Cursor, VS Code, OpenAI Codex, Gemini, OpenHands, etc.
- Benefits: domain expertise capture, repeatable workflows, cross-product reuse, portable/version-controlled
- Open development: github.com/agentskills/agentskills

## Quotes
"Agents often lack the context needed to do real work reliably. Skills solve this by packaging procedural knowledge and company-, team-, and user-specific context into portable, version-controlled folders..."

## Relevance to Skill Bundles
Foundational definition of the skill format and how bundles work. Emphasizes context packaging. Primary source for understanding skill anatomy and composition.

## Context Elements Present
- SKILL.md structure (frontmatter required: name, description)
- Optional supporting files (scripts, references, assets)
- Specification links
- No SHACL/SSSOM mentioned; the skill folder itself acts as the bundling mechanism with context

---

**Raw extraction notes:** Clean overview of the standard.