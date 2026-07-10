# Agentic Awesome Skills (sickn33/agentic-awesome-skills)

**Source:** https://github.com/sickn33/agentic-awesome-skills  
**Stars:** ~42.8k (2026-07-10)  
**Release:** v14.1.0 (2026-07-09/10)  
**License:** MIT  
**Signal rating:** 9/10 (largest installable multi-tool skill library; explicit bundles + schemas + security hardening)

## Summary

Installable GitHub library of **1,943+** agentic skills for Claude Code, Cursor, Codex CLI, Autohand Code, Gemini CLI, Antigravity, Kiro, OpenCode, Copilot, and more. Not just an awesome-list: npm installer (`npx agentic-awesome-skills`), specialized plugins, **bundles & workflows**, schemas, audit gates, and security boundary hardening.

## Bundle-relevant structure

- `skills/` — SKILL.md catalog
- `plugins/` + `.agents/plugins` + `.claude-plugin` — distribution packaging
- `schemas/` — formal structure for skills/plugins
- `skill_categorization/` — taxonomy layer
- `docs/` — user + contributor docs
- `tools/`, `scripts/` — install/audit automation
- Security: Snyk config, repository audit gates, skill security boundaries (recent commits)
- Registry-sync metadata in README: version=14.1.0; skills=1943; stars≈42661

## Install pattern

```bash
npx agentic-awesome-skills
# Default: ~/.agents/skills
# --agy for Antigravity CLI paths
```

## Context elements

| Element | Present? | Notes |
|---------|----------|-------|
| Skills (SKILL.md) | Yes | 1,943+ |
| Bundles/workflows | Yes | Role-based + ordered playbooks |
| Schemas | Yes | `schemas/` directory |
| Taxonomy/categorization | Yes | `skill_categorization/` |
| Security scanning | Yes | Audit gates, Snyk, boundary hardening |
| Multi-platform plugins | Yes | Claude/Codex/Antigravity/etc. |
| SHACL / SSSOM | No (observed) | Opportunity gap |

## Composition pattern

**Mega-catalog + installer + plugin packs + security gates** — distribution-first skill bundle. Closest peer: VoltAgent awesome lists + agentskill.sh registry; differentiates with installable CLI + specialized plugins + explicit "bundles" product surface.

## Quotes / claims

> "Instead of collecting one-off prompt snippets, this repository gives you a searchable, installable catalog of skills, bundles, workflows, plugin-safe distributions..."

## Follow-ups

- Map schema contents to agentskills.io frontmatter
- Compare security gates vs skill-validator CLI / validate-skill Action / ags scoring
