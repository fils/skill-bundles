# addyosmani/agent-skills

**Source**: https://github.com/addyosmani/agent-skills
**Date ingested**: 2026-06-11
**Type**: Production-grade engineering skill bundle for AI coding agents

## Summary
Repository providing 24+ skills that encode senior engineer workflows, quality gates, and best practices across the full development lifecycle (DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP). Skills are activated contextually and include structured anatomy: Overview, When to Use, Process, Rationalizations table, Red Flags, Verification.

## Key Context Elements
- Structured SKILL.md frontmatter + sections
- Reference checklists (testing, security, performance, accessibility)
- Agent personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor)
- Slash commands for workflow activation
- Progressive disclosure for token efficiency

## Composition Notes
Skills are designed as composable workflows with explicit verification steps. Emphasizes "Process, not prose" and anti-rationalization tables. No explicit SHACL/SSSOM but heavy emphasis on verifiable, reproducible engineering practices that could be formalized.

## Reproducibility
High — MIT license, clear structure, installable via plugin marketplaces across Claude Code, Cursor, Copilot, etc. 53.2k stars indicates strong adoption signal.

## Related
- agentskills.io standard
- anthropics/skills (official reference implementation)