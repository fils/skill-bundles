# RDF Ontologies Skill — SHACL + SPARQL Integration

**Date:** 2026-05-23  
**Source:** https://eliteai.tools/agent-skills/rdf-ontologies-1
**Installed via:** npx add-skill https://github.com/majiayu000/claude-skill-registry/tree/main/skills/other/rdf-ontologies
**Confidence:** 4/5 (Third-party catalog extraction)

## Name & Origin
RDF Ontologies — an agent skill that teaches LLMs to use Resource Description Framework (RDF) and Turtle (TTL) syntax for managing software specifications, ontologies, and knowledge graphs.

## Skills Included
- RDF triple modeling (Subject → Predicate → Object)
- Turtle (TTL) syntax for human-readable RDF
- SHACL validation of RDF data against constraint shapes
- SPARQL query construction for RDF data retrieval
- .specify/ directory workflow for specification management

## Context Elements
- **SHACL (Shapes Constraint Language)**: Formal validation of RDF data
  - Example: UserStory must have exactly one title (string), priority P1/P2/P3, and at least one acceptance criterion
- **Turtle vocabulary**: Domain-specific prefixes and namespaces (spec:, rdf:, rdfs:, xsd:)
- **SPARQL queries**: Standard query language for structured data retrieval
- **Oxigraph triple store**: High-performance RDF storage and SPARQL processing
- **Validation commands**: cargo make speckit-validate for SHACL constraint checking
- **Rendering pipeline**: ggen render converts .ttl to .md (single-direction workflow)

## How Context Elements Support Skills
The SHACL shapes provide formal validation that ensures RDF data conforms to expected structures. The Turtle vocabulary gives the agent a controlled vocabulary for specification management. The Oxigraph integration provides executable tooling for storing and querying the RDF data.

## Composition Notes
This is a rare example of a skill bundle that combines skills with formal semantic web standards (SHACL, SPARQL, RDF/TTL). The workflow enforces a clear separation: .ttl is the source of truth, .md is derived output only.

## Reproducibility
Medium — third-party skill installable via npx add-skill, but depends on external tooling (Oxigraph, ggen).
