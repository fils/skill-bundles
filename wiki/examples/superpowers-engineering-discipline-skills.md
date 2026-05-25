# Superpowers: Engineering Discipline as Skills

## Overview

[Superpowers](https://github.com/obra/superpowers) by Jesse Vincent is a **multi-host skills framework** that encodes software engineering best practices as 14 SKILL.md files. It addresses a specific failure mode: AI coding agents know best practices but skip them for shortcuts. The framework bundles **Iron Laws** (non-negotiable constraints), **Red Flags** (common rationalizations to avoid), and a **Methodology Cycle** (linear workflow enforced by skill activation).

**Context Elements:** YAML frontmatter · Iron Laws (constraint rules) · Red Flag lists (negative constraints) · Multi-host manifests · Session-start bootstrap hook

## Core Architecture

### 14 Skills
Six central skills drive the methodology:
1. **brainstorming** — Force design approval before any code
2. **writing-plans** — Break features into 2-5 minute tasks with file paths
3. **test-driven-development** — Enforce red/green/refactor; delete code if no tests written first
4. **systematic-debugging** — Four-phase process forbidding guess-and-check
5. **subagent-driven-development** — Dispatch implementation to fresh agent, second agent for review
6. **verification-before-completion** — Require reading and verifying actual command output

### Iron Laws
Each skill has a non-negotiable constraint:
- TDD: "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"
- Verification: "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE"
- Debugging: "NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST"

### Multi-Host Manifests
Small files (`.claude-plugin/`, `.cursor-plugin/`) enable discovery across:
- Claude Code, Cursor, OpenAI Codex, GitHub Copilot CLI, Gemini CLI, OpenCode

## Context Elements

**Type: Constraint Rules (Iron Laws)** — The Iron Laws are **declarative constraints** embedded in each skill's SKILL.md that the agent must not violate. This is a novel pattern: skills that encode *prohibitions* rather than just procedures.

**Type: Negative Constraints (Red Flags)** — Lists of rationalizations the agent commonly uses to skip discipline, explicitly documented so the agent can self-detect when it's rationalizing.

**Type: Session Hook Bootstrap** — A <2,000 token document loaded at session start that forces the agent to invoke relevant skills before acting.

**Type: Multi-host Discovery Manifests** — Platform-specific manifest files that enable the same markdown skills to be discovered by different AI coding tools without modification.

## Methodology Cycle
Brainstorming → Git Worktree → Written Plan → Subagent Implementation → Code Review → Finishing

This linear workflow is the **composition rule** — skills are activated in order, not randomly.

## Reproducibility
High — Clone repo, copy to `~/.claude/skills/` or equivalent, restart agent session. No dependencies beyond the markdown files.

## Confidence
9/10 — Well-documented framework with clear philosophy and testable methodology.

## Sources
- https://blog.marcnuri.com/superpowers-claude-code-skills-framework
- https://github.com/obra/superpowers
