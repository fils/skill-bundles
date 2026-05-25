# DSPy Agent Skills: Production-Grade DSPy 3.2.x for Coding Agents

## intertwine/dspy-agent-skills
**URL:** https://github.com/intertwine/dspy-agent-skills
**Date Retrieved:** 2026-05-24

Five agent skills pack for DSPy 3.2.x:
- dspy-fundamentals: Signatures, Modules, Predict/ChainOfThought/ReAct
- dspy-evaluation-harness: Metrics, dev/val splits, dspy.Evaluate
- dspy-gepa-optimizer: dspy.GEPA compilation
- dspy-rlm-module: Long context, codebase QA, recursive exploration
- dspy-advanced-workflow: Orchestrates the four other skills

Key features:
- Validated for DSPy 3.2.0 (not inferred from outdated docs)
- Dual-agent: Claude Code + Codex CLI from single source
- Progressive disclosure: short SKILL.md + deep reference.md
- 80 validation tests (frontmatter specs, JSON schemas, Python AST)
- End-to-end benchmarks with committed artifacts (baseline vs GEPA-optimized)
- 01-rag-qa: 80.47→100.00 (+19.53)
- 02-math-reasoning: 85.00→93.33 (+8.33)
- 03-invoice-extraction: 0.833→0.931 (+0.098)

Technical gotchas:
- Metrics must return dspy.Prediction(score, feedback), not dict
- GEPA requires reflection_lm at construction time
- Pydantic outputs require gepa_kwargs={"use_cloudpickle": True}, no "from __future__ import annotations"
- reflection_minibatch_size should be 6-8 when baseline >0.7

## ivanvza/dspy-skills
**URL:** https://github.com/ivanvza/dspy-skills
**Date Retrieved:** 2026-05-24

Python package integrating Agent Skills spec with DSPy ReAct agents:
- Dynamic discovery: scans directories for SKILL.md at startup
- Progressive disclosure: ~100 tokens/skill metadata initially
- Sandboxed execution: firejail (Linux)
- Four meta-tools: list_skills, activate_skill, run_skill_script, read_skill_resource
- Config via Python objects or skills_config.yaml
- Security: interpreter allowlist, path validation, env sanitization

## OmidZamani/dspy-skills
**URL:** https://github.com/OmidZamani/dspy-skills
**Date Retrieved:** 2026-05-24

Comprehensive DSPy 3.1.2 skills collection:
Categories: Optimizers (BootstrapFewShot, MIPROv2, GEPA Reflective, Simba), Development & Architecture (RAG Pipeline, Signature Designer, ReAct Agent Builder), Validation/Debugging/Integration (Output Refinement, Evaluation Suite, Debugging & Observability, Haystack Integration)
Recommended workflow: Design → Build → Validate → Optimize → Evaluate → Debug → Deploy
