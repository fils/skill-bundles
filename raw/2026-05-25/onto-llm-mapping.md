# Onto-LLM-Mapping — Ontology Mapping Using LLMs and RAG

**Source:** https://github.com/cns-iu/onto-llm-mapping
**Date:** 2026-05-25
**Signal:** 9/10

## Overview
Framework for mapping concepts between ontologies (e.g., Uberon to MeSH) using LLMs and RAG. Outputs in **SSSOM format** — directly relevant to our SSSOM search priority.

## Methodology
1. **Expansion:** LLM expands term names, synonyms, descriptions
2. **Vectorization:** Store in vector database
3. **Retrieval:** Semantic similarity search for top candidates
4. **Ranking:** LLM ranks top 3 candidates
5. **Standardization:** Output in SSSOM format

## Mapping Strategies Evaluated
| Type | Description |
|---|---|
| desc-vec | Semantic similarity via labels/synonyms/descriptions |
| llm-vec | LLM-expanded descriptions |
| llm-rank | LLM ranking of retrieved candidates |
| ubkg | UMLS/Uberon common Concept mapping |

## Tech Stack
Python 3.10+, LLM CLI, Node.js, DuckDB, Ollama, R (68.2%)

## SSSOM Connection
The `/mappings` directory contains final SSSOM mapping files. This is a concrete implementation of SSSOM mapping generation pipeline — the third SSSOM example in our catalog after the spec itself and the OxO2 service.
