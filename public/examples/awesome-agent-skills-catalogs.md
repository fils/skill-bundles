---
type: Skill Bundle Example
title: 'Awesome Agent Skills Catalogs: Ecosystem Mapping'
description: Two major **awesome-list** repositories catalog the agent skills ecosystem.
---

# Awesome Agent Skills Catalogs: Ecosystem Mapping

## Overview

Two major **awesome-list** repositories catalog the agent skills ecosystem. Together they serve as **marketplace registries** — not individual bundles, but structured collections that document the breadth of available skills, platform support, and the emergence of security-scanning marketplaces. They reveal how the skills ecosystem has organized itself and what **bundle density** looks like at scale.

**Context Elements:** Platform compatibility matrix · Quality standards · Skill path specifications · Security scanning references · Marketplace listings

## skillmatic-ai/awesome-agent-skills
The "definitive resource" catalog. Key data:
- **Platform matrix:** 13 supported platforms (Claude Code, Claude.ai, Cursor, VS Code, GitHub Copilot, Roo Code, OpenAI Codex, Gemini CLI, Mistral Vibe, Goose, Manus, OpenCode, Amp, Letta)
- **Marketplace data:** agentskill.sh (44k+ skills with security scanning), SkillsMP, Skillstore
- **Official skill collections:** Anthropic Skills, OpenAI Skills, Microsoft Skills, Google Skills, Supabase, Vercel
- **Security tools:** SkillCheck (github.com/agentigy/skillcheck)
- **Research/Benchmarks:** SkillsBench, Upskill (Hugging Face), SkillFlow (2026), Graph of Skills (2026)
- **Documentation:** Complete Guide to Building Skill for Claude (PDF)

## VoltAgent/awesome-agent-skills
1000+ curated skills from official dev teams and community:
- **Official collections by company size:**
  - NVIDIA: 155 skills across 17 products
  - Microsoft: 133 skills across 6 languages
  - Google: 17+ Workspace skills + Cloud skills
  - Anthropic: Document handling + development + creative
  - Sentry, Stripe, Vercel, Cloudflare, HuggingFace, Figma
- **Specialized domain curations:**
  - Garry Tan: 28 virtual engineering team skills
  - Dean Peters: 46 PM skills (tam-sam-som-calculator, opportunity-solution-tree)
  - Corey Haines: SaaS marketing stack
  - Addy Osmani: Web quality audits
- **Quality standards enforced:**
  - Third-person descriptions with trigger keywords
  - Progressive disclosure: <100 tokens metadata, <500 lines body
  - No absolute paths
  - Curated but not audited

## Security Scanning Ecosystem
- **agentskill.sh:** 44k+ skills with security scanning
- **SkillCheck:** GitHub scanner for identifying risks
- **Snyk agent-scan:** Commercial security scanner
- **Agent Trust Hub:** Trust infrastructure

## Context Element Analysis
The awesome-lists themselves are **not skill bundles** — they are **catalog registries**. However, they reveal critical context element patterns:
1. **Quality standards** act as implicit validation rules for skills
2. **Platform compatibility matrices** serve as deployment taxonomies
3. **Security scanning references** point to an emerging validation ecosystem
4. **Skill path specifications** (e.g., `.claude/skills/`, `.cursor/skills/`) are the **filesystem ontology** of agent skills

## Confidence
8/10 — Well-documented GitHub repos with structured data. The awesome-lists evolve rapidly.

## Sources
- https://github.com/skillmatic-ai/awesome-agent-skills
- https://github.com/VoltAgent/awesome-agent-skills
