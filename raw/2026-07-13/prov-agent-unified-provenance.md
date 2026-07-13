# PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows

**Source:** arXiv:2508.02866 (04 Aug 2025)
**Authors:** Renan Souza, Amal Gueroudji, Stephen DeWitt, Daniel Rosendo, Tirthankar Ghosal, Robert Ross, Prasanna Balaprakash, Rafael Ferreira da Silva
**Institutions:** Oak Ridge National Lab, Argonne National Lab
**License:** CC BY 4.0
**Signal Rating:** 8/10

## Abstract

Foundation models (LLMs) are increasingly used as core components of AI agents in complex, large-scale workflows across federated and heterogeneous environments. In agentic workflows, autonomous agents plan tasks, interact with humans and peers, and shape scientific outcomes. This makes transparency, traceability, reproducibility, and reliability essential. AI-based agents can hallucinate or reason incorrectly, and their decisions may propagate errors through the workflow. PROV-AGENT is a provenance model that extends W3C PROV and leverages the Model Context Protocol (MCP) to integrate agent interactions into end-to-end workflow provenance.

## Three Contributions

1. A provenance model tailored for agentic workflows (extends W3C PROV + MCP concepts)
2. A near real-time, open-source system for capturing agentic provenance during execution
3. A cross-facility evaluation spanning edge, cloud, and HPC environments demonstrating support for critical provenance queries and agent reliability analysis

## Problem

Traditional provenance approaches are not designed to capture the intrinsic dynamics of modern AI agents. Provenance data must capture not only data flow and task execution history but also:
- Reasoning processes
- Model invocations
- Contextual information that drives agent decisions

This enables rigorous root cause analysis when unexpected behavior occurs.

## Key Provenance Queries Supported

1. What specific input data led an agent to make a particular decision?
2. How did an agent's decision influence the control or data flow within the workflow?
3. Which downstream outputs were affected by a specific agent interaction?
4. Where did erroneous data originate, and through which agents' decisions did it propagate?

## Context Elements

- **W3C PROV extension:** Standard-based provenance model
- **MCP integration:** Model Context Protocol concepts for agent-tool interactions
- **Agent-centric metadata:** Prompts, responses, and decisions as first-class provenance
- **Cross-facility evaluation:** Edge devices, cloud services, HPC systems
- **Near real-time capture:** Open-source provenance system
- **Provenance graph:** Unified graph treating AI agent actions as first-class components

## Related Work

- Provenance for scientific workflows (ProvOne, W3C PROV)
- FAIR4ML Metadata Schema (w3id.org/fair4ml)
- Data provenance for multi-agent models
- Workflow provenance in scientific ML lifecycle
