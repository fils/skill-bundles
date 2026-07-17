---
type: Skill Bundle Example
title: 'Addy Osmani Agent Skills: Production-Grade Engineering Workflows'
description: '**Agent Skills** by Addy Osmani is a collection of **workflows, quality gates, and best practices** designed to force AI coding agents to follow **senior-level engineering discipline** across the entire development li...'
resource: https://github.com/addyosmani/agent-skills
timestamp: '2026-06-09T00:00:00Z'
date: '2026-06-09'
---

# Addy Osmani Agent Skills: Production-Grade Engineering Workflows

**Source:** https://github.com/addyosmani/agent-skills  \
**Date Added:** 2026-06-09  \
**Bundle Type:** Process-Oriented Engineering Discipline Skill Bundle  \
**Raw Source:** [addyosmani agent skills](../../raw/2026-06-09/addyosmani-agent-skills.md)

## Overview

**Agent Skills** by Addy Osmani is a collection of **workflows, quality gates, and best practices** designed to force AI coding agents to follow **senior-level engineering discipline** across the entire development lifecycle. It contains **23 core skills** organized by development phase, plus **specialist personas** and **reference checklists**.

This is a **process-oriented skill bundle** — each skill encodes a workflow with verification gates, anti-rationalization tables, and non-negotiable evidence requirements.

## Core Philosophy

> **Process, not prose.** Skills are workflows agents follow, not reference docs they read.

### Key Design Principles
- **Rationalizations:** Table of common excuses agents use (e.g., "I'll add tests later") and required rebuttals
- **Red Flags:** Signs that the process is failing
- **Verification:** Non-negotiable evidence requirements (tests, build logs, runtime data) — "Seems right" is never accepted
- **Google Engineering Culture:** Incorporates Hyrum's Law, Chesterton's Fence, Trunk-based development

## Skills by Development Phase (23 Total)

### 1. Define & Plan (4 Skills)
| Skill | Purpose |
|-------|---------|
| `interview-me` | One-question-at-a-time interview to extract true requirements until ~95% confidence |
| `idea-refine` | Divergent/convergent thinking for vague concepts |
| `spec-driven-development` | Writing PRDs covering style, testing, and boundaries before coding |
| `planning-and-task-breakdown` | Decomposing specs into verifiable units with dependency ordering |

### 2. Build / Implementation (9 Skills)
| Skill | Purpose |
|-------|---------|
| `incremental-implementation` | Thin vertical slices; implement, test, verify, commit |
| `test-driven-development` | Red-Green-Refactor; follows the **Beyonce Rule** ("If you liked it, you shoulda put a test on it") |
| `source-driven-development` | Grounding decisions in official documentation with citations |
| `doubt-driven-development` | Adversarial review: CLAIM → EXTRACT → DOUBT → RECONCILE |
| `context-engineering` | Feeding agents the right info via rules files and MCP integrations |
| `frontend-ui-engineering` | WCAG 2.1 AA compliance, specialized design |
| `api-and-interface-design` | Hyrum's Law awareness, contract stability |
| *(2 more specialized build skills)* | |

### 3. Verify & Review (4 Skills)
| Skill | Purpose |
|-------|---------|
| `browser-testing-with-devtools` | Live runtime data via Chrome DevTools MCP |
| `debugging-and-error-recovery` | 5-step triage: reproduce, localize, reduce, fix, guard |
| `code-review-and-quality` | 5-axis review with severity labels (Nit/Optional/FYI) |
| `security-and-hardening` | OWASP Top 10 prevention and threat modeling |

### 4. Ship & Maintain (3 Skills)
| Skill | Purpose |
|-------|---------|
| `git-workflow-and-versioning` | Trunk-based development and atomic commits (~100 lines) |
| `deprecation-and-migration` | Treating code as a liability; removing "zombie code" |
| `documentation-and-adrs` | Recording the *why* via Architecture Decision Records |

## Specialist Personas (Context Element: Role Definitions)

Pre-configured personas for targeted agent behavior:
- **code-reviewer:** Senior Staff Engineer perspective
- **test-engineer:** QA Specialist focusing on the "Prove-It" pattern
- **security-auditor:** Security Engineer focusing on threat modeling and OWASP assessment

## Slash Commands (7 Commands Mapping to Phases)

| Command | Phase | Key Principle |
|---------|-------|---------------|
| `/spec` | Define | Spec before code |
| `/plan` | Plan | Small, atomic tasks |
| `/build` | Build | One slice at a time |
| `/test` | Verify | Tests are proof |
| `/review` | Review | Improve code health |
| `/code-simplify` | Refactor | Clarity over cleverness |
| `/ship` | Deploy | Faster is safer |

## Cross-Platform Installation Support

- **Claude Code** (Recommended): `/plugin marketplace add addyosmani/agent-skills`
- **Cursor:** Copy `SKILL.md` files into `.cursor/rules/`
- **Gemini CLI:** `gemini skills install https://github.com/addyosmani/agent-skills.git --path skills`
- **GitHub Copilot:** Use agent definitions from `agents/` as personas and skill content in `.github/copilot-instructions.md`
- **Windsurf/Kiro/OpenCode:** Add skill contents to respective rules configurations

## Project Structure (Bundle Organization)

```
/skills          # The 23 core Markdown workflows
/agents          # Specialist persona definitions
/references      # Checklists for Testing, Security, Performance, Accessibility
/hooks           # Session lifecycle hooks (e.g., citation caching for source-driven development)
/.claude/commands # Slash command definitions
```

## Composition Notes

This bundle demonstrates **process-as-skill** composition patterns:

1. **Lifecycle coverage**: Skills span the entire SDLC (Define → Plan → Build → Verify → Ship → Maintain)
2. **Anti-rationalization design**: Explicit tables of agent failure modes + required corrections
3. **Verification-first**: Every skill demands concrete evidence (tests, logs, runtime data)
4. **Persona layering**: Specialist personas activate relevant skill subsets
5. **Slash command interface**: 7 commands map 1:1 to phases — a **command taxonomy** context element
6. **Reference checklists**: Separate `references/` directory with Testing, Security, Performance, Accessibility checklists — **standards/compliance artifacts**
7. **Session hooks**: Lifecycle hooks for cross-cutting concerns (citation caching) — **execution context management**
8. **Google engineering culture**: Formalized best practices (Hyrum's Law, Chesterton's Fence, Trunk-based) as **cultural/normative artifacts**

## Confidence

9/10 — Well-documented repository with clear philosophy, 23 structured skills, personas, checklists, and cross-platform installation. Actively maintained by a recognized engineering leader (Addy Osmani, Google Chrome).

## Sources

- https://github.com/addyosmani/agent-skills
- Raw: [addyosmani agent skills](../../raw/2026-06-09/addyosmani-agent-skills.md)
