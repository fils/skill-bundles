# SkillMOO: Multi-Objective Optimization of Agent Skills for Software Engineering

**Source:** https://arxiv.org/abs/2604.09297
**Date:** 2026-07-12
**Authors:** Jingzhi Gong, Ruizhen Gu, Zhiwei Fei, Yazhuo Cao, Lukas Twist, Alina Geiger, Shuo Han, Dominik Sobania, Federica Sarro, Jie M. Zhang
**Submitted:** 10 Apr 2026 (v1), revised 17 May 2026 (v2)
**Signal:** 9/10

## Abstract

Agent skills are increasingly used to configure coding agents for software engineering (SE) tasks, yet current practice treats them as static, hand-crafted assets, or evolved on pass rate alone. This is insufficient: a skill can improve task success while substantially raising token cost, or introducing misleading guidance.

### Core Contribution
SkillMOO treats SE agent skill bundles as **multi-objective search objects**:
- Evolves skill bundles through LLM-proposed edits
- NSGA-II Pareto selection on **pass rate** and **inference cost**
- 38 skill edits analyzed — pruning and substitution dominate successful operations

### Key Results (SkillsBench, 16 SE tasks)
- Top pass rate rank on **11 of 12** non-zero-pass tasks
- Cost reductions up to **31.7%** over static bundles
- Pass rate gains up to **21 percentage points**
- Improvement up to **131%** pass rate while reducing cost up to **32%** vs best baseline per task

### Skill Edit Operations
- **Pruning** — removing unnecessary skill content
- **Substitution** — replacing one skill approach with another
- These two operations dominate successful edits, offering actionable principles for skill bundle design

## Relevance to Skill Bundles

SkillMOO is a major contribution to the **skill bundle optimization** literature:
1. First framework to treat skill bundles as multi-objective search objects (not just pass rate)
2. Cost-aware skill engineering — new class of search-based skill optimization
3. Pruning + substitution as dominant edit operations → directly applicable to bundle maintenance
4. Shows that deploying skills without cost-aware validation leaves better configurations unexplored

This connects to [[coevoskills-self-evolving-skills]] (co-evolutionary verification) and [[skillsbench-agent-skills-benchmark]] (shared benchmark).

## Key Quotes

> "SE agent skill bundles can be treated as multi-objective search objects"

> "Pruning and substitution dominate successful operations, offering actionable principles for skill bundle design"

> "The current practice of deploying skills without cost-aware validation leaves better skill configurations unexplored, motivating a new class of cost-aware, search-based skill engineering."

## Links
- PDF: https://arxiv.org/pdf/2604.09297
- HTML: https://arxiv.org/html/2604.09297v2
- Semantic Scholar: https://api.semanticscholar.org/arXiv:2604.09297
