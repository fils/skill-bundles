# EXIF: Automated Skill Discovery for Language Agents through Exploration and Iterative Feedback

**Source:** arXiv:2506.04287 (https://arxiv.org/abs/2506.04287)
**Date:** Submitted 4 Jun 2025 (v2: 20 Jun 2025)
**Authors:** Yongjin Yang, Sinjae Kang, Juyong Lee, Dongjun Lee, Se-Young Yun, Kimin Lee
**Citations:** 11
**Signal Rating:** 7/10

## Summary

EXIF (EXploration and Iterative Feedback) is an automatic skill discovery framework for LLM-powered agents, designed to improve the feasibility of generated target behaviors while accounting for the agents' capabilities. It adopts an exploration-first strategy using a dual-agent (Alice-Bob) framework.

## Alice-Bob Framework

- **Alice (exploration agent):** interacts with the environment to retrospectively generate a feasible, environment-grounded skill dataset
- **Bob (target agent):** trained using Alice's generated skill dataset
- **Iterative feedback loop:** Alice evaluates Bob's performance to identify areas for improvement, then guides Alice's next round of exploration

## Key Insight

Setting Alice to the same model as Bob also notably improves performance, demonstrating EXIF's potential for building a self-evolving system. This is the self-play pattern applied to skill discovery.

## Results

- Webshop and Crafter benchmarks
- Substantial performance improvements without human intervention
- Effectively discovers meaningful skills and iteratively expands agent capabilities

## Skill Bundle Context

- Environment-grounded skill dataset = skills generated from actual environment interaction
- Alice-Bob dual-agent = skill generation + skill consumption separation
- Iterative feedback loop = skill refinement lifecycle
- Self-play (Alice=Bob) = self-evolving skill system

## Relevance to Skill Bundles

EXIF is a precursor to the 2026 skill discovery wave (ASPIRE, Memento-Skills, Skill1). The Alice-Bob dual-agent pattern maps to the "generator-executor decoupling" pattern from SkillGenBench. The self-play insight (Alice=Bob) foreshadows self-evolving skill systems. EXIF's retrospective skill generation (after environment interaction) is the "exploration-first" strategy that ASPIRE's evolutionary search and Memento-Skills' Read-Write cycle build upon.
