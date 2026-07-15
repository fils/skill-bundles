# SkillClaw: Let Skills Evolve Collectively with Agentic Evolver

**Source:** arXiv:2604.08377 (cs.AI, cs.CL)
**Authors:** Ziyu Ma, Shidong Yang, Yuxiang Ji, Xucong Wang, Yong Wang, Yiming Hu, Tongwen Huang, Xiangxiang Chu
**Submitted:** Apr 9, 2026
**Citations:** 42
**GitHub:** https://github.com/AMAP-ML/SkillClaw (2.1k stars, 202 forks, MIT license)
**Signal Rating:** 9/10

## Abstract

LLM agents such as OpenClaw rely on reusable skills to perform complex tasks, yet these skills remain largely static after deployment. Similar workflows, tool usage patterns, and failure modes are repeatedly rediscovered across users, preventing the system from improving with experience. While interactions from different users provide complementary signals about when a skill works or fails, existing systems lack a mechanism to convert such heterogeneous experiences into reliable skill updates.

**SkillClaw** is a framework for collective skill evolution in multi-user agent ecosystems, which treats cross-user and over-time interactions as the primary signal for improving skills. SkillClaw continuously aggregates trajectories generated during use and processes them with an autonomous evolver, which identifies recurring behavioral patterns and translates them into updates to the skill set by refining existing skills or extending them with new capabilities. The resulting skills are maintained in a shared repository and synchronized across users, allowing improvements discovered in one context to propagate system-wide while requiring no additional effort from users.

Experiments on WildClawBench show that with limited interaction and feedback, SkillClaw significantly improves the performance of Qwen3-Max in real-world agent scenarios.

## Key Ideas

1. **Collective skill evolution** — Skills evolve from multi-user interactions, not just single-user refinement. Cross-user and over-time signals are the primary improvement driver.
2. **Autonomous evolver** — An agent that identifies recurring behavioral patterns in trajectories and translates them into skill updates (refine existing or extend new).
3. **Shared repository + sync** — Skills maintained in shared repo, synchronized across users. Improvements in one context propagate system-wide.
4. **Zero additional user effort** — Users don't need to explicitly provide feedback; trajectory aggregation is passive.
5. **Broad compatibility** — Supports OpenClaw and Hermes agent frameworks. Python 88%, JavaScript 9.4%.
6. **Claude Code integration** — README mentions Hermes support; topics include `hermes`, `openclaw`, `self-evolving`, `skill-evolution`, `continual-learning`.

## Context Elements

- **Skill repository** (shared, synchronized) — collective knowledge base
- **Trajectory aggregation** — cross-user + over-time interaction logging
- **Autonomous evolver** — pattern recognition → skill update pipeline
- **Skill reload mechanism** — poll loop (30s default, immediate first pull) or webhook for syncing evolved skills
- **Config store** — skill backend configuration for multiple agent frameworks

## Composition Notes

SkillClaw is a meta-skill framework: it doesn't provide individual skills but rather the infrastructure for skills to evolve collectively. The skill bundle here is the evolution system itself: trajectory collector + evolver + shared repository + sync mechanism. This extends the skill lifecycle from static deployment to continuous multi-user evolution.

## Relation to Existing Wiki

- Extends [[memento-skills-agent-designing-agent]] (which mentioned SkillClaw for collective evolution)
- Complements [[coevoskills-self-evolving-skills]] (co-evolutionary verification)
- Related to [[skill1-unified-skill-evolution-rl]] (unified RL-based evolution)
- Related to [[exif-automated-skill-discovery]] (self-play skill discovery)
