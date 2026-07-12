# ORCA: Open Runtime for Capable Agents

**Source:** https://github.com/gfernandf/agent-skills
**Date:** 2026-07-12
**Author:** Guillermo Fernandez (gfernandf)
**GitHub Stars:** 43
**License:** Apache-2.0
**Signal:** 8/10

## Overview

ORCA (Open Runtime for Capable Agents) is an open-source Python framework that treats agent actions as **capabilities** — declarative YAML contracts that can be wired to any backend: pure Python, OpenAI, or external APIs.

### Core Concepts

**Capabilities** — Declarative YAML contracts:
```yaml
id: doc.content.chunk
description: Split a document into semantic chunks
input:
  content: { type: string }
  max_tokens: { type: integer, default: 512 }
output:
  chunks: { type: array, items: { type: string } }
```

**Skills** — Multi-step workflows composed from capabilities as DAGs:
```yaml
id: document.summarize
steps:
  - id: chunk
    capability: doc.content.chunk
  - id: summarize
    capability: text.body.summarize
    depends_on: [chunk]
  - id: compile
    capability: text.report.compile
    depends_on: [summarize]
```

### What's Included
- **122 capabilities** with deterministic Python baselines (no API keys needed)
- **36 ready-to-use skills** composed from those capabilities
- **DAG scheduler** with policy gates and cognitive state tracking
- **Scaffold wizard** to build new skills in minutes
- **Auto-bindings** for OpenAI and PythonCall
- **Adapters** for LangChain, CrewAI, and Semantic Kernel
- **MCP server** support
- **184/184 capabilities covered** by guardrails (canonical taxonomy alignment)
- **Provenance checks** and versioning

### Key Differentiators vs Traditional Frameworks
| Dimension | Traditional Frameworks | ORCA |
|---|---|---|
| Actions | Code functions | Declarative YAML capabilities |
| Composition | Imperative chains | DAG-based skills |
| Execution | LLM-dependent | Deterministic baselines + LLM fallback |
| Portability | Framework-locked | Bind to any backend |

## Relevance to Skill Bundles

ORCA is a **complete skill bundle runtime** with several novel elements:
1. **Capability registry** — 122 standardized capabilities with deterministic baselines (not just LLM calls)
2. **DAG-based skill composition** — skills are explicit DAGs of capabilities with dependency resolution
3. **Policy gates** — governance built into the runtime (not just the skill definition)
4. **Provenance tracking** — versioning and provenance checks on capabilities
5. **Canonical taxonomy** — 184 capabilities mapped to a canonical registry with strict coverage verification
6. **MCP integration** — skills can be exposed via MCP

This is a reference implementation for [[three-layer-validation-stack]] — capabilities (base), skills (DAG composition), and policy gates (governance).

## Key Quotes

> "ORCA is a runtime for executable cognition. Skills turns repeatable agent reasoning into executable skills: reusable, testable, observable, and portable"

> "The scheduler resolves dependencies, runs steps in parallel when possible, and enforces policies at each gate"

## Links
- GitHub: https://github.com/gfernandf/agent-skills
- Registry: https://github.com/gfernandf/agent-skill-registry
- Docs: gfernandf.github.io/agent-skills
- Blog: https://dev.to/gfernandf/introducing-orca-executable-skills-and-capabilities-for-ai-agent-workflows-120o
