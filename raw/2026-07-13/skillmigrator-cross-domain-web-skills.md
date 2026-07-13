# SkillMigrator: Beyond Domains — Reusing Web Skills via Transferable Interaction Patterns

**Source:** arXiv:2606.17645 (June 2026)
**Authors:** Shiqi He, Yue Cui, et al. (6 authors)
**Signal Rating:** 8/10

## TL;DR

Cut LLM automation costs and latency by enabling cross-domain skill reuse through structural layout matching instead of unreliable element references.

## Problem

Traditional LLM web agents operate as low-level tool callers, leading to long interaction horizons, high latency, and significant costs. While "web skills" abstract repeated interaction fragments, their reuse is often limited to the same website/domain, relying on instruction similarity or coarse site metadata. This results in low skill reuse on novel sites and domains.

## Transferable Interaction Pattern (TIP)

The core innovation: each skill is stored as a tuple k = ⟨ι_k, σ_k, Φ_k, τ_k⟩ where:

- **ι_k:** Natural-language intent for the skill
- **σ_k:** Operation template (e.g., fill-and-submit)
- **Φ_k = {ξ_1, ..., ξ_m}:** Slot schema (each slot ξ has key, one-line descriptor d_ξ, synonym set T_ξ mined from co-clustered training trajectories)
- **τ_k:** Cleaned accessibility-tree skeleton of the webpage snapshot at time of skill induction

**Key insight:** TIPs do NOT store specific element references (e.g., `ref=eN`) which are dynamic to live pages. Instead, they store structural layout skeletons that persist across page redesigns and different domains.

## Inference Pipeline

1. **Snapshot Processing & Skill Retrieval:** Generate page summary, extract interactive nodes, score each skill using combined text + layout signal:
   - Text: sentence encoder (Sentence-BERT) similarity between subtask and skill descriptor
   - Layout: 1 - TED(τ_k, τ_live) / max(|τ_k|, |τ_live|) where TED = Tree Edit Distance (APTED)
   - Combined: score = α · text_sim + (1-α) · layout_sim

2. **Gate Mechanism:** Enter "skill mode" only if top-1 skill score exceeds threshold β; otherwise fall back to ReAct-style primitive actions

3. **Slot Binding & Execution:**
   - Stage A: Parse slot values from instruction (Hungarian algorithm for one-to-one assignment)
   - Stage B: Bind slots to live page controls (role+name descriptors, Hungarian matching)
   - Execute fixed plan using bound values (variable-arity forms handled)

## Key Results

- Mind2Web and WebArena benchmarks
- 8-10% reduction in average LLM-action count on successful trajectories vs SOTA baselines (PolySkill, ASI, SkillWeaver)
- 8.5% reduction on WebArena vs PolySkill; 16.9% vs ReAct
- Cross-domain skill reuse rate: 35.4% vs PolySkill's 31% on Mind2Web
- Ablation: layout signal + slot-synonym pools critical for cross-domain transfer
- Performance gains independent of underlying LLM backbone

## Context Elements

- **Transferable Interaction Pattern (TIP):** 4-tuple skill representation
- **Layout structure matching:** Tree Edit Distance on accessibility-tree skeletons
- **Slot schema with synonyms:** Co-clustered training trajectories for synonym mining
- **Gate mechanism:** Threshold-based fallback to ReAct
- **Hungarian algorithm:** Optimal one-to-one slot assignment
- **Variable-arity handling:** Live page determines action count, not original trajectory

## Key Insights

- Cross-domain skill reuse requires structural layout matching, not element references
- Accessibility-tree skeleton (τ_k) is the key abstraction for cross-domain transfer
- Slot synonym pools from co-clustered trajectories improve matching
- Can complement existing skill libraries as initial retrieval layer
