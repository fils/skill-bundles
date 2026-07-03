# Agent Skills Overview - agentskills.io

**Source:** https://agentskills.io/home (and specification)
**Date ingested:** 2026-07-03
**Type:** Official specification + documentation

## Key Ideas
- Agent Skills: lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.
- Core: a skill is a folder containing SKILL.md (metadata: name, description + instructions).
- Skills can bundle scripts, reference materials, templates, and other resources.
- Open standard originally from Anthropic, now ecosystem-wide (GitHub Copilot, Claude, Codex, etc.).
- Progressive disclosure: agents load only needed context.
- Official Discord and GitHub org for contributions.

## Quotes / Highlights
- "Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows."
- "At its core, a skill is a folder containing a `SKILL.md` file."
- Supports resource_extensions: .md, .json, .yaml, .yml, .csv, .xml, .txt and scripts/.

## Relevance to Skill Bundles
Foundational spec for how skills (and bundles of skills) are structured and discovered. Provides the metadata and packaging standard that enables formal context (validation, mapping) to be attached. Primary reference for all skill bundle examples.

**Tags:** specification, agentskills.io, open-standard, metadata, SKILL.md