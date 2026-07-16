# Skill Bundles Knowledge Base

|**Last Updated:** 2026-07-16 (Iteration 41)|
|**Status:** Active research — 7 new examples (WildClawBench native multi-harness eval, SKILL0 internalization, OpenClaw-Skill CSTS, R3-Skill compatibility routing, ASSC SkillBOM supply chains, Registry→Repository maintenance, Inside Skill Market SE activities)|

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
  - [2026-07-16 (Iteration 41)](daily-digests/2026-07-16.md)
  - [2026-07-15 (Iteration 40)](daily-digests/2026-07-15.md)
  - [2026-07-14 (Iteration 39)](daily-digests/2026-07-14.md)
  - [2026-07-13 (Iteration 38)](daily-digests/2026-07-13.md)
  - [2026-07-12 (Iteration 37)](daily-digests/2026-07-12.md)
  - [2026-07-11 (Iteration 36)](daily-digests/2026-07-11.md)
  - [2026-07-10 (Iteration 35)](daily-digests/2026-07-10.md)
  - [2026-07-09](daily-digests/2026-07-09.md)
  - [2026-07-08](daily-digests/2026-07-08.md)
  - [2026-07-06](daily-digests/2026-07-06.md)
  - [2026-06-30 (Iteration 30)](daily-digests/2026-06-30.md)
  - [2026-06-01 (Iteration 13)](daily-digests/2026-06-01.md)
- [Documented Examples](examples/)
- [Concepts](concepts/)
- [Papers](papers/)
- [Metrics](metrics.md)
- [Q&A](qa/)

## Current Status (Iteration 41 — 2026-07-16)

Seven major new skill-bundle examples covering native multi-harness evaluation, skill internalization into weights, collective tree-search construction, composition-aware retrieval, ecosystem supply-chain inventory (1.43M skills), and empirical maintenance science:

- **[[wildclawbench-native-runtime-evaluation]]** — 60 bilingual multimodal tasks in real OpenClaw / Claude Code / Codex / Hermes harnesses; hybrid grading; 19 models; best 62.2%; harness switch ±18pp; skill ablations mixed (Code Intelligence +22.4 strongest model); InternLM (arXiv:2605.10912)
- **[[skill0-skill-internalization]]** — First RL skill-internalization framework ("skills@train, zero@infer"); Dynamic Curriculum on-policy helpfulness annealing; +9.7% ALFWorld / +10.1% WebShop; <0.5k tokens/step; ZJU-REAL/SkillZero (arXiv:2604.02268)
- **[[openclaw-skill-csts-tree-search]]** — Collective Skill Tree Search: multi-model gen + quality/transferability assess; tree-of-skills anti-fragmentation; Collective Skill RL multi-skill selection (arXiv:2606.16774)
- **[[r3-skill-compatibility-routing]]** — Skill retrieval ≠ document retrieval; Reject-as-Resource compatibility supervision; 10,246 skills; Hit@1=0.7521; Tencent R3-Skill (arXiv:2606.03565)
- **[[assc-skill-supply-chains-skillbom]]** — Agent Skill Supply Chains; SDA + SkillBOM; 1.43M skills; 58.73% name collisions; 71–73% packages transitive-only; lockfile/manifest recommendations; PKU (arXiv:2607.01136)
- **[[registry-to-repository-skill-maintenance]]** — First skill-as-artefact empirical study; 18k registry + 23k personal skills; one-time copy reuse; 53% never modified; 6 content + 6 maintenance themes (arXiv:2607.00911)
- **[[inside-skill-market-se-activities]]** — Activity-centric SE skills market study; 11,497 SE skills; construction-heavy lifecycle skew; weak version maturity signals (arXiv:2607.09065)

**Convergence signals:**
1. **Internalization ↔ externalization spectrum** — SKILL0 (weights) vs SkillOpt/Memento (external packages) vs Externalization theory.
2. **Composition-aware retrieval required** — R3-Skill Set-Compat explains negative skill deltas beyond content quality.
3. **Supply chain becomes inventory science** — ASSC SkillBOM at 1.43M scale; transitive dark matter dominates risk.
4. **Native multi-harness is the evaluation bar** — WildClawBench: harness choice can rival model choice.
5. **Maintenance science for copy-fork skills** — Registry→Repository + SE market: additive local evolution, stable behavioral contracts.
6. **Collective construction ≠ collective evolution** — CSTS (build trees multi-model) vs SkillClaw (runtime multi-user trajectories).

## Iteration History (recent)

| Iteration | Date | Focus | New Examples |
|-----------|------|-------|--------------|
| **41** | **2026-07-16** | **Native multi-harness eval + internalization + CSTS trees + compatibility routing + ASSC SkillBOM + maintenance science + SE market** | **WildClawBench, SKILL0, OpenClaw-Skill CSTS, R3-Skill, ASSCs, Registry→Repository, Inside Skill Market** |
| **40** | **2026-07-15** | **Collective evolution + security scanner + malicious tools + model backdoor + prompt injection + MCP access control + utility benchmark + externalization theory** | **SkillClaw, SkillSpector, MalTool, BadSkill, SkillJect, AgentBound, SWE-Skills-Bench, Externalization** |
| **39** | **2026-07-14** | **Robotics skill discovery + agent-designing agents + permission governance + formal verification + unified RL evolution + industry governance + precursor discovery** | **ASPIRE, Memento-Skills, SkillGuard, SkillFortify, Skill1, NVIDIA-verified, EXIF** |
| **38** | **2026-07-13** | **Auto-discovery + trainable skills + provenance + cross-domain transfer + OS abstraction + generation benchmark** | **EvoSkill, SkillOpt, PROV-AGENT, SkillMigrator, Skill OS, SkillGenBench** |
| **37** | **2026-07-12** | **Skill optimization + composition + security + runtime + ontology** | **SkillMOO, EffiSkill, SkillSieve, SkillCraft, SkillReducer, ORCA, AI-KM, Marketplace Landscape** |
| **36** | **2026-07-11** | **Self-evolving skills + supply chain provenance + marketplace attack + academic surveys** | **CoEvoSkills, ClawHavoc, SLSA/in-toto factory, Awesome-Agent-Skill-Papers, SoK, 6-layer survey** |
| **35** | **2026-07-10** | **Workshop + marketplace analysis + domain/vendor mega-bundles** | **K-Dense scientific, Agentic Awesome, Vercel Labs, OpenMontage** |
| 31–34 | 2026-07-01…09 | Core standard + SHACL 1.2 agentInstruction + reference impl refresh | Monitoring sources (agentskills.io, addyosmani, anthropics, NVIDIA) |
| 14 | 2026-06-09 | Domain bioinformatics + process engineering + conference infra | ClawBio, Addy Osmani, Agents at Conferences, DSPy v0.2.3 |
| 13 | 2026-06-01 | Three-layer validation + SHACL bridge + ontology skills | ai4curation, skill-validator, ags, validate-skill, text2shacl |

## Tomorrow Priority Searches

1. **SkillBOM / SDA tooling releases** — open-source SkillDepAnalyzer or SkillBOM exporters
2. **SDAR / Skill-GRPO absorption** — follow-on internalization beyond SKILL0
3. **SkillRouter** — large-pool body-ablation routing (cited by R3)
4. **AgentSkillOS** — 280K+ skills ecosystem orchestration
5. **SkillOps** (arXiv:2605.13716) — self-maintaining skill libraries
6. **ToxicSkills remediation** — automated quarantine beyond scanning
7. **Hermes multi-harness skill governance** — WildClawBench implications
8. **SE requirements/design skills** — marketplace gap (Inside the Skill Market)
