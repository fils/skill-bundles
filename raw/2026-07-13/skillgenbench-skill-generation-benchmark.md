# SkillGenBench: Why Generating Skills Is Harder Than Using Them

**Source:** Medium article by Vishal Mysore (May 2026), based on Zhou et al., 2026
**Signal Rating:** 8/10

## What SkillGenBench Studies

SkillGenBench is a benchmark for evaluating **skill generation pipelines** — not the skills themselves, and not the agents that use them, but the process of distilling skills from raw source material.

```
[Raw Corpora] → [Generator] → [Standardized SKILL.md] → [Executor] → [Downstream Tasks]
```

The setup decouples the generator and executor, measuring procedure-to-skill distillation directly without conflating it with the executor's planning ability or retrieval recall.

## Benchmark Scope

- **187 tasks** across 8 domains (Audio, Image, Web, Security, BioMed, Video, Data, Reasoning)
- **Two source types:** Repository-grounded and Document-grounded
- **Two generation settings:** (details truncated, but involves different execution conditions)

## Source Types

### 1. Repository-Grounded Sources
- Source material: real code repository (Python files, config scripts, READMEs)
- Procedures implicit: encoded in code structure, function call relations, entry points, environment variables
- LLM must recover latent workflows and distill them into callable skills
- **Difficulty:** Extremely high — Pass@3 scores: 7-16%

### 2. Document-Grounded Sources
- Source material: long-form technical document (API specs, system manuals)
- Procedures explicit but scattered: combining Section 2 constraint + Section 4 parameter + Section 8 validation
- **Difficulty:** Moderate — Pass@3 scores: 23-27%

## Key Findings

- SkillsBench showed curated skills substantially improve downstream task performance
- But automatically generated skills, especially on-the-fly, are often unstable
- Can induce **negative transfer** (agent performs worse with the skill than without it)
- Skill generation is much harder than skill use
- Repository-grounded skill generation is extremely difficult (7-16% pass@3)

## Context Elements

- **Generator-executor decoupling:** Isolates skill distillation from planning/retrieval
- **Standardized SKILL.md output:** Anthropic Agent Skills format
- **Domain diversity:** 8 domains including Security, BioMed, Video
- **Two source types:** Repository vs. Document grounded
- **Pass@3 metric:** Three attempts per task

## Key Insights

- Skill generation is the bottleneck, not skill use
- Repository-grounded generation (7-16%) is 2-3x harder than document-grounded (23-27%)
- Negative transfer is a real risk for auto-generated skills
- Benchmark fills the gap between "skills are valuable when done well" and "harmful when done poorly"
