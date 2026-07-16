# OpenClaw-Skill: Collective Skill Tree Search (CSTS)

**Source:** https://arxiv.org/abs/2606.16774 | https://arxiv.org/html/2606.16774v1
**Date:** Jun 2026 | PolyU / NTU / Tsinghua / RMIT / BUAA
**Signal rating:** 8/10

## Key ideas
- **CSTS** builds structured, diverse, transferable *trees of skills* via collective multi-model intelligence.
- Two phases: **CSN-Gen** (multi-model candidate generation for subtasks) + **CSN-Assess** (collective quality scoring + collective transferability scoring across models).
- Addresses: skill fragmentation (local-only procedures), limited diversity (single-model bias), poor transferability (drops across backbones).
- **Collective Skill RL**: actively selects multiple skills from the tree to broaden solution-space exploration.
- Produces OpenClaw-Skill model with strong long-horizon planning / tool use / generalization.

## Why skill-bundles
Distinct from SkillClaw (trajectory aggregation multi-user) — CSTS is *construction-time collective search* into hierarchical skill trees with explicit transferability gates. Tree structure is a first-class context element for composition.
