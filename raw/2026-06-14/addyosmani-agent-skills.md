# addyosmani/agent-skills

**Source:** https://github.com/addyosmani/agent-skills (retrieved 2026-06-14)
**Type:** Production-grade engineering skill bundle for AI coding agents
**Key Context Elements:** Structured SKILL.md with frontmatter, references/checklists (testing-patterns.md, security-checklist.md, performance-checklist.md, accessibility-checklist.md), agent personas, slash commands

## Key Ideas
- 24 skills across DEFINE-PLAN-BUILD-VERIFY-REVIEW-SHIP lifecycle with explicit workflows.
- Skills enforce production discipline (spec before code, tests as proof, verification gates).
- Every SKILL.md has: Frontmatter (name, description), Overview, When to Use, Process, Rationalizations, Red Flags, Verification.
- Auto-activation based on context; 4 specialist agent personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor).
- Supports multiple hosts: Claude Code, Cursor, Gemini, etc. via plugin or direct SKILL.md copy.

## Notable Quotes / Patterns
> "AI agents default to the shortest path, often skipping specs, tests, and security. These skills enforce production discipline drawn from Google's engineering culture."

**Composition Notes:** Skills reference shared references/ for checklists; meta skill `using-agent-skills` maps work to workflows. Strong example of skill bundle with validation (verification sections) and taxonomy (lifecycle stages).

**Reproducibility:** High — MIT license, clear structure, GitHub repo with setup docs for multiple agents.