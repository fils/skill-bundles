# addyosmani/agent-skills: Production-grade engineering skills for AI coding agents

**Source**: https://github.com/addyosmani/agent-skills (updated 2026-06-19)
**Stars**: 63.1k | License: MIT
**Type**: Skill Bundle (24 skills + 4 personas + references/checklists + lifecycle taxonomy)

## Skills Included
- Lifecycle skills: spec-driven-development, planning-and-task-breakdown, incremental-implementation, test-driven-development, code-review-and-quality, shipping-and-launch, etc.
- 23 lifecycle skills + using-agent-skills meta-skill.
- Organized by DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP.

## Context Elements
- Explicit lifecycle taxonomy and workflow diagram (state-machine style).
- 6 reference checklists (testing-patterns, security-checklist, performance-checklist, accessibility-checklist, observability-checklist, orchestration-patterns).
- 4 specialist agent personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor).
- Anti-rationalization tables, red flags, verification requirements per skill.
- Commands/slash-command integration for multiple agent hosts.

## Composition Notes
- Skills enforce senior-engineer discipline (Hyrum’s Law, Beyonce Rule, test pyramid, trunk-based development, Shift Left, feature flags).
- Progressive disclosure + verification gates.
- Designed for composability across agents (Claude Code, Cursor, Gemini CLI, GitHub Copilot, etc.).

## Reproducibility
High — full SKILL.md templates, setup docs for multiple hosts, CONTRIBUTING.md with strict criteria (specific, verifiable, battle-tested, minimal).

**Signal**: 10/10 — canonical example of a production-grade skill bundle with explicit lifecycle context, validation gates, and taxonomy. Primary target for skill-bundles catalog.
