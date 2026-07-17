---
type: Skill Bundle Example
title: 'Memento-Skills: Let Agents Design Agents'
description: 'Memento-Skills is a generalist, continually-learnable LLM agent system that functions as an **agent-designing agent**: it autonomously constructs, adapts, and improves task-specific agents through experience.'
resource: https://arxiv.org/abs/2603.18743
timestamp: '2026-07-14T00:00:00Z'
date: 2026-07-14
sources:
- arXiv:2603.18743
- https://github.com/Memento-Teams/Memento-Skills
skills_included:
- Behaviour-trainable skill router
- Read-Write Reflective Learning
- Skill library (structured markdown files)
- Stateful prompts
context_elements:
- Skills as persistent evolving memory (markdown)
- Read-Write Reflective Learning cycle
- Stateful prompts (context carry-forward)
- Skill router (selection governance)
- Continual learning without LLM parameter updates
composition: 'Agent-designing agent: read phase selects skills via router, write phase updates/expands skill library. Skills as structured markdown files serve as persistent, evolving memory.'
reproducibility: Open-sourced on GitHub (Memento-Teams/Memento-Skills). Technical report with 27 citations.
rating: 9
---

# Memento-Skills: Let Agents Design Agents

**Origin:** Memento-Teams (arXiv:2603.18743, March 2026)
**GitHub:** https://github.com/Memento-Teams/Memento-Skills
**Citations:** 27

## Overview

Memento-Skills is a generalist, continually-learnable LLM agent system that functions as an **agent-designing agent**: it autonomously constructs, adapts, and improves task-specific agents through experience. Built on a memory-based reinforcement learning framework with **stateful prompts**, where reusable skills (stored as structured markdown files) serve as persistent, evolving memory encoding both behaviour and context.

## Read-Write Reflective Learning

- **Read phase:** A behaviour-trainable skill router selects the most relevant skill conditioned on the current stateful prompt
- **Write phase:** The agent updates and expands its skill library based on new experience
- This enables **continual learning without updating LLM parameters** — all adaptation is realised through the evolution of externalised skills and prompts

## Key Results

| Benchmark | Relative Improvement |
|-----------|-------------------|
| General AI Assistants | +26.2% |
| Humanity's Last Exam | +116.2% |

80% task success vs. prior approaches relying on human-designed agents.

## Context Elements

- **Skills as structured markdown files** — persistent, evolving memory matching agentskills.io SKILL.md format
- **Stateful prompts** — carry forward knowledge across interactions
- **Skill router** — selection/governance mechanism for skill dispatch
- **Read-Write Reflective Learning** — complete skill lifecycle (creation → routing → refinement)
- **Agent-designing agent** — meta-level skill composition (skills create skills)

## Relation to Skill Bundle Patterns

Memento-Skills is a canonical example of **skills as the primary adaptation mechanism**:
- Skills = structured markdown files (matching [agent skills spec](agent-skills-spec.md) format)
- Read-Write cycle = skill lifecycle (parallels [skill1 unified skill evolution rl](skill1-unified-skill-evolution-rl.md)'s select-use-distill)
- Agent-designing agent = meta-level composition (skills create skills for new tasks)
- Continual learning without LLM updates = skills as the adaptation substrate

Also mentions **SkillClaw** framework for collective skill evolution (multi-agent skill sharing).

## Key Insight

Skills stored as structured markdown files can serve as the sole adaptation mechanism for continual learning — no LLM parameter updates needed. The Read-Write Reflective Learning cycle (read = select skill, write = update skill library) is a complete skill lifecycle that enables agents to design other agents end-to-end.

