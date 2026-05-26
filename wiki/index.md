# Skill Bundles Knowledge Base

**Last Updated:** 2026-05-26 (Iteration 11)
**Status:** Active research — 40 examples documented

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
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

## Current Status (After Iteration 11)

Eleven full research iterations completed. Iteration 11 marks a **qualitative shift** — the addition of formal security governance frameworks ([[owasp-agentic-skills-top-10]], [[agentic-trust-framework-csa]]) and a comprehensive academic survey ([[arxiv-agent-skills-survey]]) moves the catalog from empirical observation to formalized governance.

Three new categories emerge:
- **Security Governance Frameworks** — OWASP AST10 (10-class vulnerability taxonomy + Universal Skill Format), ATF (4-level Zero Trust maturity model), and the arXiv survey (26.1% vulnerability finding)
- **Enterprise Platform Implementations** — [[microsoft-agent-framework-skills]] (.NET/Python) and [[spring-ai-agent-skills]] (Java) signal enterprise readiness with DI support, script approval, and multi-source composition
- **Distribution & Marketplaces** — [[chris-ayers-plugin-ecosystem]] (Skills→Plugins→Marketplaces) and the Agensi marketplace landscape (8-marketplace comparison with consolidation trends)

**Key convergence:** The arXiv survey's composition patterns (single→pipeline→hierarchical→mesh→swarm) mirror the SC '25 paper's framework — confirming cross-domain convergence. Chris Ayers' cross-tool compatibility matrix proves SKILL.md works identically across 5 major tools.

See the [[skill-security-governance]] concept article for the complete governance stack synthesis.

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

## Tomorrow Priority Searches

1. OWASP AST10 AST01-AST06 detailed write-ups (due Q2 2026)
2. Actual marketplace consolidation events (acquisitions, shutdowns)
3. NVIDIA SkillSpector and OpenSSF signing implementation details
4. A2A (Agent-to-Agent) protocol specification and skill integration
5. Skill dependency resolution at scale (beyond Graph of Skills)
6. Snowflake Cortex Code and Databricks Genie Code skill implementations