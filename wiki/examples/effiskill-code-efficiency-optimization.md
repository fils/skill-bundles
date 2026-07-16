---
type: Skill Bundle Example
title: 'EffiSkill: Agent Skill Based Code Efficiency Optimization'
description: '- **arXiv:** 2603.27850 (submitted 29 Mar 2026) - **Authors:** Zimu Wang, Yuling Shi, Mengfan Li, Zijun Liu, Jie M.'
resource: https://arxiv.org/abs/2603.27850
timestamp: '2026-07-12T00:00:00Z'
date: 2026-07-12
source: https://arxiv.org/abs/2603.27850
authors:
- Wang
- Shi
- Li
- Liu
- Zhang
- Wan
- Gu
arxiv: 2603.2785
signal: 8
context_elements:
- Two-tier skill hierarchy
- Operator Skills
- Meta Skills
- Execution-free diagnosis
---

# EffiSkill: Agent Skill Based Automated Code Efficiency Optimization

## Origin

- **arXiv:** 2603.27850 (submitted 29 Mar 2026)
- **Authors:** Zimu Wang, Yuling Shi, Mengfan Li, Zijun Liu, Jie M. Zhang, Chengcheng Wan, Xiaodong Gu
- **Benchmark:** EffiBench-X

## Skills Included

EffiSkill builds a portable optimization toolbox of two skill tiers:

### Operator Skills (concrete transformations)
- Mechanism-level: loop unrolling, memoization, algorithm substitution
- Captures concrete slow-to-fast transformation mechanisms

### Meta Skills (strategic optimization patterns)
- Strategy-level: "reduce time complexity", "trade space for time"
- Captures higher-level optimization strategies

## Context Elements

### Two-Stage Pipeline
**Stage I — Skill Mining:**
- Mines Operator and Meta Skills from large-scale slow/fast program pairs
- Builds a reusable skill library

**Stage II — Skill Application:**
1. Execution-free diagnosis (no runtime feedback needed)
2. Skill retrieval from the library
3. Plan composition (combining Operator + Meta Skills)
4. Candidate generation

## Composition Notes

EffiSkill demonstrates a **two-tier skill hierarchy** pattern:
- Low-level skills: mechanism-specific (Operator Skills)
- High-level skills: strategy-level (Meta Skills)
- Retrieval + plan composition bridges the two tiers

Key innovation: **execution-free** skill application — no runtime feedback needed, making it portable and lightweight.

### Key Results
- Improvement over strongest baseline by **3.69–12.52 percentage points** across model/language settings
- Mechanism-level skill reuse validated

## Reproducibility

- EffiBench-X benchmark
- Same research group as [skillmoo multi objective optimization](skillmoo-multi-objective-optimization.md) (Jie M. Zhang)

## Connections

- Two-tier hierarchy maps to [skillcraft benchmark](skillcraft-benchmark.md)'s atomic tool → skill composition pattern
- Skill library concept similar to [orca cognitive runtime](orca-cognitive-runtime.md)'s capability registry
- Execution-free approach contrasts with [coevoskills self evolving skills](coevoskills-self-evolving-skills.md)'s runtime verification

