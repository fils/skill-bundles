# Agent Skills Overview
Source: https://agentskills.io/home
Date ingested: 2026-06-02

## What are Agent Skills?

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.

At its core, a skill is a folder containing a SKILL.md file. This file includes metadata (name and description, at minimum) and instructions that tell an agent how to perform a specific task.

### Standard Skill Folder Structure
```
my-skill/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

## Why Agent Skills?

Skills package procedural knowledge and context into portable, version-controlled folders that agents load on demand.

Key Benefits:
- Domain expertise — Capture specialized knowledge (legal review, data pipelines, formatting) as reusable instructions
- Repeatable workflows — Turn multi-step tasks into consistent, auditable procedures
- Cross-product reuse — Build once, use across any skills-compatible agent

## How Do Agent Skills Work?

Agents use progressive disclosure in three stages:

1. Discovery — Load only name and description at startup
2. Activation — Read full SKILL.md when a task matches the description
3. Execution — Follow instructions, run bundled code, or load referenced files as needed

Full instructions load only when needed, keeping context footprint small.

## Where Can I Use Agent Skills?

Supported by many AI tools and agentic clients, including Claude / Claude Code, Cursor, VS Code, GitHub Copilot, etc.

See full list at agentskills.io.

## Open Development

- Originally developed by Anthropic
- Released as an open standard
- Community contributions welcome

Community Links:
- GitHub: https://github.com/agentskills/agentskills
- Discord: https://discord.gg/MKPE9g8aUy

## Get Started

- Quickstart: https://agentskills.io/skill-creation/quickstart
- Specification: https://agentskills.io/specification

Documentation Index: https://agentskills.io/llms.txt

Note: This source focuses on the core spec but does not yet include SHACL/SSSOM examples in the overview. High signal for skill bundle structure.