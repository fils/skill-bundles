#!/usr/bin/env python3
"""Iteration 42 (2026-07-24) batch: raw notes + wiki examples + indexes + digest + qa + metrics + log + metadata."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path("/home/hermes/projects/skill-bundles")
RAW = ROOT / "raw" / "2026-07-24"
WIKI = ROOT / "wiki"
EX = WIKI / "examples"
DATE = "2026-07-24"
TS = "2026-07-24T12:00:00Z"
ITER = 42

RAW.mkdir(parents=True, exist_ok=True)

sources = [
    {
        "slug": "skillops-library-maintenance",
        "file": "skillops-self-maintaining-skill-libraries.md",
        "title": "SkillOps: Self-Maintaining Skill Libraries (Skill Technical Debt)",
        "desc": "Method-agnostic plug-in that maintains skill libraries via typed Skill Contracts (P,O,A,V,F), Hierarchical Skill Ecosystem Graph, and utility/compatibility/risk/validation health diagnostics.",
        "resource": "https://arxiv.org/abs/2605.13716",
        "github": "https://github.com/Hik289/SkillOps",
        "rating": 9,
        "skills": [
            "Typed Skill Contract packaging",
            "Hierarchical Skill Ecosystem Graph maintenance",
            "Rule-based merge/repair/retire actions",
            "Optional CGPD risk propagation",
        ],
        "context": [
            "Skill Contract (P,O,A,V,F)",
            "Skill technical debt formalization",
            "Hierarchical Skill Ecosystem Graph (HSEG)",
            "Library health dimensions (utility, compatibility, risk, validation)",
            "Maintenance actions (merge, repair, retire, add_validator, add_adapter)",
            "ContractGraph-Propagated Diagnosis (CGPD)",
        ],
        "composition": "raw_lib → contract extraction → HSEG → health diagnosis → typed maintenance → cleaned_lib usable by any retrieval/planning agent without internal code changes.",
        "reproducibility": "Code Hik289/SkillOps; ALFWorld 79.5% standalone (+8.8pp); plug-in +0.68–2.90pp; nearly zero library-time LLM calls.",
        "body": """# SkillOps: Self-Maintaining Skill Libraries

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
""",
        "raw_note": """# SkillOps (arXiv:2605.13716) — raw notes
**Signal:** 9/10 — first plug-in library-maintenance framework; skill technical debt; contracts + HSEG
**Source:** https://arxiv.org/abs/2605.13716 | HTML | GitHub Hik289/SkillOps
**Key quotes/ideas:**
- Skill technical debt: library-level defects harming future retrieval/composition
- Contract (P,O,A,V,F); HSEG edges dep/comp/red/alt
- cleaned_lib = run_maintenance(raw_lib)
- ALFWorld 79.5% standalone +8.8pp; plug-in +0.68–2.90pp; ~0 library-time LLM
- CGPD risk propagation for preventive validators
""",
    },
    {
        "slug": "skillrouter-body-aware-routing",
        "file": "skillrouter-body-aware-routing.md",
        "title": "SkillRouter: Body-Aware Retrieve-and-Rerank at ~80K Scale",
        "desc": "Compact 1.2B retrieve-and-rerank pipeline proving progressive-disclosure metadata hides critical body-resident routing signal (37–44pp drop when body hidden); 74.0% Hit@1 on ~80K SkillsBench-derived pool.",
        "resource": "https://arxiv.org/abs/2603.22455",
        "github": "https://github.com/zhengyanzhao1997/SkillRouter",
        "rating": 9,
        "skills": [
            "Large-pool skill routing",
            "Body-aware bi-encoder retrieval",
            "Cross-encoder listwise rerank",
            "False-negative filtering for near-duplicates",
        ],
        "context": [
            "Hidden-body progressive disclosure asymmetry",
            "~80K skill routing benchmark (Easy/Hard tiers)",
            "Body-resident routing signal (attention 91.7% on body)",
            "Retrieve-and-rerank 1.2B pipeline",
            "False-negative filtering + listwise loss",
            "End-to-end coding-agent transfer study",
        ],
        "composition": "Query → dense retrieve (body-aware encoder) → shortlist → listwise reranker on full body → top-K shortlist for agent (agent still sees metadata first).",
        "reproducibility": "GitHub zhengyanzhao1997/SkillRouter (~220★); Hit@1 74.0% (1.2B) / 76.0% (16B); 13× fewer params, 5.8× faster than strongest 16B base; v5 Jul 2026.",
        "body": """# SkillRouter: Body-Aware Retrieve-and-Rerank at ~80K Scale

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
""",
        "raw_note": """# SkillRouter (arXiv:2603.22455 v5) — raw notes
**Signal:** 9/10 — definitive body-signal finding at ~80K; practical 1.2B router
**Source:** https://arxiv.org/abs/2603.22455 | GitHub zhengyanzhao1997/SkillRouter (220★)
**Key ideas:**
- Progressive disclosure hides body → 37–44pp routing drop
- 91.7% attention on body; distilled desc insufficient
- 74.0% Hit@1 @ 1.2B; end-to-end coding agent transfer
- FN filtering + listwise loss for homogeneous pools
""",
    },
    {
        "slug": "agentskillos-capability-tree-dag",
        "file": "agentskillos-capability-tree-dag.md",
        "title": "AgentSkillOS: Capability-Tree Organization + DAG Orchestration",
        "desc": "First principled framework for ecosystem-scale skill management: recursive capability-tree organization plus DAG-based multi-skill orchestration; evaluates 200→200K skill pools on 30 artifact-rich tasks.",
        "resource": "https://arxiv.org/abs/2603.02176",
        "github": "https://github.com/ynulihao/AgentSkillOS",
        "rating": 9,
        "skills": [
            "Capability-tree skill organization",
            "Task-driven tree retrieval + prune",
            "DAG multi-skill orchestration",
            "Multi-skill execution with dataflow",
        ],
        "context": [
            "Capability tree (node-level recursive categorization)",
            "DAG-based skill orchestration (3 strategies)",
            "Ecosystem scales 200 / 1K / 200K",
            "30 artifact-rich tasks + Bradley–Terry pairwise eval",
            "Structured composition > flat invocation",
        ],
        "composition": "Offline: build capability tree from ecosystem. Online: tree retrieval → filter/dedupe/rank → DAG plan → execute with dependency/dataflow management.",
        "reproducibility": "GitHub ynulihao/AgentSkillOS (~558★); 30 tasks × 5 categories; LLM pairwise + Bradley–Terry; DAG orchestration beats flat oracle skill set.",
        "body": """# AgentSkillOS: Capability-Tree Organization + DAG Orchestration

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
""",
        "raw_note": """# AgentSkillOS (arXiv:2603.02176) — raw notes
**Signal:** 9/10 — tree org + DAG orchestration; 200K scale; DAG > flat even with oracle skills
**Source:** https://arxiv.org/abs/2603.02176 | GitHub ynulihao/AgentSkillOS (558★)
**Key ideas:**
- Manage Skills: recursive capability tree
- Solve Tasks: retrieve → DAG orchestrate → execute
- 30 artifact tasks; Bradley–Terry pairwise
- Composition is the unlock, not just selection
""",
    },
    {
        "slug": "skillc-contrastive-internalization",
        "file": "skillc-contrastive-internalization.md",
        "title": "SkillC: Contrastive Skill Credit Assignment for Internalization",
        "desc": "Skill-internalization RL that turns skill-helpfulness contrast into a dual-stream advantage learning signal (not only curriculum control), with adaptive curriculum over attribution strength and active-set pruning.",
        "resource": "https://arxiv.org/abs/2605.27899",
        "github": "",
        "rating": 8,
        "skills": [
            "Paired skill-injected vs skill-free rollouts",
            "Contrastive Skill Credit Assignment (CSCA)",
            "Adaptive internalization curriculum",
        ],
        "context": [
            "Contrastive Skill Credit Assignment",
            "Dual-stream advantage estimator",
            "One-sided correction toward skill-free success",
            "Validation-level adaptive curriculum",
            "Monotonic active-set pruning",
        ],
        "composition": "For active skill types: sample paired skill+/skill− rollouts in same policy update; inject task-level contrast into dual-stream advantages; prune active set as internalization succeeds.",
        "reproducibility": "arXiv:2605.27899; ALFWorld +5.5% and WebShop +4.4% over strongest prior internalization RL without runtime skills; competitive with skill-augmented RL.",
        "body": """# SkillC: Contrastive Skill Credit Assignment for Internalization

**Origin:** Lin, Kuai, Xue, Wang, arXiv:2605.27899, May 2026

## Overview

Skill-augmented RL keeps skills at inference; internalization RL withdraws them during training. Prior internalization (e.g. SKILL0) uses skill-helpfulness mainly for **curriculum control**, leaving the policy update unable to distinguish skill-dependent vs autonomous success. **SkillC** converts the contrast into a **direct learning signal** via Contrastive Skill Credit Assignment (CSCA).

## Method

1. Sample **paired** skill-injected and skill-free rollouts for active skill types within the same update
2. **Dual-stream advantage estimator** preserves global ranking while applying one-sided correction toward skill-free success
3. Smoothed validation signal drives adaptive curriculum over attribution strength, rollout allocation, and **monotonic active-set pruning**

## Results

| Benchmark | Gain vs strongest prior internalization RL |
|-----------|-----------------------------------------------|
| ALFWorld | +5.5% |
| WebShop | +4.4% |
| Runtime skills | **none** (zero-shot autonomous) |
| vs skill-augmented RL | remains competitive |

## Relation to Catalog

- Advances [skill0 skill internalization](skill0-skill-internalization.md) credit assignment
- Related to [skill0.5 joint internalization utilization](skill05-joint-internalization-utilization.md) hybrid pole
- Contrasts with [slim dynamic skill lifecycle](slim-dynamic-skill-lifecycle.md) (non-empty external boundary)

## Key Insight

Internalization needs **credit for autonomy**, not only a schedule that removes skills. Contrastive paired rollouts make skill-free success an explicit optimization target.

# Citations

- https://arxiv.org/abs/2605.27899
""",
        "raw_note": """# SkillC (arXiv:2605.27899) — raw notes
**Signal:** 8/10 — contrastive credit for internalization beyond curriculum
**Key ideas:** CSCA dual-stream advantages; paired skill+/skill−; +5.5% ALFWorld / +4.4% WebShop vs prior internalization
""",
    },
    {
        "slug": "skill05-joint-internalization-utilization",
        "file": "skill05-joint-internalization-utilization.md",
        "title": "Skill0.5: Joint Internalization of General Skills + Utilization of Task Skills",
        "desc": "Agentic RL framework that refuses the full-external vs full-internal binary: internalizes general skills via privileged distillation while enforcing task-specific skill utilization via diagnostic probing on easy tasks.",
        "resource": "https://arxiv.org/abs/2605.28424",
        "github": "",
        "rating": 8,
        "skills": [
            "General skill internalization (privileged distillation)",
            "Task-specific skill utilization enforcement",
            "Difficulty-aware mastery-tier routing",
        ],
        "context": [
            "General vs task-specific skill taxonomy",
            "Dynamic difficulty-aware router",
            "Mastery tiers with tailored optimization",
            "Diagnostic probing against shortcuts",
            "OOD generalization objective",
        ],
        "composition": "Difficulty-aware router streams tasks into mastery tiers: hard → internalize general skills; easy → probe and penalize shortcuts to force specific skill use.",
        "reproducibility": "arXiv:2605.28424; ALFWorld + WebShop ID and OOD gains over memory-based and skill-based RL baselines.",
        "body": """# Skill0.5: Joint Internalization + Utilization

**Origin:** Zhu, Yu, Zhao et al., arXiv:2605.28424, May 2026

## Overview

Skills split naturally into **general** (broad cognitive transfer) and **task-specific** (dynamic execution). Full externalization costs context; full internalization risks overfitting and knowledge conflicts. **Skill0.5** jointly: (1) internalizes general skills, (2) forces utilization of task-specific skills.

## Method

- **Dynamic difficulty-aware router** assigns mastery tiers
- **Hard tasks:** privileged distillation internalizes general skills as cognitive foundation
- **Easy tasks:** diagnostic probing penalizes shortcuts and enforces specific skill utilization
- Goal: ID + **OOD** generalization without choosing a single extreme

## Relation to Catalog

- Middle path between [skill0](skill0-skill-internalization.md) (zero@infer) and pure external [skillopt](skillopt-trainable-skill-parameters.md)
- Complements [skillc](skillc-contrastive-internalization.md) credit machinery
- Related to [slim](slim-dynamic-skill-lifecycle.md) learned external boundary

## Key Insight

**Not all skills deserve the same fate.** General skills can sink into weights; task-specific skills should stay usable and enforced — a nuanced bundle lifecycle design rule.

# Citations

- https://arxiv.org/abs/2605.28424
""",
        "raw_note": """# Skill0.5 (arXiv:2605.28424) — raw notes
**Signal:** 8/10 — joint general-internalize + task-utilize; OOD focus
**Key ideas:** mastery tiers; privileged distillation; diagnostic probing vs shortcuts
""",
    },
    {
        "slug": "slim-dynamic-skill-lifecycle",
        "file": "slim-dynamic-skill-lifecycle.md",
        "title": "SLIM: Dynamic Skill Lifecycle Management (Retain–Retire–Expand)",
        "desc": "Treats the active external skill set as a dynamic optimization variable jointly trained with the policy via leave-one-skill-out marginal contribution; converges to a compact non-empty skill boundary rather than full accumulation or zero-skill inference.",
        "resource": "https://arxiv.org/abs/2605.10923",
        "github": "https://github.com/ejhshen/SLIM",
        "rating": 9,
        "skills": [
            "Leave-one-skill-out marginal contribution",
            "Retain high-value external skills",
            "Retire negligible skills after exposure",
            "Expand bank on persistent failure coverage gaps",
        ],
        "context": [
            "Dynamic active skill set as optimization variable",
            "Leave-one-skill-out (LOSO) validation",
            "Retain–retire–expand lifecycle ops",
            "Non-monotonic external capability trajectory",
            "Learned internal/external boundary",
        ],
        "composition": "During RL: retrieve from active pool → estimate LOSO marginal external contribution → retain/retire/expand → continue policy optimization with updated active set.",
        "reproducibility": "GitHub ejhshen/SLIM; +7.1pp avg over best baselines on ALFWorld + SearchQA vs GRPO/SkillRL/Skill0.",
        "body": """# SLIM: Dynamic Skill Lifecycle Management

**Origin:** Shen, Zhang, Zhao, Cheng (CUHK / Lanzhou), arXiv:2605.10923, May 2026
**Code:** https://github.com/ejhshen/SLIM

## Overview

Existing skill-based agentic RL assumes the external skill set either **monotonically accumulates** (SkillRL-style) or **anneals to zero** (SKILL0-style). SLIM argues the optimal active set is **non-monotonic**, task- and stage-dependent under limited parametric capacity and uneven skill value.

## Lifecycle Operations

| Op | Trigger |
|----|---------|
| **Retain** | High leave-one-skill-out (LOSO) marginal contribution |
| **Retire** | Contribution becomes negligible after sufficient exposure |
| **Expand** | Persistent failures reveal missing capability coverage |

Active external skill set is a **joint optimization variable** with the policy.

## Results

- **+7.1pp** average over best baselines across ALFWorld and SearchQA
- Converges to a **compact non-empty** active skill set (neither full bank nor zero)
- Some skills absorbed into policy; others keep external value → learned boundary

## Relation to Catalog

- Synthesizes poles of [skill0](skill0-skill-internalization.md), SkillRL-class augmentation, and [skillopt](skillopt-trainable-skill-parameters.md)
- Complements [skillops](skillops-self-maintaining-skill-libraries.md) (library hygiene) with **training-time** lifecycle
- Aligns with Externalization trade-off in [externalization llm agents](externalization-llm-agents-unified-review.md)

## Key Insight

The endpoint of skill-augmented RL is neither “all skills forever” nor “no skills at inference,” but a **learned external capability boundary**.

# Citations

- https://arxiv.org/abs/2605.10923
- https://github.com/ejhshen/SLIM
""",
        "raw_note": """# SLIM (arXiv:2605.10923) — raw notes
**Signal:** 9/10 — retain/retire/expand; LOSO marginal value; non-empty boundary; +7.1pp
**Code:** https://github.com/ejhshen/SLIM
""",
    },
    {
        "slug": "skillcorpus-open-ecosystem-curation",
        "file": "skillcorpus-open-ecosystem-curation.md",
        "title": "SkillCorpus: Curating ~821K Open Skills → 96K Deployable Corpus",
        "desc": "End-to-end framework that aggregates, curates (16-class taxonomy + utility/robustness/safety facets), retrieves, and evaluates the open SKILL.md ecosystem; +7.5pp on SkillsBench with coverage and harness boundary analysis.",
        "resource": "https://arxiv.org/abs/2607.15557",
        "github": "",
        "rating": 9,
        "skills": [
            "Multi-stage open-skill crawl and filter",
            "16-class taxonomy organization",
            "Fine-tuned retrieval-and-selection stack",
            "Multi-benchmark multi-harness evaluation",
        ],
        "context": [
            "Open ecosystem consolidation (~821K → 96,401)",
            "Three quality facets (utility, robustness, safety)",
            "16-class skill taxonomy",
            "Coverage boundary vs harness boundary",
            "SkillsBench / GDPVal / QwenClawBench multi-eval",
        ],
        "composition": "Crawl → multi-stage filter/curate → taxonomy + quality facets → retrieval/selection models → serve corpus into agent harnesses; measure gains and failure boundaries.",
        "reproducibility": "arXiv:2607.15557 v4 (23 Jul 2026); dataset/models/code promised on acceptance; +7.5pp SkillsBench; two harnesses × two open backbones + frontier robustness check.",
        "body": """# SkillCorpus: Curating the Open Skill Ecosystem

**Origin:** Wang, Yao, Sun et al., arXiv:2607.15557 (v4 23 Jul 2026) — **very recent**

## Overview

Public skill repos are **fragmented, redundant, and uneven**. SkillCorpus asks: how to consolidate the open SKILL.md ecosystem into one usable corpus, and **what bounds** its benefit on real agent tasks?

## Pipeline Scale

| Stage | Scale |
|-------|-------|
| Crawled skills | ~**821,000** |
| Curated corpus | **96,401** |
| Taxonomy | 16 classes |
| Quality facets | utility, robustness, **safety** |
| Matching | fine-tuned retrieval-and-selection stack |

## Evaluation

- Benchmarks: **SkillsBench**, GDPVal, QwenClawBench
- Two harnesses × two open backbones + frontier robustness check
- Consistent gains; largest on SkillsBench (**+7.5pp**)
- Operational analysis: gains limited by a **coverage boundary** and a **harness boundary**

## Relation to Catalog

- Corpus-scale counterpart to [assc skillbom](assc-skill-supply-chains-skillbom.md) inventory science and [inside skill market](inside-skill-market-se-activities.md)
- Quality facets connect to [skillspector](skillspector-nvidia-security-scanner.md) / safety governance
- Harness boundary echoes [wildclawbench](wildclawbench-native-runtime-evaluation.md) multi-harness findings
- Complements [agentskillos](agentskillos-capability-tree-dag.md) orchestration of large pools

## Key Insight

Community skill mass is not automatically useful. **Curation + retrieval + harness fit** determine whether hundreds of thousands of SKILL.md files move the needle — and where they stop helping.

# Citations

- https://arxiv.org/abs/2607.15557
""",
        "raw_note": """# SkillCorpus (arXiv:2607.15557 v4) — raw notes
**Signal:** 9/10 — 821K→96K curated corpus; +7.5pp SkillsBench; coverage/harness boundaries; Jul 2026 fresh
""",
    },
]

# --- Write raw + examples ---
example_links = []
for s in sources:
    (RAW / f"{s['slug']}.md").write_text(s["raw_note"].strip() + "\n", encoding="utf-8")
    fm = f"""---
type: Skill Bundle Example
title: {json.dumps(s['title'])}
description: {json.dumps(s['desc'])}
resource: {s['resource']}
timestamp: '{TS}'
date: {DATE}
sources:
- {s['resource']}
"""
    if s.get("github"):
        fm += f"- {s['github']}\n"
    fm += "skills_included:\n"
    for x in s["skills"]:
        fm += f"- {json.dumps(x)}\n"
    fm += "context_elements:\n"
    for x in s["context"]:
        fm += f"- {json.dumps(x)}\n"
    fm += f"""composition: {json.dumps(s['composition'])}
reproducibility: {json.dumps(s['reproducibility'])}
rating: {s['rating']}
---

"""
    (EX / s["file"]).write_text(fm + s["body"].strip() + "\n", encoding="utf-8")
    example_links.append((s["file"], s["title"], s["desc"]))

# Also raw triage summary
triage = f"""# Discovery triage — {DATE} (Iteration {ITER})

## Gap context
Last digest: 2026-07-16 (Iteration 41). Eight calendar days without research commits (site/Pages work only). Anti-stagnation: followed 07-16 priority searches (SkillOps, SkillRouter, AgentSkillOS, internalization follow-ons) + fresh Jul papers.

## Ingested (7) — signal 8–9
1. SkillOps (2605.13716) — library maintenance / skill technical debt
2. SkillRouter (2603.22455 v5 Jul 20) — body-aware routing @80K
3. AgentSkillOS (2603.02176) — capability tree + DAG @200K
4. SkillC (2605.27899) — contrastive internalization credit
5. Skill0.5 (2605.28424) — joint general-internalize + task-utilize
6. SLIM (2605.10923) — retain/retire/expand lifecycle
7. SkillCorpus (2607.15557 v4 Jul 23) — 821K→96K curated corpus

## Noted but not full examples
- OWASP AST10 already cataloged (2026-05-26); live stats refresh only
- mukul975/Anthropic-Cybersecurity-Skills (26k★, 6-framework map) — candidate next run
- skillflag (CLI flag convention, no registry) — distribution pattern, low stars
- linny006 skills-tracker / awesome-agent-skills — meta trackers

## Tomorrow queries
1. Anthropic-Cybersecurity-Skills framework-mapped mega-bundle deep dive
2. SkillBOM/SDA tooling releases post-ASSC
3. skillflag / package-embedded skill distribution
4. HASP / SIRI / UCOB internalization variants
5. OWASP AST10 v1 doc + scanner integration updates
"""
(RAW / "00-triage.md").write_text(triage, encoding="utf-8")

# --- Update examples/index.md: insert alphabetically-ish by appending new bullets near related letters ---
idx_path = EX / "index.md"
idx = idx_path.read_text(encoding="utf-8")
# Insert new entries before end if not present
new_bullets = []
for f, t, d in example_links:
    bullet = f"* [{t}]({f}) - {d[:160]}{'...' if len(d)>160 else ''}\n"
    if f not in idx:
        new_bullets.append(bullet)
if new_bullets:
    # append before final newline
    if not idx.endswith("\n"):
        idx += "\n"
    # insert after AgentSkill-related area: after AgentBound line if present else append
    marker = "* [AgentBound:"
    if marker in idx:
        pos = idx.find(marker)
        # find end of that line
        end = idx.find("\n", pos)
        # better: just append all new at end of file for simplicity + OKF progressive disclosure
        idx = idx.rstrip() + "\n" + "".join(new_bullets)
    else:
        idx = idx.rstrip() + "\n" + "".join(new_bullets)
    idx_path.write_text(idx + "\n", encoding="utf-8")

# --- Daily digest ---
digest = f"""---
type: Daily Digest
title: Daily Digest — {DATE} (Skill Bundles)
description: 'Catch-up iteration after 8-day gap: library maintenance (SkillOps), body-aware 80K routing (SkillRouter), capability-tree+DAG orchestration (AgentSkillOS), internalization triad (SkillC, Skill0.5, SLIM), and open-ecosystem curation (SkillCorpus 821K→96K).'
timestamp: '{TS}'
date: '{DATE}'
---

# Daily Digest — {DATE} (Skill Bundles)

**Iteration:** {ITER}
**Sources ingested:** 7
**Note:** First research cycle since 2026-07-16 (gap filled; prior commits were Phase 6/Pages only).

## Sources

1. **SkillOps** (arXiv:2605.13716, UIUC/Emory) — Library-time **skill technical debt** maintenance; Skill Contract (P,O,A,V,F); HSEG; merge/repair/retire; ALFWorld 79.5% (+8.8pp); plug-in +0.68–2.90pp; ~0 library-time LLM; GitHub Hik289/SkillOps (~58★)
2. **SkillRouter** (arXiv:2603.22455 v5, Alibaba, updated 20 Jul 2026) — Progressive disclosure hides body → **37–44pp** routing drop on ~80K pool; 1.2B retrieve-and-rerank **74.0% Hit@1**; 13× smaller / 5.8× faster than strongest 16B base; e2e coding-agent transfer; GitHub zhengyanzhao1997/SkillRouter (~220★)
3. **AgentSkillOS** (arXiv:2603.02176, Shanghai AI Lab) — Capability tree + **DAG orchestration** over 200→**200K** skills; 30 artifact-rich tasks; Bradley–Terry pairwise; DAG beats flat invocation **even with oracle skill set**; GitHub ynulihao/AgentSkillOS (~558★)
4. **SkillC** (arXiv:2605.27899) — Contrastive Skill Credit Assignment turns skill+/skill− paired rollouts into dual-stream advantages; +5.5% ALFWorld / +4.4% WebShop vs prior internalization RL; zero runtime skills
5. **Skill0.5** (arXiv:2605.28424) — Joint **general-skill internalization** + **task-specific utilization** via difficulty-aware mastery tiers; ID+OOD gains; rejects full-external vs full-internal binary
6. **SLIM** (arXiv:2605.10923, CUHK) — Dynamic skill lifecycle **retain–retire–expand** via leave-one-skill-out marginal contribution; +7.1pp avg vs best baselines; converges to **non-empty compact** active set; GitHub ejhshen/SLIM
7. **SkillCorpus** (arXiv:2607.15557 v4, 23 Jul 2026) — Curates ~**821K** crawled skills → **96,401** with 16-class taxonomy + utility/robustness/safety facets; +**7.5pp** SkillsBench; coverage + harness boundaries; dataset/code pending release

## Emerging Patterns

1. **Library-time vs task-time vs train-time layers separate cleanly** — SkillOps (maintain library), SkillRouter/AgentSkillOS (route & orchestrate at inference), SLIM/SkillC/Skill0.5 (train the internal/external boundary). Bundle engineering is now a full stack.
2. **Body-aware routing is mandatory at registry scale** — SkillRouter's 37–44pp body ablation + 91.7% body attention falsifies metadata-only progressive-disclosure routers; pairs with R3-Skill's set-compatibility result.
3. **Orchestration ≠ retrieval** — AgentSkillOS shows DAG composition beats flat invocation even when the skill set is oracle-correct; composition is the unlock.
4. **Internalization spectrum becomes a design space** — SKILL0 (zero@infer) → SkillC (better credit) → Skill0.5 (hybrid general/task) → SLIM (learned non-empty boundary). One size does not fit all skills.
5. **Open ecosystem value is curated, not raw** — SkillCorpus 821K→96K with safety facets and harness-boundary analysis; mass without curation under-delivers.
6. **Skill technical debt is real software debt** — Contracts, validators, and graph-aware maintenance are first-class context elements for production skill bundles.

## Wiki Updates Today

- New examples: [skillops self maintaining skill libraries](../examples/skillops-self-maintaining-skill-libraries.md), [skillrouter body aware routing](../examples/skillrouter-body-aware-routing.md), [agentskillos capability tree dag](../examples/agentskillos-capability-tree-dag.md), [skillc contrastive internalization](../examples/skillc-contrastive-internalization.md), [skill05 joint internalization utilization](../examples/skill05-joint-internalization-utilization.md), [slim dynamic skill lifecycle](../examples/slim-dynamic-skill-lifecycle.md), [skillcorpus open ecosystem curation](../examples/skillcorpus-open-ecosystem-curation.md)
- Metrics + index + primary publication + log refresh
- Q&A + OKF lint pass

## Tomorrow Priority Searches

1. **Anthropic-Cybersecurity-Skills** (mukul975, ~26k★) — 817 skills × 6 security frameworks mapping
2. **SkillBOM / SDA open tooling** post-ASSC paper
3. **skillflag** package-embedded skill distribution (no registry)
4. **HASP / SIRI / UCOB** internalization variants
5. **OWASP AST10** v1 publication + scanner integration refresh
6. **SkillCorpus** code/data release tracking

**Counts:** 7 sources · 7 new examples · 0 new paper notes · 0 updated examples · 6 new patterns · 7+ new context elements

## Q&A

- [Q&A — {DATE} (Iteration {ITER})](../qa/{DATE}-qa.md)
"""
(WIKI / "daily-digests" / f"{DATE}.md").write_text(digest, encoding="utf-8")

# Update daily-digests index if exists
dd_idx = WIKI / "daily-digests" / "index.md"
if dd_idx.exists():
    ddi = dd_idx.read_text(encoding="utf-8")
    line = f"* [{DATE} (Iteration {ITER})]({DATE}.md) — SkillOps, SkillRouter, AgentSkillOS, SkillC, Skill0.5, SLIM, SkillCorpus\n"
    if f"{DATE}.md" not in ddi:
        dd_idx.write_text(ddi.rstrip() + "\n" + line, encoding="utf-8")

# --- Q&A ---
qa = f"""---
type: Q&A
title: Q&A — {DATE} (Iteration {ITER})
description: Gap-fill Q&A on library maintenance, body-aware routing, DAG orchestration, and the internalization design space after catch-up research.
timestamp: '{TS}'
date: '{DATE}'
---

# Q&A — {DATE} (Iteration {ITER})

## Q1: Is progressive disclosure enough for skill selection at marketplace scale?

**A:** No for the **router**. [SkillRouter](../examples/skillrouter-body-aware-routing.md) shows hiding the skill body costs **37–44pp** Hit@1 on an ~80K SkillsBench-derived pool; attention concentrates **91.7%** on the body. Progressive disclosure remains valid as **agent UX after routing**, but routers must be body-aware. This is orthogonal and complementary to [R3-Skill](../examples/r3-skill-compatibility-routing.md) set-compatibility.

**Confidence:** High (controlled ablations + attention analysis + e2e transfer).

## Q2: If we retrieve the right skills, is composition solved?

**A:** No. [AgentSkillOS](../examples/agentskillos-capability-tree-dag.md) finds **DAG orchestration** substantially beats native flat invocation **even with an identical oracle skill set**. Capability-tree organization helps discovery at 200K scale; structured composition unlocks multi-skill value.

**Confidence:** High within their 30-task artifact benchmark; broader domains pending.

## Q3: Should training always eliminate external skills (SKILL0) or always keep them?

**A:** Neither extreme is optimal as a universal rule.
- [SkillC](../examples/skillc-contrastive-internalization.md) improves pure internalization via contrastive credit.
- [Skill0.5](../examples/skill05-joint-internalization-utilization.md) internalizes **general** skills while enforcing **task-specific** utilization.
- [SLIM](../examples/slim-dynamic-skill-lifecycle.md) learns a **non-empty compact** active set via retain–retire–expand (+7.1pp).

**Implication:** Bundle lifecycle design should assign skills to internal vs external endpoints by marginal value and generality — not a global boolean.

**Confidence:** High on ALFWorld/WebShop/SearchQA family; production marketplace transfer still open.

## Q4: What is the new “ops” layer for skill libraries?

**A:** [SkillOps](../examples/skillops-self-maintaining-skill-libraries.md) formalizes **skill technical debt** and provides contract+graph maintenance (validators, merge, retire) as a plug-in with ~zero library-time LLM cost. Paired with [SkillCorpus](../examples/skillcorpus-open-ecosystem-curation.md) curation (821K→96K, safety facet) and [ASSCs/SkillBOM](../examples/assc-skill-supply-chains-skillbom.md), the ops stack is: **curate → inventory → maintain → route → orchestrate → evaluate**.

**Confidence:** Medium–High (strong paper results; production lock-in evidence still maturing).

## Gaps

- SHACL/SSSOM still sparse in this catch-up batch (routing/ops/internalization heavy)
- SkillCorpus artifacts not yet public (promised on acceptance)
- Cybersecurity framework-mapped mega-bundle (26k★) deferred to next run
"""
(WIKI / "qa" / f"{DATE}-qa.md").write_text(qa, encoding="utf-8")

qa_idx = WIKI / "qa" / "index.md"
if qa_idx.exists():
    q = qa_idx.read_text(encoding="utf-8")
    line = f"* [Q&A — {DATE} (Iteration {ITER})]({DATE}-qa.md)\n"
    if f"{DATE}-qa.md" not in q:
        qa_idx.write_text(q.rstrip() + "\n" + line, encoding="utf-8")

# --- log.md prepend ---
log_path = WIKI / "log.md"
log = log_path.read_text(encoding="utf-8")
entry = f"""## {DATE}
* **Update**: [Daily Digest — {DATE} (Skill Bundles)](daily-digests/{DATE}.md) — Catch-up Iteration {ITER}: SkillOps library maintenance, SkillRouter body-aware 80K routing, AgentSkillOS capability-tree+DAG, SkillC/Skill0.5/SLIM internalization design space, SkillCorpus 821K→96K curation (+7 examples).

"""
if f"## {DATE}" not in log:
    # insert after title block
    lines = log.splitlines(keepends=True)
    out = []
    inserted = False
    for i, line in enumerate(lines):
        out.append(line)
        if not inserted and line.startswith("# "):
            # skip blank after title
            out.append("\n")
            out.append(entry)
            inserted = True
    if not inserted:
        out.insert(0, entry)
    log_path.write_text("".join(out), encoding="utf-8")

# --- metadata.json via load/dump ---
meta_path = ROOT / "raw" / "metadata.json"
meta = json.loads(meta_path.read_text(encoding="utf-8"))
meta["last_updated"] = DATE
meta["iteration"] = ITER
meta["daily_runs"][DATE] = {
    "sources": 7,
    "examples": [s["slug"] for s in sources],
    "queries_used": [
        "SkillOps skill technical debt library maintenance arXiv 2605.13716",
        "SkillRouter body-aware skill routing 80K arXiv 2603.22455",
        "AgentSkillOS capability tree DAG orchestration arXiv 2603.02176",
        "SkillC contrastive skill internalization arXiv 2605.27899",
        "Skill0.5 joint skill internalization utilization arXiv 2605.28424",
        "SLIM dynamic skill lifecycle management arXiv 2605.10923",
        "SkillCorpus open skill ecosystem 821000 arXiv 2607.15557",
        "gh search repos agent skills --sort updated",
        "OWASP Agentic Skills Top 10 AST10 2026",
    ],
    "patterns": [
        "Library-time vs task-time vs train-time layers",
        "Body-aware routing mandatory at registry scale",
        "Orchestration ≠ retrieval (DAG > flat oracle)",
        "Internalization spectrum as design space",
        "Open ecosystem value is curated not raw",
        "Skill technical debt as real software debt",
    ],
}
if "cumulative_sources" in meta and isinstance(meta["cumulative_sources"], int):
    meta["cumulative_sources"] += 7
meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print("Wrote raw + examples + digest + qa + metadata")
print("examples:", len(list(EX.glob("*.md"))))
print("raw day:", list(RAW.iterdir()))
