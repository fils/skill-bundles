# SHACL 1.2 + Agent Integration

**Sources:**
- W3C SHACL 1.2 Core (https://www.w3.org/TR/shacl12-core/, recent updates)
- Kurt Cagle LinkedIn post on SHACL as rules engine for agents (2026-06-27)
- GitHub issue w3c/data-shapes#725: "Add a property to capture LLM and agent input" (2026-01-16)
- IEEE paper "Constraint Checking of Skills using SHACL" (2021, still referenced)

**Key Ideas:**
- SHACL 1.2 introduces sh:agentInstruction, sh:intent, sh:codeIdentifier — explicit support for instructing LLMs/agents.
- SHACL used as constraint gatekeeper + occasional rule engine alongside OWL inferencing in agentic workflows.
- Example: Agent processes RDF skill/qualification data; SHACL validates structure while OWL reasons about role fit.
- Growing interest in using SHACL shapes to instruct LLMs about domain entities and constraints.

**Composition Notes:**
- SHACL shapes provide validation + instruction layer for agent skills.
- Direct link to skill bundles: context element (SHACL) paired with agent reasoning skills.

**Relevance:** High-signal example of formal context (SHACL) bundled with agent skills.