# Skill Bundles Knowledge Base

|**Last Updated:** 2026-07-14 (Iteration 39)|
|**Status:** Active research — 7 new examples (ASPIRE robotics skill discovery, Memento-Skills agent-designing agent, SkillGuard permission framework, SkillFortify formal verification, Skill1 unified RL evolution, NVIDIA-verified skills governance, EXIF automated skill discovery)|

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
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

## Current Status (Iteration 39 — 2026-07-14)

Seven major new skill-bundle examples covering robotics skill discovery, agent-designing agents, permission governance, formal verification, unified RL skill evolution, industry verification governance, and precursor skill discovery:

- **[[aspire-robotics-skill-discovery]]** — NVIDIA GEAR Lab; continual learning for robotics via code-as-policy; three components (execution engine, skill library, evolutionary search); +77% LIBERO-Pro, 31% zero-shot vs 4%; sim-to-real transfer
- **[[memento-skills-agent-designing-agent]]** — agent-designing agent; skills as structured markdown files = persistent evolving memory; Read-Write Reflective Learning; continual learning without LLM parameter updates; +26.2% GAIA, +116.2% HLE; 27 citations
- **[[skillguard-permission-framework]]** — dual-plane governance (context + action); five components: manifests, runtime access control, user-mediated auth, deny-by-default, behavior monitoring; 315 skills; 99.76% taxonomy coverage; attack reduction 32%→23%
- **[[skillfortify-formal-verification-supply-chain]]** — first formal analysis framework for skill supply chains; 6 contributions: DY-Skill attacker model, sound static analysis, capability sandboxing, Agent Dependency Graph + lockfile, trust score algebra, 540-skill benchmark; 96.95% F1, 100% precision, 0% FP
- **[[skill1-unified-skill-evolution-rl]]** — single policy co-evolves skill selection, utilization, distillation; frequency decomposition credit assignment (low-freq = selection, high-freq = distillation); ALFWorld + WebShop; 18 citations
- **[[nvidia-verified-agent-skills-governance]]** — industry productionization of skill governance; verified = cataloged, scanned (SkillSpector), signed (cryptographic), documented (skill cards); built on agentskills.io; cross-platform SKILL.md
- **[[exif-automated-skill-discovery]]** — Alice-Bob dual-agent for skill discovery; exploration-first strategy; retrospective skill dataset from environment interaction; self-play enables self-evolution; precursor to 2026 wave; 11 citations

**Convergence signals:**
1. **Skill discovery now multi-domain** — ASPIRE (robotics), Memento-Skills (general agents), Skill1 (RL), EXIF (self-play). Discovery taxonomy spans domains and mechanisms.
2. **Dual-plane security governance** — SkillGuard recognizes skills operate across context + action planes. Combined with SkillFortify (formal supply chain) and NVIDIA-verified (publication), security covers: publication → supply chain → runtime → behavior.
3. **Formal verification arrives** — SkillFortify brings mathematical proofs (Dolev-Yao, abstract interpretation, capability confinement) to skills. First non-heuristic defense. Lockfile semantics adapt package management.
4. **Agent-designing agents** — Memento-Skills: agents autonomously construct and improve task-specific agents. Skills as markdown = sole adaptation mechanism (no LLM updates).
5. **Industry governance productionized** — NVIDIA-verified skills: catalog → scan → sign → document → distribute. Skill cards centralize trust metadata.
6. **Frequency decomposition for skill credit** — Skill1: single task-outcome signal decomposes into selection (low-freq) and distillation (high-freq). Novel unified governance.

## Iteration History (recent)

| Iteration | Date | Focus | New Examples |
|-----------|------|-------|--------------|
| **39** | **2026-07-14** | **Robotics skill discovery + agent-designing agents + permission governance + formal verification + unified RL evolution + industry governance + precursor discovery** | **ASPIRE, Memento-Skills, SkillGuard, SkillFortify, Skill1, NVIDIA-verified, EXIF** |
| **38** | **2026-07-13** | **Auto-discovery + trainable skills + provenance + cross-domain transfer + OS abstraction + generation benchmark** | **EvoSkill, SkillOpt, PROV-AGENT, SkillMigrator, Skill OS, SkillGenBench** |
| **37** | **2026-07-12** | **Skill optimization + composition + security + runtime + ontology** | **SkillMOO, EffiSkill, SkillSieve, SkillCraft, SkillReducer, ORCA, AI-KM, Marketplace Landscape** |
| **36** | **2026-07-11** | **Self-evolving skills + supply chain provenance + marketplace attack + academic surveys** | **CoEvoSkills, ClawHavoc, SLSA/in-toto factory, Awesome-Agent-Skill-Papers, SoK, 6-layer survey** |
| **35** | **2026-07-10** | **Workshop + marketplace analysis + domain/vendor mega-bundles** | **K-Dense scientific, Agentic Awesome, Vercel Labs, OpenMontage** |
| 31–34 | 2026-07-01…09 | Core standard + SHACL 1.2 agentInstruction + reference impl refresh | Monitoring sources (agentskills.io, addyosmani, anthropics, NVIDIA) |
| 14 | 2026-06-09 | Domain bioinformatics + process engineering + conference infra | ClawBio, Addy Osmani, Agents at Conferences, DSPy v0.2.3 |
| 13 | 2026-06-01 | Three-layer validation + SHACL bridge + ontology skills | ai4curation, skill-validator, ags, validate-skill, text2shacl |

## Tomorrow Priority Searches

1. **SkillClaw** — collective skill evolution framework (mentioned in Memento-Skills); multi-agent skill sharing
2. **SkillSpector** — NVIDIA's security scanning tool for agent skills; detection methods
3. **MalTool benchmark** — 6,487 malicious tools targeting LLM agents (arXiv, Wang et al.)
4. **Badskill** — backdoor attacks on agent skills via model-in-skill poisoning (arXiv:2604.09378)
5. **Skillject** — automating stealthy skill-based prompt injection for coding agents
6. **AgentBound** — declarative access-control for MCP servers (sandbox-based)
7. **SWE-Skills-Bench** — do agent skills help in real-world software engineering?
8. **Externalization in LLM Agents** — unified review of memory, skills, protocols, harness engineering (arXiv:2604.08224)
