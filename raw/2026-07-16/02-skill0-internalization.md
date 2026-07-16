# SKILL0: In-Context Agentic RL for Skill Internalization

**Source:** https://arxiv.org/abs/2604.02268 | https://github.com/ZJU-REAL/SkillZero
**Date:** Apr 2026 (v2 May 2026) | Zhejiang University + Meituan + Tsinghua
**Signal rating:** 9/10

## Key ideas
- Problem: inference-time skill loading adds token overhead, retrieval noise, and never truly acquires knowledge.
- **SKILL0** formulates skill internalization as explicit training objective: "Skills at training, zero at inference."
- Dynamic Curriculum: start with full skill context; evaluate on-policy helpfulness of each skill file; retain only still-helpful skills within linearly decaying budget → fully zero-shot.
- Visual Context Rendering: skills grouped offline by category + interaction history → compact visual context for tool invocation / multi-turn completion.
- Results: +9.7% ALFWorld, +6.6% Search-QA, +10.1% WebShop vs standard RL; <0.5k tokens/step (≈5× more efficient than SkillRL baselines).

## Why skill-bundles
Completes the lifecycle spectrum: external skill packages → progressive withdrawal → parametric internalization. Direct contrast to SkillOpt (skills stay external trainable text) and Memento (skills as evolving markdown memory).
