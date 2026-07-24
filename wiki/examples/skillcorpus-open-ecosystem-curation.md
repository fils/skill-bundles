---
type: Skill Bundle Example
title: "SkillCorpus: Curating ~821K Open Skills \u2192 96K Deployable Corpus"
description: "End-to-end framework that aggregates, curates (16-class taxonomy + utility/robustness/safety facets), retrieves, and evaluates the open SKILL.md ecosystem; +7.5pp on SkillsBench with coverage and harness boundary analysis."
resource: https://arxiv.org/abs/2607.15557
timestamp: '2026-07-24T12:00:00Z'
date: 2026-07-24
sources:
- https://arxiv.org/abs/2607.15557
skills_included:
- "Multi-stage open-skill crawl and filter"
- "16-class taxonomy organization"
- "Fine-tuned retrieval-and-selection stack"
- "Multi-benchmark multi-harness evaluation"
context_elements:
- "Open ecosystem consolidation (~821K \u2192 96,401)"
- "Three quality facets (utility, robustness, safety)"
- "16-class skill taxonomy"
- "Coverage boundary vs harness boundary"
- "SkillsBench / GDPVal / QwenClawBench multi-eval"
composition: "Crawl \u2192 multi-stage filter/curate \u2192 taxonomy + quality facets \u2192 retrieval/selection models \u2192 serve corpus into agent harnesses; measure gains and failure boundaries."
reproducibility: "arXiv:2607.15557 v4 (23 Jul 2026); dataset/models/code promised on acceptance; +7.5pp SkillsBench; two harnesses \u00d7 two open backbones + frontier robustness check."
rating: 9
---

# SkillCorpus: Curating the Open Skill Ecosystem

**Origin:** Wang, Yao, Sun et al., arXiv:2607.15557 (v4 23 Jul 2026) — **very recent**

## Overview

Public skill repos are **fragmented, redundant, and uneven**. SkillCorpus asks: how to consolidate the open SKILL.md ecosystem into one usable corpus, and **what bounds** its benefit on real agent tasks?

## Pipeline Scale

| Stage | Scale |
|-------|-------|
| Crawled skills | ~**821,000** |
| Curated corpus | **96,401** |
| Taxonomy | 16 classes |
| Quality facets | utility, robustness, **safety** |
| Matching | fine-tuned retrieval-and-selection stack |

## Evaluation

- Benchmarks: **SkillsBench**, GDPVal, QwenClawBench
- Two harnesses × two open backbones + frontier robustness check
- Consistent gains; largest on SkillsBench (**+7.5pp**)
- Operational analysis: gains limited by a **coverage boundary** and a **harness boundary**

## Relation to Catalog

- Corpus-scale counterpart to [assc skillbom](assc-skill-supply-chains-skillbom.md) inventory science and [inside skill market](inside-skill-market-se-activities.md)
- Quality facets connect to [skillspector](skillspector-nvidia-security-scanner.md) / safety governance
- Harness boundary echoes [wildclawbench](wildclawbench-native-runtime-evaluation.md) multi-harness findings
- Complements [agentskillos](agentskillos-capability-tree-dag.md) orchestration of large pools

## Key Insight

Community skill mass is not automatically useful. **Curation + retrieval + harness fit** determine whether hundreds of thousands of SKILL.md files move the needle — and where they stop helping.

# Citations

- https://arxiv.org/abs/2607.15557
