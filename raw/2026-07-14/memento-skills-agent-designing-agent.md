# Memento-Skills: Let Agents Design Agents

**Source:** arXiv:2603.18743 (https://arxiv.org/abs/2603.18743)
**Date:** Submitted 19 Mar 2026
**Authors:** Huichi Zhou, Siyuan Guo, Anjie Liu, Zhongwei Yu, Ziqin Gong, Bowen Zhao, Zhixun Chen, Menglong Zhang, Yihang Chen, Jinsong Li, Runyu Yang, Qiangbin Liu, Xinlei Yu, Jianmin Zhou, Na Wang, Chunyang Sun, Jun Wang
**Citations:** 27
**Code:** https://github.com/Memento-Teams/Memento-Skills
**Signal Rating:** 9/10

## Summary

Memento-Skills is a generalist, continually-learnable LLM agent system that functions as an agent-designing agent: it autonomously constructs, adapts, and improves task-specific agents through experience. Built on a memory-based reinforcement learning framework with stateful prompts, where reusable skills (stored as structured markdown files) serve as persistent, evolving memory.

## Key Mechanism: Read-Write Reflective Learning

- **Read phase:** A behaviour-trainable skill router selects the most relevant skill conditioned on the current stateful prompt.
- **Write phase:** The agent updates and expands its skill library based on new experience.
- This enables continual learning without updating LLM parameters — all adaptation is realised through the evolution of externalised skills and prompts.

## Results

- General AI Assistants benchmark: +26.2% relative improvement in overall accuracy
- Humanity's Last Exam: +116.2% relative improvement
- 80% task success vs. PT (prior approaches relying on human-designed agents)

## Skill Bundle Context

- Skills stored as structured markdown files = persistent evolving memory
- Skill router = selection/governance mechanism for skill dispatch
- Read-Write Reflective Learning = skill lifecycle (creation → routing → refinement)
- Stateful prompts = context element that carries forward knowledge
- Continual learning without LLM parameter updates = skills as the adaptation substrate
- Agent-designing agent = meta-level skill composition (skills create skills)

## Related: SkillClaw

The paper mentions SkillClaw framework for collective skill evolution (multi-agent skill sharing).

## Relevance to Skill Bundles

Memento-Skills is a canonical example of skills as the primary adaptation mechanism. Skills are structured markdown files (matching the agentskills.io SKILL.md format). The Read-Write Reflective Learning cycle is a complete skill lifecycle: discovery (read) → application → refinement (write). The agent-designing-agent pattern is meta-level skill composition. Skills encode both behaviour and context, enabling knowledge transfer across interactions.
