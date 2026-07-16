---
type: Concept
title: Skill Security Governance — The Emergence of Formalized Risk Management
description: A synthesis of four converging frameworks that together form a complete governance system for skill bundle security.
---

# Skill Security Governance — The Emergence of Formalized Risk Management

## Concept

A synthesis of four converging frameworks that together form a complete governance system for skill bundle security. As the Agent Skills ecosystem has matured from early adoption (October 2025) to widespread deployment (Q1 2026), security concerns have crystalized into structured, formalized governance approaches.

## The Four Pillars

### 1. Risk Classification: OWASP AST10
[owasp agentic skills top 10](../examples/owasp-agentic-skills-top-10.md) provides the **vulnerability taxonomy** — answering "what can go wrong?" with 10 risk categories (AST01–AST10), a Lethal Trifecta model, and a proposed Universal Skill Format with permission schemas.

### 2. Governance Process: Agentic Trust Framework
[agentic trust framework csa](../examples/agentic-trust-framework-csa.md) provides the **maturity model** — answering "how do we maintain control?" with 4 autonomy levels, 5 promotion gates, and phased implementation (crawl-walk-run).

### 3. Empirical Evidence: Mondoo + PurpleBox + arXiv Survey
[mondoo agent skills security](../examples/mondoo-agent-skills-security.md) (25%+ vulnerable, 14 attack patterns), [purplebox supply chain security](../examples/purplebox-supply-chain-security.md) (12% infection rate, 6-vector taxonomy), and [arxiv agent skills survey](../examples/arxiv-agent-skills-survey.md) (26.1% vulnerability rate, 4-tier trust framework) provide the **data foundation** — answering "how bad is it really?"

### 4. Implementation: NVIDIA Verified + Veto + GraphGuard
[nvidia verified agent skills](../examples/nvidia-verified-agent-skills.md) (OpenSSF signing, SkillSpector scanning), [veto agent authorization](../examples/veto-agent-authorization.md) (least-privilege authorization), and [graphguard os guardrails](../examples/graphguard-os-guardrails.md) (SHACL + Cypher guardrails) provide the **technical countermeasures** — answering "how do we fix it?"

## The Governance Stack

```
┌──────────────────────────────────┐
│  OWASP AST10 (Risk Taxonomy)     │  ← Identifies what can go wrong
├──────────────────────────────────┤
│  ATF (Maturity Model)            │  ← Defines how to mature safely
├──────────────────────────────────┤
│  Empirical Data (Mondoo, arXiv)  │  ← Quantifies actual risk
├──────────────────────────────────┤
│  Technical Controls (NVIDIA,     │  ← Implements countermeasures
│  Veto, GraphGuard, NemoClaw)     │
├──────────────────────────────────┤
│  Distribution (Plugins,          │  ← Enables versioning + provenance
│  Marketplaces, Versioning)       │
└──────────────────────────────────┘
```

## Key Insight: The Governance Gap is Closing

Between Iteration 10 (2026-05-25) and Iteration 11 (2026-05-26), the catalog grew from having scattered security advice (Mondoo patterns, PurpleBox taxonomy, NVIDIA signing) to having **two formal governance frameworks** (OWASP AST10, ATF) and **one academic survey** validating the problem scope. This represents a step-change from empirical observation to formal governance.

## Open Questions

1. Will OWASP's Universal Skill Format become the de facto standard, or will multiple formats (OWASP, NVIDIA SKILLCARD, marketplace-specific) fragment the ecosystem?
2. Can the ATF maturity model be automated — continuous trust scoring rather than manual promotion gates?
3. Do the 26.1% / 36.8% vulnerability rates stabilize as the ecosystem matures, or do they rise as adoption grows?

## Related Concepts
- [verified skill governance](verified-skill-governance.md) — NVIDIA's cryptographic signing approach (pre-dates both AST10 and ATF)
- [constraint rules as context](constraint-rules-as-context.md) — Rules/authorization patterns that AST10 and ATF formalize
- [validator explanation pattern](validator-explanation-pattern.md) — SHACL validation as governance mechanism
