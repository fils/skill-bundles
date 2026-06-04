# agentskills.io Specification

**Source**: https://agentskills.io/specification and https://agentskills.io/home
**Date ingested**: 2026-06-04

## Overview
Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. Originally developed by Anthropic, released as open standard.

## Directory Structure
skill-name/
├── SKILL.md          # Required
├── scripts/          # Optional executable code
├── references/       # Optional docs
├── assets/           # Optional templates, resources
└── ...

## SKILL.md Format
YAML frontmatter + Markdown body.

Frontmatter fields:
- name (required, lowercase a-z0-9-)
- description (required, 1-1024 chars, what + when to use)
- license, compatibility, metadata, allowed-tools (optional)

Body: step-by-step, examples, edge cases. <500 lines recommended.

## Progressive Disclosure
1. Metadata (~100 tokens) at startup
2. Instructions (<5000 tokens) on activation
3. Resources on demand

## Validation
skills-ref validate

## Context Elements
- Formal spec defines structure (like ontology for skills)
- Supported by 30+ tools (Claude Code, Cursor, Copilot, etc.)
- Community: GitHub agentskills/agentskills, Discord

## Composition Notes
Enables portable, version-controlled skill bundles across agents. Strong on token efficiency and reusability.

## Reproducibility
Public spec, quickstart, llms.txt, open contributions.

---

*Core standard enabling all skill bundles. High signal for taxonomy and formal context.*