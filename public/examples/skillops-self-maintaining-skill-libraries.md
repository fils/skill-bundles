---
type: Skill Bundle Example
title: "SkillOps: Self-Maintaining Skill Libraries (Skill Technical Debt)"
description: "Method-agnostic plug-in that maintains skill libraries via typed Skill Contracts (P,O,A,V,F), Hierarchical Skill Ecosystem Graph, and utility/compatibility/risk/validation health diagnostics."
resource: https://arxiv.org/abs/2605.13716
timestamp: '2026-07-24T12:00:00Z'
date: 2026-07-24
sources:
- https://arxiv.org/abs/2605.13716
- https://github.com/Hik289/SkillOps
skills_included:
- "Typed Skill Contract packaging"
- "Hierarchical Skill Ecosystem Graph maintenance"
- "Rule-based merge/repair/retire actions"
- "Optional CGPD risk propagation"
context_elements:
- "Skill Contract (P,O,A,V,F)"
- "Skill technical debt formalization"
- "Hierarchical Skill Ecosystem Graph (HSEG)"
- "Library health dimensions (utility, compatibility, risk, validation)"
- "Maintenance actions (merge, repair, retire, add_validator, add_adapter)"
- "ContractGraph-Propagated Diagnosis (CGPD)"
composition: "raw_lib \u2192 contract extraction \u2192 HSEG \u2192 health diagnosis \u2192 typed maintenance \u2192 cleaned_lib usable by any retrieval/planning agent without internal code changes."
reproducibility: "Code Hik289/SkillOps; ALFWorld 79.5% standalone (+8.8pp); plug-in +0.68\u20132.90pp; nearly zero library-time LLM calls."
rating: 9
---

# SkillOps: Self-Maintaining Skill Libraries

**Origin:** Pu, Song, Zhao (UIUC / Emory), arXiv:2605.13716, May 2026 (NeurIPS 2026 submission)
**Code:** https://github.com/Hik289/SkillOps (~58★)

## Overview

SkillOps targets **library-time** defects — *skill technical debt* — that do not break a single skill locally but degrade future retrieval, composition, and execution (redundancy, missing validators, interface drift, stale implementations). Prior work focuses on task-time retrieval/planning/repair; SkillOps is a **method-agnostic plug-in** that transforms a raw library into a maintained library.

## Architecture

1. **Skill Contract** — each skill `s = (P, O, A, V, F)`: preconditions, operation, artifacts, validators, known failure modes. Empty `V` = validation gap.
2. **HSEG** — Hierarchical Skill Ecosystem Graph with typed edges: dependency, compatibility, redundancy, alternative.
3. **Health diagnosis** — utility, redundancy, compatibility, failure-risk, validation-gap.
4. **Maintenance actions** — merge, repair, retire, add_validator, add_adapter.
5. **CGPD (optional)** — propagates local risk along dependency edges to trigger preventive validators.

Central interface: `cleaned_lib = run_maintenance(raw_lib)`.

## Key Results

| Setting | Result |
|---------|--------|
| Standalone agent (ALFWorld) | 79.5% success (+8.8pp vs strongest baseline) |
| Plug-in on retrieval baselines | +0.68 to +2.90pp |
| Library-time LLM cost | ~0 calls/tokens (rule-based) |
| CGPD @ lib=1000/2000 | +0.5 / +0.6pp over basic SkillOps |

## Context Elements

- Formalizes **skill technical debt** as persistent library-level defects
- Contracts make composability and local verifiability first-class
- Maintenance is an **architectural layer**, not an extra inference tax
- Complements supply-chain inventory ([ASSCs / SkillBOM](assc-skill-supply-chains-skillbom.md)) and registry→repository maintenance science

## Relation to Catalog

- Library-time counterpart to [registry to repository skill maintenance](registry-to-repository-skill-maintenance.md) and [assc skill supply chains skillbom](assc-skill-supply-chains-skillbom.md)
- Validators/adapters align with [three-layer validation stack](../concepts/three-layer-validation-stack.md)
- Orthogonal to task-time routing ([r3 skill compatibility routing](r3-skill-compatibility-routing.md), [skillrouter body aware routing](skillrouter-body-aware-routing.md))

## Key Insight

Skill bundles accumulate **software debt**. Treating the library as a maintained software ecosystem — with contracts, graphs, and typed repairs — is as important as writing better individual skills.

# Citations

- https://arxiv.org/abs/2605.13716
- https://github.com/Hik289/SkillOps
