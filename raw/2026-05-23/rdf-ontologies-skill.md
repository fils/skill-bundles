# RDF Ontologies — Agent Skill

Source: https://eliteai.tools/agent-skills/rdf-ontologies-1
Install: npx add-skill https://github.com/majiayu000/claude-skill-registry/tree/main/skills/other/rdf-ontologies

## Core RDF Concepts
- RDF expresses knowledge as triples: Subject → Predicate → Object
- Turtle (TTL) is the human-readable format for RDF
- Collections, shorthand (;), and rdf:type (a) supported

## Validation and Querying
- **SHACL (Shapes Constraint Language)** used to validate RDF data against rules
- Example: UserStory must have exactly one title (string), priority P1/P2/P3, and at least one acceptance criterion
- **SPARQL** standard query language for RDF data

## Technical Integration
- **Oxigraph RDF Store** for high-performance storage and SPARQL processing
- **.specify/ directory workflow:**
  1. Create structure: mkdir -p .specify/specs/[feature-name]
  2. Author .ttl files for features, entities, plans
  3. Validate SHACL constraints: cargo make speckit-validate
  4. Render Markdown: ggen render
  - Key rule: NEVER edit .md manually; always update .ttl source

## Context Elements
- **SHACL validation** for RDF data (shapes/constraints)
- **Turtle/TTL vocabulary** for specification management
- **SPARQL queries** for data retrieval
- **Oxigraph triple store** integration
