# Skill Bundles Knowledge Base

|**Last Updated:** 2026-07-24 (Iteration 42)|
|**Status:** Active research — 7 new examples (SkillOps library maintenance, SkillRouter body-aware 80K routing, AgentSkillOS tree+DAG, SkillC contrastive internalization, Skill0.5 hybrid, SLIM lifecycle, SkillCorpus 821K→96K)|

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
  - [2026-07-24 (Iteration 42)](daily-digests/2026-07-24.md)
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
  - [Complex Q&A — 2026-06-01 (Iteration 13)](qa/2026-06-01-iter13-qa.md)
  - [Q&A and Gap Analysis — 2026-05-24 Iteration 9](qa/2026-05-24-iter9-qa.md)
  - [Complex Q&A — Skill Bundles Wiki](qa/2026-05-24-complex-qa.md)

  - [Q&A — 2026-07-24 (Iteration 42)](qa/2026-07-24-qa.md)
  - [Q&A — 2026-07-16 (Iteration 41)](qa/2026-07-16-qa.md)
  - [Q&A — 2026-07-15 (Iteration 40)](qa/2026-07-15-qa.md)
  - [Q&A — 2026-07-14 (Iteration 39)](qa/2026-07-14-qa.md)
  - [Q&A — 2026-07-13 (Skill Bundles, Iteration 38)](qa/2026-07-13-qa.md)
  - [Q&A — 2026-07-12 (Iteration 37)](qa/2026-07-12-qa.md)
  - [Q&A — 2026-07-11 (Iteration 36)](qa/2026-07-11-qa.md)
  - [Q&A — 2026-07-10](qa/2026-07-10-qa.md)
  - [Q&A / Lint 2026-07-06](qa/2026-07-06-lint.md)


## Knowledge Catalog (OKF)

This directory is an [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) Knowledge Bundle.

**Format rules (read first for agents):** [OKF Knowledge Bundle — Format Rules](concepts/okf-knowledge-bundle.md)

- Required: YAML frontmatter with `type` on every concept document
- Cross-links: **relative markdown only** (OKF §5.2) — works on GitHub; never `[[wikilinks]]`
- Conformance: `python3 scripts/okf-lint.py`
- Workflow contract (outside bundle): repo-root `PLAN.md` — research loop may be Karpathy-inspired; **document format is OKF**

# Bundle sections

* [Skill Bundle Examples](examples/) - Documented real-world skill bundle case studies
* [Concepts](concepts/) - Atomic notes on patterns, composition, and governance
* [OKF format rules](concepts/okf-knowledge-bundle.md) - Local OKF v0.1 summary for this bundle
* [Papers](papers/) - Summarized papers and workshop notes
* [Tools](tools/) - Frameworks, marketplaces, and tooling landscape
* [Daily Digests](daily-digests/) - Chronological research digests
* [Q&A](qa/) - Structured exploration and gap analysis
* [Primary Publication](skill-bundles.md) - Living catalog of examples and patterns
* [Metrics](metrics.md) - KPIs and coverage tracking
* [Update Log](log.md) - Chronological change history

## Current Status (Iteration 42 — 2026-07-24)

Catch-up after 8-day research gap (prior commits were Phase 6/Pages). Seven examples spanning library ops, scale routing/orchestration, and the internalization design space:

- **[skillops self maintaining skill libraries](examples/skillops-self-maintaining-skill-libraries.md)** — Skill technical debt; Contract (P,O,A,V,F) + HSEG; ALFWorld 79.5% (+8.8pp); plug-in gains; ~0 library-time LLM (arXiv:2605.13716)
- **[skillrouter body aware routing](examples/skillrouter-body-aware-routing.md)** — Body hide −37–44pp @~80K; 1.2B Hit@1 74.0%; e2e coding-agent transfer (arXiv:2603.22455 v5)
- **[agentskillos capability tree dag](examples/agentskillos-capability-tree-dag.md)** — Capability tree + DAG @200K; DAG > flat even with oracle skills (arXiv:2603.02176)
- **[skillc contrastive internalization](examples/skillc-contrastive-internalization.md)** — CSCA dual-stream advantages; +5.5% / +4.4% vs prior internalization (arXiv:2605.27899)
- **[skill05 joint internalization utilization](examples/skill05-joint-internalization-utilization.md)** — General-internalize + task-utilize mastery tiers (arXiv:2605.28424)
- **[slim dynamic skill lifecycle](examples/slim-dynamic-skill-lifecycle.md)** — Retain–retire–expand; +7.1pp; non-empty compact boundary (arXiv:2605.10923)
- **[skillcorpus open ecosystem curation](examples/skillcorpus-open-ecosystem-curation.md)** — 821K→96K curated corpus; +7.5pp SkillsBench; coverage+harness boundaries (arXiv:2607.15557 v4)

**Convergence signals:**
1. **Full stack emerges** — library maintain (SkillOps) · route (SkillRouter/R3) · orchestrate (AgentSkillOS) · train boundary (SLIM/SkillC/Skill0.5) · curate corpus (SkillCorpus).
2. **Body-aware routing + set-compatibility** jointly required at marketplace scale.
3. **Orchestration is not retrieval** — DAG composition is a separate unlock.
4. **Internalization is a spectrum**, not a boolean — general vs task-specific endpoints differ.
5. **Curation bounds open-ecosystem value** — raw crawl mass under-delivers without facets and harness fit.

## Iteration History (recent)

| Iteration | Date | Focus | New Examples |
|-----------|------|-------|--------------|
| **42** | **2026-07-24** | **Library ops + body-aware 80K routing + tree/DAG orchestration + internalization spectrum + open corpus curation** | **SkillOps, SkillRouter, AgentSkillOS, SkillC, Skill0.5, SLIM, SkillCorpus** |
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

1. **Anthropic-Cybersecurity-Skills** (mukul975, ~26k★) — 817 skills × 6 security frameworks
2. **SkillBOM / SDA tooling releases** — open-source SkillDepAnalyzer or SkillBOM exporters
3. **skillflag** — package-embedded skill distribution without registries
4. **HASP / SIRI / UCOB** — internalization variants beyond SkillC/SLIM/Skill0.5
5. **OWASP AST10** v1 publication + scanner integration refresh
6. **SkillCorpus** code/data release tracking
7. **ToxicSkills remediation** — automated quarantine beyond scanning
8. **Hermes multi-harness skill governance** — WildClawBench implications
