---
date: 2026-05-25
sources:
  - https://ylanglabs.com/blogs/agent-skills
title: Ylang Labs — Agent Skills Portable Format Overview
skills_included:
  - Sprint planning workflow example
  - Document/asset creation patterns
  - Workflow automation patterns
  - MCP enhancement patterns
context_elements:
  - YAML frontmatter schema (name, description)
  - Progressive disclosure three-level loading
  - scripts/ references/ assets/ directory patterns
  - Distribution models (direct, marketplace, community)
composition_notes: |
  Definitive overview of the Agent Skills format. Provides the "recipes vs kitchen" metaphor
  for Skills vs MCP. Documents the three-level progressive disclosure loading pattern that
  appears across multiple bundles in our catalog.
reproducibility: High — published reference article
confidence: 9/10
---

# Ylang Labs: Agent Skills Portable Format Overview

## Overview

Ylang Labs published a comprehensive overview of the Agent Skills open standard, explaining how it provides a portable format for teaching AI agents procedural knowledge. The article provides the clearest metaphor we've found: **MCP provides the kitchen (tools/data), Skills provide the recipes (procedural knowledge)**.

## Three-Level Progressive Disclosure

| Level | Content | When Loaded | Token Cost |
|---|---|---|---|
| 1. Metadata | Name & Description | At startup | ~100 tokens |
| 2. Instructions | SKILL.md body | When triggered | <5,000 tokens |
| 3. Resources | Scripts & References | Only as needed | Variable |

This pattern is used by [[dspy-agent-skills-bundle]], [[anthropic-official-skills-repo]], and the updated [[dspy-agent-skills-v023]].

## Skills vs Alternatives

| Feature | Skills | System Prompts | MCP Servers |
|---|---|---|---|
| Provides | Procedural how-to | Momentary instructions | Tool/data access |
| Persistence | Cross-conversation | Single session | Continuous |
| Portability | High (open standard) | Low (product-specific) | High (open standard) |
| Idle Cost | ~100 tokens | High (full prompt) | Minimal |

## SKILL.md Schema
The minimal formal context element:
```yaml
---
name: skill-name
description: >
  What the skill does and when to trigger it.
---
```

## Distribution Models
1. **Direct**: `.claude/skills/`, `.cursor/skills/`, `.agents/skills/`
2. **Plugin Marketplaces**: Git-based with version pinning
3. **Community**: `skills.sh` by Vercel Labs (`npx skills add owner/repo`)

## Limitations Documented
- **Fragmentation**: Different hidden folders across products
- **Security**: Malicious skills could misuse tools
- **Runtime**: Script execution depends on agent environment
- **Interoperability**: Depth of integration varies (30+ products support)

## Connection to Pattern Catalog
This article provides the **foundational reference** for why progressive disclosure matters across all bundles. The three-level loading pattern explains the architecture of [[dspy-agent-skills-bundle]]'s SKILL.md + reference.md pair, and why [[awesome-agent-skills-catalogs]] catalogs skills by their metadata descriptions.

## Source Attribution
Raw source: [[../../raw/2026-05-25/ylang-labs-agent-skills.md]]
