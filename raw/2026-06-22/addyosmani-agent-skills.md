# addyosmani/agent-skills: Production-grade engineering skills for AI coding agents

**Source**: https://github.com/addyosmani/agent-skills (65.1k stars, MIT)
**Date ingested**: 2026-06-22
**Signal rating**: 10/10 — Prime example of a mature skill bundle with 24 lifecycle skills + personas + references/checklists (context elements: rules, taxonomies, verification patterns).

## Key Ideas
- 24 structured Markdown skills organized by engineering lifecycle (Define → Plan → Build → Verify → Review → Ship).
- Each skill includes: Frontmatter, Overview, When to Use, Process steps, Rationalizations table, Red Flags, Verification (evidence requirements).
- 4 agent personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor).
- 6 reference checklists (testing, security, performance, accessibility, observability, orchestration).
- Slash commands and auto-activation based on context.
- Core principle: embed senior engineering practices (spec before code, TDD, security reviews, observability) to prevent agents taking shortcuts.

## Quotes & Excerpts
- "AI agents default to the shortest path (skipping specs, tests, security)."
- Skills use "progressive disclosure" and "process over prose".
- "Skills must be specific, verifiable, battle-tested, and minimal."

## Composition Notes
- Skills reference shared references/ and agents/ directories.
- Context elements: explicit verification checklists (rules/taxonomies), rationalization rebuttals (rules), persona definitions (taxonomies).
- Reusability: Works across Claude Code, Cursor, GitHub Copilot, Gemini CLI, etc.

## Reproducibility
High — fully open MIT, plain Markdown + docs for installation per platform.