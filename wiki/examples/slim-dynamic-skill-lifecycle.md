---
type: Skill Bundle Example
title: "SLIM: Dynamic Skill Lifecycle Management (Retain\u2013Retire\u2013Expand)"
description: "Treats the active external skill set as a dynamic optimization variable jointly trained with the policy via leave-one-skill-out marginal contribution; converges to a compact non-empty skill boundary rather than full accumulation or zero-skill inference."
resource: https://arxiv.org/abs/2605.10923
timestamp: '2026-07-24T12:00:00Z'
date: 2026-07-24
sources:
- https://arxiv.org/abs/2605.10923
- https://github.com/ejhshen/SLIM
skills_included:
- "Leave-one-skill-out marginal contribution"
- "Retain high-value external skills"
- "Retire negligible skills after exposure"
- "Expand bank on persistent failure coverage gaps"
context_elements:
- "Dynamic active skill set as optimization variable"
- "Leave-one-skill-out (LOSO) validation"
- "Retain\u2013retire\u2013expand lifecycle ops"
- "Non-monotonic external capability trajectory"
- "Learned internal/external boundary"
composition: "During RL: retrieve from active pool \u2192 estimate LOSO marginal external contribution \u2192 retain/retire/expand \u2192 continue policy optimization with updated active set."
reproducibility: "GitHub ejhshen/SLIM; +7.1pp avg over best baselines on ALFWorld + SearchQA vs GRPO/SkillRL/Skill0."
rating: 9
---

# SLIM: Dynamic Skill Lifecycle Management

**Origin:** Shen, Zhang, Zhao, Cheng (CUHK / Lanzhou), arXiv:2605.10923, May 2026
**Code:** https://github.com/ejhshen/SLIM

## Overview

Existing skill-based agentic RL assumes the external skill set either **monotonically accumulates** (SkillRL-style) or **anneals to zero** (SKILL0-style). SLIM argues the optimal active set is **non-monotonic**, task- and stage-dependent under limited parametric capacity and uneven skill value.

## Lifecycle Operations

| Op | Trigger |
|----|---------|
| **Retain** | High leave-one-skill-out (LOSO) marginal contribution |
| **Retire** | Contribution becomes negligible after sufficient exposure |
| **Expand** | Persistent failures reveal missing capability coverage |

Active external skill set is a **joint optimization variable** with the policy.

## Results

- **+7.1pp** average over best baselines across ALFWorld and SearchQA
- Converges to a **compact non-empty** active skill set (neither full bank nor zero)
- Some skills absorbed into policy; others keep external value → learned boundary

## Relation to Catalog

- Synthesizes poles of [skill0](skill0-skill-internalization.md), SkillRL-class augmentation, and [skillopt](skillopt-trainable-skill-parameters.md)
- Complements [skillops](skillops-self-maintaining-skill-libraries.md) (library hygiene) with **training-time** lifecycle
- Aligns with Externalization trade-off in [externalization llm agents](externalization-llm-agents-unified-review.md)

## Key Insight

The endpoint of skill-augmented RL is neither “all skills forever” nor “no skills at inference,” but a **learned external capability boundary**.

# Citations

- https://arxiv.org/abs/2605.10923
- https://github.com/ejhshen/SLIM
