---
title: "PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions"
date: 2026-07-13
sources: ["arXiv:2508.02866"]
skills_included: ["Provenance capture system", "Agent interaction tracking"]
context_elements: ["W3C PROV extension", "MCP (Model Context Protocol) integration", "Agent-centric metadata (prompts, responses, decisions)", "Cross-facility provenance (edge/cloud/HPC)", "Near real-time capture system", "Provenance graph (agent actions as first-class)"]
composition: "Extends W3C PROV standard with MCP concepts to capture agent decisions, prompts, and responses as first-class provenance components in end-to-end workflow graphs."
reproducibility: "Open-source provenance capture system. Cross-facility evaluation (edge, cloud, HPC). Oak Ridge + Argonne National Labs."
rating: 8
---

# PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows

**Origin:** Oak Ridge National Lab + Argonne National Lab (arXiv:2508.02866, Aug 2025)
**Authors:** Renan Souza, Amal Gueroudji, Stephen DeWitt, Daniel Rosendo, Tirthankar Ghosal, Robert Ross, Prasanna Balaprakash, Rafael Ferreira da Silva

## Overview

In agentic workflows, autonomous agents plan tasks, interact with humans and peers, and shape scientific outcomes. When agent outputs feed into other agents' inputs, errors can propagate and compound. PROV-AGENT extends the W3C PROV standard and leverages MCP (Model Context Protocol) to capture agent interactions — prompts, responses, and decisions — as first-class provenance components in end-to-end workflow graphs.

## Problem

Traditional provenance approaches capture data flow and task execution but fail to represent:
- **Reasoning processes** behind agent decisions
- **Model invocations** and their parameters
- **Contextual information** driving agent choices

Without this, root cause analysis is impossible when unexpected behavior occurs in multi-agent workflows.

## Three Contributions

1. **Provenance model** — extends W3C PROV + incorporates MCP concepts for agent actions
2. **Near real-time system** — open-source, captures agentic provenance during execution
3. **Cross-facility evaluation** — edge devices, cloud services, HPC systems

## Critical Provenance Queries

1. What specific input data led an agent to make a particular decision?
2. How did an agent's decision influence control/data flow within the workflow?
3. Which downstream outputs were affected by a specific agent interaction?
4. Where did erroneous data originate, and through which agents' decisions did it propagate?

## Context Elements

- **W3C PROV extension** — standards-based provenance model
- **MCP integration** — Model Context Protocol concepts for agent-tool interactions
- **Agent-centric metadata** — prompts, responses, decisions as first-class provenance
- **Cross-facility** — edge + cloud + HPC provenance capture
- **Near real-time** — open-source capture system
- **Provenance graph** — unified graph with agent actions as first-class components

## Relation to Skill Bundle Patterns

PROV-AGENT addresses the **provenance and traceability** dimension of skill bundles:
- Complements [[supply-chain-agentic-factory-in-toto]] (SLSA/in-toto for supply chain) — PROV-AGENT captures runtime provenance
- Extends [[ai-km-ontology-skills]] pattern — both connect skills to formal knowledge artifacts
- Relates to W3C Agent Protocol Community Group efforts for interoperable agent standards

## Key Insight

Agent decisions, prompts, and responses must be first-class provenance components — not just data flow. The W3C PROV + MCP combination provides a standards-based foundation for agent workflow traceability, enabling root cause analysis when agents hallucinate or reason incorrectly in multi-step workflows.

[[backlinks]]
