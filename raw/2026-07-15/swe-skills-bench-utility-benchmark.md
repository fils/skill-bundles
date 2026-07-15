# SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?

**Source:** arXiv:2603.15401 (cs.SE, cs.AI)
**Authors:** Tingxu Han, Yi Zhang, Wei Song, Chunrong Fang, Zhenyu Chen, Youcheng Sun, Lijie Hu
**Submitted:** Mar 16, 2026
**Citations:** 34
**GitHub:** https://github.com/GeniusHTX/SWE-Skills-Bench
**Signal Rating:** 10/10

## Abstract

Agent skills — structured procedural knowledge packages injected at inference time — are increasingly used to augment LLM agents on software engineering tasks. However, their real utility in end-to-end development settings remains unclear.

**SWE-Skills-Bench** is the first requirement-driven benchmark that isolates the marginal utility of agent skills in real-world software engineering (SWE).

## Design

- **49 public SWE skills** paired with authentic GitHub repositories pinned at fixed commits
- **Requirement documents** with explicit acceptance criteria
- **~565 task instances** across 6 SWE subdomains
- **Deterministic verification framework** — Maps each task's acceptance criteria to execution-based tests
- **Controlled paired evaluation** — With and without the skill (same task, same repo, same commit)

## Key Results

| Metric | Value |
|--------|-------|
| Skills yielding zero improvement | 39 of 49 (80%) |
| Average gain from skill injection | +1.2% |
| Token overhead range | modest savings to +451% |
| Skills with meaningful gains | 7 (up to +30%) |
| Skills that degrade performance | 3 (up to -10%) |

## Key Ideas

1. **Skills are a narrow intervention** — Utility depends strongly on domain fit, abstraction level, and contextual compatibility. Not a universal booster.
2. **80% of skills provide zero benefit** — 39 of 49 SWE skills yield zero pass-rate improvement. This is a sobering empirical finding.
3. **Token overhead without benefit** — Some skills increase token usage by 451% while pass rates remain unchanged. Skills can be actively wasteful.
4. **Version-mismatch harm** — 3 skills degrade performance (up to -10%) due to version-mismatched guidance conflicting with project context. This is a real-world skill bundle failure mode.
5. **Requirement-driven evaluation** — Pairs skills with real GitHub repos + requirement docs + acceptance criteria, providing end-to-end (not component-level) evaluation.
6. **Deterministic verification** — Acceptance criteria → execution-based tests, removing subjective evaluation.

## Context Elements

- **Requirement-driven benchmark design** — Skills evaluated against real requirements, not synthetic tasks
- **Execution-based acceptance criteria** — Deterministic test mapping
- **Paired evaluation methodology** — With/without skill on same task instance
- **6 SWE subdomains** — Domain coverage for skill utility analysis
- **Version pinning** — GitHub repos pinned at fixed commits for reproducibility

## Relation to Existing Wiki

- First empirical challenge to the "more skills = better" assumption (complements [[skillreducer-token-efficiency]] which showed less-is-more effect)
- Related to [[skillsbench-agent-skills-benchmark]] (general skills benchmark)
- Related to [[skillgenbench-skill-generation-benchmark]] (skill generation evaluation)
- Provides the evaluation methodology missing from [[agent-skills-spec]] (specification without utility measurement)
- Critical counterpoint to skill adoption enthusiasm — 80% zero improvement is a major finding
