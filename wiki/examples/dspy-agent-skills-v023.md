---
date: 2026-05-25
sources:
  - https://github.com/intertwine/dspy-agent-skills
title: DSPy Agent Skills v0.2.3 — Production-Grade DSPy 3.2.x Bundle
skills:
  - dspy-fundamentals
  - dspy-evaluation-harness
  - dspy-gepa-optimizer
  - dspy-rlm-module
  - dspy-advanced-workflow
context_elements:
  - SKILL.md progressive disclosure
  - reference.md deep documentation
  - pytest validation suite
  - GEPA optimization benchmarks
  - Dual-platform installation (Claude Code + Codex CLI)
  - Offline dry-run testing
composition_notes: |
  Updated from v0.1.x to v0.2.3 with DSPy 3.2.x API validation. Five interdependent skills
  with an orchestrator pattern (dspy-advanced-workflow activates the other four). Includes
  committed optimization benchmark artifacts showing measurable performance deltas.
reproducibility: High — full source with install scripts for dual platforms
confidence: 9/10
---

# DSPy Agent Skills v0.2.3

## Overview

Updated version of the [[dspy-agent-skills-bundle]] for DSPy 3.2.x. This bundle provides production-grade spec-compliant skills for coding agents (Claude Code, Codex CLI) to master DSPy with validated end-to-end examples.

## Skills Included

1. **dspy-fundamentals** — Signatures, Modules, Predict/ChainOfThought/ReAct, persistence
2. **dspy-evaluation-harness** — Metrics, dev/val set splitting, dspy.Evaluate
3. **dspy-gepa-optimizer** — Compiling and optimizing DSPy programs
4. **dspy-rlm-module** — Long context, codebase QA, recursive exploration
5. **dspy-advanced-workflow** — Orchestrator skill that composes the other four

## Progressive Disclosure
Uses `SKILL.md` for quick agent context and `reference.md` for deep technical details — a pattern described in [[ylang-labs-agent-skills-overview]].

## GEPA Performance Benchmarks (Committed Artifacts)

| Task | Baseline | Optimized | Delta |
|---|---|---|---|
| 01-rag-qa | 80.47 | 100.00 | +19.53 |
| 02-math-reasoning | 85.00 | 93.33 | +8.33 |
| 03-invoice-extraction | 0.833 | 0.931 | +0.098 |

## Critical Implementation Details
- Metric returns must be `dspy.Prediction(score, feedback)`, not dict
- GEPA: `reflection_lm` must be at construction time
- Pydantic typed outputs require `gepa_kwargs={"use_cloudpickle": True}`
- `reflection_minibatch_size`: 6-8 for baseline >0.7

## Dual-Platform Installation
- Claude Code: `/plugin marketplace add intertwine/dspy-agent-skills`
- Codex CLI: `npx skills add intertwine/dspy-agent-skills --skill '*' -a codex -y`
- Manual: `./scripts/install.sh` symlinks to both `~/.claude/skills/` and `~/.agents/skills/`

## Connection to Existing Entries
This is an **update** to our existing [[dspy-agent-skills-bundle]] entry (which covered v0.1.x). The v0.2.3 version adds DSPy 3.2.1 validation, updated GEPA benchmarks, and improved dry-run testing support. The [[skillsbench-agent-skills-benchmark]] benchmarking framework is relevant for evaluating the measurable improvements this bundle provides.

## Source Attribution
Raw source: [[../../raw/2026-05-25/dspy-agent-skills-v2.md]]
