---
date: 2026-05-25
sources:
  - https://github.com/cns-iu/onto-llm-mapping
title: Onto-LLM-Mapping — SSSOM-Compliant Ontology Mapping with LLMs and RAG
skills:
  - LLM-based ontology term expansion
  - Vector similarity retrieval
  - LLM candidate ranking
  - SSSOM output generation
context_elements:
  - SSSOM mapping output format
  - DuckDB vector storage
  - Ollama local LLM integration
  - SPARQL queries for data extraction
  - YAML prompt templates (term-description.yaml, rank-similar.yaml)
composition_notes: |
  Concrete SSSOM mapping **generation** pipeline (complementary to OxO2's SSSOM **serving**).
  Uses multi-stage LLM pipeline: expand → vectorize → retrieve → rank → format as SSSOM.
  The third SSSOM example in our catalog, providing a production mapping generator.
reproducibility: Medium — research-in-progress, shell-script workflows
confidence: 8/10
---

# Onto-LLM-Mapping: SSSOM Mapping with LLMs and RAG

## Overview

A framework from cns-iu for mapping concepts between ontologies (e.g., Uberon to MeSH) using LLMs and RAG, outputting results in [[sssom-mapping-protocol]] format. This is the first SSSOM **mapping generator** in our catalog — complementary to [[oxo2-sssom-mapping-service]] (which serves SSSOM mappings) and the SSSOM specification itself.

## Multi-Stage Pipeline

1. **Expansion**: LLM expands term names, synonyms, descriptions into consistent format
2. **Vectorization**: Store expanded descriptions in DuckDB vector database
3. **Retrieval**: Semantic similarity search for top candidates (e.g., Uberon → MeSH)
4. **Ranking**: LLM ranks top 3 retrieved candidates
5. **Standardization**: **Output in SSSOM format**

## Mapping Strategies Evaluated

| Strategy | Method | Notes |
|---|---|---|
| desc-vec | Semantic similarity via labels/synonyms/descriptions | Baseline |
| llm-vec | LLM-expanded descriptions for vectorization | Enhanced |
| llm-rank | LLM ranks top 3 candidates from retrieval | Best accuracy |
| ubkg | UMLS/Uberon common Concept mapping | External reference |

## Tech Stack
- **Languages**: R (68.2%), Shell (16.3%), JavaScript (14.2%), Cypher (1.3%)
- **Tools**: LLM CLI, DuckDB, Ollama, Python 3.10+
- **Templates**: YAML prompt templates (`term-description.yaml`, `rank-similar.yaml`)

## SSSOM as Context Element
The `/mappings` directory produces SSSOM-formatted files. This is significant because it shows SSSOM being used as the **output standard** for an automated mapping pipeline — the format is not just a spec but a working artifact. The project uses the same SSSOM standard that [[oxo2-sssom-mapping-service]] serves, creating a complementary pair: generate (Onto-LLM) ↔ serve (OxO2).

## Composition Pattern
This project combines:
- LLM skills (term expansion, ranking)
- SSSOM standard (output format)
- SPARQL queries (data extraction)
- YAML templates (prompt definitions)
- Shell workflows (orchestration)

This is a concrete example of **skills + SSSOM mapping + prompt templates** as a skill bundle.

## Status
**Research in progress** — future work includes validation against gold standard, model selection refinement, and generalization for arbitrary concept sets.

## Source Attribution
Raw source: [[../../raw/2026-05-25/onto-llm-mapping.md]]
