# addyosmani/agent-skills: Production-grade engineering skills for AI coding agents

Source: https://github.com/addyosmani/agent-skills
Date ingested: 2026-06-02

Repository: addyosmani/agent-skills
Stats: 47.7k stars • 5.3k forks • 201 commits • MIT License

This is a production-grade collection of 23 structured engineering workflows (skills) for AI coding agents. It encodes senior engineer practices across the full development lifecycle, packaged for consistent use in tools like Claude Code, Cursor, Gemini CLI, and others.

## 7 Slash Commands (Lifecycle Entry Points)

| Command | Purpose | Key Principle |
|---------|---------|---------------|
| /spec | Define what to build | Spec before code |
| /plan | Plan how to build it | Small, atomic tasks |
| /build | Build incrementally | One slice at a time |
| /test | Prove it works | Tests are proof |
| /review | Review before merge | Improve code health |
| /code-simplify | Simplify the code | Clarity over cleverness |
| /ship | Ship to production | Faster is safer |

Skills also auto-activate based on context.

## All 23 Skills

**Meta**
- using-agent-skills: Maps work to the correct workflow and defines operating rules.

**Define**
- interview-me, idea-refine, spec-driven-development

**Plan**
- planning-and-task-breakdown

**Build**
- incremental-implementation, test-driven-development, context-engineering, source-driven-development, doubt-driven-development, frontend-ui-engineering, api-and-interface-design

**Verify**
- browser-testing-with-devtools, debugging-and-error-recovery

**Review**
- code-review-and-quality, code-simplification, security-and-hardening, performance-optimization

**Ship**
- git-workflow-and-versioning, ci-cd-and-automation, deprecation-and-migration, documentation-and-adrs, shipping-and-launch

## Agent Personas (Specialist Subagents)

- code-reviewer, test-engineer, security-auditor

## Skill Anatomy

Every SKILL.md follows consistent format with Frontmatter, Overview, When to Use, Process, Rationalizations, Red Flags, Verification.

Key design principles: Process over prose, anti-rationalization tables, mandatory verification, progressive disclosure.

This is an excellent example of a **skill bundle** — a curated collection of 23 inter-related skills with shared structure, personas, and lifecycle coverage. No explicit SHACL/SSSOM in this repo, but strong on reproducibility and composition patterns.