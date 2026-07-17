---
type: Skill Bundle Example
title: Genesis Skills Repository (OSTI)
description: A large curated collection of 74 Claude Code skills following the Agent Skills open standard.
resource: https://gitlab.osti.gov/genesis/genesis-skills
---

# Genesis Skills Repository (OSTI)

**Bundle Type:** Government Lab · Domain-Specific Skill Catalog · 74 Skills
**Source:** https://gitlab.osti.gov/genesis/genesis-skills
**License:** Apache 2.0 (core) + mixed third-party
**Status:** Active (updated ~1 week ago)

## Overview

A large curated collection of 74 Claude Code skills following the Agent Skills open standard. Developed as part of the Genesis Mission at OSTI (US Department of Energy). Provides specialized capabilities for scientific discovery, engineering, HPC, and AI workflows.

## Key Characteristics

- **Scale**: 74 individual skills across 10+ domains
- **Distribution**: `unpack.sh` installer with domain filtering + `skill-search` discovery skill
- **Standard Compliance**: Full SKILL.md + YAML frontmatter format
- **Multi-harness**: Supports Claude, Codex, and Gemini via `.agents/skills/`
- **Domain Depth**: Strong coverage of HPC (Slurm, Frontier, Perlmutter, Aurora), plasma simulation (GS2, Gkeyll), and scientific data (Croissant, HDMF)

## Included Skill Categories

| Category              | Count | Notable Skills                          | Context Elements          |
|-----------------------|-------|-----------------------------------------|---------------------------|
| Genesis Core          | 3     | literature-search, academy, skill-search | Scientific workflows     |
| Anthropic Skills      | 16    | Document processing, canvas, web dev   | Claude-native            |
| OpenAI Skills         | 22    | Deployment, security review, AI apps   | Vercel/Netlify/Cloudflare|
| Superpowers           | 8     | TDD, debugging, code review            | Re-packaged              |
| LangChain Skills      | 8     | RAG, LangGraph patterns                | Persistence, middleware  |
| HuggingFace Skills    | 8     | Model hub, transformers, Gradio        | ML ecosystem             |
| HPC Skills            | 5     | Slurm, PBS, Frontier, Aurora           | HPC schedulers & systems |
| Plasma Simulation     | 2     | GS2, Gkeyll                            | Domain-specific physics  |
| ModCon BASE Data      | 3     | Croissant validation, HDMF, datacards  | Data standards           |

## Packaging & Distribution Patterns

- **Installer**: `unpack.sh` supports `--mode copy|symlink`, domain filtering, and harness selection
- **Discovery**: Dedicated `skill-search` skill for catalog navigation
- **Invocation**: `/skill-name` or context-activated
- **Governance**: CONTRIBUTING.md defines skill spec format, testing, and review process

## Relevance to Skill Bundles Research

This repository is a strong example of:

- **Large-scale skill bundling** at government lab level
- **Domain taxonomy** organization (HPC, plasma, scientific computing)
- **Re-packaging** of existing bundles (Superpowers)
- **Installation & discoverability** tooling as part of the bundle
- **Multi-agent-harness** compatibility

It demonstrates how a national lab is operationalizing the Agent Skills standard for real scientific and engineering use cases.

## Links

- Repository: https://gitlab.osti.gov/genesis/genesis-skills
- Issues: https://gitlab.osti.gov/genesis/genesis-skills/-/issues
- Contact: genesis@osti.gov

---

**Documented**: 2026-06-03 (Iteration 14 candidate)
**Source file**: `raw/2026-06-03/genesis-skills-osti.md`
