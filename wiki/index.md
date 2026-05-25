# Skill Bundles Knowledge Base

**Last Updated:** 2026-05-25 (Iteration 10)
**Status:** Active research — 34 examples documented

## Overview

This wiki catalogs real-world examples of **skill bundles** — collections of agent skills packaged together with supporting context elements such as validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

## Quick Links

- [Main Publication](skill-bundles.md)
- [Daily Digests](daily-digests/)
  - [2026-05-25 (Iteration 10)](daily-digests/2026-05-25.md)
  - [2026-05-24 (Iteration 9)](daily-digests/2026-05-24-iter9.md)
  - [2026-05-24 (Iteration 8)](daily-digests/2026-05-24.md)
  - [2026-05-23 (Iteration 7)](daily-digests/2026-05-23-iter7-manual.md)
  - [2026-05-23 (Iteration 6)](daily-digests/2026-05-23-iter6.md)
- [Documented Examples](examples/)
- [Concepts](concepts/)
- [Metrics](metrics.md)
- [Q&A](qa/)

## Current Status (After Iteration 10)

Ten full research iterations completed. Major expansion in **SSSOM mapping** (2 → 4 examples — lifecycle complete: spec → generate → serve → align), **security taxonomy** (3 → 5 including PurpleBox attack→defense mapping), and **agent context documentation** (new category: CLAUDE.md + CONTEXT.md + ADR patterns).

The [[sssom-mapping-as-context]] concept article documents SSSOM as a first-class context element with a complete lifecycle. [[oxo2-sssom-mapping-service]] and [[onto-llm-mapping]] are the headline additions — production mapping service and LLM-powered generation pipeline.

Three new patterns identified: **Implicit Bundle Discovery** (grouping related skills across taxonomy catalogs), **Attack → Defense Mapping** (PurpleBox vectors map to catalog defenses), and **Agent Context as Documentation** (CLAUDE.md + CONTEXT.md + ADR as living context).

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

## Tomorrow Priority Searches

1. Agent skills marketplace implementation details (skillsmp.com, agensi.io)
2. SSSOM + MCP server integration patterns
3. OpenClaw skill metadata specification (formal context elements)
4. Skill versioning and dependency resolution (beyond GoS)
5. Agent security certification frameworks (post-ClawHavoc)