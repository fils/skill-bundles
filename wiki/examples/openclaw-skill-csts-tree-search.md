---
title: "OpenClaw-Skill: Collective Skill Tree Search (CSTS)"
date: 2026-07-16
sources: ["arXiv:2606.16774"]
skills_included: ["Tree-of-skills construction", "CSN-Gen multi-model candidates", "CSN-Assess quality+transfer scoring", "Collective Skill RL multi-skill selection"]
context_elements: ["Collective Skill Tree Search", "Collective quality scoring", "Collective transferability scoring", "Skill tree hierarchy (anti-fragmentation)", "Multi-model judge ensemble"]
composition: "CSTS iterates CSN-Gen (multi-model skill candidates) → CSN-Assess (quality + cross-model transfer scores) → tree of skills + skill-augmented training → Collective Skill RL."
reproducibility: "Paper arXiv:2606.16774 (Jun 2026); OpenClaw-Skill model trained with CSTS trees; benchmarks for long-horizon tool use."
rating: 8
---

# OpenClaw-Skill: Collective Skill Tree Search (CSTS)

**Origin:** PolyU / NTU / Tsinghua / RMIT / BUAA (Lin et al.), arXiv:2606.16774, Jun 2026

## Overview

OpenClaw-Skill proposes **Collective Skill Tree Search (CSTS)** to automatically construct structured, diverse, and **cross-model transferable** skill trees for OpenClaw-like agents — addressing handcrafted skill cost and three failure modes of prior auto-construction: fragmentation, single-model bias, and poor transferability.

## Architecture

### CSN-Gen (Collective Skill Node Generation)
- Multiple heterogeneous models propose candidate skills per subtask
- Expands coverage beyond one backbone's problem-solving bias

### CSN-Assess (Collective Skill Node Assessment)
1. **Collective quality scoring** — Independent multi-judge aggregation → robust effectiveness estimate
2. **Collective transferability scoring** — Skill from model A must help models B/C → select generalizable nodes

### Collective Skill RL
- At training/inference, **actively selects multiple** tree skills to broaden solution-space exploration
- Avoids single-skill trap → homogeneous/suboptimal trajectories

## Problems Solved

| Failure mode | CSTS fix |
|--------------|----------|
| Skill fragmentation | Tree paths = multi-step orchestration |
| Limited diversity | Multi-model candidate generation |
| Poor transferability | Explicit cross-model transfer scoring |

## Context Elements

- **Tree-of-skills** as first-class composition structure (nodes + dependency paths)
- **Transferability as a gate** — not just quality — before skill inclusion
- **Collective intelligence** for construction (multi-model gen + multi-model judge)
- **Multi-skill RL selection** — composition at policy time, not only package time

## Relation to Skill Bundle Patterns

- Distinct from [[skillclaw-collective-skill-evolution]] (runtime multi-user trajectory aggregation) — CSTS is **construction-time** collective search
- Complements [[coevoskills-self-evolving-skills]] (generator+verifier co-evolution)
- Complements [[evoskill-automated-skill-discovery]] (failure-driven Pareto discovery)
- Transfer gates relate to [[skillmigrator-cross-domain-transfer]] and [[skillsbench-agent-skills-benchmark]] transfer findings
- Tree structure extends [[graph-of-skills-dependency-retrieval]] / [[skillcraft-benchmark]] composition themes

## Key Insight

Automatic skill construction needs **collective generation + collective transfer gates**, not single-model trajectory distillation. Packaging skills as trees (not flat lists) is the structural antidote to fragmentation for long-horizon OpenClaw-class work.

[[backlinks]]
