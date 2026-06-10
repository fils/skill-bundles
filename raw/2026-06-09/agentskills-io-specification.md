# Agent Skills Specification (agentskills.io)

**Source:** https://agentskills.io/home
**Date Retrieved:** 2026-06-09
**Type:** Official Specification Website - Open Standard Definition

---

## Summary

**Agent Skills** is an **open standard** (originally developed by **Anthropic**) designed to extend AI agent capabilities through a lightweight, portable format. It allows agents to access specialized knowledge and procedural workflows on demand.

This is the **foundational specification** that defines what a "skill" is and how skill bundles should be structured. All skill bundles in this research should conform to or extend this specification.

---

## Core Definition

> "A \"skill\" is a **structured folder** containing a mandatory `SKILL.md` file and optional supporting resources. It packages instructions and context into version-controlled units."

### Standard Directory Structure

```
my-skill/
├── SKILL.md          # Required: metadata (name/description) + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

---

## Core Benefits (from spec)

- **Domain Expertise:** Captures specialized processes (e.g., legal reviews, data pipelines) as reusable instructions
- **Repeatable Workflows:** Converts multi-step tasks into auditable, consistent procedures
- **Cross-Product Reuse:** Skills are portable and work across any compatible agentic client
- **Context Efficiency:** Uses "progressive disclosure" to minimize the agent's context window footprint

---

## Progressive Disclosure (Three-Stage Interaction Model)

This is a **key architectural pattern** for skill bundles:

1. **Discovery:** At startup, the agent only loads the **name and description** to identify relevance
2. **Activation:** When a task matches the description, the agent reads the **full `SKILL.md` instructions** into its context
3. **Execution:** The agent follows instructions, executing bundled code or loading referenced files as required

---

## Ecosystem & Compatibility (Formal Adoption)

The specification lists **officially compatible clients** — this is a **catalog/registry artifact**:

### Major AI Platforms
- **Claude** (Anthropic)
- **GitHub Copilot**
- **Google AI Edge**
- **OpenAI Codex**
- **Mistral AI Vibe**

### IDE & Code Tools
- **VS Code**
- **Cursor**
- **Trae**
- **Roo Code**
- **Tabnine**
- **Qodo**

### Agent Frameworks & CLIs
- **Claude Code**
- **Goose**
- **Letta**
- **OpenHands**
- **Spring AI**
- **Gemini CLI**

### Enterprise Tools
- **Snowflake Cortex Code**
- **Databricks Genie Code**

---

## Key Specification Artifacts

1. **`/llms.txt`** — Complete documentation index (token-optimized for LLM consumption)
2. **Skill Creation Quickstart** — `/skill-creation/quickstart`
3. **Full Format Specification** — `/specification`
4. **Development Hub** — GitHub: `agentskills/agentskills`
5. **Community** — Discord: `discord.gg/MKPE9g8aUy`

---

## Composition Notes

The Agent Skills specification provides the **base layer** for all skill bundles:

1. **Minimal viable skill** = `SKILL.md` only (metadata + instructions)
2. **Rich skills** add: `scripts/`, `references/`, `assets/`, custom directories
3. **Bundles** = collections of skills with shared context (validation, mapping, rules, vocabularies, taxonomies, ontologies)
4. **Progressive disclosure** is the key UX pattern that makes large bundles tractable
5. **Cross-platform portability** is a design goal — same skill works in Claude Code, Codex, Copilot, etc.

---

## Key Quotes

> "Agent Skills is an **open standard** (originally developed by **Anthropic**) designed to extend AI agent capabilities through a lightweight, portable format."

> "A \"skill\" is a **structured folder** containing a mandatory `SKILL.md` file and optional supporting resources. It packages instructions and context into version-controlled units."

> "Agents interact with skills in three distinct stages to maintain efficiency:
> 1. **Discovery:** At startup, the agent only loads the **name and description** to identify relevance.
> 2. **Activation:** When a task matches the description, the agent reads the **full `SKILL.md` instructions** into its context.
> 3. **Execution:** The agent follows instructions, executing bundled code or loading referenced files as required."

> "**Cross-Product Reuse:** Skills are portable and work across any compatible agentic client."

---

## Relevance to Skill Bundle Research

This specification is the **canonical reference** for:
- What constitutes a "skill" (atomic unit)
- How skills should be packaged (directory structure, `SKILL.md` format)
- How agents discover and activate skills (progressive disclosure)
- What compatibility means across agent runtimes
- The ecosystem of tools that support the standard

All skill bundles discovered in this research should be evaluated against this specification for compliance and extension patterns.