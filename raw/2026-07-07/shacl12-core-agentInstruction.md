# SHACL 1.2 Core — New sh:agentInstruction Property

**Source:** https://www.w3.org/TR/shacl12-core/ (W3C Working Draft, 30 June 2026)

**Key Ideas:**
- SHACL 1.2 introduces sh:agentInstruction (along with sh:intent, sh:codeIdentifier).
- Explicit support for using SHACL shapes to instruct LLMs/agents about domain entities.
- SHACL used for validating, inferencing, modeling domains, generating ontologies to inform other agents, building UIs, generating code, integrating data.
- New focus on agentic workflows: shapes graphs can directly guide agent behavior.

**Relevance to Skill Bundles:** Direct formal bridge between SHACL (validation + constraints) and agent skills. The new sh:agentInstruction property is a canonical example of bundling skills with formal context (SHACL shapes that serve as agent instructions). This is a high-signal development for the catalog.

**Quotes:**
> "SHACL may be used for a variety of purposes such as validating, inferencing, modeling domains, generating ontologies to inform other agents..."

**Composition Notes:** SHACL shapes now explicitly designed to be consumed by agents. Strong candidate for [[shacl-agent-bundles]] pattern.