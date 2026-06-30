# SHACL 1.2 Core — New agentInstruction, intent, and codeIdentifier properties (2026-06-30 WD)

**Source:** https://www.w3.org/TR/shacl12-core/ (W3C Working Draft, 30 June 2026)
**Editors:** Holger Knublauch et al.

## Key Ideas & New Features Relevant to Agents
- SHACL 1.2 adds explicit support for agentic use cases via non-validating properties in Section 8:
  - `sh:agentInstruction` — Instructions for agents/LLMs on how to use or interpret the shape.
  - `sh:intent` — Human-readable intent/purpose of the shape.
  - `sh:codeIdentifier` — Regex for code generation identifiers.
- Node expressions (`sh:values`, `sh:defaultValue`, `sh:targetWhere`, `sh:shape`) enable dynamic computation, powerful for agent-driven validation/inference.
- List-taking parameters generalized; `sh:ByTypes`, reifier shapes, rootClass, etc.
- SHACL can now directly instruct agents ("sh:agentInstruction") while continuing to serve as validation + constraint engine.
- Ties directly to skill bundles: shapes can now carry agent instructions + validation rules in one artifact.

## Quotes
> "SHACL may be used for a variety of purposes such as validating, inferencing, modeling domains, generating ontologies to inform other agents, building user interfaces, generating code, and integrating data."
> New in 1.2: `sh:agentInstruction`, `sh:intent`, `sh:codeIdentifier`.

## Composition Notes
This is a major evolution for **validation + agent-instruction bundles**. SHACL shapes can now serve as both guardrails (validation) and skill context (agent instructions). Perfect complement to Agent Skills SKILL.md files.

**Relevance:** Directly supports the mission — formal context elements (SHACL shapes) that include agent instructions.
**Reproducibility:** W3C spec, full conformance rules documented.