# SHACL 1.2 Core Specification

**Source:** https://www.w3.org/TR/shacl12-core/ (Published Jun 22, 2026)
**Type:** W3C Recommendation - Shapes Constraint Language

## Key Points
- SHACL defines classes, properties, and constraints for RDF data.
- Used for validation, inference support, and as a rules engine in agentic systems.
- Recent 1.2 update expands expressivity for classes, instances, and property constraints.
- Can trigger alerts, detect patterns, constrain reasoning paths in AI agents.
- Often paired with OWL for inferencing + SHACL for constraint gatekeeping.

## Agent/Skills Integration Examples
- In complex agents: SHACL validates applicant skills data (degree, experience) to ensure structure before OWL reasoning infers qualifications.
- SHACL shapes can be used to instruct LLMs about domain entities.
- GitHub issue: "Add a property to capture LLM and agent input" in data-shapes repo.
- Skills marketplace examples: "shacl" skill for design/implementation/validation of RDF using SHACL.

## Composition Notes
- SHACL provides the formal validation layer that can be bundled with agent skills.
- Enables "skill bundles" where skills (procedural) are guarded by SHACL shapes (declarative constraints).
- High relevance for bundles involving structured data, taxonomies, or knowledge graphs.

**Relevance:** Direct example of formal context element (SHACL) that pairs naturally with agent skills for reliable execution.