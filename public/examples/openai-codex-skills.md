---
type: Skill Bundle Example
title: OpenAI Codex Agent Skills — Structured Skill System
description: OpenAI Agent Skills for Codex — the official skill system for OpenAI's Codex CLI agent.
resource: https://developers.openai.com/codex/skills
timestamp: '2026-05-23T00:00:00Z'
date: '2026-05-23'
---

# OpenAI Codex Agent Skills — Structured Skill System

**Date:** 2026-05-23
**Source:** https://developers.openai.com/codex/skills
**Confidence:** 5/5 (Official documentation)

## Name & Origin
OpenAI Agent Skills for Codex — the official skill system for OpenAI's Codex CLI agent. Based on the open agent skills standard (agentskills.io).

## Skills Included
Codex implements the skill specification with progressive disclosure:
- Skill manifests (SKILL.md) with YAML frontmatter
- Supporting directories: scripts/, references/, assets/
- Agent-specific configuration (agents/openai.yaml)

## Context Elements
- **YAML configuration**: agents/openai.yaml defines UI display_name, brand_color, invocation policy (allow_implicit_invocation), and tool dependencies
- **MCP dependency declarations**: Skills declare external tool server requirements in YAML
  ```yaml
  dependencies:
    tools:
      - type: "mcp"
        value: "serverName"
  ```
- **Context budget management**: Progressive disclosure formalized — 2% of context window for skill discovery (~8,000 chars)
- **Multi-scope hierarchy**: REPO → USER → ADMIN → SYSTEM scope resolution
- **Config-driven enable/disable**: TOML-based skill configuration in ~/.codex/config.toml

## How Context Elements Support Skills
The progressive disclosure pattern is a form of resource management that ensures skills don't overwhelm the context window. The YAML configuration (openai.yaml) provides a declarative way to constrain skill behavior (e.g., require explicit invocation) and declare external dependencies (MCP servers).

## Composition Notes
This represents a mature, production-grade skill system with:
- Formal specification compliance (agentskills.io)
- Context budget awareness
- Dependency declarations for external tools
- Scope hierarchy for skill resolution

## Reproducibility
High — official documentation with clear installation steps via `$skill-installer`. The skill format is standardized across OpenAI's agent ecosystem.
