# ASPIRE: Agentic Skill Programming through Iterative Robot Exploration

**Source:** arXiv:2607.00272 (https://arxiv.org/abs/2607.00272)
**Date:** Submitted 30 Jun 2026
**Authors:** Runyu Lu, Yubo Wu, Ethan Kou, Letian Fu, Wenli Xiao, Ajay Mandlekar, Yinzhen Xu, Guanya Shi, Ken Goldberg, Ang Chen, Mosharaf Chowdhury, Yuke Zhu, Linxi "Jim" Fan, Guanzhi Wang
**Institution:** NVIDIA GEAR Lab, UC Berkeley, UT Austin
**Project:** https://research.nvidia.com/labs/gear/aspire/
**Signal Rating:** 9/10

## Summary

ASPIRE (Agentic Skill Programming through Iterative Robot Exploration) is a continual learning system for robotics that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience into a reusable skill library. Skills persist across tasks, simulation and real-world settings, and embodiments.

## Three Components

1. **Closed-loop robot execution engine** — exposes fine-grained multimodal traces, enabling autonomous failure diagnosis, repair synthesis, and validation.
2. **Continually expanding skill library** — distills validated fixes into reusable, transferable knowledge.
3. **Evolutionary search** — generates diverse task sequences and control programs to explore beyond single-trajectory refinement.

## Key Results

- LIBERO-Pro manipulation under perturbation: +77% over prior methods
- Robosuite bimanual handover: +72%
- BEHAVIOR-1K long-horizon household tasks: +32%
- LIBERO-Pro Long (zero-shot generalization): 31% success vs 4% for prior methods (despite their test-time reasoning and retries)
- Sim-to-real transfer evidence: simulation-discovered skills reduce real-robot programming effort across embodiments and robot APIs

## Skill Bundle Context

- Skills are robot control programs (code-as-policy) with validated repair knowledge
- Skill library = context element providing persistent, transferable knowledge
- Evolutionary search = governance/discovery mechanism for skill diversity
- Cross-embodiment transfer = skill portability evidence
- Closed-loop execution engine = runtime validation/verification mechanism

## Relevance to Skill Bundles

ASPIRE demonstrates skill discovery and compounding in the robotics domain. The code-as-policy paradigm means skills are executable programs with formal structure. The evolutionary search for diverse repair hypotheses is a novel skill generation pattern. The cross-embodiment and sim-to-real transfer evidence supports the skill transfer thesis from a new domain (robotics).
