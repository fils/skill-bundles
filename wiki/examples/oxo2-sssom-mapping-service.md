---
type: Skill Bundle Example
title: OxO2 — SSSOM-Compliant Ontology Mapping Service
description: OxO2 is a production SSSOM-compliant ontology mapping service from EMBL-EBI's EBISPOT team.
resource: https://github.com/EBISPOT/oxo2/blob/dev/CLAUDE.md
timestamp: '2026-05-25T00:00:00Z'
date: 2026-05-25
sources:
- https://github.com/EBISPOT/oxo2/blob/dev/CLAUDE.md
- https://github.com/EBISPOT/oxo2
skills:
- CLAUDE.md agent context instructions
- ADR-driven architectural decisions
context_elements:
- SSSOM mapping compliance
- CONTEXT.md per-module documentation
- CLAUDE.md root-level agent context
- Architectural Decision Records (docs/adr/)
- REST API for SSSOM mapping queries
- Nextflow data load pipeline
composition_notes: 'OxO2 demonstrates the formal context artifact pattern applied to a production bioinformatics service.

  The CLAUDE.md + CONTEXT.md + ADR stack provides structured, multi-level context for AI assistants

  working on the codebase. The SSSOM compliance layer provides ontology mapping standardization

  that agents can query programmatically.

  '
reproducibility: High — full source available on GitHub, Docker Compose setup documented
confidence: 9/10
---

# OxO2: SSSOM-Compliant Ontology Mapping Service

## Overview

OxO2 is a production SSSOM-compliant ontology mapping service from EMBL-EBI's EBISPOT team. It downloads SSSOM mappings, converts them to JSON, and serves them via REST API for ontology term alignment and cross-referencing.

## Context Artifacts

### CLAUDE.md Agent Context
The project includes a `CLAUDE.md` file at the repository root — a structured instruction document specifically designed for AI coding assistants. This is a concrete example of **agent context as formal documentation**.

The pattern includes:
- `CLAUDE.md` (root) — canonical project overview, build commands, environment setup
- `CONTEXT.md` per module — specific module details
- `docs/adr/` — Architectural Decision Records
- `README.md` — operational instructions

### SSSOM Compliance
OxO2 implements the [sssom mapping protocol](sssom-mapping-protocol.md) standard:
- Downloads SSSOM-format mappings
- Converts to JSON for REST API serving
- Integrates with OLS (Ontology Lookup Service) and O×O (Ontology Xref Ontology)
- Uses Nemo v0.9.1 inference engine for rules and explanations

## Architecture
| Layer | Technology |
|---|---|
| Backend | Java 25, Maven, Spring Boot 3.4.1 |
| Frontend | React 19, TypeScript, Vite, Tailwind CSS |
| Data Store | Apache Solr 9.9.0 |
| Inference | Nemo v0.9.1 |
| Pipeline | Nextflow |
| CI/CD | GitHub Actions → ghcr.io |
| Orchestration | Kubernetes (Helm), SLURM (HPC) |

## Issue Management
Uses `gh` CLI with triage labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix` — another example of formal workflow context.

## Composition Pattern
This project is the **third SSSOM implementation** in our catalog (after [sssom mapping protocol](sssom-mapping-protocol.md) spec and [onto llm mapping](onto-llm-mapping.md) mapping generator), but the **first to combine SSSOM with agent context documentation** (CLAUDE.md). It represents a mature production system where the ontology mapping standard and the AI assistant context pattern coexist.

## Source Attribution
Raw source: [oxo2 claude](../../raw/2026-05-25/oxo2-claude.md)
