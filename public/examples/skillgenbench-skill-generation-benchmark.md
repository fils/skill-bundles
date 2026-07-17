---
type: Skill Bundle Example
title: 'SkillGenBench: Benchmarking Skill Generation Pipelines'
description: SkillGenBench is a benchmark for evaluating **skill generation pipelines** — not the skills themselves, not the agents that use them, but the process of distilling skills from raw source material.
timestamp: '2026-07-13T00:00:00Z'
date: 2026-07-13
sources:
- Medium (Vishal Mysore, May 2026)
- Zhou et al., 2026
skills_included:
- Generator pipeline
- Executor (standardized)
context_elements:
- Generator-executor decoupling
- Standardized SKILL.md output
- Two source types (repository vs. document)
- Pass@3 metric
- 8 domain coverage
- Negative transfer detection
composition: 'Decouples generator from executor: [Raw Corpora] → [Generator] → [Standardized SKILL.md] → [Executor] → [Downstream Tasks]. Measures procedure-to-skill distillation directly.'
reproducibility: '187 tasks across 8 domains. Open benchmark. Repository-grounded pass@3: 7-16%. Document-grounded pass@3: 23-27%.'
rating: 8
---

# SkillGenBench: Why Generating Skills Is Harder Than Using Them

**Origin:** Zhou et al., 2026 (summarized by Vishal Mysore, Medium, May 2026)

## Overview

SkillGenBench is a benchmark for evaluating **skill generation pipelines** — not the skills themselves, not the agents that use them, but the process of distilling skills from raw source material. It fills the gap between "skills are valuable when done well" and "harmful when done poorly."

## Pipeline

```
[Raw Corpora] → [Generator] → [Standardized SKILL.md] → [Executor] → [Downstream Tasks]
```

The generator-executor decoupling isolates skill distillation from planning ability and retrieval recall.

## Benchmark Scope

| Dimension | Value |
|-----------|-------|
| Tasks | 187 |
| Domains | 8 (Audio, Image, Web, Security, BioMed, Video, Data, Reasoning) |
| Source types | 2 (Repository-grounded, Document-grounded) |
| Metric | Pass@3 |

## Two Source Types

### Repository-Grounded
- Source: real code repository (Python, configs, READMEs)
- Procedures: implicit in code structure, function relations, entry points
- LLM must recover latent workflows and distill into callable skills
- **Pass@3: 7-16%** (extremely hard)

### Document-Grounded
- Source: long-form technical document (API specs, manuals)
- Procedures: explicit but scattered across sections
- **Pass@3: 23-27%** (moderate)

## Key Findings

- Skill generation is **2-3x harder** than skill use
- Auto-generated skills can induce **negative transfer** (agent worse with skill than without)
- Repository-grounded generation is extremely difficult (7-16%)
- SkillsBench showed curated skills improve performance; SkillGenBench shows generating them is the bottleneck

## Context Elements

- **Generator-executor decoupling** — isolates skill distillation quality
- **Standardized SKILL.md** — Anthropic Agent Skills format as output
- **Two source types** — repository vs. document grounded
- **Pass@3 metric** — three attempts per task
- **8 domain coverage** — broad, including Security and BioMed
- **Negative transfer detection** — identifies when skills harm performance

## Relation to Skill Bundle Patterns

SkillGenBench represents the **skill generation evaluation** dimension:
- Complements [skillsbench agent skills benchmark](skillsbench-agent-skills-benchmark.md) — SkillsBench evaluates skill use; SkillGenBench evaluates skill generation
- Relates to [evoskill automated skill discovery](evoskill-automated-skill-discovery.md) — EvoSkill is a skill generator that would be evaluated by SkillGenBench
- Connects to [skillopt trainable skill parameters](skillopt-trainable-skill-parameters.md) — SkillOpt is a skill optimizer; SkillGenBench measures the generation step that precedes optimization

## Key Insight

Skill generation is the bottleneck in the skill ecosystem, not skill use. Repository-grounded skill generation (7-16% pass@3) is extraordinarily difficult because procedures are implicit in code. Auto-generated skills risk negative transfer. This benchmark fills the critical gap between "skills help when done right" and "skills hurt when done wrong."

