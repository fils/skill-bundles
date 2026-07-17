---
type: Skill Bundle Example
title: 'SkillOpt: Agent Skills as Trainable Parameters'
description: SkillOpt reframes the question from "how do we write a better prompt?" to "how do we train the skill?" It treats the skill file as a **trainable parameter** living outside a frozen target model — like LoRA for prompts...
timestamp: '2026-07-13T00:00:00Z'
date: 2026-07-13
sources:
- Microsoft Research Blog
- 'SkillOpt: Executive Strategy for Self-Evolving Agent Skills'
skills_included:
- Optimizer model
- Frozen target model
- Validation gate
context_elements:
- Textual learning rate (per-step edit budget)
- Validation gating (held-out split)
- Rejected-edit buffer (negative feedback)
- Slow/meta updates (epoch-wise consolidation)
- Bounded text edits (add/delete/replace)
- Compact auditable skill files
composition: 'Forward-backward-update cycle: frozen target model executes tasks → optimizer model reflects on trajectories → bounded text edits → validation gate. Skills transfer across model scales, agent harnesses, and tasks.'
reproducibility: Evaluated across 6 benchmarks, 7 target models, 3 execution modes (52 cells). Outperforms EvoSkill, GEPA, TextGrad, Trace2Skill, one-shot LLM skills, human-written skills.
rating: 10
---

# SkillOpt: Agent Skills as Trainable Parameters

**Origin:** Microsoft Research Asia (Bei Liu, Kai Qiu, Dongdong Chen, Chong Luo), June 2026
**Paper:** "SkillOpt: Executive Strategy for Self-Evolving Agent Skills"

## Overview

SkillOpt reframes the question from "how do we write a better prompt?" to "how do we train the skill?" It treats the skill file as a **trainable parameter** living outside a frozen target model — like LoRA for prompts instead of weights. The result is a training-style optimization loop with consistent gains, compact readable skill files, and transferable workflow knowledge.

## Forward-Backward-Update Cycle

1. **Forward pass:** Frozen target model executes a batch of training tasks with the current skill
2. **Backward pass:** Separate optimizer model reads trajectories in reflection minibatches — distills patterns to preserve (success) and patterns to correct (failures)
3. **Update step:** Optimizer proposes small add/delete/replace edits → merged, deduplicated, ranked, clipped by **textual learning rate** (per-step edit budget)

### Validation Gating
- Candidate skill adopted **only if** it scores strictly higher than current skill on held-out validation
- Rejected edits → **rejected-edit buffer** (negative feedback for later optimizer calls)
- **Slow/meta updates** on slower cadence consolidate longer-horizon lessons

## Key Results

| Configuration | Baseline | SkillOpt | Improvement |
|---------------|----------|----------|-------------|
| GPT-5.5 (6-benchmark avg) | 58.8 | 82.3 | +23.5 |
| GPT-5.5 in Codex | — | — | +24.8 |
| GPT-5.5 in Claude Code | — | — | +19.1 |
| SpreadsheetBench | 41.8 | 80.7 | +38.9 |
| OfficeQA | 33.1 | 72.1 | +39.0 |
| LiveMathematicianBench | 37.6 | 66.9 | +29.3 |

**52/52 evaluation cells:** Best or tied-best against human-written skills, one-shot LLM skills, Trace2Skill, TextGrad, GEPA, and EvoSkill.

## Small Model + Skill File

- GPT-5.4-mini + skill (64.3) > GPT-5.4 no-skill (59.7)
- GPT-5.4-nano + skill (57.4) > GPT-5.2 no-skill (51.3)
- Qwen3.5-4B + skill > GPT-5.2 no-skill baseline
- **"Gains that once required a larger model can now be approximated by one optimized skill file"**

## Skill Transfer

| Transfer Type | Example | Result |
|---------------|---------|--------|
| Cross-model-scale | GPT-5.4 → Qwen3.5-4B | Skills continue to deliver gains |
| Cross-harness | Codex → Claude Code | 22.1 → 81.8 (+59.7, above direct training 80.4) |
| Cross-task | Math skill → Math benchmark | Gains maintained |

Cross-harness transfer suggests SkillOpt learns **general workflow logic**, not harness-specific recipes.

## Relation to Skill Bundle Patterns

SkillOpt represents the **training-based optimization** paradigm, complementing:
- [evoskill automated skill discovery](evoskill-automated-skill-discovery.md) (discovery-based) — SkillOpt outperforms EvoSkill on all cells
- [skillmoo multi objective optimization](skillmoo-multi-objective-optimization.md) (search-based) — SkillOpt uses gradient-like text optimization
- [coevoskills self evolving skills](coevoskills-self-evolving-skills.md) (evolution-based) — SkillOpt adds validation gating + bounded edits
- [skillreducer token efficiency](skillreducer-token-efficiency.md) (content reduction) — SkillOpt grows skills purposefully; SkillReducer reduces them

## Key Insight

Treating skill files as trainable parameters with a proper optimization loop (forward-backward-update, validation gating, learning rate, rejected-edit buffer) produces skills that are compact, auditable, and transferable across models, harnesses, and tasks — without changing model weights. This is the closest analogue to deep learning optimization applied to the skill layer.

