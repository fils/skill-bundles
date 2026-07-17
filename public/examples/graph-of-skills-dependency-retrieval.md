---
type: Skill Bundle Example
title: 'Graph of Skills (GoS): Dependency-Aware Structural Retrieval'
description: Graph of Skills (GoS) (Li et al., 2026) presents an **inference-time structural retrieval layer** for large skill libraries.
resource: https://arxiv.org/abs/2604.05333
---

# Graph of Skills (GoS): Dependency-Aware Structural Retrieval

## Overview

[Graph of Skills (GoS)](https://arxiv.org/abs/2604.05333) (Li et al., 2026) presents an **inference-time structural retrieval layer** for large skill libraries. Instead of retrieving skills independently by semantic similarity, GoS builds a **dependency graph** offline from a library of SKILL.md documents, then retrieves a small, ranked set of relevant skills at task time using reverse-weighted PageRank on the skill subgraph.

**Context Elements:** Skill dependency graph (DAG) · PageRank-based retrieval · SKILL.md parsing for dependency extraction · Subgraph ranking algorithm

## Core Method

### Offline Graph Construction
1. Parse SKILL.md files from the skill library
2. Extract dependencies (skills reference/call other skills via `allowed-tools`, script imports, or explicit mentions)
3. Build a directed acyclic graph (DAG) where nodes are skills and edges represent dependencies

### Inference-Time Retrieval
1. Semantic retrieval: Find top-k skills matching the task query
2. Graph expansion: Retrieve prerequisite skills via the dependency graph
3. Re-ranking: Apply reverse-weighted PageRank on the skill subgraph
4. Return ranked skill bundle for the agent to load

### Key Insight
Skills are **not independent** — loading a skill without its dependencies leads to failure. GoS ensures that when an agent activates a high-level skill (e.g., "deploy web app"), it also loads prerequisite skills (e.g., "build frontend", "configure CI/CD"). This is the first formal **composition model** for agent skill bundles.

## Context Element Coverage

**Type: Dependency Graph (DAG)** — The offline-constructed skill dependency graph serves as a formal **ontology of skill composition**. Each node (skill) has edges (dependencies) to other skills.

**Type: Retrieval Algorithm** — Reverse-weighted PageRank on the skill subgraph provides a **scoring function** for bundle selection. The algorithm weights skills by relevance and dependency depth.

**Type: SKILL.md Parser** — The system parses SKILL.md YAML frontmatter (especially `allowed-tools`) and script imports to automatically extract dependency edges.

## Reproducibility
High — GitHub repo at davidliuk/graph-of-skills with code for graph construction, retrieval, and PageRank ranking.

## Impact for Skill Bundles
GoS formalizes what we've seen informally: skills form dependency graphs that need to be resolved before execution. The [dspy agent skills bundle](dspy-agent-skills-bundle.md)'s `dspy-advanced-workflow` orchestrator skill and [superpowers engineering discipline skills](superpowers-engineering-discipline-skills.md)'s methodology cycle are both **dependency-ordered** — GoS provides the theoretical foundation for these patterns.

## v3 Update (2026-07-11)

GoS v3 (27 May 2026) includes concrete SkillsBench benchmark results:
- **Peak reward increase: +25.55%** on SkillsBench using GPT-5.2 Codex
- **Token savings: -56.72%** total tokens vs vanilla full skill-loading baseline
- Consistent improvements across Claude Sonnet 4.5, MiniMax M2.7, GPT-5.2 Codex
- Validated on skill libraries from 200 to 2,000 skills

Method refined: hybrid semantic-lexical seeding → reverse-aware Personalized PageRank → context-budgeted hydration.

This provides **concrete benchmark evidence** that dependency-aware skill bundle retrieval outperforms flat retrieval — validating the skill bundle composition thesis with both quality AND efficiency gains.

## Confidence
9/10 — Published on arXiv (2604.05333v3), code on GitHub, SkillsBench-validated.

## Sources
- https://arxiv.org/abs/2604.05333
- https://github.com/davidliuk/graph-of-skills
- https://skillsbench.ai/ (SkillsBench v1.1 leaderboard)
