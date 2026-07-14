---
title: "Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning"
date: 2026-07-14
sources: ["arXiv:2605.06130", "https://github.com/AlphaLab-USTC/Skill1"]
skills_included: ["Skill selection (query + re-rank)", "Skill utilization (task solving)", "Skill distillation (trajectory → new skill)"]
context_elements: ["Persistent skill library", "Single task-outcome reward signal", "Frequency decomposition credit assignment", "Co-evolution of select + use + distill"]
composition: "Single policy generates query → searches skill library → re-ranks candidates → solves task conditioned on selected skill → distills new skill from trajectory. All learning from one task-outcome signal."
reproducibility: "Open-sourced on GitHub (AlphaLab-USTC/Skill1). 18 citations. ALFWorld + WebShop benchmarks."
rating: 8
---

# Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning

**Origin:** AlphaLab, USTC (arXiv:2605.06130, May 2026)
**GitHub:** https://github.com/AlphaLab-USTC/Skill1
**Citations:** 18

## Overview

Skill1 is a framework that trains a **single policy** to co-evolve skill selection, utilization, and distillation toward a shared task-outcome objective. It addresses the problem that existing methods optimize these three capabilities in isolation or with separate reward sources, resulting in partial and conflicting evolution.

## Three Coupled Capabilities

1. **Skill selection** — agent generates a query to search the skill library and re-ranks candidates
2. **Skill utilization** — agent solves the task conditioned on the selected skill
3. **Skill distillation** — agent distills a new skill from the trajectory

## Key Innovation: Frequency Decomposition

All learning derives from a **single task-outcome signal**. The policy's:
- **Low-frequency trend** credits selection (long-term skill quality)
- **High-frequency variation** credits distillation (per-task skill creation)

This frequency decomposition avoids the conflicting reward problem of separate optimization.

## Results

- ALFWorld and WebShop benchmarks
- Outperforms prior skill-based and RL baselines
- Training dynamics confirm co-evolution of all three capabilities
- Ablations: removing any credit signal degrades evolution

## Context Elements

- **Persistent skill library** — reusable strategies across tasks
- **Single task-outcome signal** — unified governance for skill lifecycle
- **Frequency decomposition** — novel credit assignment for skill management
- **Co-evolution** — select + use + distill evolve together

## Relation to Skill Bundle Patterns

Skill1 unifies the three core skill lifecycle operations under a single learning signal:
- Select → Use → Distill = complete skill lifecycle (parallels [[memento-skills-agent-designing-agent]]'s Read-Write cycle)
- RL-based approach complements [[evoskill-automated-skill-discovery]] (failure-driven) and [[aspire-robotics-skill-discovery]] (evolutionary search)
- Frequency decomposition is a novel governance pattern for credit assignment
- Skill distillation = skill creation from experience (parallels [[coevoskills-self-evolving-skills]]'s co-evolutionary verification)

## Key Insight

Skill selection, utilization, and distillation are coupled capabilities that must co-evolve under a single reward signal. Separate optimization leads to partial and conflicting evolution. The frequency decomposition of a single task-outcome signal naturally credits selection (low-freq) and distillation (high-freq), enabling unified skill lifecycle management.

[[backlinks]]
