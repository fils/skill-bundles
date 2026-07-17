---
type: Skill Bundle Example
title: Open Ontologies — GitHub Repository (Rust MCP Server)
description: Open Ontologies — a high-performance, Rust-based Model Context Protocol (MCP) server and desktop Studio for AI-native ontology engineering.
resource: https://github.com/fabio-rovai/open-ontologies
timestamp: '2026-05-23T00:00:00Z'
date: '2026-05-23'
---

# Open Ontologies — GitHub Repository (Rust MCP Server)

**Source:** https://github.com/fabio-rovai/open-ontologies
**Author:** Fabio Rovai
**Date Added:** 2026-05-23
**Bundle Type:** MCP Tools + Ontology Engineering + Mapping/Alignment
**License:** MIT
**Confidence:** 5/5 (Production codebase with benchmarks, 17,400 LOC Rust)

## Name & Origin

Open Ontologies — a high-performance, Rust-based Model Context Protocol (MCP) server and desktop Studio for AI-native ontology engineering. Companion to the arXiv paper (see [open ontologies paper](open-ontologies-paper.md)), this repo represents the production implementation.

## Skills Included

- **43 MCP tools** for full ontology lifecycle: `onto_build`, `onto_query`, `onto_align`, `onto_shacl`, `onto_reason`, `onto_diff`, `onto_lint`, `onto_plan`, `onto_apply`, `onto_drift`, `onto_monitor`, `onto_lineage`, `onto_ingest`, `onto_convert`, `onto_embed`, `onto_stats`, `onto_version`, and more
- **AI Agent Chat:** `/build` (13-step deep pipeline) and `/sketch` (3-step prototype) commands in the Studio
- **Property Inspector:** Protégé-style inline triple editor for real-time graph updates
- **Virtualized Tree:** Handles 1,500+ classes with zero lag

## Context Elements

- **Mapping/Alignment (`onto_align`):** Hybrid alignment engine using structural signals (labels, properties, parents, instances, restrictions, neighborhood) + LLM adjudication. Supports cross-ontology matching.
- **SHACL validation (`onto_shacl`):** Formal constraint checking of RDF data against defined shapes
- **Marketplace — 32 standard ontologies:** Schema.org, BFO, FOAF, SKOS, etc. — ready-made vocabularies and taxonomies for cross-ontology mapping
- **Clinical crosswalks:** ICD-10, SNOMED, MeSH — domain-specific ontology mappings
- **IES (Information Exchange Standard):** 4D/BORO patterns for Digital Twin programs — ontology-based data modeling rules
- **OWL2-DL tableaux reasoner:** Native Rust implementation for consistency checking and classification
- **Oxigraph triple store:** Pure Rust, in-memory SPARQL 1.1 engine
- **SQLite lineage/versioning:** Append-only audit trail of all ontology changes
- **Terraform-style lifecycle:** `plan`, `apply`, `lock`, `drift` tools for knowledge graph governance

## How Context Elements Support Skills

The MCP tool interface is the key innovation: all ontology operations are exposed as structured tools rather than raw file access. This enables LLM agents to interact with ontologies symbolically, avoiding the parsing errors and hallucination risks of reading Turtle/OWL files directly (the paper shows raw file access *degrades* LLM performance by 25%).

The `onto_align` tool directly addresses the SSSOM mapping gap — it implements the six-signal similarity scoring + stable matching algorithm from the paper, with LLM adjudication for ambiguous cases. This is a production-ready mapping engine that could be integrated into any agent skill bundle requiring cross-ontology alignment.

## Composition Notes

This is arguably the most complete skill bundle example in the catalog, combining:
1. **Agent skills** (43 MCP tools for LLM ontology engineering)
2. **Mapping/alignment** (`onto_align` with stable matching + LLM adjudication)
3. **Validation** (`onto_shacl`, 32 standard ontology shapes)
4. **Vocabularies** (Schema.org, BFO, FOAF, SKOS marketplace)
5. **Taxonomies** (ICD-10, SNOMED, MeSH clinical crosswalks)
6. **Ontologies** (OWL2-DL reasoner, full ontology lifecycle management)

The bundle is self-contained: single Rust binary, no JVM/Python dependencies, works with any MCP-compatible client.

## Reproducibility

Very high — installation via curl, Cargo, Docker. MCP server configures via JSON in any MCP-compatible client. Studio is a Tauri desktop app (React 19 frontend).

## Technical Stack

- **Language:** Rust (Edition 2024), TypeScript, Python
- **Triple Store:** Oxigraph 0.4
- **Database:** SQLite (rusqlite) for lineage/versioning
- **ML:** tract-onnx for semantic embeddings
- **Frontend:** React 19, Vite 7, Tailwind CSS 4, Zustand 5
- **Desktop:** Tauri 2

## Key Benchmarks

- **Reasoning Speed:** 14ms vs 1,200ms (HermiT) for 10,000 axioms — **86× speedup**
- **Reasoning Speed:** 15ms vs 24,490ms (HermiT) for 50,000 axioms — **1,633× speedup**
- **Build modes:** `/sketch` (2 min, 95 classes) vs `/build` (15 min, 1,433 classes, 218 object properties, depth 11)
- **OntoAxiom:** MCP Extraction F1 = 0.717, **+264% vs paper best**
