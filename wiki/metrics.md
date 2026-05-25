# Skill Bundles — Metrics & Progress

**Last Updated:** 2026-05-24 (Iteration 9)

## KPIs

| Metric | Value | Previous | Change |
| Documented Examples | 28 | 20 | +8 |
| Raw Sources (total) | 41 | 27 | +14 |
| Wiki Articles | 37 | 28 | +9 |
| Concept Articles | 4 | 3 | +1 |
| Daily Digests | 6 | 5 | +1 |
| Q&A Passes | 2 | 1 | +1 |
| Context Element Types Covered | 11/11 | 8/8 | +3 |
| SSSOM Coverage | 2 | 2 | Unchanged |
## Context Element Coverage

| Context Element | Examples | Status |
|-----------------|----------|--------|
| SHACL Validation | 7 | **Strong** |
| Constraint Rules | 6 | **Strong** (new) |
| Rules / Authorization | 5 | **Strong** |
| Ontology / Taxonomy | 8 | **Strong** |
| Governance / Verification | 5 | **Strong** |
| Dependency Graphs | 2 | **Strong** (new) |
| YAML Configuration | 8+ | Ubiquitous |
| MCP Dependencies | 3 | Emerging |
| SSSOM Mapping | 2 | Emerging |
| Supply Chain / Provenance | 2 | Emerging |
| Benchmarking | 1 | Emerging (new) |

## Word Count

| File | Words |
| wiki/skill-bundles.md | ~480 |
| wiki/index.md | ~350 |
| wiki/metrics.md | ~350 |
| wiki/concepts/*.md | 4 files × ~650 avg |
| wiki/examples/*.md | 23 files × ~250 avg |
| wiki/daily-digests/*.md | ~3,000 |
| wiki/qa/*.md | ~600 |
| **Total wiki** | ~10,600 |
## Research Velocity

| Iteration | New Examples | New Concepts | Raw Sources |
|-----------|-------------|--------------|-------------|
| 1-5 | 9 | 1 | 13 |
| 6 | 5 | 1 | 3 |
| 7 | 2 (manual seed) | 0 | 2 |
| 8 | 6 | 1 | 9 |
| **9** | **8** | **1** | **14** |

## Quality Notes
- All 28 examples have confidence scores and source attribution
- Constraint Rules identified as new category (6 examples across Iron Laws, SHACL, crypto)
- Dependency Graphs identified as new category (2 examples: GoS + GraphGuard OS)
- All wikilinks resolve (automated lint pass: 30 links, 1 broken fixed)
- DSPy agent skills bundle includes 80 validation tests (AST + JSON schema + frontmatter)
- SkillsBench provides first quantitative benchmark (+16.2pp avg improvement)
- Mondoo security analysis reveals 25%+ vulnerability rate — critical gap
- SSSOM still at 2 (spec + algorithm) — ongoing gap
- Anthropic Official Skills repo (140k stars) is canonical reference
- NemoClaw entry created to fix previously broken wikilink

## Epistemic Coherence Check

Randomly sampled 3 claims from today's new wiki entries:
1. xpSHACL "99.48% cache hit rate" → Verified in raw source (arXiv 2507.08432) ✅
2. GraphGuard OS "Shadow Policy Manager" → Verified in raw source (Medium article) ✅
3. SHACL Data Quality "69 metrics" → Verified in raw source (arXiv 2507.22305) ✅

Match rate: 3/3 (100%)
