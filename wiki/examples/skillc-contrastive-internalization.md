---
type: Skill Bundle Example
title: "SkillC: Contrastive Skill Credit Assignment for Internalization"
description: "Skill-internalization RL that turns skill-helpfulness contrast into a dual-stream advantage learning signal (not only curriculum control), with adaptive curriculum over attribution strength and active-set pruning."
resource: https://arxiv.org/abs/2605.27899
timestamp: '2026-07-24T12:00:00Z'
date: 2026-07-24
sources:
- https://arxiv.org/abs/2605.27899
skills_included:
- "Paired skill-injected vs skill-free rollouts"
- "Contrastive Skill Credit Assignment (CSCA)"
- "Adaptive internalization curriculum"
context_elements:
- "Contrastive Skill Credit Assignment"
- "Dual-stream advantage estimator"
- "One-sided correction toward skill-free success"
- "Validation-level adaptive curriculum"
- "Monotonic active-set pruning"
composition: "For active skill types: sample paired skill+/skill\u2212 rollouts in same policy update; inject task-level contrast into dual-stream advantages; prune active set as internalization succeeds."
reproducibility: "arXiv:2605.27899; ALFWorld +5.5% and WebShop +4.4% over strongest prior internalization RL without runtime skills; competitive with skill-augmented RL."
rating: 8
---

# SkillC: Contrastive Skill Credit Assignment for Internalization

**Origin:** Lin, Kuai, Xue, Wang, arXiv:2605.27899, May 2026

## Overview

Skill-augmented RL keeps skills at inference; internalization RL withdraws them during training. Prior internalization (e.g. SKILL0) uses skill-helpfulness mainly for **curriculum control**, leaving the policy update unable to distinguish skill-dependent vs autonomous success. **SkillC** converts the contrast into a **direct learning signal** via Contrastive Skill Credit Assignment (CSCA).

## Method

1. Sample **paired** skill-injected and skill-free rollouts for active skill types within the same update
2. **Dual-stream advantage estimator** preserves global ranking while applying one-sided correction toward skill-free success
3. Smoothed validation signal drives adaptive curriculum over attribution strength, rollout allocation, and **monotonic active-set pruning**

## Results

| Benchmark | Gain vs strongest prior internalization RL |
|-----------|-----------------------------------------------|
| ALFWorld | +5.5% |
| WebShop | +4.4% |
| Runtime skills | **none** (zero-shot autonomous) |
| vs skill-augmented RL | remains competitive |

## Relation to Catalog

- Advances [skill0 skill internalization](skill0-skill-internalization.md) credit assignment
- Related to [skill0.5 joint internalization utilization](skill05-joint-internalization-utilization.md) hybrid pole
- Contrasts with [slim dynamic skill lifecycle](slim-dynamic-skill-lifecycle.md) (non-empty external boundary)

## Key Insight

Internalization needs **credit for autonomy**, not only a schedule that removes skills. Contrastive paired rollouts make skill-free success an explicit optimization target.

# Citations

- https://arxiv.org/abs/2605.27899
