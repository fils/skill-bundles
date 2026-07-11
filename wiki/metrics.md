# Skill Bundles — Metrics & Progress

|**Last Updated: 2026-07-11 (Iteration 36)**

## KPIs

| Metric | Value | Previous | Change |
|--------|-------|----------|--------|
| Documented Examples | 61 | 57 | +4 |
| Raw Sources (daily folders) | 48 days | 47 | +1 (2026-07-11) |
| Wiki Example Files | 61 | 57 | +4 |
| Paper Notes | 6 | 4 | +2 (SoK + Procedural Infrastructure survey) |
| Concept Articles | 8 | 8 | Unchanged |
| Daily Digests | +1 (2026-07-11) | — | +1 |
| Q&A Passes | +1 (2026-07-11-qa) | — | +1 |
| Context Element Types Covered | 27+ | 22 | +5 (Co-Evo Verification, SLSA/in-toto, Formal Definition, 6-Layer Taxonomy, Paper Catalog) |

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

## 2026-07-11 Run Notes (Iteration 36)

- Pre-flight: Clean tree (`## master...origin/master`). No `raw/2026-07-11/` (created today). Last commit 2026-07-10. Digests current through 2026-07-10. No leftover uncommitted raw.
- Anti-stagnation: Diversified away from core monitoring sources — focused on arXiv survey papers (SoK, 6-layer), self-evolving skills (CoEvoSkills), supply chain provenance (SLSA/in-toto), marketplace attack (ClawHavoc), benchmark updates (GoS v3, SkillsBench v1.1), and paper catalog (Awesome-Agent-Skill-Papers).
- Phase 1: **6 sources** — CoEvoSkills, SoK: Agentic Skills, Procedural Infrastructure survey, Supply Chain Agentic Factory, ClawHavoc Campaign, GoS v3 + SkillsBench v1.1.
- Phase 2: 4 new example articles + 2 new paper notes + daily digest. Updated 2 existing entries (GoS, SkillsBench).
- Phase 3: skill-bundles.md count 61 (+6 paper notes); index + patterns + context element coverage updated; 6 new emerging patterns.
- Phase 4: Q&A with 4 complex questions + 3 epistemic sample checks (all verified against primary sources). Lint: 33 broken links (25 pre-existing, 8 new false positives fixed inline — path-style wikilinks).
- Phase 5: Unconditional git commit + push.
- Daily sources: 6 | New examples: 4 | Papers: 2 | Updated: 2 | New patterns: 6 | New context elements: 5

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
