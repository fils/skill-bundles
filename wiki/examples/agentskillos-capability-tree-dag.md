---
type: Skill Bundle Example
title: "AgentSkillOS: Capability-Tree Organization + DAG Orchestration"
description: "First principled framework for ecosystem-scale skill management: recursive capability-tree organization plus DAG-based multi-skill orchestration; evaluates 200\u2192200K skill pools on 30 artifact-rich tasks."
resource: https://arxiv.org/abs/2603.02176
timestamp: '2026-07-24T12:00:00Z'
date: 2026-07-24
sources:
- https://arxiv.org/abs/2603.02176
- https://github.com/ynulihao/AgentSkillOS
skills_included:
- "Capability-tree skill organization"
- "Task-driven tree retrieval + prune"
- "DAG multi-skill orchestration"
- "Multi-skill execution with dataflow"
context_elements:
- "Capability tree (node-level recursive categorization)"
- "DAG-based skill orchestration (3 strategies)"
- "Ecosystem scales 200 / 1K / 200K"
- "30 artifact-rich tasks + Bradley\u2013Terry pairwise eval"
- "Structured composition > flat invocation"
composition: "Offline: build capability tree from ecosystem. Online: tree retrieval \u2192 filter/dedupe/rank \u2192 DAG plan \u2192 execute with dependency/dataflow management."
reproducibility: "GitHub ynulihao/AgentSkillOS (~558\u2605); 30 tasks \u00d7 5 categories; LLM pairwise + Bradley\u2013Terry; DAG orchestration beats flat oracle skill set."
rating: 9
---

# AgentSkillOS: Capability-Tree Organization + DAG Orchestration

**Origin:** Li, Mu, Chen et al., Shanghai AI Lab, arXiv:2603.02176, Mar 2026
**Code:** https://github.com/ynulihao/AgentSkillOS (~558★)

## Overview

With **280K+** public skills (skillsmp.com, late Feb 2026) and decentralized third-party authorship, AgentSkillOS asks how to **leverage, manage, and scale** the ecosystem. It is positioned as the first principled framework combining **capability-tree organization** with **DAG multi-skill orchestration**.

## Two Stages

### 1. Manage Skills (offline)
- Build a **capability tree** via node-level recursive categorization
- Split nodes exceeding per-node capacity until balanced
- Surfaces non-obvious but functionally relevant skills beyond pure semantic retrieval

### 2. Solve Tasks (online)
1. **Task-driven retrieval** — explore tree, then filter/dedupe/rank
2. **DAG orchestration** — decompose task; compose skills into DAGs (three strategies)
3. **Multi-skill execution** — manage order, dependencies, data flow

## Benchmark

| Property | Detail |
|----------|--------|
| Tasks | 30 expert-authored, artifact-rich |
| Categories | data computation, document creation, motion video, visual design, web interaction |
| Evaluation | LLM pairwise (both orderings) → Bradley–Terry unified scores |
| Scales | 200, 1K, **200K** skills |

## Findings

- Tree retrieval approximates **oracle** skill selection at scale
- **DAG orchestration substantially outperforms native flat invocation even with the identical oracle skill set**
- Structured composition — not mere skill availability — unlocks ecosystem value

## Relation to Catalog

- Orchestration layer above [skillrouter](skillrouter-body-aware-routing.md) / [r3-skill](r3-skill-compatibility-routing.md) routing
- Complements [skill-os skills as apps](skill-os-skills-as-apps.md) (OS abstraction) with concrete tree+DAG system
- Aligns with [openclaw skill csts tree search](openclaw-skill-csts-tree-search.md) collective tree construction (different phase: runtime org vs multi-model build)

## Key Insight

**Skills without orchestration are inventory.** Capability trees + DAG pipelines turn fragmented marketplaces into composable systems.

# Citations

- https://arxiv.org/abs/2603.02176
- https://github.com/ynulihao/AgentSkillOS
