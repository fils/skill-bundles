---
type: Skill Bundle Example
title: Agent Skills for LLMs — Architecture, Acquisition, Security (arXiv Survey)
description: 'The first **comprehensive academic survey** of the Agent Skills landscape, organized along four axes: architectural foundations, skill acquisition, deployment at scale, and security.'
resource: https://arxiv.org/html/2602.12430v3
timestamp: '2026-05-26T00:00:00Z'
date: '2026-05-26'
---

# Agent Skills for LLMs — Architecture, Acquisition, Security (arXiv Survey)

**Source:** https://arxiv.org/html/2602.12430v3
**Repository:** https://github.com/scienceaix/agentskills
**Date Added:** 2026-05-26 (Iteration 11)
**Authors:** Renjun Xu, Yang Yan (Zhejiang University)
**License:** CC BY-NC-ND 4.0
**Bundle Type:** Academic Survey · Skill Taxonomy · Security Governance Framework
**Confidence:** 9/10

## Name & Origin

The first **comprehensive academic survey** of the Agent Skills landscape, organized along four axes: architectural foundations, skill acquisition, deployment at scale, and security. Published on arXiv in February 2026, it provides the most thorough scholarly treatment of skill bundles as a research domain.

## Skills Included

- Taxonomy of skill types and composition patterns
- Skill acquisition methodologies (RL, autonomous discovery, compositional synthesis)
- Deployment patterns (computer-use agent stack, benchmarks)
- Security governance: **Skill Trust and Lifecycle Governance Framework** with four-tier gate-based permission model

## Context Elements

- **Architectural Taxonomy:** Three-level progressive disclosure (metadata 50t → instructions 2kt → scripts 15kt), SKILL.md specification, MCP integration
- **Paradigm Timeline:** Prompt Engineering (2022-23) → Tool Use (2023-24) → Skill Engineering (2025-present) — validates the "transitional layer" thesis
- **Skills vs MCP Formal Distinction:** Skills = procedural knowledge (modifies preparation/context); MCP = tool connectivity (modifies available tools) — the definitive academic articulation
- **Security Finding:** 26.1% of community-contributed skills contain vulnerabilities
- **Skill Trust Framework:** Four-tier permission model with gate-based escalation

## Key Findings

**From the Paradigm Shift Section:**
> *"A PDF-processing skill does not merely expose a 'fill form' function; it teaches the agent how to approach PDF manipulation, which libraries to use, what edge cases to handle, and what code to execute."*

This formalizes the distinction between skills and tool calls — a skill modifies the agent's **preparation and understanding**, not just its available functions.

**Four Composition Axes (from the paper's hidden structure):**
The survey maps composition patterns along (a) intelligence dimension — static → adaptive → learning → optimizing → intelligent, and (b) composition dimension — single → pipeline → hierarchical → mesh → swarm. This mirrors the [sc25 autonomous science workflows](../papers/sc25-autonomous-science-workflows.md) framework, confirming cross-domain convergence.

## How Context Elements Support Skills

The survey provides the **formal academic foundation** for the entire skill bundle research program:

1. **Architecture:** Documents progressive disclosure, SKILL.md format, and execution lifecycle — provides the canonical reference for [agent skills spec](agent-skills-spec.md)
2. **Acquisition:** Explores RL-based skill learning, autonomous discovery, and compositional synthesis — research directions for future bundles
3. **Deployment:** Computer-use agent stack, benchmarking methodologies — informs [skillsbench agent skills benchmark](skillsbench-agent-skills-benchmark.md)
4. **Security:** 26.1% vulnerability rate validates the concerns raised by [mondoo agent skills security](mondoo-agent-skills-security.md) and [owasp agentic skills top 10](owasp-agentic-skills-top-10.md)

## Composition Notes

This survey serves as a **meta-catalog** for the entire wiki:

| Survey Section | Corresponding Wiki Examples |
|----------------|---------------------------|
| Architecture (SKILL.md) | [agent skills spec](agent-skills-spec.md), [ylang labs agent skills overview](ylang-labs-agent-skills-overview.md), [spring ai agent skills](spring-ai-agent-skills.md), [microsoft agent framework skills](microsoft-agent-framework-skills.md) |
| Security | [owasp agentic skills top 10](owasp-agentic-skills-top-10.md), [mondoo agent skills security](mondoo-agent-skills-security.md), [purplebox supply chain security](purplebox-supply-chain-security.md) |
| Composition | [graph of skills dependency retrieval](graph-of-skills-dependency-retrieval.md), [graphguard os guardrails](graphguard-os-guardrails.md) |
| Benchmarks | [skillsbench agent skills benchmark](skillsbench-agent-skills-benchmark.md), [dspy agent skills v023](dspy-agent-skills-v023.md) |

## Reproducibility

High — open-access arXiv paper under CC BY-NC-ND 4.0, accompanying GitHub repo with resources.

## Bundle Links
- [owasp agentic skills top 10](owasp-agentic-skills-top-10.md) — AST10 validates the survey's 26.1% vulnerability finding
- [agent skills spec](agent-skills-spec.md) — The SKILL.md specification documented in the survey's architectural section
- [skillsbench agent skills benchmark](skillsbench-agent-skills-benchmark.md) — One of the benchmarks the survey analyzes
- [sc25 autonomous science workflows](../papers/sc25-autonomous-science-workflows.md) — Convergent composition framework (same single→pipeline→hierarchical→mesh→swarm pattern)
