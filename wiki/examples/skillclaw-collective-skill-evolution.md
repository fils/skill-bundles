---
title: "SkillClaw: Collective Skill Evolution with Agentic Evolver"
date: 2026-07-15
sources: ["arXiv:2604.08377", "https://github.com/AMAP-ML/SkillClaw"]
skills_included: ["Trajectory aggregation", "Autonomous skill evolver", "Shared skill repository", "Skill synchronization", "Skill reload (poll/webhook)"]
context_elements: ["Collective skill evolution (cross-user + over-time)", "Autonomous evolver (pattern recognition → skill update)", "Shared synchronized skill repository", "Trajectory aggregation pipeline", "Multi-framework compatibility (OpenClaw, Hermes)"]
composition: "Meta-skill framework: trajectory collector → autonomous evolver (identifies recurring patterns → refines/extends skills) → shared repository → cross-user synchronization. Users contribute experience passively; improvements propagate system-wide."
reproducibility: "Open-sourced on GitHub (AMAP-ML/SkillClaw, 2.1k stars, 202 forks, MIT license). Evaluated on WildClawBench with Qwen3-Max. Supports OpenClaw and Hermes."
rating: 9
---

# SkillClaw: Collective Skill Evolution with Agentic Evolver

**Origin:** AMAP-ML (Alibaba Maps AI), arXiv:2604.08377, Apr 2026
**GitHub:** https://github.com/AMAP-ML/SkillClaw (2.1k★, 202 forks)
**Citations:** 42

## Overview

SkillClaw is a framework for **collective skill evolution** in multi-user agent ecosystems. It treats cross-user and over-time interactions as the primary signal for improving skills. Unlike single-user skill refinement, SkillClaw aggregates trajectories from all users and processes them through an autonomous evolver that identifies recurring behavioral patterns and translates them into skill updates.

## Architecture

1. **Trajectory aggregation** — Continuously collects interaction trajectories from all users (passive, no additional user effort)
2. **Autonomous evolver** — Identifies recurring behavioral patterns in aggregated trajectories; translates patterns into skill updates (refine existing skills or extend with new capabilities)
3. **Shared repository** — Skills maintained in a shared repository, synchronized across users
4. **Skill reload** — Poll loop (30s default, immediate first pull) or webhook for syncing evolved skills to running agents

## Key Innovations

- **Cross-user knowledge transfer** — Improvements discovered in one context propagate system-wide
- **Cumulative capability improvement** — Skills compound experience across sessions, agents, devices, and users
- **Multi-framework support** — OpenClaw and Hermes agent frameworks
- **Zero additional user effort** — Trajectory collection is passive

## Evaluation

- Benchmark: WildClawBench
- Model: Qwen3-Max
- Result: Significant improvement in real-world agent scenarios with limited interaction and feedback

## Context Elements

- **Collective skill evolution** — Novel evolution model: cross-user + over-time (not single-user or single-session)
- **Autonomous evolver** — Pattern recognition → skill update pipeline (self-improving skill infrastructure)
- **Shared synchronized repository** — Distributed skill knowledge base with automatic sync
- **Trajectory aggregation** — Cross-user interaction logging as improvement signal

## Relation to Skill Bundle Patterns

SkillClaw represents a **meta-skill bundle**: the bundle is the evolution system itself (trajectory collector + evolver + shared repo + sync). This extends the skill lifecycle from static deployment to continuous multi-user evolution.

- Extends [[memento-skills-agent-designing-agent]] (which mentioned SkillClaw for collective evolution)
- Complements [[coevoskills-self-evolving-skills]] (co-evolutionary verification approach)
- Related to [[skill1-unified-skill-evolution-rl]] (RL-based unified evolution)
- Related to [[exif-automated-skill-discovery]] (self-play skill discovery)
- Connects to [[externalization-llm-agents-unified-review]] (shared agent infrastructure as emerging direction)

## Key Insight

Skills don't need to be static after deployment. By aggregating multi-user interaction trajectories and processing them through an autonomous evolver, skills can collectively evolve — improvements in one context benefit all users. This transforms skill bundles from static artifacts into living, self-improving infrastructure.

[[backlinks]]
