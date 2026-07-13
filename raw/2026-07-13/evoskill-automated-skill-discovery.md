# EvoSkill: Automated Skill Discovery for Multi-Agent Systems

**Source:** arXiv:2603.02766 (03 Mar 2026)
**Authors:** Salaheddin Alzubi (Sentient), Noah Provenzano, Jaydon Bingham, Weiyuan Chen, Tu Vu (Virginia Tech)
**GitHub:** https://github.com/sentient-agi/EvoSkill (1k stars, 110 forks, 322 commits, 12 contributors)
**Code:** Open-sourced (Python 74.9%, Jupyter 23.7%)
**Signal Rating:** 9/10

## Abstract

Coding agents are increasingly used as general-purpose problem solvers, but their flexibility does not by itself confer the domain expertise needed for specialized tasks. Recent work addresses this through agent skills: reusable workflows, and code, that augment agents with domain-specific capabilities. Most skills today are hand-crafted, and existing evolutionary approaches optimize low-level artifacts (e.g. prompts & code) that are tightly coupled to specific models and tasks. EvoSkill is a self-evolving framework that automatically discovers and refines agent skills through iterative failure analysis. EvoSkill analyzes execution failures, proposes new skills or edits to existing ones, and materializes them into structured, reusable skill folders. A Pareto frontier of agent programs governs selection, retaining only skills that improve held-out validation performance while the underlying model remains frozen.

## Key Results

- OfficeQA: 60.6% → 67.9% (+7.3% exact-match accuracy) using only a small training subset
- SealQA: 26.6% → 38.7% (+12.1% improvement)
- Zero-shot transfer: Skills evolved on SealQA transfer to BrowseComp (+5.3% accuracy) without modification — proving skill-level optimization produces transferable capabilities

## Three-Agent Architecture

1. **Executor Agent (AA):** Executes tasks under the governance of the current agent program. Base program initializes with no skills.
2. **Proposer Agent (PP):** Analyzes Executor's output traces, predicted answers, and ground-truth to diagnose failures and propose high-level skill descriptions. Ground-truth answers enable root-cause diagnosis (like error analysis in supervised learning). Determines whether to create a new skill or refine an existing one.
3. **Skill-Builder Agent (SS):** Materializes a high-level proposal into a concrete skill folder comprising trigger metadata, procedural instructions (SKILL.md), and optional helper scripts (Python/TypeScript) or reference material. Bootstrapped with a meta-skill that codifies best practices for skill authoring.

## Pareto Frontier Selection

- Maintains a bounded set of top-performing programs (K=3 default) tracked via git tags (prefixed frontier/)
- Each program stored on a dedicated git branch (prefixed program/) with YAML configuration
- Parent-child lineage encoded via git; tree-structured search over program space
- Each node is a fully reproducible snapshot: lineage reconstructable via parent pointers
- Children admitted to frontier only if score exceeds worst member; weakest evicted
- Failed children's branches deleted to prevent repository bloat
- Early stopping after configurable consecutive iterations without improvement

## Context Elements

- **Structured skill folders:** trigger metadata + SKILL.md + helper scripts
- **Pareto frontier governance:** validation-gated skill admission
- **Git-backed version control:** program/ branches + frontier/ tags for lineage
- **Failure analysis:** ground-truth comparison for root-cause diagnosis
- **Meta-skill bootstrapping:** best-practice codification for skill authoring
- **Multi-tolerance scoring:** weighted average over 5 tolerance levels (τ ∈ {0, 0.01, 0.025, 0.05, 0.10})

## Key Insights

- Operates at the *skill abstraction level* rather than on low-level artifacts (prompts, code)
- Skills accumulate across iterations, progressively expanding agent capabilities
- Underlying model remains frozen throughout — only skill repository evolves
- Zero-shot transfer evidence: skill-level optimization produces capabilities that generalize beyond training task
- Supports Claude Code, Codex, OpenCode harnesses
