# Skill Bundles Knowledge Base

|**Last Updated:** 2026-07-01 (Iteration 31)
|**Status:** Active research — 50+ examples documented (raw ingestion + SHACL 1.2 agent primitives + core standard focus)

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
  - [2026-06-30 (Iteration 30)](daily-digests/2026-06-30.md)
  - [2026-06-29 (Iteration 15)](daily-digests/2026-06-09.md)
  - [2026-06-05 (Iteration 14)](daily-digests/2026-06-05.md)
  - [2026-06-04 (Iteration 14)](daily-digests/2026-06-04.md)
  - [2026-06-01 (Iteration 13)](daily-digests/2026-06-01.md)
  - [2026-05-28 (Iteration 12)](daily-digests/2026-05-28.md)
  - [2026-05-26 (Iteration 11)](daily-digests/2026-05-26.md)
  - [2026-05-25 (Iteration 10)](daily-digests/2026-05-25.md)
  - [2026-05-24 (Iteration 9)](daily-digests/2026-05-24-iter9.md)
  - [2026-05-24 (Iteration 8)](daily-digests/2026-05-24.md)
  - [2026-05-23 (Iteration 7)](daily-digests/2026-05-23-iter7-manual.md)
  - [2026-05-23 (Iteration 6)](daily-digests/2026-05-23-iter6.md)
- [Documented Examples](examples/)
- [Concepts](concepts/)
- [Metrics](metrics.md)
- [Q&A](qa/)

## Current Status (After Iteration 14)

Fourteen full research iterations completed. Iteration 14 adds **four major new skill bundles** and two foundational papers:

- **[[clawbio-bioinformatics-skills]]** — Bioinformatics-native library: 88 skills (29 production), 8,000+ Galaxy tools, reproducibility bundles, Corpasome reference genome, 92.3% validation pass rate
- **[[addyosmani-engineering-skills]]** — 23 production-grade engineering workflow skills across full SDLC, 3 specialist personas, 7 slash commands, Iron Laws/Red Flags constraint rules, Google engineering culture
- **[[agents-at-conferences-infrastructure]]** — Infrastructure for AI agent conference participation: 6-component protocol (registration, feeds, communication, moderation, benchmarking, memory), capability schema taxonomy, SciFM26 target: 50 agents
- **[[dspy-agent-skills-bundle]]** (Updated v0.2.3) — Exact DSPy 3.2.1 pinning, 34+ validators, GEPA gotchas documented, committed performance benchmarks (+19.53pp RAG), offline validation
- **Seeded Papers** — SC25 "Revolution of Scientific Workflows" (Intelligence×Composition matrix) and "Beginning of scAInce" (co-pilot→lab-pilot, SDLs as skill bundles)

**Convergence signals strengthened:**
1. **Domain specialization is maturing** — ClawBio shows 88 skills cohering around genomics with formal specs, reproducibility, reference data
2. **Process-as-skill bundles are emerging** — Addy Osmani encodes full SDLC with anti-rationalization, verification gates, personas
3. **Infrastructure-as-skills** — Agents at Conferences defines 6 core components as agent capabilities
4. **Framework-specific bundles deepen** — DSPy v0.2.3 adds exact pinning, 34+ validators, benchmark artifacts

Six new examples added in Iteration 13 (46 total):
- **[[ai4curation-curation-skills]]** — Chris Mungall's ontology/biocuration bundle (7 skills: OAK, ROBOT, DOSDP, OBO editing). Production users: Mondo, Cell Ontology, Uberon, EFO
- **[[skill-validator-cli]]** — Go CLI validator with LLM-as-judge, 13 platform pre-commit hooks (151 stars)
- **[[agentskill-sh-ags-security-scoring]]** — Registry with 12-category threat taxonomy, 100k+ skills scanned
- **[[validate-skill-github-action]]** — CI/CD layer of the validation stack
- **[[text2shacl-multi-agent-shacl]]** — Multi-agent LangGraph SHACL generation from text (forward direction of the bridge)
- **[[genesis-skills-osti]]** — OSTI Genesis lab-scale bundle: 74 skills across HPC, plasma, scientific computing + Superpowers re-packaging

**Convergence signal:** Three independent projects (skill-validator, validate-skill, ags) emerged to fill the three validation layers in 2026 — strong evidence the pattern is now stable.

## Iteration History

| Iteration | Date | Focus | New Examples |
|-----------|------|-------|-------------|
| 1 | — | Bootstrap | Initial seed |
| 2 | — | Expansion | NORA, Agent Skills Spec |
| 3 | — | Deep dive | Ontologizer, OpenClaw PKB |
| 4 | — | Rules & validation | Veto, Tool-Use Firewall, Schimatos |
| 5 | — | Synthesis | Research state document |
| **6** | **2026-05-23** | **Governance & platforms** | **NVIDIA Verified, NVIDIA Repo, Codex, VS Code, RDF Ontologies** |
| **7** | **2026-05-23** | **SSSOM/Mapping seed** | **Open Ontologies (paper + GitHub)** |
| **8** | **2026-05-24** | **SHACL deep + supply chain + ecosystem** | **GraphGuard OS, xpSHACL, gh skill, SHACL DQ, SSSOM Protocol, Claude Ecosystem** |
| **9** | **2026-05-24** | **DSPy + Security + Benchmarking + Constraint Rules** | **DSPy Agent Skills, Superpowers, Mondoo Security, Graph of Skills, SkillsBench, Anthropic Official** |
| **10** | **2026-05-25** | **SSSOM lifecycle + Supply chain risk + CLI catalogs** | **OxO2, DSPy v0.2.3, PurpleBox, Onto-LLM-Mapping, Awesome OpenClaw, Ylang Labs** |
| **11** | **2026-05-26** | **Security governance + Enterprise platforms + Distribution** | **OWASP AST10, ATF, arXiv Survey, Microsoft, Spring AI, Chris Ayers Plugins** |
| **12** | **2026-05-28** | **Agent Skills ecosystem** | **agentskills.io overview** (raw only, integration pending) |
| **13** | **2026-06-01** | **Three-layer validation + SHACL bridge + ontology skills** | **ai4curation, skill-validator CLI, agentskill.sh ags, validate-skill Action, text2shacl** |
| **14** | **2026-06-09** | **Domain bioinformatics + Process engineering + Conference infra + DSPy deepening** | **ClawBio, Addy Osmani, Agents at Conferences, DSPy v0.2.3 update** |

## Tomorrow Priority Searches

1. SLSA / in-toto attestation for skill bundles (provenance chain across validation layers)
2. Bundle-level interaction effects (2+ skills installed together — privilege accumulation, version skew)
3. A2A (Agent-to-Agent) protocol skill integration (carried from last week)
4. SHACL round-trip evaluation studies (empirical text → shapes → text fidelity)
5. ai-blame deep-dive (Mungall's line-level attribution for AI-assisted ontology edits)
6. Monorepo SKILL.md / Claude Plugin Marketplace consolidation events
7. Self-driving lab skill bundles (ChemCrow, autonomous synthesis → skill decomposition)
8. Bioinformatics skill taxonomy (ClawBio categories → formal ontology)

|| **31** | **2026-07-01** | **Core Agent Skills standard + major reference implementations + SHACL 1.2 agent primitives** | **agentskills.io, addyosmani/agent-skills (68k), anthropics/skills (157k), SHACL 1.2 Core** |
