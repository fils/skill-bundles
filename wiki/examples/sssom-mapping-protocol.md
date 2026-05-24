# SSSOM Protocol — Simple Standard for Sharing Ontological Mappings

**Source:** https://github.com/mapping-commons/sssom/, https://mapping-commons.github.io/sssom/dev/  
**Python Toolkit:** https://github.com/mapping-commons/sssom-py  
**Date Added:** 2026-05-24 (Iteration 8)  
**Author:** Mapping Commons  
**Bundle Type:** SSSOM Mapping + Ontology Interoperability  
**Confidence:** 9/10

## Name & Origin

SSSOM (Simple Standard for Sharing Ontological Mappings) provides a TSV-based representation for ontology term mappings with a comprehensive metadata model for provenance. It is designed for interoperability between different systems and organizations that need to map terms across ontologies.

## Skills Included

- Reading and writing SSSOM mapping files (TSV format)
- Mapping provenance documentation
- Converting mappings between formats
- Integrating SSSOM mappings into agent workflows for cross-ontology translation

## Context Elements

- **SSSOM Mapping:** Core specification — standardized TSV format for ontology-to-ontology mappings with fields for:
  - Subject/concept identifiers
  - Mapping predicates (exactMatch, closeMatch, relatedMatch, etc.)
  - Confidence scores
  - Provenance metadata (who created the mapping, when, using what method)
  - Justification and evidence
- **Python Toolkit (sssom-py):** CLI and library for programmatic SSSOM manipulation
- **Metadata Model:** Rich provenance tracking built into the format itself

## How Context Elements Support Skills

SSSOM provides the **mapping layer** that agents need when they work with data from multiple ontologies or schema systems. A skill that uses SSSOM can:
1. Read pre-existing mappings between ontologies
2. Create new mappings with full provenance tracking
3. Use mappings to translate queries across schema boundaries
4. Report confidence scores on mapping relationships

This directly addresses the "SSSOM Mapping" category in our bundle taxonomy. Combined with [[open-ontologies-paper]] (which implements stable matching for ontology alignment), SSSOM provides the standard format for expressing those mapping results.

## Composition Notes

SSSOM is a **context element first** — it's not a skill itself but a standard that skills can use. The pattern is:
- Agent has a skill that needs to work across multiple ontologies
- SSSOM files provide the mapping definitions
- The skill reads SSSOM to translate between schemas
- All mappings carry provenance and confidence scores

This is analogous to how SHACL provides validation shapes: SSSOM provides mapping definitions. Both are declarative artifacts that skills consume.

## Reproducibility

High — open standard with Python implementation. TSV format is human-readable. sssom-py provides programmatic access.

## Relationship to Other Examples

- **[[open-ontologies-paper]]** implements ontology alignment (stable matching); SSSOM is the format for expressing those alignment results
- **[[open-ontologies-github]]** provides 32 standard ontologies in its marketplace; SSSOM mappings could be added to define relationships between these ontologies
- **[[xpshacl-explainable-shacl]]** validates RDF graphs; SSSOM mappings enable multi-ontology validation scenarios
