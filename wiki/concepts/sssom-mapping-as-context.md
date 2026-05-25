---
date: 2026-05-25
title: SSSOM Mapping as Skill Bundle Context
related:
  - sssom-mapping-protocol
  - oxo2-sssom-mapping-service
  - onto-llm-mapping
  - open-ontologies-paper
---

# SSSOM Mapping as Skill Bundle Context

## What is SSSOM?

The [[sssom-mapping-protocol]] (Simple Standard for Sharing Ontological Mappings) is a community standard for sharing mappings between ontology terms in a machine-readable format. It provides a standardized way to say "Term A in Ontology X is equivalent to Term B in Ontology Y."

## SSSOM Implementations in Our Catalog

As of 2026-05-25 (Iteration 10), we have **4 SSSOM-relevant examples**:

| # | Implementation | Role | SSSOM Usage |
|---|---|---|---|
| 1 | [[sssom-mapping-protocol]] | Specification | Defines the standard itself |
| 2 | [[oxo2-sssom-mapping-service]] | Production Service | Downloads, converts, serves SSSOM mappings via REST |
| 3 | [[onto-llm-mapping]] | Mapping Generator | Multi-stage LLM pipeline outputs SSSOM format |
| 4 | [[open-ontologies-paper]] | Alignment Algorithm | Stable matching for ontology alignment (related standard) |

## SSSOM as a Context Element

SSSOM can serve as a **formal context element** in skill bundles in several ways:

### 1. Cross-Ontology Skill Discovery
Skills that work across multiple ontologies can use SSSOM mappings to discover equivalent concepts. Example: a skill that maps disease terminologies (SNOMED CT → ICD-10) using SSSOM as the translation layer.

### 2. Mapping Validation
Skills can validate their outputs against SSSOM-compliant mappings, ensuring that any terminology transformations are standards-compliant. This is analogous to how [[shacl-1-2-spec]] validates RDF graphs.

### 3. Knowledge Graph Integration
SSSOM mappings enable skills to integrate with existing knowledge graphs (e.g., Uberon for anatomy, MeSH for medical subjects) without hardcoding term correspondences. [[oxo2-sssom-mapping-service]] demonstrates this at production scale.

### 4. LLM-Assisted Mapping Generation
[[onto-llm-mapping]] shows that LLMs can generate SSSOM mappings through a multi-stage pipeline:
```
Expand → Vectorize → Retrieve → Rank → Format as SSSOM
```
This pattern could be packaged as a skill bundle: a "mapping skill" with LLM prompts, vector search, and SSSOM output generation.

## Why SSSOM Coverage Matters

The SSSOM category was previously our weakest (only 2 examples). With OxO2 and Onto-LLM-Mapping, we now have a **complete lifecycle**:
- **Define**: SSSOM specification
- **Generate**: Onto-LLM-Mapping pipeline
- **Serve**: OxO2 production service
- **Align**: Open Ontologies alignment algorithms

This positions SSSOM as a mature context element type, comparable to our stronger categories like SHACL Validation (7 examples) and Ontology/Taxonomy (8 examples).

## Research Questions
1. Can SSSOM mappings be used to automatically discover which skills should work together?
2. Is there a pattern where SSSOM mappings define the "vocabulary" that a skill bundle operates on?
3. How does SSSOM relate to the [[sssom-mapping-protocol]]'s own mapping justification standard?
