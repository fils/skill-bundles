---
type: Concept
title: Skill Bundle Patterns
description: 'The strongest examples (NORA, agentskills.io) combine executable skills with rich declarative files:'
timestamp: '2026-05-24T00:00:00Z'
date: '2026-05-24'
---

# Skill Bundle Patterns

**Date:** 2026-05-24 (Updated Iteration 8)

## Observed Pattern: Skills + Declarative Context

The strongest examples (NORA, agentskills.io) combine executable skills with rich declarative files:

- `CLAUDE.md` / `REWATCH_PLAN.md`
- Skill manifests
- Launcher commands

This pattern appears more important than pure code for reusability.

## Pattern: Skills + SHACL Validation + Explainability

**New in Iteration 8.** The [xpshacl explainable shacl](../examples/xpshacl-explainable-shacl.md) and [shacl data quality 69 metrics](../examples/shacl-data-quality-69-metrics.md) examples demonstrate an emerging pattern: SHACL validation is paired with an explanation layer that converts technical validation results into natural language. The Violation KG caching mechanism (99.48% hit rate) shows that validation errors are highly repetitive — a signature-based cache makes explainable validation practical.

Key insight: **Validation alone is insufficient** for skill bundles. The explanation layer (RAG + LLM) and caching (Violation KG) are what make validation actionable.

## Pattern: SHACL + Cypher Rules + Shadow Testing

**New in Iteration 8.** [graphguard os guardrails](../examples/graphguard-os-guardrails.md) introduces a sophisticated guardrails pattern: SHACL shapes for structural constraints, Cypher policies for behavioral rules, and a Shadow Policy Manager for safe rule evolution. This addresses the "rules that almost work" problem by testing candidate policies against production traffic.

## Pattern: Distribution + Provenance Tracking

**New in Iteration 8.** `gh skill` (GitHub CLI) and OpenAI Codex both implement supply chain integrity for skills: immutable releases, content-addressed detection (git tree SHA), version pinning, and portable provenance in SKILL.md frontmatter. This represents the **maturation phase** of the skill ecosystem.

## Pattern: Taxonomy-Driven Skill Collections

**New in Iteration 8.** The Anthropic-Cybersecurity-Skills collection (754 skills mapped to MITRE/NIST frameworks) demonstrates a large-scale taxonomy-driven bundle. Formal frameworks (MITRE ATT&CK, NIST) provide hierarchical organization and standardized naming across hundreds of skills.

## Missing Elements (Gaps)

Current examples are light on:
- **Formal SSSOM skill implementations** — SSSOM is a specification, not yet paired with agent skills (addressed in part by adding [sssom mapping protocol](../examples/sssom-mapping-protocol.md))
- **Explicit rule layers** beyond authorization (partially addressed by GraphGuard OS Cypher policies)
- **Ontology/taxonomy integration** in non-security domains

## Context Element Coverage (Updated)

| Context Element | Examples | Trajectory |
| SHACL Validation | 6 | Strong (was 3) |
| Rules / Authorization | 5 | Strong (was 4) |
| Ontology / Taxonomy | 5 | Strong |
| Governance / Verification | 4 | Strong (was 3) |
| YAML Configuration | 8+ | Ubiquitous |
| MCP Dependencies | 3 | Emerging |
| SSSOM Mapping | 2 | Emerging (was 1) |
| Supply Chain / Provenance | 2 | Emerging |
