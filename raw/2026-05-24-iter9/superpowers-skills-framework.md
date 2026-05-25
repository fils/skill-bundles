# Superpowers: The Claude Code Skills Framework

**URL:** https://blog.marcnuri.com/superpowers-claude-code-skills-framework
**Author:** Jesse Vincent (obra/superpowers)
**Date Retrieved:** 2026-05-24

## Core Concept
Instills engineering discipline into AI coding agents as markdown. Addresses the failure mode where agents possess best-practice knowledge but skip it for shortcuts.

- 14 SKILL.md files
- Session-start hook: bootstrap < 2,000 tokens
- Multi-host manifests (Claude Code, Cursor, Codex, GitHub Copilot CLI, Gemini CLI, OpenCode)

## "Iron Laws"
| Skill | Iron Law |
| TDD | NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST |
| Verification | NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE |
| Debugging | NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST |

## Six Central Skills
1. brainstorming: Design approval before coding
2. writing-plans: 2-5 minute tasks with file paths
3. test-driven-development: Red/green/refactor
4. systematic-debugging: Four-phase process
5. subagent-driven-development: Dispatch + review
6. verification-before-completion: Verify actual output

## Methodology Cycle
Brainstorming → Git Worktree → Written Plan → Subagent Implementation → Code Review → Finishing
