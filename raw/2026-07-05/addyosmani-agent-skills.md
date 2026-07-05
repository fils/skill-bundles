# addyosmani/agent-skills

**Source:** https://github.com/addyosmani/agent-skills (68.8k stars, updated ~2 days ago as of 2026-07-05)
**Type:** Large-scale production-grade engineering skills bundle for AI coding agents

## Key Points
- 24 skills total: 23 lifecycle skills + 1 meta-skill ("using-agent-skills").
- Skills encode workflows, quality gates, and best practices used by senior engineers.
- Focused on production engineering: code review, testing, deployment, debugging, architecture decisions.
- Installable via GitHub; designed for Claude Code, Cursor, Codex, etc.
- Includes commands as entry points for agent invocation.

## Context Elements
- Skills directory structure with SKILL.md files.
- References to quality gates and best practices (implicit rules/taxonomies for engineering).
- No explicit SHACL/SSSOM in this bundle, but heavy emphasis on reproducible workflows and validation steps.

## Composition Notes / Reusability
- High "bundle density": many skills composed into a coherent engineering persona.
- Meta-skill for using other skills demonstrates composition patterns.
- Strong reproducibility via documented commands and gates.

**Relevance:** Prime example of a large, curated skill bundle with implicit rule-based context. Good baseline for comparing bundles that add explicit SHACL validation or SSSOM mappings.