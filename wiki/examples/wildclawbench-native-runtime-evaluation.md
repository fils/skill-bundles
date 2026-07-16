---
type: Skill Bundle Example
title: 'WildClawBench: Native-Runtime Long-Horizon Agent Evaluation'
description: 'WildClawBench is a **native-runtime** benchmark for AI agents: 60 human-authored bilingual multimodal tasks run inside Docker containers hosting the **actual** CLI harnesses used in deployment (OpenClaw, Claude Code,...'
resource: https://arxiv.org/abs/2605.10912
timestamp: '2026-07-16T00:00:00Z'
date: 2026-07-16
sources:
- arXiv:2605.10912
- https://github.com/InternLM/WildClawBench
skills_included:
- Optional category skill sets
- Multi-harness skill packaging
- OpenClaw/Claude Code/Codex/Hermes skill load
context_elements:
- Native-runtime Docker harness
- Hybrid grading (rules + env audit + LLM/VLM judge)
- Skill-set ablation methodology
- ClawHub-aligned task taxonomy
- Multi-harness comparative protocol
composition: 'Benchmark bundle: 60 bilingual multimodal tasks × 4 real CLI harnesses × optional domain skill sets; measures long-horizon work not mock APIs.'
reproducibility: Open tasks, code, containers (InternLM/WildClawBench, 477★). 19 models evaluated; best 62.2% Claude Opus 4.7 / OpenClaw.
rating: 9
---

# WildClawBench: Native-Runtime Long-Horizon Agent Evaluation

**Origin:** InternLM / Shanghai AI Lab et al., arXiv:2605.10912, May 2026
**GitHub:** https://github.com/InternLM/WildClawBench (~477★)
**Leaderboard:** https://internlm.github.io/WildClawBench/

## Overview

WildClawBench is a **native-runtime** benchmark for AI agents: 60 human-authored bilingual multimodal tasks run inside Docker containers hosting the **actual** CLI harnesses used in deployment (OpenClaw, Claude Code, Codex, Hermes Agent), with real tools rather than mock service APIs.

## Architecture

1. **Task specs** — Markdown + YAML metadata (id, category, time budget), agent-facing prompt, rubrics, optional skills/env vars
2. **Runtime** — Isolated Docker workspace; ground-truth and grading assets mounted only after agent exit (anti-leakage)
3. **Harnesses** — OpenClaw, Claude Code, Codex CLI, Hermes Agent under unified OpenRouter access
4. **Grading** — Hybrid: deterministic rule checks + environment-state auditing + LLM/VLM judge for semantic criteria
5. **Skill ablation** — Category-relevant skill sets added to measure marginal skill impact

## Key Findings

- Best model (Claude Opus 4.7) reaches only **62.2%** overall under OpenClaw; all others <60%
- **Harness switch alone** can shift a single model by up to **18 percentage points**
- Skill augmentation: **mixed**, baseline-dependent; GPT-5.4 gains most (+5.2 overall, **+22.4** Code Intelligence)
- Code Intelligence and Creative Synthesis improve with skills **without exception** across tested models
- Tasks average ~8 min wall-clock and **20+ tool calls**; budgets 300–1200s

## Context Elements

- **Native-runtime protocol** — Evaluates skills/agents in production harnesses, not synthetic sandboxes
- **Hybrid grading** — Deterministic + side-effect audit + semantic judge
- **Skill-set ablation** — Isolates skill contribution on long-horizon real work (complements SkillsBench paired delta and SWE-Skills-Bench utility)
- **ClawHub-aligned categories** — Productivity, code intelligence, social, search/retrieval, creative, safety

## Relation to Skill Bundle Patterns

- Complements [skillsbench agent skills benchmark](skillsbench-agent-skills-benchmark.md) (paired +16.2pp curated delta across domains) with **in-the-wild multi-harness** reality
- Complements [swe skills bench utility benchmark](swe-skills-bench-utility-benchmark.md) (SWE-only, 80% zero gain) with non-SWE long-horizon categories
- Evaluation substrate used by [skillclaw collective skill evolution](skillclaw-collective-skill-evolution.md)
- Multi-harness sensitivity reinforces [skill os skills as apps](skill-os-skills-as-apps.md) and harness-as-infrastructure themes from [externalization llm agents unified review](externalization-llm-agents-unified-review.md)

## Key Insight

Skill utility and model quality are **not harness-invariant**. Measuring skill bundles requires native runtimes, multi-harness comparison, and skill-set ablations — synthetic sandboxes understate both difficulty and configuration sensitivity.

