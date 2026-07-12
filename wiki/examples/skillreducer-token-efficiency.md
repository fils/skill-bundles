---
title: "SkillReducer: Optimizing LLM Agent Skills for Token Efficiency"
date: 2026-07-12
source: https://arxiv.org/abs/2603.29919
authors: [Gao, Li, Yuan, Ji, Ma, Wang]
arxiv: 2603.29919
signal: 9
context_elements: [Delta debugging, Taxonomy-driven classification, Progressive disclosure, Faithfulness checks]
---

# SkillReducer: Optimizing LLM Agent Skills for Token Efficiency

## Origin

- **arXiv:** 2603.29919 (submitted 31 Mar 2026, v2 24 Jun 2026)
- **Authors:** Yudong Gao, Zongjie Li, Yuanyuan Yuan, Zimo Ji, Pingchuan Ma, Shuai Wang
- **Study scale:** 55,315 publicly available skills

## Skills Included

SkillReducer is a **skill optimization framework** that reduces token waste in agent skills while preserving or improving functional quality.

## Context Elements

### Empirical Study (55,315 skills)
Systemic inefficiencies:
- **26.4%** lack routing descriptions entirely
- Over **60%** of body content is non-actionable
- Reference files inject **tens of thousands of tokens** per invocation

### Two-Stage Optimization

**Stage 1 — Routing Layer:**
- Compresses verbose descriptions
- Generates missing descriptions via **adversarial delta debugging**

**Stage 2 — Body Restructuring:**
- **Taxonomy-driven classification** of content
- **Progressive disclosure** — separates actionable core rules from supplementary content loaded on demand
- **Faithfulness checks** + **self-correcting feedback loop**

## Composition Notes

SkillReducer reveals the **bloat problem** in the skill bundle ecosystem and demonstrates a **less-is-more effect**:

1. Removing non-essential content reduces distraction in the context window
2. Functional quality actually **improves by 2.8%** when content is optimized
3. Progressive disclosure pattern: load supplementary content on demand, not always
4. Taxonomy-driven classification: structured approach to identifying actionable vs supplementary content

### Key Results (600 skills + SkillsBench)
- **48%** description compression
- **39%** body compression
- Functional quality **+2.8%** (less-is-more)
- Cross-model transfer: **5 models, 4 families**, mean retention 0.965
- Generalizes to independent agent framework

## Reproducibility

- 55,315 skills studied + 600 skills optimized + SkillsBench benchmark
- CC-BY license

## Connections

- **Skill optimization triad:**
  - [[skillmoo-multi-objective-optimization]]: search-based (NSGA-II Pareto)
  - [[coevoskills-self-evolving-skills]]: evolution-based (co-evolutionary verification)
  - SkillReducer: content reduction (delta debugging + taxonomy)
- 26.4% missing routing + 60% non-actionable → quantifies the problem [[skillsbench-agent-skills-benchmark]] tests
- Progressive disclosure pattern connects to [[orca-cognitive-runtime]]'s DAG-based lazy loading

[[backlinks]]
