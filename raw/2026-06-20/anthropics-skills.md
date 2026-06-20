# anthropics/skills — Anthropic's Public Agent Skills Repository

**Source:** https://github.com/anthropics/skills (153k stars)
**Date ingested:** 2026-06-20
**Signal rating:** 8/10 (official Anthropic examples + document skills + template)

## Key Ideas
- Official reference implementation of Agent Skills for Claude
- Skills/ folder with Creative & Design, Development & Technical, Enterprise & Communication, Document Skills
- spec/ and template/ directories
- Document skills (docx, pdf, pptx, xlsx) — source-available
- Plugin marketplace installation for Claude Code

## Context Elements
- SKILL.md YAML frontmatter (name, description)
- Template as reusable starting artifact
- Spec as the reference ontology for the format
- Document capabilities as bundled context providers

## Quotes
> "Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks."

## Composition Notes
Anthropic's repo demonstrates **official skill bundles** with both general examples and high-value document skills. Serves as the reference implementation for the agentskills.io spec.

## Reproducibility
Apache 2.0 for most; plugin marketplace for Claude Code.