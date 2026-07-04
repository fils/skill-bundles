# SHACL 1.2 Core — sh:agentInstruction & sh:codeIdentifier

**Source:** https://www.w3.org/TR/shacl12-core/ (W3C Working Draft, 30 June 2026)
**Date ingested:** 2026-07-04
**Type:** W3C specification update

**Key content:**
- New properties in SHACL 1.2 Core: sh:agentInstruction, sh:codeIdentifier, sh:intent.
- SHACL shapes can now directly instruct agents and reference code identifiers.
- SHACL used for validating RDF, inferencing, modeling domains, generating ontologies for agents, UI generation, code generation, data integration.
- Complementary with OWL for agent decision-making pipelines (SHACL as constraint gatekeeper + rule engine).

**Context elements present:**
- Formal shapes language with agent-specific extensions
- sh:agentInstruction for embedding instructions targeted at LLM agents
- Integration patterns with agentic workflows

**Relevance to skill bundles:** Direct evolution of the standard that now natively supports agent skills via SHACL shapes. Strong example of formal context (validation + instruction) bundled with skills.