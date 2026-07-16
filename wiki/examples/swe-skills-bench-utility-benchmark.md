---
type: Skill Bundle Example
title: 'SWE-Skills-Bench: Do Agent Skills Actually Help in Software Engineering?'
description: SWE-Skills-Bench is the first **requirement-driven** benchmark that isolates the **marginal utility** of agent skills in real-world software engineering.
resource: https://arxiv.org/abs/2603.15401
timestamp: '2026-07-15T00:00:00Z'
date: 2026-07-15
sources:
- arXiv:2603.15401
- https://github.com/GeniusHTX/SWE-Skills-Bench
skills_included:
- 49 public SWE skills
- Deterministic verification framework
- Paired evaluation methodology (with/without skill)
- Acceptance criteria → execution test mapping
context_elements:
- Requirement-driven benchmark design
- Execution-based acceptance criteria (deterministic verification)
- Paired evaluation (with/without skill, same task)
- 6 SWE subdomains
- Version-pinned GitHub repositories
composition: 'Evaluation benchmark: 49 SWE skills × GitHub repos pinned at fixed commits × requirement docs with acceptance criteria → ~565 task instances across 6 subdomains → deterministic verification (acceptance criteria → execution tests) → paired with/without skill evaluation.'
reproducibility: Open-sourced on GitHub (GeniusHTX/SWE-Skills-Bench). 49 skills, ~565 task instances, 6 SWE subdomains. arXiv:2603.15401, 34 citations.
rating: 10
---

# SWE-Skills-Bench: Do Agent Skills Actually Help in Software Engineering?

**Origin:** Nanjing University (arXiv:2603.15401, Mar 2026)
**Citations:** 34
**GitHub:** https://github.com/GeniusHTX/SWE-Skills-Bench
**Authors:** Tingxu Han, Yi Zhang, Wei Song, Chunrong Fang, Zhenyu Chen, Youcheng Sun, Lijie Hu

## Overview

SWE-Skills-Bench is the first **requirement-driven** benchmark that isolates the **marginal utility** of agent skills in real-world software engineering. It asks the critical question: do agent skills actually help? The answer is more sobering than the rapid adoption of skills suggests.

## Benchmark Design

- **49 public SWE skills** — Real skills from the wild, not synthetic
- **Authentic GitHub repositories** — Pinned at fixed commits for reproducibility
- **Requirement documents** — With explicit, verifiable acceptance criteria
- **~565 task instances** — Across 6 SWE subdomains
- **Deterministic verification** — Each task's acceptance criteria mapped to execution-based tests
- **Paired evaluation** — Same task evaluated with and without the skill (controlled comparison)

## Results: The Sobering Reality

| Metric | Value |
|--------|-------|
| Skills yielding zero pass-rate improvement | 39 of 49 (80%) |
| Average gain from skill injection | +1.2% |
| Token overhead range | modest savings to **+451%** |
| Skills with meaningful gains | 7 (up to +30%) |
| Skills that **degrade** performance | 3 (up to -10%) |

## Key Findings

1. **80% of skills provide zero benefit** — 39 of 49 SWE skills yield zero pass-rate improvement. This is the first large-scale empirical challenge to the "more skills = better" assumption.

2. **Token overhead without benefit** — Some skills increase token usage by 451% while pass rates remain unchanged. Skills can be actively wasteful, not just neutral.

3. **Version-mismatch harm** — 3 skills degrade performance (up to -10%) due to version-mismatched guidance conflicting with project context. This is a real-world skill bundle failure mode.

4. **Skills are a narrow intervention** — Utility depends strongly on:
   - **Domain fit** — Does the skill match the task domain?
   - **Abstraction level** — Is the skill at the right level of abstraction?
   - **Contextual compatibility** — Does the skill's guidance align with the project's actual state?

5. **Only 7 specialized skills help** — Meaningful gains (up to +30%) come from highly specialized, well-matched skills.

## Context Elements

- **Requirement-driven benchmark** — Skills evaluated against real requirements (not synthetic tasks)
- **Execution-based acceptance criteria** — Deterministic test mapping (no subjective evaluation)
- **Paired evaluation methodology** — With/without skill on same task instance (isolates marginal utility)
- **6 SWE subdomains** — Domain coverage for utility analysis
- **Version pinning** — GitHub repos at fixed commits (reproducibility)

## Relation to Skill Bundle Patterns

SWE-Skills-Bench provides the first rigorous empirical evaluation of skill utility. Its findings challenge the field's assumptions.

- Critical counterpoint to skill adoption enthusiasm (80% zero improvement)
- Complements [skillreducer token efficiency](skillreducer-token-efficiency.md) (less-is-more effect — SWE-Skills-Bench quantifies the waste)
- Related to [skillsbench agent skills benchmark](skillsbench-agent-skills-benchmark.md) (general skills benchmark — SWE-Skills-Bench is SWE-specific)
- Related to [skillgenbench skill generation benchmark](skillgenbench-skill-generation-benchmark.md) (generation evaluation — SWE-Skills-Bench is deployment evaluation)
- Provides evaluation methodology missing from [agent skills spec](agent-skills-spec.md) (specification without utility measurement)
- Validates [externalization llm agents unified review](externalization-llm-agents-unified-review.md) theory (skills as externalized procedural expertise can fail when expertise doesn't match context)
- Version-mismatch finding connects to [skillmigrator cross domain transfer](skillmigrator-cross-domain-transfer.md) (contextual compatibility matters)

## Key Insight

Agent skills are not a universal performance booster. In real-world software engineering, 80% of skills provide zero benefit, and some are actively harmful (both in wasted tokens and degraded performance). Skill utility is a narrow, context-dependent intervention — the field needs rigorous evaluation, not just enthusiastic adoption.

