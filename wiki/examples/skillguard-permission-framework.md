---
type: Skill Bundle Example
title: 'SkillGuard: A Permission Framework for Agent Skills'
description: SkillGuard is a skill-centric permission framework that treats skills as **permission-bearing executable artifacts**.
resource: https://arxiv.org/abs/2606.03024
timestamp: '2026-07-14T00:00:00Z'
date: 2026-07-14
sources:
- arXiv:2606.03024
- https://github.com/Dianshu-Liao/SkilLGuard
skills_included:
- Skill manifests
- Runtime permission access control
- User-mediated authorization
- Capability inference
- Behavior monitoring
context_elements:
- Dual-plane governance (context + action)
- Skill manifests (capability declaration)
- Deny-by-default enforcement
- Permission taxonomy (99.76% coverage)
- Runtime access control with canonical capability mapping
composition: 'Five-component framework: skill manifests declare capabilities → runtime access control maps tool invocations to canonical capabilities → user-mediated authorization for sensitive permissions → deny-by-default enforcement → behavior monitoring.'
reproducibility: Open-sourced on GitHub (Dianshu-Liao/SkilLGuard). 315 real-world skills evaluated.
rating: 9
---

# SkillGuard: A Permission Framework for Agent Skills

**Origin:** CSIRO + Australian National University + UNSW (arXiv:2606.03024, June 2026)
**GitHub:** https://github.com/Dianshu-Liao/SkilLGuard

## Overview

SkillGuard is a skill-centric permission framework that treats skills as **permission-bearing executable artifacts**. It introduces a **dual-plane governance model** that jointly regulates context influence (what a skill injects into an agent's reasoning) and action side effects (what a skill causes the agent to do at runtime). This addresses a fundamental gap: existing approaches secure either context OR actions, but not both.

## Dual-Plane Governance

- **Context plane:** skills introduce instructions, examples, retrieved documents, memory fragments, hidden assumptions that reshape agent reasoning
- **Action plane:** skills trigger tool calls, file/secret access, code execution, network communication, delegation to other agents/skills/MCP servers

## Five Core Components

1. **Skill Manifest** — declares capability surface; instantiates permissions into runtime policy state
2. **Runtime permission access control** — maps host-specific tool invocations to canonical capabilities
3. **User-mediated authorization** — approve once, approve for session, or deny
4. **Deny-by-default enforcement** — actions not explicitly permitted are blocked
5. **Capability inference + behavior monitoring** — infers skill capabilities, monitors runtime behavior

## Evaluation

| Metric | Result |
|--------|--------|
| Permission taxonomy coverage | 99.76% of observed protected objects |
| Automated manifest generation F1 | 91.0% |
| Contextual injection attack reduction | 32.37% → 23.02% |
| Obvious injection attack reduction | 25.56% → 16.67% |
| Benign task utility | Maintained |

## Context Elements

- **Dual-plane governance** — novel architectural pattern recognizing skills operate across context + action planes
- **Skill manifests** — formal declaration of capability surface (pre-execution)
- **Permission taxonomy** — formal vocabulary for skill capabilities
- **Deny-by-default** — security posture requiring explicit grants
- **Behavior monitoring** — runtime verification element

## Relation to Skill Bundle Patterns

SkillGuard extends the skill bundle thesis to include **permission governance** as a formal context element:
- Complements [skillfortify formal verification supply chain](skillfortify-formal-verification-supply-chain.md) (formal verification/static analysis) — SkillGuard governs runtime, SkillFortify governs supply chain
- Complements [skillsieve malicious skill detection](skillsieve-malicious-skill-detection.md) (detection) — SkillGuard prevents, SkillSieve detects
- Extends [veto agent authorization](veto-agent-authorization.md) and [tool use firewall](tool-use-firewall.md) patterns to skill-centric governance
- Dual-plane model is novel: recognizes skills shape both reasoning (context) and execution (actions)

## Key Insight

Agent skills operate across two coupled planes — context (what a skill tells the agent to think) and action (what a skill causes the agent to do). Security frameworks that address only one plane leave the other vulnerable. SkillGuard's dual-plane governance with deny-by-default enforcement provides a practical foundation for skill ecosystem security.

