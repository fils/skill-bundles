# DSPy Agent Skills v0.2.3 — intertwine/dspy-agent-skills

**Source:** https://github.com/intertwine/dspy-agent-skills
**Date:** 2026-05-25
**Signal:** 9/10

## Overview
Production-grade DSPy 3.2.x skills for coding agents (Claude Code, Codex CLI). 5 spec-compliant skills with validated end-to-end examples. Updated from previous ingestion (v0.1.x -> v0.2.3).

## Included Skills
1. `dspy-fundamentals` — Signatures, Modules, Predict/ChainOfThought/ReAct
2. `dspy-evaluation-harness` — Metrics, dev/val splitting, dspy.Evaluate
3. `dspy-gepa-optimizer` — Compiling and optimizing DSPy programs
4. `dspy-rlm-module` — Long context, codebase QA, recursive exploration
5. `dspy-advanced-workflow` — Orchestrates the other four

## Progressive Disclosure
Uses SKILL.md for quick context + reference.md for deep details. Supports dual installation to both `.claude/skills/` and `.agents/skills/`.

## Performance Benchmarks (GEPA)
- 01-rag-qa: 80.47 → 100.00 (+19.53)
- 02-math-reasoning: 85.00 → 93.33 (+8.33)
- 03-invoice-extraction: 0.833 → 0.931 (+0.098)

## Key Technical Details
- Metric returns must be dspy.Prediction(score, feedback), not dict
- GEPA: reflection_lm at construction time
- Pydantic: gepa_kwargs={"use_cloudpickle": True}
- Minibatch sizing: 6-8 for baseline >0.7
