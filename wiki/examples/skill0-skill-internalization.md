---
title: "SKILL0: In-Context Agentic RL for Skill Internalization"
date: 2026-07-16
sources: ["arXiv:2604.02268", "https://github.com/ZJU-REAL/SkillZero"]
skills_included: ["Training-time skill scaffolding", "Dynamic Curriculum skill withdrawal", "Category-grouped skill rendering"]
context_elements: ["Skill internalization objective", "Dynamic Curriculum (on-policy helpfulness + decaying budget)", "Visual Context Rendering", "Zero-shot inference (skills@train, zero@infer)", "Token-budget efficiency (<0.5k/step)"]
composition: "Training loop: full skill context → on-policy helpfulness filter → linear budget decay → zero-shot parametric agent."
reproducibility: "Code at ZJU-REAL/SkillZero; ALFWorld + Search-QA + WebShop; +9.7% / +6.6% / +10.1% over RL baselines."
rating: 9
---

# SKILL0: In-Context Agentic RL for Skill Internalization

**Origin:** Zhejiang University + Meituan + Tsinghua (Lu et al.), arXiv:2604.02268, Apr 2026 (v2 May 2026)  
**GitHub:** https://github.com/ZJU-REAL/SkillZero

## Overview

SKILL0 asks whether agent skills must remain **external packages at inference**, or can be **internalized into model parameters**. Motto: **"Skills at training, zero at inference."** It is the first RL framework that treats skill internalization as an explicit training objective via a Dynamic Curriculum that anneals skill scaffolding.

## Architecture

1. **Offline skill grouping** — Skills categorized and rendered with interaction history into compact **visual context**
2. **Full-scaffold phase** — Policy trained with complete skill files for tool invocation and multi-turn completion
3. **Dynamic Curriculum** — On-policy helpfulness scores each skill file; retain only skills that still help within a **linearly decaying** context budget
4. **Zero-shot end state** — Agent operates without runtime skill retrieval

## Key Results

| Benchmark | Gain vs standard RL |
|-----------|---------------------|
| ALFWorld | +9.7% |
| Search-QA | +6.6% |
| WebShop | +10.1% |
| Context | <0.5k tokens/step (≈5× vs SkillRL-class baselines) |

## Context Elements

- **Internalization objective** — Skills become weights, not prompt payloads
- **On-policy helpfulness gating** — Curriculum keeps only still-useful skill files
- **Progressive disclosure inverted** — Disclosure shrinks over training rather than expands at inference
- **Efficiency contract** — Removes retrieval noise and token tax at deployment

## Relation to Skill Bundle Patterns

- Opposite pole of [[skillopt-trainable-skill-parameters]] (skills stay external text parameters)
- Contrasts [[memento-skills-agent-designing-agent]] (skills as persistent markdown memory, no weight updates)
- Related to [[skill1-unified-skill-evolution-rl]] (co-evolve selection/utilization/distillation still external)
- Complements [[coevoskills-self-evolving-skills]] and [[evoskill-automated-skill-discovery]] (evolution of external packages)
- Theoretical frame: [[externalization-llm-agents-unified-review]] weights↔context trade-off

## Key Insight

Skill bundles can be a **training substrate**, not only a runtime product. Dynamic Curriculum internalization trades post-training adaptability for zero-shot autonomy and massive context savings — a first-class design choice in the Define→Generate→Serve→Align lifecycle.

[[backlinks]]
