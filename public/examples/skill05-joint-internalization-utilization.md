---
type: Skill Bundle Example
title: "Skill0.5: Joint Internalization of General Skills + Utilization of Task Skills"
description: "Agentic RL framework that refuses the full-external vs full-internal binary: internalizes general skills via privileged distillation while enforcing task-specific skill utilization via diagnostic probing on easy tasks."
resource: https://arxiv.org/abs/2605.28424
timestamp: '2026-07-24T12:00:00Z'
date: 2026-07-24
sources:
- https://arxiv.org/abs/2605.28424
skills_included:
- "General skill internalization (privileged distillation)"
- "Task-specific skill utilization enforcement"
- "Difficulty-aware mastery-tier routing"
context_elements:
- "General vs task-specific skill taxonomy"
- "Dynamic difficulty-aware router"
- "Mastery tiers with tailored optimization"
- "Diagnostic probing against shortcuts"
- "OOD generalization objective"
composition: "Difficulty-aware router streams tasks into mastery tiers: hard \u2192 internalize general skills; easy \u2192 probe and penalize shortcuts to force specific skill use."
reproducibility: "arXiv:2605.28424; ALFWorld + WebShop ID and OOD gains over memory-based and skill-based RL baselines."
rating: 8
---

# Skill0.5: Joint Internalization + Utilization

**Origin:** Zhu, Yu, Zhao et al., arXiv:2605.28424, May 2026

## Overview

Skills split naturally into **general** (broad cognitive transfer) and **task-specific** (dynamic execution). Full externalization costs context; full internalization risks overfitting and knowledge conflicts. **Skill0.5** jointly: (1) internalizes general skills, (2) forces utilization of task-specific skills.

## Method

- **Dynamic difficulty-aware router** assigns mastery tiers
- **Hard tasks:** privileged distillation internalizes general skills as cognitive foundation
- **Easy tasks:** diagnostic probing penalizes shortcuts and enforces specific skill utilization
- Goal: ID + **OOD** generalization without choosing a single extreme

## Relation to Catalog

- Middle path between [skill0](skill0-skill-internalization.md) (zero@infer) and pure external [skillopt](skillopt-trainable-skill-parameters.md)
- Complements [skillc](skillc-contrastive-internalization.md) credit machinery
- Related to [slim](slim-dynamic-skill-lifecycle.md) learned external boundary

## Key Insight

**Not all skills deserve the same fate.** General skills can sink into weights; task-specific skills should stay usable and enforced — a nuanced bundle lifecycle design rule.

# Citations

- https://arxiv.org/abs/2605.28424
