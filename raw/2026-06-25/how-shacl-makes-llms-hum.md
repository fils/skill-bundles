# How SHACL Makes Your LLMs Hum

**Source:** https://ontologist.substack.com/p/how-shacl-makes-your-llms-hum  
**Author:** Kurt Cagle  
**Ingested:** 2026-06-25

## Key Ideas
- SHACL is self-documenting: pass SHACL to an LLM to generate high-quality documentation.
- SHACL, SPARQL, and RAG operate on similar principles; SHACL can be used as "LLM MadLibs" for query generation and validation.
- In agentic services, SHACL serves as the validation layer instead of relying solely on LLMs (avoid hallucination).
- Benefits for data integration, loading only needed SHACL, and using shapes to instruct LLMs about domain entities.

## Notable Quotes
- "If you have the SHACL and a services-enabled knowledge graph, have the LLM read the SHACL, then use this as a basis for generating a SPARQL query..."
- "The best approach when working with agentic systems is not to have the LLM become the validation layer... Instead... have the LLM write an application based on shapes."

## Relevance to Skill Bundles
Excellent example of SHACL + LLM/agent skills bundle. SHACL shapes provide guardrails, documentation, and query-generation context for agent skills. High reproducibility via self-documenting shapes.