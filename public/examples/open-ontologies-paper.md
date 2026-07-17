---
type: Skill Bundle Example
title: Open Ontologies — Stable Matching Alignment Paper
description: Open Ontologies — a Rust-based, open-source system for ontology engineering that bridges LLMs and formal ontology work via the Model Context Protocol (MCP).
resource: https://arxiv.org/html/2605.09184v1
timestamp: '2026-05-23T00:00:00Z'
date: '2026-05-23'
---

# Open Ontologies — Stable Matching Alignment Paper

**Source:** https://arxiv.org/html/2605.09184v1
**Author:** Fabio Rovai (The Tesseract Academy, London)
**Date Added:** 2026-05-23
**Bundle Type:** Mapping/Alignment + Agent Tooling
**Confidence:** 5/5 (Peer-reviewed preprint with empirical benchmarks)

## Name & Origin

Open Ontologies — a Rust-based, open-source system for ontology engineering that bridges LLMs and formal ontology work via the Model Context Protocol (MCP). This paper presents the core research on ontology alignment using stable matching algorithms.

## Skills Included

- Ontology construction via LLM+MCP tools (build, query, validate)
- Ontology alignment using multi-signal scoring + stable matching
- OWL-RL forward-chaining reasoning
- SHACL validation of RDF data
- SPARQL 1.1 querying via Oxigraph triple store
- SHIQ tableaux consistency checking

## Context Elements

- **SSSOM-style similarity signals:** The alignment engine scores candidate mappings across six signals — labels, properties, parents, instances, restrictions, and neighborhood structure. This closely mirrors the SSSOM framework's approach to documenting mappings with provenance and confidence scores.
  - Similarity formula: `score(c_s, c_t) = Σ(w_i × s_i(c_s, c_t))` for six weighted signals
- **Stable matching algorithm:** 1-to-1 assignment constraint — sorts candidates by confidence, retains only top-scoring unique pairs. Proven dominant: "signal weights are irrelevant when stable matching is applied (F1 varies by <0.004), while removing stable matching drops F1 to 0.728."
- **SHACL (Shapes Constraint Language):** Formal validation of RDF data via `shacl` tool
- **32 standard ontologies in marketplace:** Schema.org, BFO, FOAF, SKOS, etc. — cross-ontology vocabulary mappings
- **Clinical crosswalks:** ICD-10, SNOMED, MeSH — domain-specific ontology mappings
- **OWL2-DL tableaux reasoner:** Native Rust implementation for consistency checking
- **MCP tool interface:** 43 `onto_*` tools exposing ontology operations to LLM agents

## How Context Elements Support Skills

The paper's central finding directly addresses the mapping gap: structured tool access (MCP/SPARQL) yields a **+264% improvement** in LLM ontology interaction (F1 0.717) over baseline (F1 0.431), while raw file access (Turtle syntax) actually *degrades* performance to F1 0.323. This demonstrates that **mapping quality depends on access modality, not just signal weights**.

The stable matching breakthrough shows that for skill bundles involving ontology alignment or SSSOM-style mappings, the **assignment constraint** (1-to-1) matters more than the similarity function itself. This is a fundamental insight for how skills should be bundled with mapping artifacts.

## Composition Notes

This is one of the strongest examples in the catalog because it combines:
1. **Agent skills** (MCP tools for LLM ontology engineering)
2. **Mapping/alignment** (six-signal similarity + stable matching)
3. **Validation** (SHACL shapes)
4. **Vocabularies** (32 standard ontologies in marketplace)
5. **Taxonomies** (clinical crosswalks: ICD-10, SNOMED, MeSH)
6. **Rules** (OWL-RL forward-chaining)

The "Infrastructure-as-Code" lifecycle (Plan, Enforce, Apply, Monitor, Drift) with append-only lineage provides governance for the entire skill bundle.

## Reproducibility

High — single Rust binary, no JVM/Python dependencies. Installation via curl, Cargo, or Docker. MCP server integrates with Claude Desktop, Cursor, and any MCP-compatible client.

## Key Benchmarks

- **OAEI Anatomy Track:** P=0.963, R=0.733, F1=0.832 (highest precision of any reported system)
- **Reasoning Speed:** 15ms vs 24,490ms (HermiT) for 50,000 axioms — **1,633× speedup**
- **OntoAxiom (LLM + MCP Tools):** F1 = 0.717, **+264% vs paper best**
- **Construction:** 91-class Pizza ontology in <5 minutes with 96% coverage

## Limitations

- Recall gap needs domain-specific background knowledge (e.g., UMLS) for matches with low label similarity
- Results measured against reference alignments but not yet independently evaluated by external benchmarks
