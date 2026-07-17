---
type: Skill Bundle Example
title: 'SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?'
description: '- **arXiv:** 2603.00718 (submitted 28 Feb 2026, v2 10 Mar 2026) - **Authors:** Shiqi Chen, Jingze Gai, +15 others (Junxian He, Yee Whye Teh) - **Code:** https://github.com/shiqichen17/SkillCraft'
resource: https://arxiv.org/abs/2603.00718
timestamp: '2026-07-12T00:00:00Z'
date: 2026-07-12
source: https://arxiv.org/abs/2603.00718
authors:
- Chen
- Gai
- Zhou
- Zhang
- Zhu
- Li
- Wang
- Wang
- Chen
- Kaleb
- Miao
- Gao
- Lu
- Li
- He
- Teh
arxiv: 2603.00718
signal: 9
context_elements:
- Skill composition benchmark
- Auto-composition protocol
- Persistent skill library
---

# SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?

## Origin

- **arXiv:** 2603.00718 (submitted 28 Feb 2026, v2 10 Mar 2026)
- **Authors:** Shiqi Chen, Jingze Gai, +15 others (Junxian He, Yee Whye Teh)
- **Code:** https://github.com/shiqichen17/SkillCraft
- **Cited by:** 20

## Skills Included

SkillCraft is a **benchmark** that stress-tests agent ability to form and reuse higher-level tool compositions (called "Skills").

### Skill Definition
- Skills = higher-level tool compositions
- Auto-composed from atomic tools by the agent itself
- Cached and reused inside and across tasks
- Accumulates as a **persistent library** of reusable skills

## Context Elements

### Benchmark Design
- Difficulty scaled along **quantitative** (number of tools) and **structural** (composition depth) dimensions
- Realistic, highly compositional tool-use scenarios
- Designed to elicit skill abstraction and cross-task reuse

### Auto-Composition Protocol
- Lightweight evaluation protocol
- Agents auto-compose atomic tools into executable Skills
- Cache and reuse across tasks
- Accumulates persistent skill library

## Composition Notes

SkillCraft validates the core skill bundle thesis: **composing tools into reusable skills dramatically improves efficiency**.

### Key Results
- Token usage reduced by up to **80%** by skill saving and reuse
- Success rate strongly correlates with tool composition ability at test time
- Compositional skill acquisition is a **core capability** for agents

### Key Insight
The inverse of static skill bundles: instead of humans authoring skills, agents **auto-compose** them from tools and build their own persistent library.

## Reproducibility

- Open-source code: https://github.com/shiqichen17/SkillCraft
- Project page: https://skillcraft-website.github.io/page

## Connections

- Auto-composition pattern complements [orca cognitive runtime](orca-cognitive-runtime.md) (declarative composition) and [effiskill code efficiency optimization](effiskill-code-efficiency-optimization.md) (two-tier mining)
- Cited by [coevoskills self evolving skills](coevoskills-self-evolving-skills.md) as foundational
- 80% token savings quantifies efficiency benefit (cf. [skillreducer token efficiency](skillreducer-token-efficiency.md)'s 48%+39% compression)
- Skill abstraction maps to the atomic skill decomposition pattern (see arXiv:2604.05013, withdrawn)

