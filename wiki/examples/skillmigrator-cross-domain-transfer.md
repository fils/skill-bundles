---
type: Skill Bundle Example
title: 'SkillMigrator: Cross-Domain Web Skill Transfer via Transferable Interaction Patterns'
description: Web agents that use LLM skills typically can only reuse them within the same website/domain.
resource: https://arxiv.org/abs/2606.17645
timestamp: '2026-07-13T00:00:00Z'
date: 2026-07-13
sources:
- arXiv:2606.17645
skills_included:
- Skill retrieval layer
- Slot binding (Hungarian algorithm)
- Gate mechanism (threshold fallback)
context_elements:
- Transferable Interaction Pattern (TIP) 4-tuple
- Accessibility-tree skeleton (layout structure)
- Tree Edit Distance (APTED) matching
- Slot schema with synonym pools (co-clustered)
- Sentence-BERT text similarity
- Variable-arity form handling
composition: 'TIP stores skills as 4-tuples ⟨intent, template, slots, layout-skeleton⟩ without element references. At inference: text+layout score → gate → slot binding (Hungarian) → execute fixed plan.'
reproducibility: Evaluated on Mind2Web and WebArena. 8-10% LLM call reduction vs SOTA. Cross-domain reuse rate 35.4%.
rating: 8
---

# SkillMigrator: Beyond Domains — Reusing Web Skills via Transferable Interaction Patterns

**Origin:** Shiqi He, Yue Cui et al. (arXiv:2606.17645, June 2026)

## Overview

Web agents that use LLM skills typically can only reuse them within the same website/domain. SkillMigrator enables **cross-domain skill reuse** by matching structural layout patterns instead of specific element references. The core abstraction is the **Transferable Interaction Pattern (TIP)**.

## Transferable Interaction Pattern (TIP)

Each skill is stored as a 4-tuple: **k = ⟨ι_k, σ_k, Φ_k, τ_k⟩**

| Component | Description |
|-----------|-------------|
| ι_k | Natural-language intent |
| σ_k | Operation template (e.g., fill-and-submit) |
| Φ_k | Slot schema: {ξ_1, ..., ξ_m} each with key, descriptor d_ξ, synonym set T_ξ |
| τ_k | Cleaned accessibility-tree skeleton of page at skill induction time |

**Key design choice:** TIPs do NOT store element references (e.g., `ref=eN`) — these are dynamic to live pages. Instead, they store **structural layout skeletons** that persist across redesigns and domains.

## Inference Pipeline

1. **Skill Retrieval:** Score = α · text_sim (Sentence-BERT) + (1-α) · layout_sim (1 - TED/max_size)
2. **Gate:** Enter skill mode only if top-1 score > β; else fall back to ReAct
3. **Slot Binding (Stage A):** Parse slot values from instruction → Hungarian algorithm for one-to-one assignment
4. **Slot Binding (Stage B):** Bind slots to live page controls (role+name descriptors) → Hungarian matching
5. **Execute:** Fixed plan with bound values; live page determines action count (variable-arity)

## Key Results

| Metric | SkillMigrator | Baselines |
|--------|---------------|-----------|
| LLM call reduction (WebArena) | 8.5% vs PolySkill | 16.9% vs ReAct |
| Cross-domain reuse rate (Mind2Web) | 35.4% | 31% (PolySkill) |
| LLM call reduction (avg) | 8-10% | vs PolySkill, ASI, SkillWeaver |

Ablation confirms layout signal + slot-synonym pools are critical for cross-domain transfer.

## Context Elements

- **TIP (Transferable Interaction Pattern)** — 4-tuple skill representation
- **Accessibility-tree skeleton** — structural layout for cross-domain matching
- **Tree Edit Distance (APTED)** — layout similarity metric
- **Slot schema with synonym pools** — co-clustered training trajectories
- **Gate mechanism** — threshold-based ReAct fallback
- **Hungarian algorithm** — optimal one-to-one slot assignment

## Relation to Skill Bundle Patterns

SkillMigrator represents **cross-domain skill transfer** in web automation:
- Complements [skillcraft benchmark](skillcraft-benchmark.md) (composition) — Migrator transfers, Craft composes
- Relates to [skillreducer token efficiency](skillreducer-token-efficiency.md) — both reduce LLM calls (Migrator by reuse, Reducer by content reduction)
- Extends progressive disclosure pattern — skills loaded on-demand via structural matching

## Key Insight

Cross-domain skill reuse requires **structural layout matching** (accessibility-tree skeletons), not element references. The TIP abstraction (intent + template + slots + layout skeleton) is portable across domains because layout structure is more stable than DOM element IDs. This enables skills learned on one website to be reused on completely different websites.

