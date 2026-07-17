---
type: Skill Bundle Example
title: 'R3-Skill: Query-Conditional Skill Routing with Compatibility'
description: 'R3-Skill formalizes that **skill retrieval is not document retrieval**: top-K success depends on whether retrieved skills **work together under a query** (skill compatibility), not independent relevance alone.'
resource: https://arxiv.org/abs/2606.03565
timestamp: '2026-07-16T00:00:00Z'
date: 2026-07-16
sources:
- arXiv:2606.03565
- https://github.com/Tencent/R3-Skill
skills_included:
- 10,246 skill corpus routing
- R3-Embedding recall
- R3-Reranker graded ranking
context_elements:
- Skill compatibility (query-conditioned)
- Reject-as-Resource supervision
- 8-class rejection-reason taxonomy
- Bilingual skill-routing benchmark
- Two-stage embedding+rerank pipeline
composition: R3-Skill benchmark trains R3-Embedding + R3-Reranker using LLM rejection decisions as compatibility labels for set-aware top-K routing.
reproducibility: GitHub Tencent/R3-Skill; HF models R3-embedding-0.6b + R3-rerank-0.6b; Hit@1=0.7521, NDCG@10=0.8173, Set-Compat=0.3188.
rating: 9
---

# R3-Skill: Query-Conditional Skill Routing with Compatibility

**Origin:** Tencent IMA Product Center + Youtu Lab (Wang, Wen et al.), arXiv:2606.03565 (v4 Jul 2026)
**Code/Data:** https://github.com/Tencent/R3-Skill
**Models:** https://huggingface.co/tencent/R3-embedding-0.6b , R3-rerank-0.6b

## Overview

R3-Skill formalizes that **skill retrieval is not document retrieval**: top-K success depends on whether retrieved skills **work together under a query** (skill compatibility), not independent relevance alone. **Reject-as-Resource (R3)** reuses LLM rejection decisions — normally discarded — as compatibility supervision.

## Benchmark (R3-Skill)

| Asset | Scale |
|-------|-------|
| Skills | 10,246 (8 super-domains) |
| Accepted queries | 41,592 |
| Rejected annotations | 32,828 |
| Languages | Bilingual CN/EN, 4 directions |
| Rejection taxonomy | 8 classes |
| Test ground truth | Multi-expert verified |

Token reality: mean skill body ~2,073 tokens; full library ≈ **21.2M** tokens — all-prompt is impossible.

## Architecture

1. **R3-Embedding** — bi-encoder recall stage
2. **R3-Reranker** — cross-encoder with graded compatibility supervision
3. Gradient analysis: compatibility signal is diluted in bi-encoder bilateral balancing; **cross-encoder** can use it as ranking supervision without loss

## Key Metrics

- Hit@1 = **0.7521**
- NDCG@10 = **0.8173**
- Set-Compat = **0.3188**

## Context Elements

- **Skill compatibility** — joint set quality under query as first-class retrieval objective
- **Reject-as-Resource** — negative composition labels from LLM synthesis pipelines
- **Body-sensitive routing** — descriptions alone fail; body carries 31–44pp of routing signal (cited SkillRouter)
- **Sandbox provisioning** — K-skill install only for cold-start latency

## Relation to Skill Bundle Patterns

- Explains negative deltas in [skillsbench agent skills benchmark](skillsbench-agent-skills-benchmark.md) and zero-gain skills in [swe skills bench utility benchmark](swe-skills-bench-utility-benchmark.md): wrong co-retrieval hurts
- Complements [graph of skills dependency retrieval](graph-of-skills-dependency-retrieval.md) (GoS dependency-aware retrieval)
- Complements [skillcraft benchmark](skillcraft-benchmark.md) (composition/reuse)
- Complements [skillreducer token efficiency](skillreducer-token-efficiency.md) (less-is-more compression)
- Production counterpart to [skill os skills as apps](skill-os-skills-as-apps.md) management demands (caching, env construction)

## Key Insight

A skill bundle is not a bag of independently relevant packages. **Compatibility under the query** is a formal context element: retrieval systems must train on co-suitability (including rejections), not just relevance.

