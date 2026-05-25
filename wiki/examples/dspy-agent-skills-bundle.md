# DSPy Agent Skills Bundle: Production-Grade DSPy Optimization

## Overview

A family of three interoperable repositories that package **DSPy (Declarative Self-Improving Language Model programs)** expertise as agent skills. Together they represent one of the most mature **framework-specific skill bundles** documented: skills that teach agents how to systematically build and optimize LLM programs.

**Context Elements:** YAML frontmatter validation · Python AST testing · MCP-style meta-tools · Sandbox security config · Structured metric validation

## Skills Included

### 1. intertwine/dspy-agent-skills
Five tightly-scoped skills for **DSPy 3.2.x**:
| Skill | Purpose |
|-------|---------|
| `dspy-fundamentals` | Signatures, Modules, Predict/CoT/ReAct |
| `dspy-evaluation-harness` | Metrics, dev/val splits, `dspy.Evaluate` |
| `dspy-gepa-optimizer` | `dspy.GEPA` compilation and reflection |
| `dspy-rlm-module` | Long context, codebase QA, recursive exploration |
| `dspy-advanced-workflow` | Orchestrates the above four for end-to-end builds |

### 2. ivanvza/dspy-skills
A **Python SDK** that implements the Agent Skills specification as a reusable framework for ReAct agents:
- `SkillsReActAgent` with automatic SKILL.md discovery
- Four meta-tools: `list_skills`, `activate_skill`, `run_skill_script`, `read_skill_resource`
- `skills_config.yaml` for sandbox, interpreter allowlist, network access
- Firejail sandbox integration

### 3. OmidZamani/dspy-skills
Broad DSPy 3.1.2 skills collection covering optimizers, architecture patterns, and debugging:
- Optimizers: BootstrapFewShot, MIPROv2, GEPA Reflective, Simba
- Architecture: RAG Pipeline, Signature Designer, ReAct Agent Builder
- Validation: Output Refinement, Evaluation Suite, MLflow tracing

## Context Elements & Validation

**Type: YAML Frontmatter + Python AST Validation** — intertwine's bundle includes 80 validation tests that check SKILL.md frontmatter specs, JSON schemas, and Python AST correctness of bundled examples. This is the first bundle found that **validates its own skill definitions programmatically**.

**Type: Configuration Schema** — ivanvza's `skills_config.yaml` provides a declarative security posture (sandbox, timeout, allowed_interpreters, allow_network, allow_filesystem_write) that constrains what loaded skills can execute.

**Type: Metric Validation Schema** — The requirement that metrics must return `dspy.Prediction(score, feedback)` instead of raw dicts serves as a protocol constraint on the evaluation skill.

## Composition Pattern: Orchestrator Skill

The `dspy-advanced-workflow` skill orchestrates the other four, representing a **meta-bundle pattern**: a skill whose purpose is to combine and sequence other skills. The recommended workflow (Design → Build → Validate → Optimize → Evaluate → Debug → Deploy) is encoded as skill activation order.

## Confidence
9/10 — All three repos are on GitHub, verifiable source. intertwine includes runnable demos with committed benchmark artifacts.

## Sources
- https://github.com/intertwine/dspy-agent-skills
- https://github.com/ivanvza/dspy-skills
- https://github.com/OmidZamani/dspy-skills
