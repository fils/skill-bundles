# addyosmani/agent-skills

**Source:** https://github.com/addyosmani/agent-skills
**Date ingested:** 2026-05-27
**Signal:** High (production-grade engineering skills bundle with 23 skills + 7 slash commands, explicit process guardrails, anti-rationalization tables, verification requirements)

**Summary:** Production-grade engineering skills for AI coding agents. Packages workflows, quality gates, and senior-engineer best practices (Google-inspired) so agents follow disciplined SDLC instead of shortest-path-to-done. 23 skills across Define/Plan/Build/Verify/Review/Ship + meta. Supports Claude Code, Cursor, Gemini, Copilot, etc. via markdown SKILL.md files or marketplace.

**Skills included:** 23 skills (interview-me, idea-refine, spec-driven-development, planning-and-task-breakdown, incremental-implementation, test-driven-development, context-engineering, source-driven-development, doubt-driven-development, frontend-ui-engineering, api-and-interface-design, browser-testing-with-devtools, debugging-and-error-recovery, code-review-and-quality, code-simplification, security-and-hardening, performance-optimization, git-workflow-and-versioning, ci-cd-and-automation, deprecation-and-migration, documentation-and-adrs, shipping-and-launch, using-agent-skills)

**Context elements:** 
- SKILL.md frontmatter + structured sections (Overview, When to Use, Process, Rationalizations, Red Flags, Verification)
- 7 slash commands as entry points (/spec, /plan, /build, /test, /review, /code-simplify, /ship)
- Agent personas (code-reviewer, test-engineer, security-auditor)
- Reference checklists (testing-patterns.md, security-checklist.md, performance-checklist.md, accessibility-checklist.md)
- Hooks for session lifecycle
- Progressive disclosure for token efficiency

**Composition notes:** Skills are composable via meta-router (using-agent-skills). Each skill enforces verification (tests, evidence). Anti-rationalization tables prevent skipping steps. Designed for marketplace install or direct file drop.

**Reproducibility:** High — MIT license, clear structure, works across multiple agent platforms. 

**Related patterns:** Constraint Rules (via verification and red flags), Dependency Graphs (lifecycle phases), Benchmarking (via checklists and evidence requirements).