# Skill Bundles — Metrics & Progress

|**Last Updated: 2026-07-12 (Iteration 37)

## KPIs

| Metric | Value | Previous | Change |
|--------|-------|----------|--------|
| Documented Examples | 69 | 61 | +8 |
| Raw Sources (daily folders) | 49 days | 48 | +1 (2026-07-12) |
| Wiki Example Files | 69 | 61 | +8 |
| Paper Notes | 6 | 6 | Unchanged |
| Concept Articles | 8 | 8 | Unchanged |
| Daily Digests | +1 (2026-07-12) | — | +1 |
| Q&A Passes | +1 (2026-07-12-qa) | — | +1 |
| Context Element Types Covered | 34+ | 27 | +7 (Multi-objective optimization, Delta debugging, Progressive disclosure, DAG scheduler, Canonical taxonomy, Closed-loop knowledge, LLM jury voting) |

## Context Element Coverage (summary)

|| Context Element | Status |
|-----------------|--------|
| SHACL Validation | Strong (monitoring sh:agentInstruction) |
| Constraint Rules | Strong (+Vercel handbooks) |
| Ontology / Taxonomy / Scientific DBs | Strong (+K-Dense) |
| Security / Governance | Strong (+ClawHavoc case study, +SoK 7-pattern) |
| Plugin / Distribution | Strong (+Awesome-Agent-Skill-Papers catalog) |
| Human Approval Gates | Stable (OpenMontage) |
| SSSOM Mapping | Mature (no new hit today) |
| Co-Evolutionary Verification | New (CoEvoSkills surrogate verifier) |
| SLSA/in-toto Provenance | New (Agentic Factory, fullsend) |
| Formal Skill Definition | New (SoK S=(C,π,T,R)) |
| Six-Layer Taxonomy | New (Procedural Infrastructure survey) |
| Paper Catalog | New (Awesome-Agent-Skill-Papers) |
| Multi-Objective Optimization | New (SkillMOO NSGA-II Pareto) |
| Delta Debugging | New (SkillReducer adversarial delta) |
| Progressive Disclosure | New (SkillReducer on-demand loading) |
| DAG Scheduler | New (ORCA dependency resolution + policy gates) |
| Canonical Taxonomy | New (ORCA 184/184 capability coverage) |
| Closed-Loop Knowledge | New (AI-KM knowledge→skill→knowledge) |
| LLM Jury Voting | New (SkillSieve 3-LLM debate) |

## 2026-07-12 Run Notes (Iteration 37)

- Pre-flight: Clean tree (`## master...origin/master`). No `raw/2026-07-12/` (created today). Last commit 2026-07-11. Digests current through 2026-07-11. No leftover uncommitted raw.
- Anti-stagnation: Followed yesterday's priority search list (6 targets from digest) — found 5/6 directly + diversified into SkillReducer, ORCA, AI-KM, marketplace landscape. All sources novel (none appeared in prior week's digests).
- Phase 1: **8 sources** — SkillMOO, EffiSkill, SkillSieve, SkillCraft, SkillReducer, ORCA, AI-KM, Marketplace Landscape. Atomic Skills (arXiv:2604.05013) found but WITHDRAWN — documented as raw source only.
- Phase 2: 8 new example articles + daily digest.
- Phase 3: index + patterns + context element coverage updated; 6 new emerging patterns.
- Phase 4: Q&A + lint pass.
- Phase 5: Unconditional git commit + push.
- Daily sources: 8 | New examples: 8 | Papers: 0 | Updated: 0 | New patterns: 6 | New context elements: 7

## Velocity Notes (prior)

### 2026-07-06 Update (Iteration 34)
- Maintenance-oriented core refresh (SHACL 1.2, agentskills.io, NVIDIA); 3 sources.

### 2026-06-30 Run Notes (Iteration 30)
- 5 sources; SHACL agentInstruction + production bundles; total raw days growing.

### Bundle density leaderboard (Iteration 36 refresh)

| Rank | Example | Density signal |
|------|---------|----------------|
| 1 | OpenMontage | 500+ skills × 12 pipelines × hard gates × tools × audit trail |
| 2 | Agentic Awesome Skills | 1,943 skills × schemas × plugins × workflows × audit gates |
| 3 | Scientific Agent Skills | 148 skills × 100+ DBs × packages × security CI |
| 4 | ClawBio | 88 skills × Galaxy tools × reproducibility × validation rate |
| 5 | SoK: Agentic Skills | S=(C,π,T,R) × 7 patterns × 7-stage lifecycle × ClawHavoc case study × 73 citations |
| 6 | Vercel Labs | Few skills × very high rule density (40–100+/skill) |
| 7 | CoEvoSkills | Multi-file packages × co-evolutionary verification × 8-LLM generalization × SkillsBench-validated |
| 8 | SkillSieve | 3-layer triage × LLM jury × 49K skills evaluated × F1=0.920 × $0.006/skill |
| 9 | ORCA | 122 capabilities × 36 DAG skills × policy gates × provenance × 184/184 taxonomy |
| 10 | SkillReducer | 55K skills studied × delta debugging × taxonomy × progressive disclosure × less-is-more |
