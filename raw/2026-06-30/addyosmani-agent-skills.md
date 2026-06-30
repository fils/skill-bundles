# addyosmani/agent-skills: Production-grade engineering skills for AI coding agents

**Source:** https://github.com/addyosmani/agent-skills (accessed 2026-06-30)
**Stars:** 68.1k | **License:** MIT
**Last updated:** ~2 days ago

## Key Ideas
- 24 production-grade engineering skills encoding senior workflows, quality gates, and best practices across the full SDLC (DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP).
- Skills are modular Markdown files with consistent structure: YAML frontmatter + Overview, When to Use, Process, Rationalizations (anti-excuse tables), Red Flags, Verification.
- 4 specialist agent personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor).
- 7 reference checklists in references/ (definition-of-done, testing-patterns, security-checklist, etc.).
- Supports multiple platforms: Claude Code, Cursor, Gemini CLI, GitHub Copilot, etc. via .claude/commands/ or direct SKILL.md.
- Strong emphasis on progressive disclosure, minimal token usage, and "process not prose".

## Composition Notes (Skill Bundle Pattern)
This is a canonical **engineering skill bundle**: 24 skills + 4 personas + 7 reference checklists + hooks + platform adapters. Context elements include anti-rationalization tables (rules), verification gates (validation), and checklists (taxonomies of quality criteria). Directly aligns with SHACL-style constraint enforcement via Red Flags and Verification sections.

## Quotes
> "Skills encode the workflows, quality gates, and best practices that senior engineers use when building software."
> "Verification is non-negotiable."

**Reproducibility:** High — MIT license, clear structure, multiple platform docs.
**Relevance to Skill Bundles:** Exemplar of how skills are bundled with formal process artifacts (rules, checklists) for reliable agent behavior.