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

## Confidence
8/10 — Published on arXiv, website at skillsbench.ai, multiple secondary confirmations.

## Sources
- https://arxiv.org/abs/2602.12670
- https://www.skillsbench.ai
- https://www.skillsbench.ai/blogs/introducing-skillsbench
