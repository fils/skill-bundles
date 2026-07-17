---
type: Metrics
title: Skill Bundles — Metrics & Progress
description: 'Tracked KPIs for the skill-bundles research wiki: example counts, coverage, and iteration progress.'
---

# Skill Bundles — Metrics & Progress

|**Last Updated: 2026-07-16 (Iteration 41)**|

## KPIs

|| Metric | Value | Previous | Change |
|--------|-------|----------|--------|
| Documented Examples | 97 | 90 | +7 |
| Raw Sources (daily folders) | 53 days | 52 | +1 (2026-07-16) |
| Wiki Example Files | 97 | 90 | +7 |
| Paper Notes | 7 | 7 | Unchanged |
| Concept Articles | 8 | 8 | Unchanged |
| Daily Digests | +1 (2026-07-16) | — | +1 |
| Q&A Passes | +1 (2026-07-16-qa) | — | +1 |
| Context Element Types Covered | 62+ | 55+ | +7 (Native multi-harness protocol, Skill internalization/Dynamic Curriculum, Collective Skill Tree Search + transfer scoring, Skill compatibility / Reject-as-Resource, ASSC SkillBOM multi-channel deps, One-time copy reuse model, SE activity→skill mapping) |

## Context Element Coverage (summary)

|| Context Element | Status |
|-----------------|--------|
| SHACL Validation | Strong (monitoring sh:agentInstruction) |
| Constraint Rules | Strong (+Vercel handbooks) |
| Ontology / Taxonomy / Scientific DBs | Strong (+K-Dense) |
| Security / Governance | Strong (+ClawHavoc, +SoK 7-pattern, +SkillGuard dual-plane, +SkillFortify formal) |
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
| Dual-Plane Governance (Context + Action) | New (SkillGuard dual-plane permission model) |
| Skill Manifests (Capability Declaration) | New (SkillGuard pre-execution permission surface) |
| Deny-by-Default Enforcement | New (SkillGuard runtime access control) |
| DY-Skill Attacker Model | New (SkillFortify Dolev-Yao for 5-phase skill lifecycle) |
| Agent Dependency Graph + Lockfile | New (SkillFortify SAT resolution, SHA-256 integrity) |
| Trust Score Algebra | New (SkillFortify formal monotonicity) |
| Capability-Based Sandboxing | New (SkillFortify confinement proof) |
| Frequency Decomposition Credit | New (Skill1 low-freq=selection, high-freq=distillation) |
| Skill Cards (Trust Metadata) | New (NVIDIA-verified ownership, deps, limitations, status) |
| Cryptographic Skill Signing | New (NVIDIA-verified detached skill.oms.sig) |
| Skills as Persistent Evolving Memory | New (Memento-Skills markdown files as memory) |
| Read-Write Reflective Learning | New (Memento-Skills skill lifecycle cycle) |
| Code-as-Policy Skill Library | New (ASPIRE robot control programs as reusable skills) |
| Evolutionary Skill Search | New (ASPIRE diverse task/program generation) |
| Collective Skill Evolution (Cross-User + Over-Time) | New (SkillClaw multi-user trajectory aggregation + autonomous evolver) |
| Autonomous Skill Evolver | New (SkillClaw pattern recognition → skill update pipeline) |
| YARA Rules (Pattern-Based Detection) | New (SkillSpector YARA rule engine for malicious code) |
| CIA Triad for Agent Tools | New (MalTool confidentiality/integrity/availability taxonomy) |
| Model-in-Skill Threat Surface | New (BadSkill backdoor-fine-tuned models in skills) |
| Two-Channel Attack Model | New (SkillJect artifact channel + instruction channel) |
| Declarative MCP Access Control | New (AgentBound Android-permission-inspired policy) |
| Cognitive Artifacts Framework | New (Externalization four-form taxonomy) |

| Native Multi-Harness Evaluation Protocol | New (WildClawBench OpenClaw/Claude Code/Codex/Hermes) |
| Skill Internalization Dynamic Curriculum | New (SKILL0 on-policy helpfulness annealing) |
| Collective Skill Tree Search + Transfer Scoring | New (CSTS CSN-Gen/CSN-Assess) |
| Skill Compatibility / Reject-as-Resource | New (R3-Skill Set-Compat routing) |
| ASSC SkillBOM Multi-Channel Deps | New (skill/package/service graphs + lockfiles) |
| One-Time Copy Reuse Model | New (Registry→Repository maintenance science) |
| SE Activity→Skill Lifecycle Mapping | New (Inside the Skill Market) |

## 2026-07-16 Run Notes (Iteration 41)

- Pre-flight: Clean tree (`## master...origin/master`). No `raw/2026-07-16/` (created today). Last commit 2026-07-15 (0b9b792). Digests current through 2026-07-15. No leftover uncommitted raw.
- Anti-stagnation: Followed 2026-07-15 priority list (WildClawBench first hit) + diversified into Jul-2026 arXiv (ASSCs, Registry→Repository, SE market) + SKILL0 internalization + CSTS + R3-Skill. All 7 sources novel (none in prior week digests). Theme: evaluation + internalization + supply-chain inventory + maintenance science.
- Phase 1: **7 sources** — WildClawBench, SKILL0, OpenClaw-Skill CSTS, R3-Skill, ASSCs, Registry→Repository, Inside Skill Market. All novel.
- Phase 2: 7 new example articles + daily digest.
- Phase 3: index + patterns + context element coverage updated; 6 new emerging patterns.
- Phase 4: Q&A + lint pass.
- Phase 5: Unconditional git commit + push.
- Daily sources: 7 | New examples: 7 | Papers: 0 | Updated: 0 | New patterns: 6 | New context elements: 7

## 2026-07-15 Run Notes (Iteration 40)

- Pre-flight: Clean tree (`## master...origin/master`). No `raw/2026-07-15/` (created today). Last commit 2026-07-14 (aa0016c). Digests current through 2026-07-14. No leftover uncommitted raw.
- Anti-stagnation: Followed 2026-07-14 priority search list (8 targets). Found all 8/8 directly (SkillClaw, SkillSpector, MalTool, BadSkill, SkillJect, AgentBound, SWE-Skills-Bench, Externalization). 100% hit rate on priority list. All 8 sources novel (none appeared in prior week's digests). Theme: security attack/defense + evaluation + theory.
- Phase 1: **8 sources** — SkillClaw, SkillSpector, MalTool, BadSkill, SkillJect, AgentBound, SWE-Skills-Bench, Externalization. All novel.
- Phase 2: 8 new example articles + daily digest.
- Phase 3: index + patterns + context element coverage updated; 6 new emerging patterns.
- Phase 4: Q&A + lint pass.
- Phase 5: Unconditional git commit + push.
- Daily sources: 8 | New examples: 8 | Papers: 1 (Externalization) | Updated: 0 | New patterns: 6 | New context elements: 8

## 2026-07-14 Run Notes (Iteration 39)

- Pre-flight: Clean tree (`## master...origin/master`). No `raw/2026-07-14/` (created today). Last commit 2026-07-13 (fa8b066). Digests current through 2026-07-13. No leftover uncommitted raw.
- Anti-stagnation: Followed 2026-07-13 priority search list. Found 4/7 directly (ASPIRE, Memento-Skills, EXIF, SkillGuard) + diversified into SkillFortify, Skill1, NVIDIA-verified. All 7 sources novel (none appeared in prior week's digests). GitHub `gh search` showed many new repos updated today but papers were the main yield.
- Phase 1: **7 sources** — ASPIRE, Memento-Skills, SkillGuard, SkillFortify, Skill1, NVIDIA-verified, EXIF. All novel.
- Phase 2: 7 new example articles + daily digest.
- Phase 3: index + patterns + context element coverage updated; 6 new emerging patterns.
- Phase 4: Q&A + lint pass.
- Phase 5: Unconditional git commit + push.
- Daily sources: 7 | New examples: 7 | Papers: 0 | Updated: 0 | New patterns: 6 | New context elements: 7

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

## Bundle density leaderboard (Iteration 39 refresh)

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
