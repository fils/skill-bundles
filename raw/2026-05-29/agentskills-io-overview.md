# Agent Skills Overview - https://agentskills.io/home

**Extracted:** 2026-05-29

**Content:**

**Agent Skills Overview**

## What are Agent Skills?

Agent Skills are a **lightweight, open format** for extending AI agent capabilities with specialized knowledge and workflows. A skill is a folder containing a required `SKILL.md` file with metadata (`name`, `description`) and instructions.

```
my-skill/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

## Why Agent Skills?

Skills package procedural knowledge and context into portable, version-controlled folders. Benefits include:

- **Domain expertise**: Capture specialized knowledge (legal processes, data pipelines, formatting) as reusable instructions
- **Repeatable workflows**: Convert multi-step tasks into consistent, auditable procedures
- **Cross-product reuse**: Build once, use across any compatible agent

## How Agent Skills Work

Agents load skills via **progressive disclosure** in three stages:

1. **Discovery**: Load only `name` and `description` at startup
2. **Activation**: Read full `SKILL.md` when a task matches the skill's description
3. **Execution**: Follow instructions, optionally running bundled code or loading files

This keeps context usage minimal even with many skills available.

## Supported Clients

Agent Skills are supported by a large and growing ecosystem of AI tools and agentic clients, including:

- **Major platforms**: Claude / Claude Code, Cursor, GitHub Copilot, VS Code, OpenAI Codex
- **Agent frameworks**: OpenHands, Letta, fast-agent, Goose, Roo Code
- **Enterprise/Other**: Snowflake Cortex, Databricks Genie, Spring AI, Tabnine, Gemini CLI, Mistral AI Vibe, and many others (Factory, Amp, Emdash, Firebender, etc.)

Full list available at the [Client Showcase](https://agentskills.io/clients).

## Open Development

- Originally developed by **Anthropic**
- Released as an **open standard**
- Contributions welcome from the ecosystem
- Discussion: [GitHub](https://github.com/agentskills/agentskills) • [Discord](https://discord.gg/MKPE9g8aUy)

## Get Started

- **[Quickstart](https://agentskills.io/skill-creation/quickstart)**: Create your first Agent Skill
- **[Specification](https://agentskills.io/specification)**: Complete format specification

> **Documentation Index**: Fetch the complete index at [https://agentskills.io/llms.txt](https://agentskills.io/llms.txt) to discover all pages.