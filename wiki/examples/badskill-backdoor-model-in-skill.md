---
title: "BadSkill: Backdoor Attacks via Model-in-Skill Poisoning"
date: 2026-07-15
sources: ["arXiv:2604.09378"]
skills_included: ["Backdoor-fine-tuned model embedding", "Semantic compositional triggers", "Composite training objective", "Hard negative training"]
context_elements: ["Model-in-skill threat surface", "Semantic compositional triggers (multi-parameter)", "Composite training objective (classification + margin + poison)", "Poison rate analysis", "Cross-architecture robustness (5 families, 8 architectures)"]
composition: "Backdoor attack: adversary publishes benign-looking skill with embedded backdoor-fine-tuned model → model activates hidden payload only when skill parameters satisfy attacker-chosen semantic trigger combinations. Composite objective: classification loss + margin-based separation + poison-focused optimization."
reproducibility: "arXiv:2604.09378. 13 skills (8 triggered + 5 control), 571 negative-class + 396 trigger-aligned queries, 8 architectures (494M–7.1B), 5 model families. OpenClaw-inspired simulation."
rating: 9
---

# BadSkill: Backdoor Attacks via Model-in-Skill Poisoning

**Origin:** arXiv:2604.09378, Apr 2026
**Citations:** 12
**Authors:** Guiyao Tie, Jiawen Shi, Pan Zhou, Lichao Sun

## Overview

BadSkill introduces a novel backdoor attack surface: **model-in-skill poisoning**. Some agent skills bundle learned model artifacts (e.g., classifiers, embeddings) as part of their execution logic. BadSkill exploits this by publishing a seemingly benign skill whose embedded model is backdoor-fine-tuned to activate a hidden payload only when specific combinations of routine skill parameters are present.

## Threat Surface: Model-in-Skill

This is a **distinct** threat from:
- **Prompt injection** (manipulating skill instructions — cf. [[skillject-automated-prompt-injection]])
- **Code-level malicious tools** (malicious code in tool implementation — cf. [[maltool-malicious-tool-attacks]])
- **Permission misuse** (skills accessing unauthorized resources — cf. [[skillguard-permission-framework]])

Model-in-skill poisoning hides malicious behavior **inside model weights**, making it invisible to code scanning, prompt inspection, and permission frameworks.

## Attack Design

- **Composite training objective:**
  - Classification loss (maintain benign accuracy)
  - Margin-based separation (clean separation between triggered and non-triggered)
  - Poison-focused optimization (maximize trigger activation)
- **Semantic compositional triggers** — Triggers are combinations of routine skill parameters, not single values
- **Hard negatives** — Training includes difficult negative examples to maintain benign-side accuracy
- **OpenClaw-inspired simulation** — Preserves skill installation + execution in controlled environment

## Evaluation

| Metric | Result |
|--------|--------|
| Max ASR (attack success rate) | 99.5% across 8 triggered skills |
| ASR at 3% poison rate | 91.7% |
| Model architectures | 8 (494M–7.1B params), 5 families |
| Skills tested | 13 (8 triggered + 5 control) |
| Query sets | 571 negative-class + 396 trigger-aligned |
| Text perturbation robustness | Effective across 5 perturbation types |
| Benign accuracy | Maintained on negative-class queries |

## Context Elements

- **Model-in-skill threat model** — New threat surface: bundled model artifacts in skills
- **Semantic compositional triggers** — Multi-parameter trigger combinations (not single-value)
- **Backdoor training objective** — Classification + margin separation + poison optimization
- **Poison rate analysis** — Training data contamination quantification (3% → 91.7% ASR)

## Relation to Skill Bundle Patterns

BadSkill identifies a threat surface that existing defense frameworks don't address:

- Beyond [[skillject-automated-prompt-injection]] (prompt-level, not model-level)
- Beyond [[maltool-malicious-tool-attacks]] (code-level, not weight-level)
- Bypasses [[skillguard-permission-framework]] (malicious behavior is inside the model, not in tool calls)
- Motivates [[skillfortify-formal-verification-supply-chain]] (formal provenance verification for model artifacts)
- Motivates [[skillspector-nvidia-security-scanner]] (behavioral vetting, not just code scanning)
- Related to [[supply-chain-agentic-factory-in-toto]] (provenance for model artifacts in skills)

## Key Insight

Skills that bundle model artifacts create a supply-chain risk invisible to current defense frameworks. Backdoor-fine-tuned models can achieve 99.5% attack success with only 3% training data contamination, and the attack generalizes across architectures and model scales. This motivates stronger provenance verification and behavioral vetting for third-party skill artifacts containing models.

[[backlinks]]
