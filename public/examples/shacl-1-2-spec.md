---
type: Skill Bundle Example
title: SHACL 1.2 Core Specification — W3C Standard
description: SHACL 1.2 (Shapes Constraint Language) is the latest evolution of the W3C standard for describing conditions that a dataset must meet.
resource: https://www.w3.org/TR/shacl12-core/
timestamp: '2026-05-24T00:00:00Z'
date: '2026-05-24'
---

# SHACL 1.2 Core Specification — W3C Standard

**Source:** https://www.w3.org/TR/shacl12-core/
**Date Added:** 2026-05-24 (Iteration 8)
**Author:** W3C
**Bundle Type:** SHACL Validation (Core Specification)
**Confidence:** 9/10

## Name & Origin

SHACL 1.2 (Shapes Constraint Language) is the latest evolution of the W3C standard for describing conditions that a dataset must meet. It is the foundational specification that all SHACL-based skill bundles depend on.

## Skills Included

- Shape definition and validation
- Constraint components (datatype, pattern, min/max count, value range, etc.)
- Target declarations (nodes to validate)
- Validation report generation

## Context Elements

- **SHACL Validation:** Core W3C standard. Defines shapes that constrain RDF graph structure
- **Shape Graphs:** Collections of constraints that define expected data structure
- **Validation Reports:** Standardized output format for validation results

## How Context Elements Support Skills

SHACL 1.2 is the foundational specification for SHACL-based validation in skill bundles. Every example that uses SHACL (Schimatos, RDF Ontologies, Open Ontologies, GraphGuard OS, xpSHACL, SHACL Data Quality paper) ultimately depends on this specification.

Key capabilities useful for skill bundles:
- Validate skill input/output contracts
- Ensure knowledge graphs conform to expected schemas
- Provide structural constraints that agents cannot bypass through prompt engineering

## Composition Notes

This entry serves as a **reference node** in the wiki — all SHACL-based skill bundles link back to this specification. It is not a bundle example itself but the standard that enables SHACL-based bundles.

SHACL 1.2 vs 1.0: The 1.2 version adds improved constraint components and better integration with SPARQL-based constraints, making it more suitable for complex skill bundle validation scenarios.

## Reproducibility

N/A — this is a W3C specification, not software.

## Related Examples

- [schimatos shacl knowledge graph](schimatos-shacl-knowledge-graph.md)
- [rdf ontologies skill](rdf-ontologies-skill.md)
- [open ontologies paper](open-ontologies-paper.md)
- [open ontologies github](open-ontologies-github.md)
- [graphguard os guardrails](graphguard-os-guardrails.md)
- [xpshacl explainable shacl](xpshacl-explainable-shacl.md)
- [shacl data quality 69 metrics](shacl-data-quality-69-metrics.md)
