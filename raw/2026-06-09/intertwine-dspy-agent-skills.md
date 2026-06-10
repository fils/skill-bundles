# DSPy Agent Skills (intertwine/dspy-agent-skills)

**Source:** https://github.com/intertwine/dspy-agent-skills
**Date Retrieved:** 2026-06-09
**Type:** GitHub Repository - Production-grade agent skills bundle

---

## Summary

**DSPy Agent Skills** is a production-grade suite of **five agent skills** designed to turn coding agents (Claude Code, Codex CLI) into DSPy experts. It follows the [agentskills.io](https://agentskills.io/) specification and is fully validated against **DSPy 3.2.x** (tested on 3.2.1).

This is a **prime example of a skill bundle** — it packages multiple related skills with formal validation infrastructure, evaluation harnesses, optimization pipelines, and end-to-end performance benchmarks.

---

## Skills Included (5 Total)

| Skill | Purpose / Auto-invocation Trigger |
|-------|-----------------------------------|
| `dspy-fundamentals` | Signatures, Modules, Predict/ChainOfThought/ReAct, save/load |
| `dspy-evaluation-harness` | Writing metrics, splitting dev/val sets, calling `dspy.Evaluate` |
| `dspy-gepa-optimizer` | Optimizing/compiling DSPy programs with `dspy.GEPA` |
| `dspy-rlm-module` | Long context, codebase QA, recursive exploration via `dspy.RLM` |
| `dspy-advanced-workflow` | Orchestrates the other four skills for end-to-end builds |

---

## Context Elements (Formal Artifacts)

This bundle includes **multiple formal context elements** that qualify it as a rich skill bundle:

### 1. Evaluation & Validation Infrastructure
- **34+ pytest validators** in `tests/` directory
- **Offline testing mode** via `example_*.py --dry-run` scripts
- **DSPy API surface validation** via `scripts/check_dspy_surface.py` (pins DSPy 3.2.1 exactly)
- **Metric contract enforcement**: Metrics must return `dspy.Prediction(score, feedback)`, not a dict

### 2. Optimization Pipeline Artifacts
- **GEPA (Generalized Evaluation & Prompt Analysis)** integration with strict requirements:
  - `reflection_lm` must be provided at construction time
  - `gepa_kwargs={"use_cloudpickle": True}` for Pydantic outputs
  - `reflection_minibatch_size` tuning guidance (6–8 when baseline >0.7)
- **BetterTogether** chaining for multi-skill orchestration

### 3. End-to-End Performance Benchmarks (Validated Artifacts)
| Example | Task LM | Baseline | Optimized | Δ |
|---------|---------|----------|-----------|---|
| 01-rag-qa | Ministral 3B | 80.47 | **100.00** | **+19.53** |
| 02-math-reasoning | Ministral 3B | 85.00 | **93.33** | **+8.33** |
| 03-invoice-extraction | Liquid LFM 1.2B | 0.833 | **0.931** | **+0.098** |

### 4. Installation & Distribution Standards
- **Agent Skills CLI** (`npx skills`) for cross-platform installation
- **Marketplace install** for Claude Code (`/plugin marketplace add ...`)
- **Symlink installer** (`./scripts/install.sh`) for `~/.claude/skills/` and `~/.agents/skills/`
- **Dual compatibility**: Claude Code + Codex CLI

### 5. Development Environment Lock-in
- **uv** for deterministic environment management
- **Python 3.10+**, **Deno** (required for `dspy.RLM` Pyodide sandbox)
- **MIT License**

---

## Composition Notes

This bundle demonstrates **excellent composition patterns**:

1. **Layered skill architecture**: 4 foundational skills + 1 orchestration skill (`dspy-advanced-workflow`)
2. **Progressive disclosure**: `SKILL.md` for quick agent context + `reference.md` for deep technical details
3. **Validation as first-class citizen**: Tests, dry-run modes, API surface checks are part of the bundle
4. **Reproducibility artifacts**: Exact DSPy version pinning, offline test scripts, performance baselines
5. **Cross-platform distribution**: Single bundle installs to multiple agent runtimes

---

## Key Quotes

> "DSPy Agent Skills is a production-grade suite of five agent skills designed to turn coding agents like **Claude Code** and **Codex CLI** into DSPy experts. It is fully validated against **DSPy 3.2.x** and follows the [agentskills.io](https://agentskills.io/) specification."

> "The project documentation highlights several critical \"gotchas\" for DSPy 3.2.x:
> * **Metric Contract:** Metrics must return `dspy.Prediction(score, feedback)`, not a dictionary, to work with DSPy's parallel evaluator.
> * **GEPA Requirements:** `reflection_lm` must be provided at construction time, not during compilation.
> * **Pydantic Outputs:** Typed outputs require `gepa_kwargs={\"use_cloudpickle\": True}` and must avoid `from __future__ import annotations`."

> "To maintain quality, the repo uses `uv` for environment management and `pytest` for validation."

---

## Reproducibility Assessment

**High.** The bundle includes:
- Exact dependency versions (DSPy 3.2.1 pinned)
- Offline validation scripts with `--dry-run` mode
- Full test suite (34+ validators)
- Performance baselines with specific model names
- Deterministic environment via `uv`
- Clear installation procedures for multiple platforms