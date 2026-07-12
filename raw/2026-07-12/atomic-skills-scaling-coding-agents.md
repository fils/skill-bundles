# Scaling Coding Agents via Atomic Skills

**Source:** https://arxiv.org/abs/2604.05013
**Date:** 2026-07-12
**Authors:** Yue Liu
**Submitted:** 6 Apr 2026 (v1), withdrawn 24 Apr 2026 (v2)
**Signal:** 7/10
**Status:** WITHDRAWN — "significant errors discovered in the data after submission, which affect the validity of the results." Author may submit a corrected version.

## Abstract

Current LLM coding agents are predominantly trained on composite benchmarks (e.g., bug fixing), which often leads to task-specific overfitting and limited generalization. This paper proposes a novel scaling paradigm that shifts the focus from task-level optimization to atomic skill mastery.

### Five Fundamental Atomic Skills
1. Code localization
2. Code editing
3. Unit-test generation
4. Issue reproduction
5. Code review

These atomic skills serve as "basis vectors" for complex software engineering tasks — more generalizable and composable than composite tasks.

### Key Idea
- Joint RL over atomic skills (not task-level optimization)
- Atomic skills consistently improved without negative interference or trade-offs
- Improvements generalize to unseen composite tasks (bug-fixing, refactoring, ML engineering, code security)
- Joint RL improves average performance by 18.7% on 5 atomic skills and 5 composite tasks

## Relevance to Skill Bundles

This paper introduces the **atomic skill decomposition** pattern — the idea that complex skills can be decomposed into fundamental, reusable "basis vectors" that can be trained jointly. This is directly relevant to skill bundle composition:
- Skills as basis vectors (not monolithic tools)
- Joint RL without interference (compositional training)
- Generalization from atomic → composite tasks

**Caveat:** Paper is WITHDRAWN. Results may not be reliable. The conceptual framework (atomic skill decomposition) is still valuable, but empirical claims need verification.

## Key Quotes

> "We first formalize five fundamental atomic skills... that serve as the basis vectors for complex software engineering tasks."

> "Atomic skills are consistently improved without negative interference or trade-offs between them."

> "Improvements in these atomic skills generalize well to other unseen composite coding tasks."
