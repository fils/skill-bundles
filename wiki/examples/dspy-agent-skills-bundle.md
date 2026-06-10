# DSPy Agent Skills Bundle: Production-Grade DSPy Optimization

**Source:** https://github.com/intertwine/dspy-agent-skills  \
**Date Added:** 2026-05-23 (Updated: 2026-06-09)  \
**Bundle Type:** Framework-Specific Skill Bundle (DSPy 3.2.x)  \
**Raw Sources:** [[../raw/2026-06-09/intertwine-dspy-agent-skills.md]]

## Overview

A family of three interoperable repositories that package **DSPy (Declarative Self-Improving Language Model programs)** expertise as agent skills. Together they represent one of the most mature **framework-specific skill bundles** documented: skills that teach agents how to systematically build and optimize LLM programs.

**Context Elements:** YAML frontmatter validation · Python AST testing · MCP-style meta-tools · Sandbox security config · Structured metric validation · GEPA optimization benchmarks · Exact DSPy version pinning

## Skills Included (5 Core Skills in intertwine/dspy-agent-skills v0.2.3)

| Skill | Purpose / Auto-invocation Trigger |
|-------|-----------------------------------|
| **`dspy-fundamentals`** | Signatures, Modules, Predict/ChainOfThought/ReAct, save/load |
| **`dspy-evaluation-harness`** | Writing metrics, splitting dev/val sets, calling `dspy.Evaluate` |
| **`dspy-gepa-optimizer`** | Optimizing/compiling DSPy programs with `dspy.GEPA` |
| **`dspy-rlm-module`** | Long context, codebase QA, recursive exploration via `dspy.RLM` |
| **`dspy-advanced-workflow`** | Orchestrates the other four skills for end-to-end builds |

## Related Repositories in the Bundle

### 1. intertwine/dspy-agent-skills (Primary — v0.2.3, DSPy 3.2.1 validated)
- **Five tightly-scoped skills** for **DSPy 3.2.x** (fully validated against 3.2.1)
- **Progressive disclosure:** `SKILL.md` for quick agent context + `reference.md` for deep technical details
- **Offline testing:** `example_*.py` scripts with `--dry-run` mode
- **Optimization:** Features `GEPA` (Generalized Evaluation & Prompt Analysis) and `BetterTogether` chaining
- **Dual Compatibility:** Works with **Claude Code** and **Codex CLI**
- **Installation:** Marketplace (`/plugin marketplace add intertwine/dspy-agent-skills`), Agent Skills CLI (`npx skills`), or manual symlink installer

### 2. ivanvza/dspy-skills
- A **Python SDK** implementing the Agent Skills specification as a reusable framework for ReAct agents
- `SkillsReActAgent` with automatic SKILL.md discovery
- Four meta-tools: `list_skills`, `activate_skill`, `run_skill_script`, `read_skill_resource`
- `skills_config.yaml` for sandbox, interpreter allowlist, network access
- Firejail sandbox integration

### 3. OmidZamani/dspy-skills
- Broad DSPy 3.1.2 skills collection covering optimizers, architecture patterns, and debugging
- Optimizers: BootstrapFewShot, MIPROv2, GEPA Reflective, Simba
- Architecture: RAG Pipeline, Signature Designer, ReAct Agent Builder
- Validation: Output Refinement, Evaluation Suite, MLflow tracing

## Context Elements & Validation (v0.2.3 Enhancements)

**Type: YAML Frontmatter + Python AST Validation** — intertwine's bundle includes **34+ pytest validators** that check SKILL.md frontmatter specs, JSON schemas, and Python AST correctness of bundled examples. This is the first bundle found that **validates its own skill definitions programmatically**.

**Type: Configuration Schema** — ivanvza's `skills_config.yaml` provides a declarative security posture (sandbox, timeout, allowed_interpreters, allow_network, allow_filesystem_write) that constrains what loaded skills can execute.

**Type: Metric Validation Schema** — The requirement that metrics must return `dspy.Prediction(score, feedback)` instead of raw dicts serves as a protocol constraint on the evaluation skill.

**Type: Exact Dependency Pinning** — `scripts/check_dspy_surface.py` validates against **DSPy 3.2.1 exactly** via `uv run --with dspy==3.2.1`. Prevents API drift.

**Type: Offline Validation Scripts** — `example_*.py --dry-run` for smoke-testing skills without API calls.

**Type: Performance Benchmarks (Validated Artifacts)** — End-to-end examples with measured improvements:
| Example | Task LM | Baseline | Optimized | Δ |
|---------|---------|----------|-----------|---|
| **01-rag-qa** | Ministral 3B | 80.47 | **100.00** | **+19.53** |
| **02-math-reasoning** | Ministral 3B | 85.00 | **93.33** | **+8.33** |
| **03-invoice-extraction** | Liquid LFM 1.2B | 0.833 | **0.931** | **+0.098** |

**Type: GEPA Requirements (Critical Gotchas Documented)**
- `reflection_lm` must be provided at construction time, not during compilation
- Pydantic outputs require `gepa_kwargs={"use_cloudpickle": True}` and must avoid `from __future__ import annotations`
- If baseline score >0.7, `reflection_minibatch_size` should be increased (6–8) to ensure reflection LM triggers on incorrect samples

## Composition Pattern: Orchestrator Skill

The `dspy-advanced-workflow` skill orchestrates the other four, representing a **meta-bundle pattern**: a skill whose purpose is to combine and sequence other skills. The recommended workflow (Design → Build → Validate → Optimize → Evaluate → Debug → Deploy) is encoded as skill activation order.

## Development & Quality Infrastructure

```bash
# Run validation suite (34+ pytest validators)
uv run --with pytest python -m pytest tests/ -v

# Smoke-test skills offline
for f in skills/*/example_*.py; do uv run --with dspy python "$f" --dry-run; done

# Validate current DSPy API surface
env -u UV_EXCLUDE_NEWER uv run --with dspy==3.2.1 python scripts/check_dspy_surface.py
```

- **Environment Management:** `uv` for deterministic, reproducible environments
- **Python:** 3.10+
- **Deno:** Required for `dspy.RLM` (Pyodide sandbox)
- **License:** MIT

## Confidence

9/10 — All three repos are on GitHub, verifiable source. intertwine includes runnable demos with committed benchmark artifacts, exact version pinning, 34+ validators, and documented GEPA gotchas.

## Sources

- https://github.com/intertwine/dspy-agent-skills
- https://github.com/ivanvza/dspy-skills
- https://github.com/OmidZamani/dspy-skills
- Raw (v0.2.3): [[../raw/2026-06-09/intertwine-dspy-agent-skills.md]]