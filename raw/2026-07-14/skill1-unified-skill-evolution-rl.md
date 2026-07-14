# Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning

**Source:** arXiv:2605.06130 (https://arxiv.org/abs/2605.06130)
**Date:** Submitted 7 May 2026 (v3: 12 May 2026)
**Authors:** Yaorui Shi, Yuxin Chen, Zhengxi Lu, Yuchun Miao, Shugui Liu, Qi GU, Xunliang Cai, Xiang Wang, An Zhang
**Citations:** 18
**Code:** https://github.com/AlphaLab-USTC/Skill1
**Signal Rating:** 8/10

## Summary

Skill1 is a framework that trains a single policy to co-evolve skill selection, utilization, and distillation toward a shared task-outcome objective. It addresses the problem that existing methods optimize these three capabilities in isolation or with separate reward sources, resulting in partial and conflicting evolution.

## Three Coupled Capabilities

1. **Skill selection** — the agent generates a query to search the skill library and re-ranks candidates to select one
2. **Skill utilization** — the agent solves the task conditioned on the selected skill
3. **Skill distillation** — the agent distills a new skill from the trajectory

## Key Innovation

All learning derives from a single task-outcome signal. The policy's low-frequency trend credits selection (long-term skill quality), while high-frequency variation credits distillation (per-task skill creation). This frequency decomposition avoids the conflicting reward problem of separate optimization.

## Results

- ALFWorld and WebShop benchmarks
- Outperforms prior skill-based and RL baselines
- Training dynamics confirm co-evolution of all three capabilities
- Ablations show removing any credit signal degrades evolution

## Skill Bundle Context

- Skill library = persistent memory of reusable strategies
- Skill selection = routing/retrieval mechanism
- Skill utilization = execution/runtime
- Skill distillation = skill creation/lifecycle (experience → new skill)
- Single task-outcome signal = unified governance for skill lifecycle
- Frequency decomposition = novel credit assignment for skill management

## Relevance to Skill Bundles

Skill1 unifies the three core skill lifecycle operations (select → use → create) under a single learning signal. This is the RL-based counterpart to Memento-Skills' Read-Write Reflective Learning and ASPIRE's evolutionary search. The frequency decomposition insight (low-freq = selection quality, high-freq = distillation) is a novel credit assignment pattern for skill bundle management.
