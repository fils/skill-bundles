# Skill Bundles Knowledge Base

**Last Updated:** 2026-05-24 (Iteration 9)
**Status:** Active research — 28 examples documented

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
- [2026-05-24 (Iteration 9)](daily-digests/2026-05-24-iter9.md)
  - [2026-05-24 (Iteration 8)](daily-digests/2026-05-24.md)
  - [2026-05-23 (Iteration 7)](daily-digests/2026-05-23-iter7-manual.md)
  - [2026-05-23 (Iteration 6)](daily-digests/2026-05-23-iter6.md)
- [Documented Examples](examples/)
- [Concepts](concepts/)
- [Metrics](metrics.md)

## Current Status (After Iteration 8)

Eight full research iterations completed. Major expansion in **SHACL validation** (3 → 6 examples), **supply chain/provenance** (new category), and **explainable validation** patterns. The [[xpshacl-explainable-shacl]] paper's Violation KG caching mechanism (99.48% hit rate) is a breakthrough pattern for making SHACL validation practical. [[graphguard-os-guardrails]] provides an enterprise-ready guardrail pattern.

SSSOM mapping coverage at 2 (spec + algorithm). [[claude-skills-ecosystem-1116]] revealed 754 MITRE/NIST-mapped cybersecurity skills — largest taxonomy-driven bundle.

## Iteration History

| Iteration | Date | Focus | New Examples |
| 1 | — | Bootstrap | Initial seed |
| 2 | — | Expansion | NORA, Agent Skills Spec |
| 3 | — | Deep dive | Ontologizer, OpenClaw PKB |
| 4 | — | Rules & validation | Veto, Tool-Use Firewall, Schimatos |
| 5 | — | Synthesis | Research state document |
| **6** | **2026-05-23** | **Governance & platforms** | **NVIDIA Verified, NVIDIA Repo, Codex, VS Code, RDF Ontologies** |
| **7** | **2026-05-23** | **SSSOM/Mapping seed** | **Open Ontologies (paper + GitHub) — ontology alignment, stable matching, MCP tools** |
| **8** | **2026-05-24** | **SHACL deep + supply chain + ecosystem** | **GraphGuard OS, xpSHACL, gh skill, SHACL DQ, SSSOM Protocol, Claude Ecosystem** |
| **9** | **2026-05-24** | **DSPy + Security + Benchmarking + Constraint Rules** | **DSPy Agent Skills, Superpowers, Mondoo Security, Graph of Skills, SkillsBench, Anthropic Official** |

## Tomorrow Priority Searches

1. "SSSOM agent skills" OR "SSSOM mapping tool" MCP implementation
2. "MITRE ATT&CK agent skills" OR "NIST cybersecurity skills" bundle details
3. SHACL + rules engine for non-semantic domains
4. Skill provenance tracking systems beyond GitHub CLI
5. Ontology alignment tools beyond Open Ontologies (e.g., LogMap, AgreementMaker)
