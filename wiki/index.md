# Skill Bundles Knowledge Base

|**Last Updated:** 2026-07-11 (Iteration 36)
|**Status:** Active research — 4 new examples (CoEvoSkills self-evolving, ClawHavoc attack, SLSA/in-toto provenance, paper catalog) + 2 new papers (SoK Agentic Skills, Procedural Infrastructure survey); GoS v3 + SkillsBench v1.1 updates

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
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

## Current Status (Iteration 36 — 2026-07-11)

Four major new skill-bundle examples plus two foundational survey papers and two benchmark updates:

- **[[coevoskills-self-evolving-skills]]** — first self-evolving multi-file skill package framework; co-evolutionary verification; surpasses human-curated skills in 5 iterations (arXiv:2604.01687)
- **[[clawhavoc-marketplace-attack]]** — ~1,184 malicious skills on ClawHub; 13% malicious rate; canonical supply-chain attack case study
- **[[supply-chain-agentic-factory-in-toto]]** — SLSA/in-toto provenance extended to agentic code generation; "intent → source → binary" trust gap; Konflux/fullsend project
- **[[awesome-agent-skill-papers-catalog]]** — curated paper catalog; discovery index for academic agent skill research
- **[[sok-agentic-skills-beyond-tool-use]]** — formal skill definition S=(C,π,T,R); 7-stage lifecycle; 7 design patterns; 73 citations (arXiv:2602.20867)
- **[[survey-agent-skills-procedural-infrastructure]]** — six-layer taxonomy; marketplace scale data (800K+ skills); Awesome-Agent-Skill-Papers catalog
- Updated: [[graph-of-skills-dependency-retrieval]] (v3: +25.55% reward, -56.72% tokens), [[skillsbench-agent-skills-benchmark]] (v1.1: 87 tasks, 24-config leaderboard)

**Convergence signals:**
1. **Academic convergence on skill formalization** — three surveys (SoK, 4-axis, 6-layer) all define skills as multi-file packages ≠ tools; lifecycle models needed; security critical
2. **Marketplace risk quantified** — ClawHavoc 13% + SoK 26.1% + workshop 37% ≈ 1 in 4–8 marketplace skills malicious/vulnerable
3. **Co-evolutionary verification** — dynamic verifier co-evolves with generator (generalizes static validation)
4. **SLSA/in-toto for skills** — supply chain provenance extended to "intent → source" gap
5. **Dependency-aware retrieval validated** — GoS v3 concrete benchmark evidence (+25.55% quality, -56.72% efficiency)

## Iteration History (recent)

| Iteration | Date | Focus | New Examples |
|-----------|------|-------|--------------|
| **36** | **2026-07-11** | **Self-evolving skills + supply chain provenance + marketplace attack + academic surveys** | **CoEvoSkills, ClawHavoc, SLSA/in-toto factory, Awesome-Agent-Skill-Papers, SoK, 6-layer survey** |
| **35** | **2026-07-10** | **Workshop + marketplace analysis + domain/vendor mega-bundles** | **K-Dense scientific, Agentic Awesome, Vercel Labs, OpenMontage** |
| 31–34 | 2026-07-01…09 | Core standard + SHACL 1.2 agentInstruction + reference impl refresh | Monitoring sources (agentskills.io, addyosmani, anthropics, NVIDIA) |
| 14 | 2026-06-09 | Domain bioinformatics + process engineering + conference infra | ClawBio, Addy Osmani, Agents at Conferences, DSPy v0.2.3 |
| 13 | 2026-06-01 | Three-layer validation + SHACL bridge + ontology skills | ai4curation, skill-validator, ags, validate-skill, text2shacl |

## Tomorrow Priority Searches

1. **Atomic Skills** (arXiv:2604.05013) — Scaling Coding Agents via Atomic Skills decomposition pattern
2. **SkillMOO** (arXiv:2604.09297) — Multi-Objective Optimization for SE skills
3. **EffiSkill** (arXiv:2603.27850) — Agent Skill Based Code Efficiency Optimization
4. **arXiv:2604.06550** — Hierarchical Triage Framework for detecting malicious skills (ClawHavoc-validated)
5. **SkillsMP / LobeHub marketplace** — largest skill marketplaces (425K / 170K skills) — governance models
6. **SkillCraft** — Can LLM agents learn to use tools skillfully? (cited by CoEvoSkills)
