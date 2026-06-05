# Agent Skills Specification - agentskills/agentskills

Source: https://github.com/agentskills/agentskills
Date ingested: 2026-06-05

**Summary:** Official specification repo for the Agent Skills open standard. Defines the SKILL.md format, folder structure, progressive disclosure loading model. Stars: 20k, active ecosystem.

**Relevance to skill bundles:** This is the canonical definition of the skill format itself. Bundles would be collections of such skills + accompanying context elements (SHACL for validation of SKILL.md, SSSOM for skill mapping, ontologies for skill taxonomies).

Key elements:
- SKILL.md with metadata and instructions
- scripts/, references/, assets/
- Discovery/Activation/Execution stages
- Cross-tool compatibility (Claude, Codex, VS Code, etc.)

This source provides the foundational spec that any skill bundle must conform to.