# Paper: The (R)evolution of Scientific Workflows in the Agentic AI Era — Towards Autonomous Science

> **Source:** ACM SC '25 Workshops — https://dl.acm.org/doi/full/10.1145/3731599.3767580
> **Added:** 2026-05-25 (manual seed for initial research)
> **Raw:** [[../raw/2026-05-25/autonomous-science-workflows-acm.md]]

## Summary

This paper presents a framework for the evolution of scientific workflows from traditional orchestrated pipelines to fully autonomous, distributed scientific laboratories. The authors propose that the transition is an **evolution (not revolution)** using a **State Machine Abstraction** where both traditional workflows and AI agents are modeled as state machines M = (S, Σ, δ, s₀, F). The evolution occurs along two dimensions:

### Intelligence Dimension (sophistication of transition function δ):
- **Static** → **Adaptive** → **Learning** → **Optimizing** → **Intelligent** (meta-optimization)

### Composition Dimension (coordination patterns):
- **Single** → **Pipeline** → **Hierarchical** → **Mesh** → **Swarm** (emergent behavior)

### Key Architectural Layers:
- Human Interface Layer (Science IDEs)
- Intelligence Service Layer (Hypothesis, Design, Analysis, Knowledge agents)
- Workflow Orchestration Layer (with Facility Agents)
- Resource & Data Management (Knowledge Graphs, Data Fabrics)
- Infrastructure Abstraction (TPUs, robotics, quantum)

## Relevance to Skill Bundles

This paper provides a **formal framework for skill composition**:
- The composition dimension (Single→Pipeline→Hierarchical→Mesh→Swarm) maps directly to **skill bundle orchestration patterns**
- The intelligence dimension provides a **taxonomy for skill sophistication levels**
- Knowledge Graphs & Data Fabrics align with **SSSOM mappings** and semantic layers
- The state machine abstraction could formalize **skill execution and composition**

## Strategic Bets for the Community:
1. AI Research — invest in scientific foundation models
2. Workflow Research — move beyond DAGs to stateful AI services
3. Workforce Investment — blend domain science with AI fluency

## Actionable Insights:
- Build on top of existing WMS (Pegasus, Parsl, FireWorks) with intelligence-aware components
- Adopt standards: AMQP 1.0 for event-driven workflows, Globus Auth for inter-agent security
- Focus on meta-optimization — the goal is Intelligent Swarm
- Join AISLE (Autonomous Interconnected Science Lab Ecosystem)

## Tags
#autonomous-science #workflow-evolution #state-machine #agentic-ai #swarm-intelligence #skill-composition #knowledge-graphs
