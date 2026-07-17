---
type: Skill Bundle Example
title: Spring AI — Generic Agent Skills for the Java Ecosystem
description: Spring AI's **Generic Agent Skills** implementation brings the Agent Skills open specification to the Java/Spring ecosystem.
resource: https://spring.io/blog/2026/01/13/spring-ai-generic-agent-skills
timestamp: '2026-05-26T00:00:00Z'
date: '2026-05-26'
---

# Spring AI — Generic Agent Skills for the Java Ecosystem

**Source:** https://spring.io/blog/2026/01/13/spring-ai-generic-agent-skills
**Date Added:** 2026-05-26 (Iteration 11)
**Dependency:** Spring AI 2.0.0-M2+, spring-ai-agent-utils v0.4.2
**Bundle Type:** Java Framework · LLM-Agnostic Platform · Generic Skill Implementation
**Confidence:** 8/10

## Name & Origin

Spring AI's **Generic Agent Skills** implementation brings the Agent Skills open specification to the Java/Spring ecosystem. Published January 2026 as the first in a five-part series on agentic patterns, it makes skills available to any Spring AI application regardless of LLM provider (OpenAI, Anthropic, Google Gemini, etc.).

## Skills Included

- Standard SKILL.md-based skill discovery and loading (Claude Code compatible)
- File system access tools for skill reference files
- Shell script execution for skill helper scripts
- Dynamic Tool Discovery integration for large skill inventories

## Context Elements

- **Three Core Tools Architecture:**
  1. `SkillsTool` (Required) — discovery + loading of SKILL.md, handles progressive disclosure
  2. `FileSystemTools` (Optional) — LLM reads reference files on demand
  3. `ShellTools` (Optional) — LLM executes helper scripts via local Bash
- **Progressive Disclosure (3-stage):** Discovery (name+description) → Activation (full SKILL.md) → Execution (scripts + references)
- **LSM Agnostic:** Skills work with OpenAI, Anthropic, Google Gemini, and any LLM supported by Spring AI
- **Integration:** Works with Dynamic Tool Discovery (tool search reduces token overhead by up to 85%) and Tool Argument Augmentation

## How Context Elements Support Skills

Spring AI's architecture formalizes the **three core capabilities** any skill runtime needs:

1. **SkillsTool = Discovery + Loading:** Handles progressive disclosure, separating metadata browsing from full instruction loading
2. **FileSystemTools = Reference Access:** Skills can reference documentation, templates, and data files without embedding them in SKILL.md
3. **ShellTools = Execution:** Scripts run locally, only output is added to context — saving tokens on long-running operations

**Example:** A YouTube transcript skill has SKILL.md instructing the LLM to run `uv run scripts/get_youtube_transcript.py <url>`. The script executes via ShellTools, only the resulting transcript enters context.

## Comparison: Generic vs Anthropic Native

| Dimension | Spring AI Generic | Anthropic Native |
|-----------|------------------|-----------------|
| Environment | Your infrastructure | Anthropic cloud sandbox |
| Model Support | Any LLM | Claude only |
| Resource Access | Local filesystem, network | Restricted sandbox |
| Security | No built-in sandboxing | Cloud sandbox |
| Portability | Portable across runtimes | Claude-specific |

## Critical Considerations

- **No sandboxing:** Scripts execute on host machine — containers (Docker/Kubernetes) recommended
- **No approval mechanism:** Custom ToolCallback wrappers needed for sensitive operations
- **Series roadmap:** Part 2 covers AskUserQuestionTool, Part 3 TodoWriteTool, Part 4 Subagent Orchestration, Part 5 A2A Integration

## Reproducibility

High - public Spring blog post with complete code examples, Maven/Gradle dependency available, open-source spring-ai-agent-utils library.

## Bundle Links
- [microsoft agent framework skills](microsoft-agent-framework-skills.md) — .NET/Python counterpart
- [agent skills spec](agent-skills-spec.md) — The open standard Spring AI implements
- [claude api skills integration](claude-api-skills-integration.md) — Anthropic's native implementation (Generic vs Native comparison)
- [ylang labs agent skills overview](ylang-labs-agent-skills-overview.md) — Defines the "recipes vs kitchen" metaphor for Skills vs MCP
