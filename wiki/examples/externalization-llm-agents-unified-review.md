---
title: "Externalization in LLM Agents: Unified Review of Memory, Skills, Protocols, and Harness"
date: 2026-07-15
sources: ["arXiv:2604.08224"]
skills_included: ["Theoretical framework for skill externalization", "Four-form taxonomy (memory, skills, protocols, harness)", "Historical progression (weights→context→harness)", "Parametric/externalized trade-off analysis"]
context_elements: ["Cognitive artifacts framework", "Four-form externalization taxonomy", "Weights→Context→Harness progression model", "Parametric vs. externalized capability trade-off", "Self-evolving harnesses (emerging direction)", "Shared agent infrastructure (emerging direction)"]
composition: "Theoretical review: cognitive artifacts lens → four forms of externalization (memory=state across time, skills=procedural expertise, protocols=interaction structure, harness=unification layer) → historical progression (weights→context→harness) → trade-off analysis → emerging directions → open challenges."
reproducibility: "arXiv:2604.08224, 54 pages, 21 authors including Jun Wang (UCL) and Weinan Zhang (SJTU). 35 citations."
rating: 10
---

# Externalization in LLM Agents: Unified Review of Memory, Skills, Protocols, and Harness Engineering

**Origin:** arXiv:2604.08224, Apr 2026 (54 pages)
**Citations:** 35
**Authors:** Chenyu Zhou, Huacan Chai, ... Jun Wang (UCL), Weinan Zhang (SJTU) — 21 authors

## Overview

This paper provides the first **unified systems-level review** of how LLM agent capabilities are increasingly externalized — moved from model weights into runtime infrastructure. Drawing on the idea of **cognitive artifacts**, it argues that agent infrastructure matters not merely because it adds auxiliary components, but because it transforms hard cognitive burdens into forms the model can solve more reliably.

## Core Framework: Four Forms of Externalization

| Form | What It Externalizes | Role |
|------|---------------------|------|
| **Memory** | State across time | Persists information across sessions |
| **Skills** | Procedural expertise | Encodes how-to knowledge as reusable packages |
| **Protocols** | Interaction structure | Standardizes agent-resource communication |
| **Harness engineering** | Unification layer | Coordinates memory + skills + protocols into governed execution |

## Historical Progression: Weights → Context → Harness

1. **Weights era** — Capabilities baked into model parameters (fine-tuning, RLHF)
2. **Context era** — Capabilities externalized into prompts, memory stores, skill packages
3. **Harness era** — Capabilities coordinated by surrounding infrastructure (governed execution, policy enforcement, orchestration)

## Key Theoretical Contributions

1. **Cognitive artifacts lens** — Agent infrastructure components are cognitive artifacts that transform hard cognitive burdens into tractable forms. This is not just "adding stuff" — it fundamentally changes what the model needs to compute internally.

2. **Three coupled forms** — Memory, skills, and protocols are distinct but coupled. They interact inside a larger agent system. Changes in one form affect the others.

3. **Harness as unification layer** — Harness engineering is not just "glue code" but the coordination layer that makes memory + skills + protocols reliable in practice. It provides governed execution.

4. **Parametric vs. externalized trade-off** — There's a fundamental design trade-off between capabilities baked into model weights vs. those externalized into runtime infrastructure. The optimal balance is an open question.

5. **Self-evolving harnesses** — Emerging direction: harnesses that improve themselves over time (cf. [[skillclaw-collective-skill-evolution]], [[coevoskills-self-evolving-skills]])

6. **Shared agent infrastructure** — Emerging direction: collective/shared agent infrastructure (cf. [[skillclaw-collective-skill-evolution]] shared skill repository)

## Open Challenges

- **Evaluation** — How to measure the effectiveness of externalized infrastructure?
- **Governance** — How to govern externalized capabilities?
- **Long-term co-evolution** — How do models and external infrastructure co-evolve over time?

## Context Elements

- **Cognitive artifacts framework** — Theoretical lens for understanding externalization
- **Four-form taxonomy** — Memory, skills, protocols, harness (unified classification system)
- **Weights→Context→Harness progression** — Historical development framework
- **Parametric/externalized trade-off** — Design space for capability placement

## Relation to Skill Bundle Patterns

This paper provides the **theoretical foundation** for the entire skill bundles wiki. Skills are formally defined as "externalized procedural expertise" — one of four coupled forms of externalization.

- Skills = externalized procedural expertise (formal definition)
- Harness engineering → [[skillguard-permission-framework]] (governance), [[skillfortify-formal-verification-supply-chain]] (verification), [[agentbound-mcp-access-control]] (access control)
- Self-evolving harnesses → [[skillclaw-collective-skill-evolution]], [[coevoskills-self-evolving-skills]]
- Shared infrastructure → [[skillclaw-collective-skill-evolution]] (shared skill repo)
- Related to [[arxiv-agent-skills-survey]] (prior survey — this is more systems-level and theoretical)
- Related to [[skill-os-skills-as-apps]] (OS abstraction = harness engineering)
- Validates [[swe-skills-bench-utility-benchmark]] findings (externalized expertise can fail when it doesn't match context)
- Connects to [[skillreducer-token-efficiency]] (parametric/externalized trade-off in practice)

## Key Insight

Agent progress increasingly depends not just on stronger models, but on better external cognitive infrastructure. Skills, memory, and protocols are not auxiliary add-ons — they are cognitive artifacts that transform what the model needs to compute. The harness — the coordination layer that governs their interaction — is the emerging frontier. Understanding the parametric/externalized trade-off and enabling self-evolving, shared infrastructure are the key open challenges.

[[backlinks]]
