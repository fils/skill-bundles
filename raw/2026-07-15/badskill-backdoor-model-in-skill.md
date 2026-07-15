# BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning

**Source:** arXiv:2604.09378 (cs.CR, cs.AI)
**Authors:** Guiyao Tie, Jiawen Shi, Pan Zhou, Lichao Sun
**Submitted:** Apr 10, 2026
**Citations:** 12
**Signal Rating:** 9/10

## Abstract

Agent ecosystems increasingly rely on installable skills to extend functionality, and some skills bundle learned model artifacts as part of their execution logic. This creates a supply-chain risk not captured by prompt injection or ordinary plugin misuse: a third-party skill may appear benign while concealing malicious behavior inside its bundled model.

**BadSkill** is a backdoor attack formulation that targets this **model-in-skill** threat surface. An adversary publishes a seemingly benign skill whose embedded model is backdoor-fine-tuned to activate a hidden payload only when routine skill parameters satisfy attacker-chosen semantic trigger combinations.

## Attack Design

- **Composite training objective** — classification loss + margin-based separation + poison-focused optimization
- **Semantic compositional triggers** — Triggers activate only when specific combinations of skill parameters are present
- **Hard negatives** — Training includes difficult negative examples to maintain benign-side accuracy
- **OpenClaw-inspired simulation environment** — Preserves third-party skill installation + execution while enabling controlled multi-model study

## Evaluation

- **13 skills** — 8 triggered tasks + 5 non-trigger control skills
- **Query sets** — 571 negative-class queries + 396 trigger-aligned queries
- **8 architectures** — 494M to 7.1B parameters, 5 model families
- **Attack success rate (ASR):** up to 99.5% average across 8 triggered skills
- **Poison rate efficiency:** 3% poison rate → 91.7% ASR
- **Robustness:** Effective across model scales and 5 text perturbation types
- **Benign accuracy:** Maintained on negative-class queries

## Key Ideas

1. **Model-in-skill as distinct threat surface** — Skills that bundle model artifacts (not just code/prompts) create a new attack vector distinct from prompt injection or plugin misuse.
2. **Semantic compositional triggers** — Triggers are combinations of routine skill parameters, making them hard to detect via single-parameter analysis.
3. **Low poison rate effectiveness** — 3% poison rate achieves 91.7% ASR, showing minimal training data contamination is needed.
4. **Cross-architecture generalization** — Attack works across 5 model families and 8 architectures (494M–7.1B params).
5. **Motivates stronger provenance verification** — Identifies need for behavioral vetting of third-party skill artifacts containing models.

## Context Elements

- **Model-in-skill threat model** — New threat surface: bundled model artifacts in skills
- **Semantic compositional triggers** — Multi-parameter trigger combinations
- **Backdoor training objective** — Classification + margin separation + poison optimization
- **Poison rate sweeps** — Training data contamination analysis

## Relation to Existing Wiki

- Identifies a threat surface beyond [[skillject-automated-prompt-injection]] (prompt injection)
- Related to [[maltool-malicious-tool-attacks]] (code-level malicious tools)
- Motivates defense frameworks: [[skillfortify-formal-verification-supply-chain]] (formal verification), [[skillspector-nvidia-security-scanner]] (scanning)
- Related to [[skillguard-permission-framework]] (runtime governance — but BadSkill bypasses permission models since the malicious behavior is inside the model)
