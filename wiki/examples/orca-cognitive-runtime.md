---
type: Skill Bundle Example
title: 'ORCA: Open Runtime for Capable Agents'
description: '- **GitHub:** https://github.com/gfernandf/agent-skills (43 stars, 407 commits) - **Author:** Guillermo Fernandez (gfernandf) - **License:** Apache-2.0 - **Language:** Python (99.3%)'
resource: https://github.com/gfernandf/agent-skills
timestamp: '2026-07-12T00:00:00Z'
date: 2026-07-12
source: https://github.com/gfernandf/agent-skills
authors:
- Guillermo Fernandez
github_stars: 43
license: Apache-2.0
signal: 8
context_elements:
- Capability registry
- DAG scheduler
- Policy gates
- Provenance tracking
- Canonical taxonomy
- MCP integration
---

# ORCA: Open Runtime for Capable Agents

## Origin

- **GitHub:** https://github.com/gfernandf/agent-skills (43 stars, 407 commits)
- **Author:** Guillermo Fernandez (gfernandf)
- **License:** Apache-2.0
- **Language:** Python (99.3%)

## Skills Included

ORCA is a complete **skill bundle runtime**:
- **122 capabilities** with deterministic Python baselines (no API keys needed)
- **36 ready-to-use skills** composed from those capabilities
- Skills are multi-step workflows defined as DAGs

## Context Elements

### Capability Registry (122 capabilities)
Declarative YAML contracts:
```yaml
id: doc.content.chunk
description: Split a document into semantic chunks
input:
  content: { type: string }
  max_tokens: { type: integer, default: 512 }
output:
  chunks: { type: array, items: { type: string } }
```

### DAG Scheduler
- Resolves dependencies, runs steps in parallel
- **Policy gates** at each step
- Cognitive state tracking

### Canonical Taxonomy
- **184/184 capabilities covered** by guardrails
- Canonical taxonomy alignment (agent.*, eval.*, model.*, text.*, ops.*, provenance.*, task.*)
- Strict verification: no aliases, deprecated-selection guard

### Provenance Tracking
- Versioning and provenance checks
- Production-readiness controls
- PR gate enforcement

### MCP Integration
- MCP server support
- Auto-bindings for OpenAI and PythonCall

## Composition Notes

ORCA is a reference implementation for [three layer validation stack](../concepts/three-layer-validation-stack.md):
1. **Capabilities** (base layer) — 122 standardized, deterministic baselines
2. **Skills** (composition layer) — DAG-based workflows with dependency resolution
3. **Policy gates** (governance layer) — runtime enforcement at each step

### Key Differentiators
| Dimension | Traditional Frameworks | ORCA |
|---|---|---|
| Actions | Code functions | Declarative YAML capabilities |
| Composition | Imperative chains | DAG-based skills |
| Execution | LLM-dependent | Deterministic baselines + LLM fallback |
| Portability | Framework-locked | Bind to any backend |

### Adapters
- LangChain, CrewAI, Semantic Kernel
- MCP server support

## Reproducibility

- `pip install agent-skills`
- Open-source, Apache-2.0
- 407 commits, active development (last commit Jul 1, 2026)
- Paper run artifacts published for external reproducibility

## Connections

- Complete runtime implementation of capability→skill→governance stack
- Canonical taxonomy maps to [agent skills spec](agent-skills-spec.md) naming conventions
- Provenance tracking connects to [supply chain agentic factory in toto](supply-chain-agentic-factory-in-toto.md)'s SLSA/in-toto approach
- DAG composition is a formalization of [skillcraft benchmark](skillcraft-benchmark.md)'s auto-composition pattern

