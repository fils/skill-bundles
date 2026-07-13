# Skill Bundles — Metrics & Progress

|**Last Updated: 2026-07-13 (Iteration 38)**|

## KPIs

| Metric | Value | Previous | Change |
|--------|-------|----------|--------|
| Documented Examples | 75 | 69 | +6 |
| Raw Sources (daily folders) | 50 days | 49 | +1 (2026-07-13) |
| Wiki Example Files | 75 | 69 | +6 |
| Paper Notes | 6 | 6 | Unchanged |
| Concept Articles | 8 | 8 | Unchanged |
| Daily Digests | +1 (2026-07-13) | — | +1 |
| Q&A Passes | +1 (2026-07-13-qa) | — | +1 |
| Context Element Types Covered | 40+ | 34+ | +6 (Pareto frontier governance, Textual learning rate, TIP 4-tuple, W3C PROV+MCP provenance, Skill OS abstraction, Generator-executor decoupling) |

## Context Element Coverage (summary)

|| Context Element | Status |
|-----------------|--------|
| SHACL Validation | Strong (monitoring sh:agentInstruction) |
| Constraint Rules | Strong (+Vercel handbooks) |
| Ontology / Taxonomy / Scientific DBs | Strong (+K-Dense) |
| Security / Governance | Strong (+ClawHavoc, +SoK 7-pattern) |
| Plugin / Distribution | Strong (+Awesome-Agent-Skill-Papers catalog) |
| Human Approval Gates | Stable (OpenMontage) |
| SSSOM Mapping | Mature (no new hit today) |
| Co-Evolutionary Verification | Stable (CoEvoSkills) |
| SLSA/in-toto Provenance | Stable (Agentic Factory) |
| Formal Skill Definition | Stable (SoK S=(C,π,T,R)) |
| Six-Layer Taxonomy | Stable (Procedural Infrastructure survey) |
| Paper Catalog | Stable (Awesome-Agent-Skill-Papers) |
| Multi-Objective Optimization | Stable (SkillMOO) |
| Delta Debugging | Stable (SkillReducer) |
| Progressive Disclosure | Stable (SkillReducer, Skill OS) |
| DAG Scheduler | Stable (ORCA) |
| Canonical Taxonomy | Stable (ORCA) |
| Closed-Loop Knowledge | Stable (AI-KM) |
| LLM Jury Voting | Stable (SkillSieve) |
| Pareto Frontier Governance | New (EvoSkill K=3 git-backed selection) |
| Textual Learning Rate | New (SkillOpt per-step edit budget) |
| Validation Gating + Rejected-Edit Buffer | New (SkillOpt training-style skill optimization) |
| Transferable Interaction Pattern (TIP) | New (SkillMigrator 4-tuple ⟨intent,template,slots,layout⟩) |
| Accessibility-Tree Skeleton Matching | New (SkillMigrator TED on structural layout) |
| W3C PROV + MCP Provenance | New (PROV-AGENT agent-centric provenance) |
| Skill OS Abstraction | New (100K skill analysis → 5 OS demands) |
| Generator-Executor Decoupling | New (SkillGenBench skill generation evaluation) |
| Negative Transfer Detection | New (SkillGenBench auto-skill risk) |

## 2026-07-13 Run Notes (Iteration 38)

- Pre-flight: Clean tree (`## master...origin/master`). No `raw/2026-07-13/` (created today). Last commit 2026-07-12. Digests current through 2026-07-12. No leftover uncommitted raw.
- Anti-stagnation: Followed yesterday's priority search list (6 targets). Found 3/6 directly (auto-skill discovery → EvoSkill, skill transfer → SkillOpt/SkillMigrator, skill provenance → PROV-AGENT) + diversified into Skill OS, SkillGenBench. All 6 sources novel (none appeared in prior week's digests). GitHub `gh search` found new repos but papers were the main yield today.
- Phase 1: **6 sources** — EvoSkill, SkillOpt, PROV-AGENT, SkillMigrator, Skill OS, SkillGenBench. All novel.
- Phase 2: 6 new example articles + daily digest.
- Phase 3: index + patterns + context element coverage updated; 6 new emerging patterns.
- Phase 4: Q&A + lint pass.
- Phase 5: Unconditional git commit + push.
- Daily sources: 6 | New examples: 6 | Papers: 0 | Updated: 0 | New patterns: 6 | New context elements: 6

## Velocity Notes (prior)

### 2026-07-12 Update (Iteration 37)
- 8 sources; skill optimization + composition + security + runtime + ontology.

### 2026-07-06 Update (Iteration 34)
- Maintenance-oriented core refresh (SHACL 1.2, agentskills.io, NVIDIA); 3 sources.

### 2026-06-30 Run Notes (Iteration 30)
- 5 sources; SHACL agentInstruction + production bundles; total raw days growing.

## Bundle density leaderboard (Iteration 38 refresh)

| Rank | Example | Density signal |
|------|---------|----------------|
| 1 | OpenMontage | 500+ skills × 12 pipelines × hard gates × tools × audit trail |
| 2 | Agentic Awesome Skills | 1,943 skills × schemas × plugins × workflows × audit gates |
| 3 | Scientific Agent Skills | 148 skills × 100+ DBs × packages × security CI |
| 4 | ClawBio | 88 skills × Galaxy tools × reproducibility × validation rate |
| 5 | SoK: Agentic Skills | S=(C,π,T,R) × 7 patterns × 7-stage lifecycle × ClawHavoc case study × 73 citations |
| 6 | Skill OS | ~100K skills analyzed × 6 properties × 5 OS demands × 4 problems |
| 7 | SkillOpt | 6 benchmarks × 7 models × 3 modes × 52/52 cells × validation gating × textual LR |
| 8 | Vercel Labs | Few skills × very high rule density (40–100+/skill) |
| 9 | CoEvoSkills | Multi-file packages × co-evolutionary verification × 8-LLM generalization × SkillsBench-validated |
| 10 | EvoSkill | 3-agent architecture × Pareto frontier K=3 × git-backed × zero-shot transfer × 2 benchmarks |
| 11 | SkillSieve | 3-layer triage × LLM jury × 49K skills evaluated × F1=0.920 × $0.006/skill |
| 12 | ORCA | 122 capabilities × 36 DAG skills × policy gates × provenance × 184/184 taxonomy |
| 13 | SkillReducer | 55K skills studied × delta debugging × taxonomy × progressive disclosure × less-is-more |
| 14 | SkillGenBench | 187 tasks × 8 domains × 2 source types × generator-executor decoupling × pass@3 |
| 15 | SkillMigrator | TIP 4-tuple × TED layout matching × Hungarian slot binding × 35.4% cross-domain reuse |
| 16 | PROV-AGENT | W3C PROV + MCP × edge/cloud/HPC × near real-time × agent-centric provenance |
