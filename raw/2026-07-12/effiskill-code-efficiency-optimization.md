# EffiSkill: Agent Skill Based Automated Code Efficiency Optimization

**Source:** https://arxiv.org/abs/2603.27850
**Date:** 2026-07-12
**Authors:** Zimu Wang, Yuling Shi, Mengfan Li, Zijun Liu, Jie M. Zhang, Chengcheng Wan, Xiaodong Gu
**Submitted:** 29 Mar 2026
**Signal:** 8/10

## Abstract

Code efficiency is a fundamental aspect of software quality, yet how to harness LLMs to optimize programs remains challenging. Prior approaches (one-shot rewriting, retrieved exemplars, prompt-based search) do not explicitly distill reusable optimization knowledge, which limits generalization beyond individual instances.

### Two-Stage Design
**Stage I — Skill Mining:** Mines Operator Skills and Meta Skills from large-scale slow/fast program pairs to build a skill library
- Operator Skills: concrete transformation mechanisms (e.g., loop unrolling, memoization)
- Meta Skills: higher-level optimization strategies (e.g., "reduce time complexity", "trade space for time")

**Stage II — Skill Application:** Applies the library to unseen programs through:
1. Execution-free diagnosis
2. Skill retrieval
3. Plan composition
4. Candidate generation
5. No runtime feedback needed

### Key Results (EffiBench-X)
- Improvement over strongest baseline by **3.69 to 12.52 percentage points** across model and language settings
- Mechanism-level skill reuse provides foundation for execution-free code optimization
- Resulting skill library serves as reusable resource for broader agent workflows

## Relevance to Skill Bundles

EffiSkill introduces the **two-tier skill hierarchy** pattern:
1. **Operator Skills** (concrete transformations) — like "atomic tools" in [[skillcraft-benchmark]]
2. **Meta Skills** (strategic optimization patterns) — like "composite skills"

This maps to the skill bundle composition pattern where:
- Low-level skills are mechanism-specific (operator-level)
- High-level skills are strategy-level (meta-level)
- Retrieval + plan composition bridges the two tiers

Key innovation: **execution-free** skill application — no runtime feedback needed, making it portable and lightweight.

## Key Quotes

> "Model recurring slow-to-fast transformations as reusable agent skills that capture both concrete transformation mechanisms and higher-level optimization strategies"

> "Mechanism-level skill reuse provides a useful foundation for execution-free code optimization"

## Links
- PDF: https://arxiv.org/pdf/2603.27850
- HTML: https://arxiv.org/html/2603.27850v1
- Same group as SkillMOO (Jie M. Zhang)
