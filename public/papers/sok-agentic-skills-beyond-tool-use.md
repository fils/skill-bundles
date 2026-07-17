---
type: Paper
title: 'SoK: Agentic Skills — Beyond Tool Use in LLM Agents'
description: A comprehensive Systematization of Knowledge paper that provides the **first formal definition** of agentic skills, a complete lifecycle model, and dual taxonomies.
resource: https://arxiv.org/abs/2602.20867
timestamp: '2026-07-11T00:00:00Z'
date: '2026-07-11'
---

# SoK: Agentic Skills — Beyond Tool Use in LLM Agents

**Source:** https://arxiv.org/abs/2602.20867 (arXiv:2602.20867v1, 24 Feb 2026)
**Date Added:** 2026-07-11 (Iteration 36)
**Authors:** Yanna Jiang, Delong Li, Haiyu Deng, Baihe Ma, Xu Wang, Qin Wang, Guangsheng Yu
**License:** CC BY 4.0
**Bundle Type:** Systematization of Knowledge (SoK) · Formal Definition · Lifecycle Model · Security Analysis
**Confidence:** 10/10

## Name & Origin

A comprehensive Systematization of Knowledge paper that provides the **first formal definition** of agentic skills, a complete lifecycle model, and dual taxonomies. Grounded by the **ClawHavoc case study** — a real-world supply-chain attack on a skill marketplace.

## Skills Included (as conceptual framework)

- **Formal skill definition:** S = (C, π, T, R) — applicability conditions, execution policy, termination criteria, reusable interface
- **Skill lifecycle model:** 7 stages — discovery → practice → distillation → storage → composition → evaluation → update
- **Seven design patterns** for skill packaging/execution:
  1. Metadata-driven progressive disclosure (SKILL.md)
  2. Executable code skills
  3. Workflow enforcement
  4. Self-evolving libraries
  5. Marketplace distribution
  6–7. (detailed in full paper)
- **Representation × Scope taxonomy:** NL/code/policy/hybrid × web/OS/SE/robotics

## Context Elements

- **Formal skill definition** S=(C,π,T,R) — the canonical formal vocabulary for skill bundle analysis
- **Lifecycle model** — 7-stage framework for tracking skill bundle evolution
- **Seven design patterns** — system-level taxonomy of how skills are packaged and executed
- **ClawHavoc case study** — ~1,200 malicious skills infiltrated ClawHub marketplace; exfiltrated API keys, crypto wallets, browser credentials
- **Security/governance analysis** — supply-chain risks, prompt injection via payloads, trust-tiered execution, pattern-specific risk matrix
- **Evaluation framework** — benchmark mapping; curated skills outperform self-generated ones

## How Context Elements Support Skills

The SoK provides the **theoretical foundation** for the entire skill bundle research program:

1. **S=(C,π,T,R) definition** — gives precise boundary conditions: skills ≠ tools (atomic), ≠ plans (one-time), ≠ memory (observations). Skills are simultaneously **executable, reusable, and governable**.
2. **Lifecycle model** — maps the full trajectory from discovery to update, providing a framework for bundle evolution tracking.
3. **Seven design patterns** — systematizes how skills are packaged in practice, mapping to existing wiki examples.
4. **ClawHavoc case study** — quantifies real-world supply-chain risk (~13% malicious rate in a marketplace), validating security concerns.
5. **"Self-generated skills degrade performance"** — a key empirical finding that validates the need for formal context elements (verification, validation).

## Composition Notes

This SoK serves as a **meta-framework** for the wiki:

| SoK Component | Wiki Mapping |
|----------------|-------------|
| Formal definition (S) | All wiki/examples/ entries |
| Lifecycle model | [skill bundle patterns](../concepts/skill-bundle-patterns.md) |
| Design patterns | [skill bundle patterns](../concepts/skill-bundle-patterns.md), individual examples |
| Security analysis | [skill security governance](../concepts/skill-security-governance.md), [owasp agentic skills top 10](../examples/owasp-agentic-skills-top-10.md) |
| ClawHavoc case study | [clawhavoc marketplace attack](../examples/clawhavoc-marketplace-attack.md) (new) |
| Evaluation framework | [skillsbench agent skills benchmark](../examples/skillsbench-agent-skills-benchmark.md) |

## Reproducibility

High — open-access arXiv paper (CC BY 4.0), 192K+ characters of full text, comprehensive bibliography (76+ references).

## Bundle Links

- [skill bundle patterns](../concepts/skill-bundle-patterns.md) — design patterns taxonomy
- [skill security governance](../concepts/skill-security-governance.md) — security analysis
- [three layer validation stack](../concepts/three-layer-validation-stack.md) — trust tier model
- [owasp agentic skills top 10](../examples/owasp-agentic-skills-top-10.md) — security threats
- [purplebox supply chain security](../examples/purplebox-supply-chain-security.md) — supply chain
- [coevoskills self evolving skills](../examples/coevoskills-self-evolving-skills.md) — self-evolving pattern (Pattern 4)
- [clawhavoc marketplace attack](../examples/clawhavoc-marketplace-attack.md) — case study
- [supply chain agentic factory in toto](../examples/supply-chain-agentic-factory-in-toto.md) — SLSA/in-toto provenance
- [agentskills workshop 2026](agentskills-workshop-2026.md) — workshop venue

## Sources

- https://arxiv.org/abs/2602.20867
- https://arxiv.org/html/2602.20867v1
- https://www.semanticscholar.org/paper/SoK%3A-Agentic-Skills-Beyond-Tool-Use-in-LLM-Agents-Jiang-Li/ae06bb0819ec521d45909b2cbf599ff36ea025e2
