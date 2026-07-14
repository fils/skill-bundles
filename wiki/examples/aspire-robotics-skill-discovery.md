---
title: "ASPIRE: Agentic Skill Programming through Iterative Robot Exploration"
date: 2026-07-14
sources: ["arXiv:2607.00272", "https://research.nvidia.com/labs/gear/aspire/"]
skills_included: ["Closed-loop robot execution engine", "Skill library (code-as-policy programs)", "Evolutionary search for task/program diversity"]
context_elements: ["Multimodal execution traces (failure diagnosis)", "Validated repair knowledge compounding", "Evolutionary search governance", "Cross-embodiment skill transfer", "Sim-to-real transfer verification"]
composition: "Three-component open-ended loop: execution engine generates traces → skill library distills validated fixes → evolutionary search explores diverse task sequences and control programs."
reproducibility: "Project page with PDF; NVIDIA GEAR Lab; 43 pages, 12 figures, 9 tables. Code-as-policy paradigm with Claude as coding agent."
rating: 9
---

# ASPIRE: Agentic Skill Programming through Iterative Robot Exploration

**Origin:** NVIDIA GEAR Lab + UC Berkeley + UT Austin (arXiv:2607.00272, June 2026)
**Authors:** Runyu Lu, Yubo Wu, ..., Linxi "Jim" Fan, Guanzhi Wang, Ken Goldberg

## Overview

ASPIRE is a continual learning system for robotics that autonomously writes and refines robot control programs in a **code-as-policy** paradigm while compounding experience into a reusable skill library. A coding agent (Claude) writes robot control code, executes it, diagnoses failures from multimodal traces, and repairs programs. Validated fixes are distilled into reusable skills that persist across tasks, simulation/real-world settings, and embodiments.

## Three Components

1. **Closed-loop robot execution engine** — exposes fine-grained multimodal traces for autonomous failure diagnosis, repair synthesis, and validation
2. **Continually expanding skill library** — distills validated fixes into reusable, transferable knowledge
3. **Evolutionary search** — generates diverse task sequences and control programs to explore beyond single-trajectory refinement

## Key Results

| Benchmark | Improvement |
|-----------|------------|
| LIBERO-Pro (perturbation) | +77% over prior methods |
| Robosuite (bimanual handover) | +72% |
| BEHAVIOR-1K (long-horizon household) | +32% |
| LIBERO-Pro Long (zero-shot) | 31% vs 4% for prior methods |

Sim-to-real transfer: simulation-discovered skills reduce real-robot programming effort across different embodiments and robot APIs.

## Context Elements

- **Multimodal execution traces** — enable autonomous failure diagnosis
- **Validated repair knowledge** — skills compound from validated fixes
- **Evolutionary search** — governance mechanism for skill diversity
- **Cross-embodiment transfer** — skills portable across robot platforms
- **Sim-to-real transfer verification** — evidence of real-world applicability

## Relation to Skill Bundle Patterns

ASPIRE brings skill bundle patterns to the **robotics domain**:
- Code-as-policy = skills as executable programs with formal structure
- Skill library = persistent, transferable knowledge (analogous to [[evoskill-automated-skill-discovery]]'s skill folders)
- Evolutionary search = skill discovery mechanism (complements [[skill1-unified-skill-evolution-rl]]'s RL-based approach)
- Cross-embodiment transfer = skill portability evidence (parallels [[skillmigrator-cross-domain-transfer]]'s cross-domain transfer)

## Key Insight

Robotics skill discovery via code-as-policy + evolutionary search produces skills that transfer across tasks, embodiments, and sim-to-real. The accumulated library enables zero-shot generalization to unseen long-horizon tasks (31% vs 4%), demonstrating that compounding validated repairs into a skill library is a viable continual learning strategy.

[[backlinks]]
