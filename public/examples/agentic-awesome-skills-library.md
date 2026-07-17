---
type: Skill Bundle Example
title: Agentic Awesome Skills Library
description: 1,943+ `SKILL.md` playbooks spanning development, testing, security, infrastructure, product, and marketing.
resource: https://github.com/sickn33/agentic-awesome-skills
timestamp: '2026-07-10T00:00:00Z'
date: 2026-07-10
sources:
- raw/2026-07-10/agentic-awesome-skills.md
- https://github.com/sickn33/agentic-awesome-skills
skills_included: 1943
context_elements:
- schemas
- skill-categorization-taxonomy
- plugin-distribution
- bundles-workflows
- security-audit-gates
composition_notes: Installable mega-catalog with explicit bundles, schemas, plugins, and security boundary hardening.
reproducibility: High — npm installer, release-pinned clone, v14.1.0 tags
---

# Agentic Awesome Skills Library

**Origin:** [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) (~42.8k stars, v14.1.0)

## Skills included

1,943+ `SKILL.md` playbooks spanning development, testing, security, infrastructure, product, and marketing. Multi-tool: Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, Kiro, OpenCode, Copilot, Autohand Code.

## Context elements

- **Schemas** — `schemas/` formal structure for skills/plugins
- **Taxonomy** — `skill_categorization/`
- **Bundles & workflows** — role-based recommendations and ordered execution playbooks
- **Plugin distribution** — specialized plugins + full-library plugin; `.agents/plugins`, `.claude-plugin`
- **Security audit gates** — repository audit gates, Snyk, skill security boundary hardening (v14.1.0)

## How context supports skills

The catalog is not only content: installer + schemas + categorization + security gates form a **distribution and governance layer**. Specialized plugins reduce privilege/context overload versus installing everything (bundle-level interaction concern).

## Composition notes / reusability

- Distribution-first peer to [awesome agent skills catalogs](awesome-agent-skills-catalogs.md) / VoltAgent lists
- Security gates relate to [three layer validation stack](../concepts/three-layer-validation-stack.md) and [agentskill sh ags security scoring](agentskill-sh-ags-security-scoring.md)
- Install: `npx agentic-awesome-skills` → `~/.agents/skills`

## Reproducibility assessment

**High.** Release tags, npm package, shallow release-pinned install, MIT.

## Related

- [awesome agent skills catalogs](awesome-agent-skills-catalogs.md)
- [chris ayers plugin ecosystem](chris-ayers-plugin-ecosystem.md)
- [three layer validation stack](../concepts/three-layer-validation-stack.md)
- [skill security governance](../concepts/skill-security-governance.md)

