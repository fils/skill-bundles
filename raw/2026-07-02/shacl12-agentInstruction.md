# SHACL 1.2 Core — sh:agentInstruction Property

**Source:** https://www.w3.org/TR/shacl12-core/ (Working Draft 2026-06-30)
**Date ingested:** 2026-07-02
**Type:** W3C specification update

**Key Ideas:**
- SHACL 1.2 introduces sh:agentInstruction property explicitly for agent/LLM instruction support in validation shapes.
- Enables shapes to carry instructions for agents/LLMs about domain entities.
- Part of Core: sh:intent, sh:agentInstruction, sh:codeIdentifier.
- Supports validating, inferencing, modeling domains, generating ontologies for agents, building UIs, code generation.

**Quotes/Highlights:**
- "sh:agentInstruction — explicit agent/LLM instruction support in validation shapes"
- "We have algorithms that take SHACL shape definitions to instruct LLMs about what sort of entities exist in the domain of interest"

**Context Elements:** SHACL shapes now directly include agent instructions — tight integration of validation + agent guidance.

**Relevance to Skill Bundles:** Direct formal context element (SHACL) now natively supports agent instructions. Critical bridge between skills and validation layers.