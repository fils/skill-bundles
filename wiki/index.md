# Skill Bundles Knowledge Base

|**Last Updated:** 2026-07-15 (Iteration 40)|
|**Status:** Active research — 8 new examples (SkillClaw collective evolution, SkillSpector security scanner, MalTool malicious tools, BadSkill model-in-skill backdoor, SkillJect automated prompt injection, AgentBound MCP access control, SWE-Skills-Bench utility benchmark, Externalization unified review)|

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
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

## Current Status (Iteration 40 — 2026-07-15)

Eight major new skill-bundle examples covering collective skill evolution, security scanning, malicious tool attacks, model-in-skill backdoors, automated prompt injection, MCP access control, skill utility benchmarking, and theoretical foundations:

- **[[skillclaw-collective-skill-evolution]]** — Collective skill evolution in multi-user agent ecosystems; cross-user + over-time trajectory aggregation; autonomous evolver (pattern recognition → skill update); shared synchronized repository; supports OpenClaw + Hermes; WildClawBench + Qwen3-Max; 42 citations; GitHub: AMAP-ML/SkillClaw (2.1k★)
- **[[skillspector-nvidia-security-scanner]]** — NVIDIA's security scanner for AI agent skills; YARA rules + LLM semantic analysis; OWASP/MITRE alignment; batch scanning; CI/CD integration; 1312 unit tests; v2.3.13; 13.2k★; scanning step of NVIDIA-Verified ecosystem
- **[[maltool-malicious-tool-attacks]]** — First systematic study of malicious tool code implementations; CIA triad taxonomy; coding-LLM-based synthesis (standalone + embedded); automated verifier; 1,300 standalone + 5,727 embedded malicious tools; existing detection insufficient; UC Berkeley (Dawn Song) + Duke (Neil Gong); 10 citations
- **[[badskill-backdoor-model-in-skill]]** — Backdoor attacks via model-in-skill poisoning; semantic compositional triggers; composite training objective; 99.5% ASR; 3% poison rate → 91.7% ASR; 8 architectures (494M–7.1B), 5 model families; 12 citations
- **[[skillject-automated-prompt-injection]]** — First automated framework for poisoned skills; two-channel attack (artifact: helper script + instruction: front-loaded SKILL.md); closed-loop multi-agent (Attack→Victim→Evaluate→refine); supports Claude Code + OpenClaw; authors include Philip Torr (Oxford); 7 citations
- **[[agentbound-mcp-access-control]]** — First access control framework for MCP servers; Android permission model inspired; declarative policy + enforcement engine; 296 most popular MCP servers; 80.9% automated policy generation; negligible overhead; ACM FSE 2026
- **[[swe-skills-bench-utility-benchmark]]** — First requirement-driven benchmark isolating marginal utility of agent skills in SWE; 49 skills × GitHub repos × requirement docs; ~565 task instances; 39/49 skills yield zero improvement; avg gain +1.2%; token overhead up to +451%; only 7 help (up to +30%), 3 degrade (up to -10%); 34 citations
- **[[externalization-llm-agents-unified-review]]** — Unified review of memory, skills, protocols, harness engineering; cognitive artifacts lens; four-form taxonomy; weights→context→harness progression; parametric/externalized trade-off; self-evolving harnesses + shared infrastructure; 54 pages; 21 authors including Jun Wang (UCL), Weinan Zhang (SJTU); 35 citations

**Convergence signals:**
1. **Complete attack taxonomy now spans four threat surfaces** — MalTool (code), BadSkill (model weights), SkillJect (SKILL.md instructions), ClawHavoc (marketplace distribution). Each requires a different defense layer.
2. **Defense stack achieves full lifecycle coverage** — SkillSpector (pre-installation) + SkillFortify (supply chain) + SkillGuard (runtime) + AgentBound (MCP) now cover: pre-installation → supply chain → runtime → infrastructure. Gap: model-in-skill verification.
3. **MCP as critical infrastructure layer** — AgentBound recognizes MCP as the connective tissue requiring its own security model (296 servers, unrestricted access). Extends skill security beyond skills to the protocol layer.
4. **Empirical reality check on skill utility** — SWE-Skills-Bench: 80% of skills yield zero improvement. Combined with SkillReducer's less-is-more effect, the field needs rigorous evaluation, not just adoption enthusiasm.
5. **Theoretical foundation arrives** — Externalization framework: skills = externalized procedural expertise, one of four coupled forms. Weights→context→harness progression explains the field's evolution. Self-evolving + shared infrastructure are the frontier.
6. **Collective evolution as paradigm shift** — SkillClaw: multi-user skill evolution transforms skills from static artifacts to living, self-improving infrastructure. Connects to Externalization paper's emerging directions.

## Iteration History (recent)

| Iteration | Date | Focus | New Examples |
|-----------|------|-------|--------------|
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

1. **WildClawBench** — SkillClaw's benchmark for real-world agent scenarios; methodology and task design
2. **Skill provenance for model artifacts** — How to verify model weights embedded in skills (motivated by BadSkill)
3. **MCP server security landscape** — Beyond AgentBound: what other MCP security frameworks exist?
4. **Skill utility in non-SWE domains** — SWE-Skills-Bench showed 80% zero improvement in SWE; is this domain-specific?
5. **Skill versioning and compatibility** — SWE-Skills-Bench's version-mismatch finding; how should skills declare version compatibility?
6. **Cognitive artifacts in agent design** — Further theoretical work on the externalization framework
7. **Automated policy generation** — AgentBound's 80.9% accuracy; can this be improved?
8. **MalTool defense gap** — MalTool shows existing detection insufficient; what new approaches are needed?
