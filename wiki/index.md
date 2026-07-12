# Skill Bundles Knowledge Base

|**Last Updated:** 2026-07-12 (Iteration 37)
|**Status:** Active research — 8 new examples (SkillMOO multi-objective optimization, EffiSkill two-tier skills, SkillSieve malicious skill detection, SkillCraft composition benchmark, SkillReducer token efficiency, ORCA cognitive runtime, AI-KM ontology+skills, marketplace landscape)

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
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

## Current Status (Iteration 37 — 2026-07-12)

Eight major new skill-bundle examples covering skill optimization, composition, security, runtime, and ontology integration:

- **[[skillmoo-multi-objective-optimization]]** — first multi-objective skill bundle optimization; NSGA-II Pareto on pass rate + cost; pruning/substitution dominate edits; top rank on 11/12 SkillsBench tasks
- **[[effiskill-code-efficiency-optimization]]** — two-tier skill hierarchy (Operator + Meta Skills); execution-free diagnosis; +3.69–12.52pp improvement on EffiBench-X
- **[[skillsieve-malicious-skill-detection]]** — three-layer triage (heuristic→LLM→LLM jury); F1=0.920 at $0.006/skill; cross-ecosystem (ClawHub→Feishu); open-sourced
- **[[skillcraft-benchmark]]** — benchmark for skill composition/reuse; agents auto-compose tools into skills; 80% token savings; cited by 20
- **[[skillreducer-token-efficiency]]** — 55K skill empirical study: 26.4% lack routing, 60%+ non-actionable; delta debugging + progressive disclosure; 48%+39% compression, +2.8% quality (less-is-more)
- **[[orca-cognitive-runtime]]** — Open Runtime for Capable Agents; 122 capabilities + 36 DAG skills + policy gates + provenance; 184/184 taxonomy coverage; MCP support
- **[[ai-km-ontology-skills]]** — skills + ontology-driven knowledge modeling in closed loop; NL extraction builds ontologies; conversation-invokable + autonomous planning
- **[[marketplace-landscape-2026]]** — 8 major marketplaces compared; SkillsMP 800K+, LobeHub 169K+; 6.3 issues/skill, 36% prompt injection; MCP access rising

**Convergence signals:**
1. **Skill optimization triad** — SkillMOO (search), CoEvoSkills (evolution), SkillReducer (content reduction) address different axes; could compose
2. **Less-is-more effect** — removing non-essential content *improves* quality (+2.8%); progressive disclosure is the architectural pattern
3. **Skill composition as core capability** — SkillCraft validates composition strongly correlates with success; 80% token savings from caching
4. **Hierarchical security validation** — SkillSieve's LLM jury (3-LLM voting + debate) is production-ready at $0.006/skill
5. **Skills + ontologies integrated** — AI-KM closes the knowledge→skill→knowledge loop
6. **Marketplace consolidation** — 8 → 3-4 within a year; security scanning + creator payments becoming table stakes

## Iteration History (recent)

| Iteration | Date | Focus | New Examples |
|-----------|------|-------|--------------|
| **37** | **2026-07-12** | **Skill optimization + composition + security + runtime + ontology** | **SkillMOO, EffiSkill, SkillSieve, SkillCraft, SkillReducer, ORCA, AI-KM, Marketplace Landscape** |
| **36** | **2026-07-11** | **Self-evolving skills + supply chain provenance + marketplace attack + academic surveys** | **CoEvoSkills, ClawHavoc, SLSA/in-toto factory, Awesome-Agent-Skill-Papers, SoK, 6-layer survey** |
| **35** | **2026-07-10** | **Workshop + marketplace analysis + domain/vendor mega-bundles** | **K-Dense scientific, Agentic Awesome, Vercel Labs, OpenMontage** |
| 31–34 | 2026-07-01…09 | Core standard + SHACL 1.2 agentInstruction + reference impl refresh | Monitoring sources (agentskills.io, addyosmani, anthropics, NVIDIA) |
| 14 | 2026-06-09 | Domain bioinformatics + process engineering + conference infra | ClawBio, Addy Osmani, Agents at Conferences, DSPy v0.2.3 |
| 13 | 2026-06-01 | Three-layer validation + SHACL bridge + ontology skills | ai4curation, skill-validator, ags, validate-skill, text2shacl |

## Tomorrow Priority Searches

1. **SkillVerifier / SkillGuard** — runtime verification frameworks for skill execution safety
2. **Skill transfer learning** — cross-domain skill reuse patterns (SE → data analysis?)
3. **Auto-skill discovery** — agents autonomously discovering new skills from task patterns
4. **SkillsBench v2** — latest developments beyond v1.1 (87 tasks, 24 configs)
5. **Skill provenance standards** — W3C or other standards bodies working on skill provenance
6. **OpenClaw / ClawHub ecosystem** — latest governance changes post-ClawHavoc
