---
type: Skill Bundle Example
title: 'AI-KM: Agent Skills and Ontology-Driven Knowledge Modeling'
description: '- **Journal:** SoftwareX, Volume 35, September 2026, 102855 - **Authors:** Haolin Wen, Songyi Wang, Bingjie Li, Junfen Xiong, Tong Chen, Xin Liang - **DOI:** https://doi.org/10.1016/j.softx.2026.102855'
resource: https://www.sciencedirect.com/science/article/pii/S235271102600347X
timestamp: '2026-07-12T00:00:00Z'
date: 2026-07-12
source: https://www.sciencedirect.com/science/article/pii/S235271102600347X
authors:
- Wen
- Wang
- Li
- Xiong
- Chen
- Liang
journal: SoftwareX
signal: 8
context_elements:
- Ontology-driven knowledge modeling
- Agentic skill framework
- Closed-loop knowledge cycle
- Natural language entity extraction
---

# AI-KM: Agent Skills and Ontology-Driven Knowledge Modeling (v6.6.1)

## Origin

- **Journal:** SoftwareX, Volume 35, September 2026, 102855
- **Authors:** Haolin Wen, Songyi Wang, Bingjie Li, Junfen Xiong, Tong Chen, Xin Liang
- **DOI:** https://doi.org/10.1016/j.softx.2026.102855
- **License:** Open Access

## Skills Included

AI-KM v6.6.1 introduces two integrated capabilities:

### 1. Agentic Skill Framework
- Encapsulates complex AI behaviors as **reusable, conversation-invokable skills**
- Supports both:
  - **Predefined expert skills** — manually authored
  - **Autonomous planning mode** — for novel tasks where no predefined skill exists
- Skills invoked through conversation (accessible to domain experts)

### 2. Ontology-Driven Knowledge Modeling
- Formal, machine-interpretable ontologies (not simple slice structures)
- Built through **natural language entity extraction**
- Domain experts encode expertise as structured knowledge

## Context Elements

### Closed-Loop Design
Knowledge ↔ Skills feedback cycle:
1. Knowledge → Ontology (formal representation via NL extraction)
2. Ontology → Skills (executable behavior)
3. Skills → Knowledge (feedback from execution)

### Natural Language → Ontology
- Entity extraction from natural language input
- Lowers barrier to formal knowledge modeling
- Domain experts don't need ontology engineering skills

## Composition Notes

AI-KM is a rare example of **skills + ontologies** in a single integrated system:
1. Skills are conversation-invokable (not just CLI/file-based)
2. Autonomous planning mode for novel tasks (no predefined skill needed)
3. Ontology built from NL extraction (no manual ontology engineering)
4. Closed-loop: knowledge → skills → knowledge feedback

This directly implements the "skills bundled with ontologies" pattern from the skill bundle taxonomy.

## Reproducibility

- SoftwareX journal (open access, peer-reviewed software)
- Previous version: https://doi.org/10.1016/j.softx.2024.101840

## Connections

- Skills + ontology integration is the core skill bundle thesis
- Conversation-invokable skills contrast with file-based [agent skills spec](agent-skills-spec.md)
- Autonomous planning mode connects to [skillcraft benchmark](skillcraft-benchmark.md)'s auto-composition
- Closed-loop design is a novel governance pattern (skills validate knowledge, knowledge guides skills)

