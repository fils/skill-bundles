# Skill Bundles Knowledge Base

|**Last Updated:** 2026-06-04 (Iteration 14)
|**Status:** Active research — 50 examples documented (est.)

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
  - [2026-06-04 (Iteration 14)
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

## Current Status (After Iteration 13)

Thirteen full research iterations completed. Iteration 13 establishes **two new architectural patterns**:

- **[[three-layer-validation-stack|Three-Layer Validation Stack]]** — Convergence on pre-commit (skill-validator CLI) → CI/CD (Validate Skill GitHub Action) → Registry (agentskill.sh 12-category threat scanner) pattern. Mirrors the mature software supply chain three-layer model.
- **[[bidirectional-shacl-llm-bridge|Bidirectional SHACL↔LLM Bridge]]** — Forward (text2shacl multi-agent SHACL generation) + Reverse (xpSHACL natural-language explanation) complete the loop: requirements → shapes → validation → explanation → refined requirements.

Six new examples added (46 total):
- **[[ai4curation-curation-skills]]** — Chris Mungall's ontology/biocuration bundle (7 skills, production users: Mondo, CL, Uberon, EFO)
- **[[skill-validator-cli]]** — Go CLI validator with LLM-as-judge, 13 platform pre-commit hooks (151 stars)
- **[[agentskill-sh-ags-security-scoring]]** — Registry with 12-category threat taxonomy, 100k+ skills scanned
- **[[validate-skill-github-action]]** — CI/CD layer of the validation stack
- **[[text2shacl-multi-agent-shacl]]** — Multi-agent LangGraph SHACL generation from text (forward direction of the bridge)
- **[[genesis-skills-osti]]** — OSTI Genesis lab-scale bundle: 74 skills across HPC, plasma, scientific computing + Superpowers re-packaging (NEW)

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

## Tomorrow Priority Searches

1. SLSA / in-toto attestation for skill bundles (provenance chain across validation layers)
2. Bundle-level interaction effects (2+ skills installed together — privilege accumulation, version skew)
3. A2A (Agent-to-Agent) protocol skill integration (carried from last week)
4. SHACL round-trip evaluation studies (empirical text → shapes → text fidelity)
5. ai-blame deep-dive (Mungall's line-level attribution for AI-assisted ontology edits)
6. Monorepo SKILL.md / Claude Plugin Marketplace consolidation events
