---
type: Skill Bundle Example
title: 'SkillsBench: First Benchmark for Agent Skills Effectiveness'
description: SkillsBench is the **first systematic benchmark** designed to measure how well agent skills improve AI agent performance across diverse tasks.
---

# SkillsBench: First Benchmark for Agent Skills Effectiveness

## Overview

SkillsBench is the **first systematic benchmark** designed to measure how well agent skills improve AI agent performance across diverse tasks. Rather than measuring fixed agent capabilities, SkillsBench uses **paired evaluation** — it measures the delta between agent performance with and without skills to isolate augmentation efficacy.

**Context Elements:** Paired evaluation methodology · Task taxonomy across domains · Procedural knowledge evaluation framework · Score normalization for cross-domain comparison

## Key Findings

### Overall Results
- Curated agent skills raise AI performance by **+16.2 percentage points** on average
- Healthcare domain sees gains of **+51.9pp** — the largest single-domain improvement
- Procedural knowledge (what to do, how to do it) is the primary driver of skill effectiveness

### Methodology
SkillsBench introduces **paired evaluation**:
1. Agent completes task WITHOUT skills → baseline score
2. Agent completes task WITH skills → augmented score
3. Delta = augmentation efficacy

This contrasts with traditional benchmarks that measure absolute performance on fixed tasks. The paired approach isolates the **incremental value of skills**.

### Task Coverage
Skills evaluated across diverse domains:
- Healthcare (largest gains)
- Engineering / Development
- Research / Analysis
- Business / Marketing
- Legal / Compliance

## Context Element Coverage

**Type: Benchmark Methodology** — The paired evaluation framework provides a formal **scoring function** that can be applied to any skill bundle to measure its empirical effectiveness.

**Type: Task Taxonomy** — SkillsBench's categorized task set serves as a **benchmark taxonomy** that can be used to evaluate skill bundle coverage and identify gaps.

**Type: Augmentation Efficacy Metric** — The delta metric (with-skills score minus without-skills score) provides a standardized way to compare skill bundles across tools and domains.

## Impact for Skill Bundles
SkillsBench provides the **measurement foundation** for skill bundle quality claims. Until now, bundle effectiveness was assessed qualitatively. SkillsBench enables:
- Quantified claims: "Bundle X improves task completion by +Y%"
- Cross-platform comparison: Same skills tested on Claude Code vs Codex vs Gemini CLI
- Domain optimization: Identify which skill categories matter most per domain

## v1.1 Update (2026-07-11)

SkillsBench v1.1 now has **87 tasks across 8 domains** with a live leaderboard of **24 model-harness configurations**:

| Rank | Agent | Without | With Skills | Δ | Gain (g) |
|------|-------|---------|-------------|---|----------|
| 1 | GPT-5.5 OpenHands | 51.5% | 67.3% | +15.8 | 32.6% |
| 2 | GPT-5.5 Codex | 46.8% | 66.5% | +19.7 | 37.0% |
| 3 | Opus 4.7 Claude Code | 43.0% | 61.2% | +18.2 | 31.9% |
| 4 | Gemini 3.1 Pro Gemini CLI | 36.0% | 60.8% | +24.8 | 38.7% |
| 5 | GLM 5.1 OpenHands | 32.7% | 58.4% | +25.7 | 38.1% |

- **Normalized gain (g)** measures skill effectiveness relative to room for improvement
- **Three abstraction layers:** Skills (applications) → Agent Harness (OS) → Models (CPUs)
- **8 professional domains:** SE, Industrial & Physical Systems, Natural Science, Office & White Collar, Finance & Economics, Mathematics & OR, Cybersecurity, Media & Content Production
- **Fleet trend:** Resolution rate improving +2.2 pts/month across model releases

## Confidence
9/10 — Published on arXiv, live website at skillsbench.ai with leaderboard, 24-config evaluation.

## Sources
- https://arxiv.org/abs/2602.12670
- https://www.skillsbench.ai
- https://www.skillsbench.ai/blogs/introducing-skillsbench
- https://github.com/benchflow-ai/skillsbench (v1.1)
