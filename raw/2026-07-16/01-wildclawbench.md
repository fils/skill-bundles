# WildClawBench: Real-World Long-Horizon Agent Evaluation

**Source:** https://arxiv.org/abs/2605.10912 | https://arxiv.org/html/2605.10912v1
**GitHub:** https://github.com/InternLM/WildClawBench (477★ as of 2026-07-16)
**Date:** May 2026 | Authors: InternLM / Shanghai AI Lab (Ding et al.)
**Signal rating:** 9/10

## Key ideas
- Native-runtime benchmark: 60 human-authored bilingual multimodal tasks in real CLI harnesses (OpenClaw, Claude Code, Codex, Hermes Agent) inside Docker — not mock APIs.
- ~8 min wall-clock / 20+ tool calls per task; hybrid grading (deterministic rules + env state audit + LLM/VLM judge).
- 19 frontier models: best Claude Opus 4.7 only 62.2% on OpenClaw; harness switch alone shifts a model by up to 18 points.
- **Skill ablation (high relevance):** domain-specific skills yield mixed results; GPT-5.4 gains most (+5.2 overall, +22.4 Code Intelligence); Code Intelligence and Creative Synthesis improve without exception across models.
- Categories follow ClawHub skill hub taxonomy: productivity, code intelligence, social, search/retrieval, creative, safety.

## Quotes
> "switching harness alone shifts a single model by up to 18 points"
> "augmenting agents with domain-specific skills yields mixed results that depend on the model’s baseline capability"

## Why skill-bundles
First multi-harness native evaluation that isolates skill-set impact on long-horizon real work; complements SkillsBench (curated delta) and SWE-Skills-Bench (SWE-only utility).
