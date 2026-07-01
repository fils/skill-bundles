# SHACL 1.2 Core (W3C Working Draft)

**Source:** https://www.w3.org/TR/shacl12-core/ (2026-06-30 WD)
**Type:** Specification

## Key Ideas
- SHACL 1.2 extends the Shapes Constraint Language for validating RDF graphs.
- New in 1.2: sh:agentInstruction property (explicit support for instructing agents/LLMs).
- Used for validating, inferencing, modeling domains, generating ontologies to inform other agents, building UIs, generating code, integrating data.
- Part of larger SHACL 1.2 family (SPARQL extensions, Node Expressions, Rules, UI, Profiling).

## Quotes / Highlights
- "SHACL may be used for a variety of purposes such as validating, inferencing, modeling domains, generating ontologies to inform other agents, building user interfaces, generating code, and integrating data."
- New property: sh:agentInstruction.

## Relevance to Skill Bundles
Direct formal context element (validation + agent instructions) that can be bundled with skills. SHACL shapes provide guardrails and constraints for agent skills. Emerging pattern: SHACL as rules engine for agentic workflows.
