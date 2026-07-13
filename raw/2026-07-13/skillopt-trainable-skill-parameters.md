# SkillOpt: Agent Skills as Trainable Parameters

**Source:** Microsoft Research Blog (June 2026)
**Paper:** "SkillOpt: Executive Strategy for Self-Evolving Agent Skills"
**Authors:** Bei Liu, Kai Qiu, Dongdong Chen, Chong Luo (Microsoft Research Asia)
**Signal Rating:** 10/10

## At a Glance

- SkillOpt turns skill editing into a training process, making agent behavior more reliable without changing model weights
- Treats agent skill file as a trainable parameter outside a frozen target model
- Best or tied-best method in all 52 evaluation cells across 6 benchmarks, 7 target models, and 3 execution modes
- Skills stay compact and auditable through bounded text edits, validation gating, rejected-edit feedback, and slow/meta updates
- Optimized skills transfer across model scales, agent harnesses, and related tasks

## How SkillOpt Works

**Forward-Backward-Update Cycle in Text Space:**

1. **Forward pass:** Frozen target model executes a batch of training tasks with the current skill
2. **Backward pass:** Separate optimizer model reads trajectories in reflection minibatches, distilling patterns to preserve (success) and patterns to correct (failures)
3. **Update step:** Optimizer proposes small add/delete/replace edits; candidates are merged, deduplicated, ranked, and clipped by a textual learning rate (per-step edit budget)

**Validation Gating:**
- Every candidate skill must pass strict validation gate: adopted only if it scores strictly higher than current skill on held-out validation split
- Rejected edits enter a rejected-edit buffer (negative feedback for later optimizer calls)
- Epoch-wise slow/meta update consolidates longer-horizon lessons on slower cadence

## Key Results

- GPT-5.5 in direct chat: 58.8 → 82.3 six-benchmark average (+23.5 points)
- +5.4 points above oracle that picks the single best competing method per cell
- SpreadsheetBench: 41.8 → 80.7
- OfficeQA: 33.1 → 72.1
- LiveMathematicianBench: 37.6 → 66.9
- Inside Codex: +24.8 points; inside Claude Code: +19.1 points over no skill
- Outperforms: human-written skills, one-shot LLM skills, Trace2Skill, TextGrad, GEPA, and EvoSkill

## Small Model + Skill File

- GPT-5.4-mini with optimized skill (64.3) exceeds GPT-5.4 no-skill baseline (59.7)
- GPT-5.4-nano with optimized skill (57.4) exceeds GPT-5.2 no-skill baseline (51.3)
- Qwen3.5-4B (4B params) surpasses GPT-5.2's no-skill baseline
- "Gains that once required a larger model can now be approximated by one optimized skill file"

## Skill Transfer

- **Cross-model-scale:** Skills trained on one model improve performance on different models
- **Cross-harness:** Spreadsheet skill trained in Codex, dropped into Claude Code: 22.1 → 81.8 (+59.7) — above direct training (80.4). Suggests SkillOpt learns general workflow logic, not harness-specific recipes
- **Cross-task:** Skills transfer to nearby benchmarks (math skill → math benchmark)

## Context Elements

- **Validation gating:** Strict held-out validation before skill adoption
- **Textual learning rate:** Per-step edit budget constraining skill modifications
- **Rejected-edit buffer:** Negative feedback mechanism for failed edits
- **Slow/meta updates:** Epoch-wise consolidation of longer-horizon lessons
- **Compact skill files:** Very few accepted edits (auditable, readable)
- **Bounded text edits:** Add/delete/replace with deduplication and ranking

## Key Insights

- Reframes "how do we write a better prompt?" to "how do we train the skill?"
- Skill file = trainable parameter, model = frozen (like LoRA for prompts)
- Prevents uncontrolled skill evolution / prompt drift
- Skill-level optimization captures reusable workflow knowledge, not benchmark-specific instructions
- Small models + optimized skills can approximate frontier model performance
