---
title: "SkillMOO: Multi-Objective Optimization of Agent Skills for SE"
date: 2026-07-12
source: https://arxiv.org/abs/2604.09297
authors: [Gong, Gu, Fei, Cao, Twist, Geiger, Han, Sobania, Sarro, Zhang]
arxiv: 2604.09297
signal: 9
context_elements: [Multi-objective optimization, NSGA-II Pareto selection, Skill edit taxonomy]
---

# SkillMOO: Multi-Objective Optimization of Agent Skills for Software Engineering

## Origin

- **arXiv:** 2604.09297 (submitted 10 Apr 2026, v2 17 May 2026)
- **Authors:** Jingzhi Gong, Ruizhen Gu, Zhiwei Fei, Yazhuo Cao, Lukas Twist, Alina Geiger, Shuo Han, Dominik Sobania, Federica Sarro, Jie M. Zhang
- **Benchmark:** SkillsBench (16 SE tasks)

## Skills Included

SkillMOO is not a skill bundle itself — it is a **skill bundle optimization framework** that evolves existing skill bundles through LLM-proposed edits.

## Context Elements

### Multi-Objective Optimization
- Treats skill bundles as **multi-objective search objects**
- Uses **NSGA-II Pareto selection** on two objectives: pass rate and inference cost
- LLM proposes edits; NSGA-II selects the Pareto frontier

### Skill Edit Taxonomy
Analysis of 38 skill edits reveals two dominant successful operations:
- **Pruning** — removing unnecessary skill content
- **Substitution** — replacing one skill approach with another

## Composition Notes

SkillMOO introduces the first **cost-aware, search-based skill engineering** paradigm:
1. Current practice: static, hand-crafted bundles or evolution on pass rate alone
2. Problem: a skill can improve task success while raising token cost or introducing misleading guidance
3. Solution: multi-objective Pareto optimization that balances pass rate AND cost

### Key Results
- Top pass rate rank on **11/12** non-zero-pass tasks
- Cost reductions up to **31.7%** over static bundles
- Pass rate gains up to **21 percentage points**
- Up to **131%** pass rate improvement while reducing cost up to 32%

## Reproducibility

- Evaluated on SkillsBench (shared benchmark with [[skillsbench-agent-skills-benchmark]])
- 16 SE tasks, 38 skill edits analyzed
- CC-BY 4.0 license

## Connections

- Complements [[coevoskills-self-evolving-skills]] (co-evolutionary verification) — SkillMOO optimizes structure, CoEvoSkills optimizes content+verifier
- Complements [[skillreducer-token-efficiency]] — SkillReducer reduces content, SkillMOO searches configuration space
- Uses [[skillsbench-agent-skills-benchmark]] as evaluation platform
- Same research group as [[effiskill-code-efficiency-optimization]] (Jie M. Zhang)

[[backlinks]]
