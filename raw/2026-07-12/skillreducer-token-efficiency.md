# SkillReducer: Optimizing LLM Agent Skills for Token Efficiency

**Source:** https://arxiv.org/abs/2603.29919
**Date:** 2026-07-12
**Authors:** Yudong Gao, Zongjie Li, Yuanyuan Yuan, Zimo Ji, Pingchuan Ma, Shuai Wang
**Submitted:** 31 Mar 2026 (v1), revised 24 Jun 2026 (v2)
**Signal:** 9/10

## Abstract

LLM-based coding agents rely on skills, pre-packaged instruction sets that extend agent capabilities, yet every token of skill content injected into the context window incurs both monetary cost and attention dilution.

### Large-Scale Empirical Study (55,315 skills)
Systemic inefficiencies found:
- **26.4%** lack routing descriptions entirely
- Over **60%** of body content is non-actionable
- Reference files can inject **tens of thousands of tokens** per invocation

### SkillReducer Two-Stage Framework

**Stage 1 — Routing Layer Optimization:**
- Compresses verbose descriptions
- Generates missing descriptions via **adversarial delta debugging**

**Stage 2 — Skill Body Restructuring:**
- **Taxonomy-driven classification** of content
- **Progressive disclosure** — separates actionable core rules from supplementary content loaded on demand
- **Faithfulness checks** + **self-correcting feedback loop**

### Key Results (600 skills + SkillsBench)
- **48%** description compression
- **39%** body compression
- Functional quality **improved by 2.8%** (less-is-more effect)
- Benefits transfer across **5 models from 4 families** (mean retention 0.965)
- Generalizes to independent agent framework

## Relevance to Skill Bundles

SkillReducer reveals a critical problem in the skill bundle ecosystem: **bloat**. Key contributions:
1. **First large-scale empirical study** of skill content inefficiency (55,315 skills)
2. **Less-is-more effect** — removing non-essential content improves performance
3. **Progressive disclosure** pattern — load supplementary content on demand, not always
4. **Taxonomy-driven classification** — structured approach to identifying what's actionable vs supplementary
5. **Cross-model transfer** — optimization generalizes across model families

This is the skill optimization counterpart to [[skillmoo-multi-objective-optimization]] (search-based) and [[coevoskills-self-evolving-skills]] (evolution-based):
- SkillMOO: search-based optimization (NSGA-II)
- CoEvoSkills: evolutionary co-optimization
- SkillReducer: content reduction (delta debugging + taxonomy)

## Key Quotes

> "Every token of skill content injected into the context window incurs both monetary cost and attention dilution"

> "26.4% lack routing descriptions entirely, over 60% of body content is non-actionable"

> "A less-is-more effect where removing non-essential content reduces distraction in the context window"

## Links
- PDF: https://arxiv.org/pdf/2603.29919
- HTML: https://arxiv.org/html/2603.29919v2
