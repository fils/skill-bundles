# SHACL 1.2 Data Quality Assessment — 69 Metrics as Shapes

**Source:** https://arxiv.org/abs/2507.22305  
**Date Added:** 2026-05-24 (Iteration 8)  
**Authors:** Carolina Cortés, Lisa Ehrlinger, Lorena Etcheverry, Felix Naumann  
**Venue:** Proc. WOP-HAIBRIDGE 2025 (co-located with ISWC 2025)  
**Bundle Type:** SHACL Validation + Data Quality Framework  
**Confidence:** 9/10

## Name & Origin

This research paper investigates the viability of using SHACL as a comprehensive tool for assessing data quality in Knowledge Graphs. The authors bridge the gap between high-level quality frameworks and technical implementation by mapping **69 data quality metrics** to SHACL shapes.

## Skills Included

- Automated SHACL shape instantiation from data quality metrics
- Knowledge Graph validation against quality shapes
- Quality score computation from validation results (violations → numerical measures)
- Multi-dimensional quality assessment (accessibility, intrinsic, contextual, representational)

## Context Elements

- **SHACL Validation:** 69 data quality metrics from Zaveri et al.'s framework operationalized as SHACL shapes. Covers:
  - **Intrinsic dimensions:** Syntactic validity, consistency
  - **Accessibility dimensions:** Data availability, licensing
  - **Contextual dimensions:** Relevancy, timeliness (requires external metadata)
  - **Representational dimensions:** Conciseness, understandability
- **Data Quality Framework:** Zaveri et al.'s comprehensive DQ dimensions mapped to constraints
- **Prototype Code:** Open-source tool that automates shape instantiation and quality computation

## How Context Elements Support Skills

The paper demonstrates that SHACL can systematically validate knowledge graph quality across multiple dimensions. An agent skill that incorporates these 69 SHACL shapes could automatically assess KG quality as part of its workflow. The prototype computes a numerical quality score from validation results, making quality assessment machine-readable.

**Key finding:** SHACL excels at intrinsic dimensions (structural validation, consistency) but struggles with contextual dimensions (relevancy, timeliness) that require external metadata or complex SPARQL-based constraints beyond core SHACL features.

## Composition Notes

This is a "library of shapes" bundle pattern: a curated collection of 69 SHACL shapes that can be composed with any agent skill that creates or modifies knowledge graph data. The shapes are a reusable artifact — an agent could check KG quality before deploying it.

The computational overhead insight is important: validating massive KGs with complex shapes has measurable performance cost. This matters for skills that need real-time quality assessment.

## Reproducibility

High — all resources (SHACL shapes, prototype code) are provided. The paper is 43 pages with appendices. Venue: ISWC 2025 workshop ensures academic rigor.

## Key Insight

> "SHACL is excellent for intrinsic dimensions but some contextual or representational dimensions may require external metadata or complex SPARQL-based SHACL constraints that go beyond core SHACL features."

This defines the **boundary** of what SHACL validation alone can achieve for skill bundles.
