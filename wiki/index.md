# Skill Bundles Knowledge Base

|**Last Updated:** 2026-07-13 (Iteration 38)
|**Status:** Active research — 6 new examples (EvoSkill auto-discovery, SkillOpt trainable parameters, PROV-AGENT provenance, SkillMigrator cross-domain, Skill OS abstraction, SkillGenBench generation benchmark)

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
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

## Current Status (Iteration 38 — 2026-07-13)

Six major new skill-bundle examples covering auto-skill discovery, trainable skill optimization, provenance, cross-domain transfer, OS-level skill management, and skill generation benchmarking:

- **[[evoskill-automated-skill-discovery]]** — self-evolving framework for auto-discovering agent skills via failure analysis; three-agent architecture (Executor→Proposer→Skill-Builder); Pareto frontier K=3; git-backed lineage; +7.3% OfficeQA, +12.1% SealQA; zero-shot transfer to BrowseComp (+5.3%); open-sourced (1k★)
- **[[skillopt-trainable-skill-parameters]]** — treats skill files as trainable parameters; forward-backward-update in text space; frozen model + optimizer; textual learning rate + validation gating; best/tied-best on all 52 evaluation cells; +23.5 points on GPT-5.5; skills transfer across model scales, harnesses, and tasks
- **[[prov-agent-unified-provenance]]** — extends W3C PROV + MCP for agent interaction provenance; agent decisions/prompts/responses as first-class; near real-time capture; cross-facility (edge/cloud/HPC); Oak Ridge + Argonne
- **[[skillmigrator-cross-domain-transfer]]** — cross-domain web skill reuse via Transferable Interaction Patterns (TIP 4-tuple); accessibility-tree skeleton matching with Tree Edit Distance; 8-10% LLM call reduction; 35.4% cross-domain reuse rate
- **[[skill-os-skills-as-apps]]** — "Skills are the new Apps"; surveys ~100K public skills; 6 properties identified; argues for Skill OS abstraction (caching, env construction, global management, failure handling, security)
- **[[skillgenbench-skill-generation-benchmark]]** — benchmark for skill generation pipelines; 187 tasks × 8 domains; generator-executor decoupling; repo-grounded pass@3: 7-16%, doc-grounded: 23-27%; auto-generated skills risk negative transfer

**Convergence signals:**
1. **Skill optimization taxonomy completing** — Five approaches now mapped: SkillMOO (search), CoEvoSkills (evolution), SkillReducer (content reduction), SkillOpt (training/gradient-like), EvoSkill (discovery). SkillOpt outperforms all on 52/52 cells.
2. **Skill transfer is quantified** — EvoSkill (task→task +5.3%), SkillOpt (cross-harness +59.7, cross-model-scale), SkillMigrator (cross-domain 35.4%). Skills capture reusable workflow knowledge.
3. **Skill generation is the bottleneck** — SkillGenBench proves generating skills (7-27% pass@3) is 2-3x harder than using them. Negative transfer is a real risk.
4. **Skills need OS-level management** — Skill OS paper (100K skill analysis) argues skills are applications requiring OS abstractions. ORCA is early implementation.
5. **Provenance standards converging** — PROV-AGENT (W3C PROV + MCP), SLSA/in-toto, W3C Agent Protocol CG. Provenance becoming standard context element.
6. **Cross-domain via structural layout** — SkillMigrator's TIP enables cross-domain transfer by matching layout structure, not element IDs.

## Iteration History (recent)

| Iteration | Date | Focus | New Examples |
|-----------|------|-------|--------------|
| **38** | **2026-07-13** | **Auto-discovery + trainable skills + provenance + cross-domain transfer + OS abstraction + generation benchmark** | **EvoSkill, SkillOpt, PROV-AGENT, SkillMigrator, Skill OS, SkillGenBench** |
| **37** | **2026-07-12** | **Skill optimization + composition + security + runtime + ontology** | **SkillMOO, EffiSkill, SkillSieve, SkillCraft, SkillReducer, ORCA, AI-KM, Marketplace Landscape** |
| **36** | **2026-07-11** | **Self-evolving skills + supply chain provenance + marketplace attack + academic surveys** | **CoEvoSkills, ClawHavoc, SLSA/in-toto factory, Awesome-Agent-Skill-Papers, SoK, 6-layer survey** |
| **35** | **2026-07-10** | **Workshop + marketplace analysis + domain/vendor mega-bundles** | **K-Dense scientific, Agentic Awesome, Vercel Labs, OpenMontage** |
| 31–34 | 2026-07-01…09 | Core standard + SHACL 1.2 agentInstruction + reference impl refresh | Monitoring sources (agentskills.io, addyosmani, anthropics, NVIDIA) |
| 14 | 2026-06-09 | Domain bioinformatics + process engineering + conference infra | ClawBio, Addy Osmani, Agents at Conferences, DSPy v0.2.3 |
| 13 | 2026-06-01 | Three-layer validation + SHACL bridge + ontology skills | ai4curation, skill-validator, ags, validate-skill, text2shacl |

## Tomorrow Priority Searches

1. **SkillVerifier / SkillGuard** — runtime verification frameworks for skill execution safety (still not found)
2. **OpenClaw / ClawHub ecosystem** — latest governance changes post-ClawHavoc (still not found)
3. **Memento-Skills** — RL-based skill self-evolution; "Complete Autopsy" article suggests analysis available
4. **ASPIRE** (NVIDIA) — agentic skill programming through iterative robot exploration; robotics-focused skill discovery
5. **EXIF** — Automated Skill Discovery for Language Agents through Exploration
6. **JayLZhou/Awesome-Agent-Skills** — curated paper list + "Comprehensive Survey on Agent Skills" — check for new papers
7. **Skill OS implementations** — any systems implementing the Skill OS abstraction demands?
