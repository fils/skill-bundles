# SkillSieve: A Hierarchical Triage Framework for Detecting Malicious AI Agent Skills

**Source:** https://arxiv.org/abs/2604.06550
**Date:** 2026-07-12
**Authors:** Yinghan Hou, Zongyou Yang, Zaihu Pang, Xiujun Ma
**Submitted:** 8 Apr 2026 (v1), revised 26 May 2026 (v2)
**Signal:** 9/10

## Abstract

OpenClaw's ClawHub marketplace hosts tens of thousands of community-contributed agent skills (49,592 in 2026-04-04 snapshot), and recent audits report that 13-26% contain security vulnerabilities. Regex scanners miss obfuscated payloads; formal static analyzers cannot read the natural-language skill.md instructions that hide prompt injection and social engineering. Neither approach covers both modalities.

### Three-Layer Detection Pipeline

**Layer 1 — Heuristic Filter (recall-tuned):**
- Regex, AST, and metadata checks
- Filters **86%** of volume
- Runs on $440 ARM single-board computer

**Layer 2 — LLM Analysis:**
- Routes suspicious skills to an LLM
- Splits analysis into **4 parallel sub-tasks** with structured outputs
- Corrects Layer 1 false positives from domain-specific idioms

**Layer 3 — LLM Jury:**
- High-risk skills go before a **jury of 3 LLMs**
- Independent voting + debate when they disagree
- Optional XGBoost fast-path cuts 32% of Layer-2/3 LLM calls (1.6-point F1 reduction, preserves full recall)

### Key Results
- **F1 = 0.920** (precision 0.912, recall 0.929) on 390-skill labeled benchmark
- Cost: **$0.006 per skill**
- Evaluated on 49,592 real ClawHub skills + adversarial samples across 5 evasion techniques
- Cross-ecosystem generalization: adapted to Feishu/Lark, scanned 52 real packages
- Deployed as Feishu chat bot for real-time skill vetting
- Code, data, and benchmark **open-sourced**

### Key Findings on Malicious Skills
- Malicious skills average **4.03 vulnerabilities** across median **3 kill chain phases**
- Ecosystem split into two archetypes: Data Exfiltration and System Compromise

## Relevance to Skill Bundles

SkillSieve is the most sophisticated **skill security validation** framework to date:
1. **Multi-modal detection** — combines static analysis (regex/AST) with semantic analysis (LLM) for both code and natural-language threats
2. **Hierarchical triage** — cost-efficient pipeline that applies expensive analysis only where needed (86% filtered at Layer 1)
3. **LLM jury mechanism** — 3-LLM voting + debate for high-risk skills, a novel governance pattern
4. **Cross-ecosystem portability** — adapted from ClawHub to Feishu/Lark, suggesting generalizability

This extends the [[three-layer-validation-stack]] pattern with a specifically security-focused hierarchy, complementing [[clawhavoc-marketplace-attack]] (threat) and [[supply-chain-agentic-factory-in-toto]] (provenance).

## Key Quotes

> "Regex scanners miss obfuscated payloads; formal static analyzers cannot read the natural-language skill.md instructions that hide prompt injection and social engineering. Neither approach covers both modalities."

> "Malicious skills average 4.03 vulnerabilities across a median of three kill chain phases, and the ecosystem has split into two archetypes: Data Exfiltration and System Compromise"

## Links
- PDF: https://arxiv.org/pdf/2604.06550
- HTML: https://arxiv.org/html/2604.06550v2
- Cited by 17
