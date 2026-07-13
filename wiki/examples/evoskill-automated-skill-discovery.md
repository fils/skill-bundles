---
title: "EvoSkill: Automated Skill Discovery for Multi-Agent Systems"
date: 2026-07-13
sources: ["arXiv:2603.02766", "https://github.com/sentient-agi/EvoSkill"]
skills_included: ["Executor Agent", "Proposer Agent", "Skill-Builder Agent"]
context_elements: ["Pareto frontier governance", "Git-backed version control (program/ branches + frontier/ tags)", "Structured skill folders (SKILL.md + trigger metadata + helper scripts)", "Multi-tolerance scoring (5 tolerance levels)", "Meta-skill bootstrapping"]
composition: "Three-agent collaboration: Executor runs tasks, Proposer analyzes failures and proposes skills, Skill-Builder materializes into skill folders. Pareto frontier governs selection."
reproducibility: "Open-sourced on GitHub (1k stars, 322 commits). Git-backed program version control enables full lineage reconstruction. Supports Claude Code, Codex, OpenCode."
rating: 9
---

# EvoSkill: Automated Skill Discovery for Multi-Agent Systems

**Origin:** Sentient + Virginia Tech (arXiv:2603.02766, March 2026)
**GitHub:** https://github.com/sentient-agi/EvoSkill (1k stars, 110 forks, 12 contributors)

## Overview

EvoSkill is a self-evolving framework that automatically discovers and refines agent skills through iterative failure analysis. Unlike evolutionary approaches that optimize low-level artifacts (prompts, code) tightly coupled to specific models/tasks, EvoSkill operates at the **skill abstraction level** — the underlying model remains frozen, and only the skill repository evolves.

## Three-Agent Architecture

1. **Executor Agent (AA):** Executes tasks under the current agent program. Starts with no skills.
2. **Proposer Agent (PP):** Analyzes execution traces, predicted answers, and ground-truth to diagnose failures. Proposes new skills or edits to existing ones. Ground-truth enables root-cause diagnosis (like error analysis in supervised learning).
3. **Skill-Builder Agent (SS):** Materializes proposals into concrete skill folders: trigger metadata + procedural instructions (SKILL.md) + optional helper scripts (Python/TypeScript). Bootstrapped with a meta-skill codifying best practices for skill authoring.

## Pareto Frontier Selection

A bounded set of top-performing programs (K=3 default) tracked via git tags. Each program stored on a dedicated git branch with YAML configuration recording name, parent pointer, generation counter, system prompt, tools, and evaluation scores. Children admitted only if they outscore the worst frontier member. Tree-structured search with full lineage reconstruction via parent pointers.

## Key Results

| Benchmark | Baseline | EvoSkill | Improvement |
|-----------|----------|----------|-------------|
| OfficeQA | 60.6% | 67.9% | +7.3% |
| SealQA | 26.6% | 38.7% | +12.1% |
| BrowseComp (zero-shot transfer) | — | +5.3% | Transfer from SealQA |

**Zero-shot transfer:** Skills evolved on SealQA transfer to BrowseComp without modification, proving skill-level optimization produces capabilities that generalize beyond the training task.

## Context Elements

- **Pareto frontier governance** — validation-gated skill admission
- **Git-backed version control** — program/ branches + frontier/ tags for full lineage
- **Structured skill folders** — SKILL.md + trigger metadata + helper scripts
- **Multi-tolerance scoring** — weighted average over 5 tolerance levels
- **Meta-skill bootstrapping** — best-practice codification for skill authoring

## Relation to Skill Bundle Patterns

EvoSkill represents the **auto-discovery** paradigm in the skill bundle ecosystem. It complements:
- [[coevoskills-self-evolving-skills]] (evolution-based) and [[skillmoo-multi-objective-optimization]] (search-based) as skill optimization approaches
- [[skillcraft-benchmark]] (composition) by demonstrating skills can be discovered, not just composed
- [[skillreducer-token-efficiency]] (content reduction) — both modify skills but EvoSkill creates, SkillReducer reduces

## Key Insight

Skills discovered through failure analysis at the skill abstraction level (not prompt/code level) produce **transferable capabilities** — a skill evolved on one benchmark improves a completely different one without modification. This is direct evidence that skill-level optimization captures generalizable knowledge.

[[backlinks]]
