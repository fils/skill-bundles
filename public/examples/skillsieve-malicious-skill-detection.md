---
type: Skill Bundle Example
title: 'SkillSieve: Hierarchical Triage for Detecting Malicious Agent Skills'
description: '- **arXiv:** 2604.06550 (submitted 8 Apr 2026, v2 26 May 2026) - **Authors:** Yinghan Hou, Zongyou Yang, Zaihu Pang, Xiujun Ma - **Cited by:** 17 - **Data:** 49,592 ClawHub skills (2026-04-04 snapshot) + adversarial s...'
resource: https://arxiv.org/abs/2604.06550
timestamp: '2026-07-12T00:00:00Z'
date: 2026-07-12
source: https://arxiv.org/abs/2604.06550
authors:
- Hou
- Yang
- Pang
- Ma
arxiv: 2604.0655
signal: 9
context_elements:
- Three-layer detection pipeline
- LLM jury voting
- Cross-ecosystem adaptation
---

# SkillSieve: A Hierarchical Triage Framework for Detecting Malicious AI Agent Skills

## Origin

- **arXiv:** 2604.06550 (submitted 8 Apr 2026, v2 26 May 2026)
- **Authors:** Yinghan Hou, Zongyou Yang, Zaihu Pang, Xiujun Ma
- **Cited by:** 17
- **Data:** 49,592 ClawHub skills (2026-04-04 snapshot) + adversarial samples

## Skills Included

SkillSieve is a **skill security validation framework** — a three-layer detection pipeline for identifying malicious agent skills.

## Context Elements

### Three-Layer Detection Pipeline

**Layer 1 — Heuristic Filter (recall-tuned):**
- Regex, AST, and metadata checks
- Filters **86%** of volume at near-zero cost
- Runs on $440 ARM single-board computer

**Layer 2 — LLM Analysis:**
- Routes suspicious skills to an LLM
- Splits analysis into **4 parallel sub-tasks** with structured outputs
- Corrects Layer 1 false positives from domain-specific idioms

**Layer 3 — LLM Jury:**
- High-risk skills go before a **jury of 3 LLMs**
- Independent voting + debate when they disagree
- Optional XGBoost fast-path cuts 32% of Layer-2/3 calls (1.6-point F1 reduction)

## Composition Notes

SkillSieve is the most sophisticated skill security validation framework to date:

1. **Multi-modal detection** — combines static analysis (regex/AST) with semantic analysis (LLM) for both code and natural-language threats
2. **Hierarchical triage** — cost-efficient pipeline applying expensive analysis only where needed
3. **LLM jury mechanism** — 3-LLM voting + debate, a novel governance pattern for high-stakes decisions
4. **Cross-ecosystem portability** — adapted from ClawHub to Feishu/Lark (52 packages scanned)
5. **Deployed** as Feishu chat bot for real-time skill vetting

### Key Results
- **F1 = 0.920** (precision 0.912, recall 0.929) on 390-skill labeled benchmark
- Cost: **$0.006 per skill**
- Malicious skills average **4.03 vulnerabilities** across median **3 kill chain phases**
- Two ecosystem archetypes: Data Exfiltration vs System Compromise
- Open-sourced (code, data, benchmark)

## Reproducibility

- 49,592 real ClawHub skills + adversarial samples across 5 evasion techniques
- Cross-validated on Feishu/Lark (52 real packages)
- Open-sourced

## Connections

- Extends [three layer validation stack](../concepts/three-layer-validation-stack.md) with security-specific hierarchy
- Complements [clawhavoc marketplace attack](clawhavoc-marketplace-attack.md) (the threat being detected)
- Complements [supply chain agentic factory in toto](supply-chain-agentic-factory-in-toto.md) (provenance approach to similar problem)
- Validates marketplace risk data from [sok agentic skills beyond tool use](../papers/sok-agentic-skills-beyond-tool-use.md) (13-26% vulnerability rate)

