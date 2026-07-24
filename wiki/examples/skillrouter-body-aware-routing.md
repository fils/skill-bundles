---
type: Skill Bundle Example
title: "SkillRouter: Body-Aware Retrieve-and-Rerank at ~80K Scale"
description: "Compact 1.2B retrieve-and-rerank pipeline proving progressive-disclosure metadata hides critical body-resident routing signal (37\u201344pp drop when body hidden); 74.0% Hit@1 on ~80K SkillsBench-derived pool."
resource: https://arxiv.org/abs/2603.22455
timestamp: '2026-07-24T12:00:00Z'
date: 2026-07-24
sources:
- https://arxiv.org/abs/2603.22455
- https://github.com/zhengyanzhao1997/SkillRouter
skills_included:
- "Large-pool skill routing"
- "Body-aware bi-encoder retrieval"
- "Cross-encoder listwise rerank"
- "False-negative filtering for near-duplicates"
context_elements:
- "Hidden-body progressive disclosure asymmetry"
- "~80K skill routing benchmark (Easy/Hard tiers)"
- "Body-resident routing signal (attention 91.7% on body)"
- "Retrieve-and-rerank 1.2B pipeline"
- "False-negative filtering + listwise loss"
- "End-to-end coding-agent transfer study"
composition: "Query \u2192 dense retrieve (body-aware encoder) \u2192 shortlist \u2192 listwise reranker on full body \u2192 top-K shortlist for agent (agent still sees metadata first)."
reproducibility: "GitHub zhengyanzhao1997/SkillRouter (~220\u2605); Hit@1 74.0% (1.2B) / 76.0% (16B); 13\u00d7 fewer params, 5.8\u00d7 faster than strongest 16B base; v5 Jul 2026."
rating: 9
---

# SkillRouter: Body-Aware Retrieve-and-Rerank at ~80K Scale

**Origin:** Zheng et al., Alibaba Group, arXiv:2603.22455 (v5 20 Jul 2026)
**Code:** https://github.com/zhengyanzhao1997/SkillRouter (~220★)

## Overview

As skill registries reach tens of thousands of overlapping entries, agents need **skill routing** before planning. Deployed stacks often use **progressive disclosure** (expose name+description; hide body). SkillRouter shows this hides the **decisive routing signal**: on a SkillsBench-derived ~80K pool, hiding the body drops routing accuracy **37–44pp**.

## Key Empirical Finding

| Control | Result |
|---------|--------|
| Hide body (name+desc only) | −37 to −44pp across dense/rerank baselines |
| Body-distilled descriptions | recover some gap but still −7 to −21pp vs all-field |
| Metadata-only encoder (same data) | −14.0pp vs all-field counterpart |
| Cross-encoder attention | **91.7%** concentrates on body field |

## Architecture (SkillRouter)

- Compact **1.2B** pipeline: 0.6B body-aware encoder + 0.6B reranker
- Training adaptations for homogeneous pools: **false-negative filtering** (near-duplicates) + **listwise reranking loss**
- Optional scaled 8B+8B = 16B config

## Results

| Metric | Value |
|--------|-------|
| Hit@1 (1.2B primary) | **74.0%** (strongest avg among evaluated baselines) |
| R@10 | 70.4% |
| vs strongest 16B base | comparable/higher accuracy, **13×** fewer params, **5.8×** faster |
| Scaled 16B SkillRouter | 76.0% Hit@1 |
| Transfer | end-to-end gains on four coding agents; larger for stronger agents |
| Supp benchmark | generalizes to 256-query multi-source set |

## Relation to Catalog

- Complements [r3 skill compatibility routing](r3-skill-compatibility-routing.md) (compatibility/set-aware) with **body-field necessity** at 80K scale
- Explains part of negative skill deltas in [skillsbench](skillsbench-agent-skills-benchmark.md) / [swe skills bench](swe-skills-bench-utility-benchmark.md): wrong shortlist before composition
- Feeds [agentskillos](agentskillos-capability-tree-dag.md) / [skill-os](skill-os-skills-as-apps.md) scale narratives

## Key Insight

**Progressive disclosure is an agent UX, not a routing feature.** Routers must read full skill bodies; agents can still receive short metadata after routing.

# Citations

- https://arxiv.org/abs/2603.22455
- https://github.com/zhengyanzhao1997/SkillRouter
