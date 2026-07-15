---
title: "AgentBound: Declarative Access Control for MCP Servers"
date: 2026-07-15
sources: ["arXiv:2510.21236", "https://github.com/dortort/agent-bound"]
skills_included: ["Declarative policy generation", "Policy enforcement engine", "Source code analysis for policy derivation", "MCP server sandboxing"]
context_elements: ["Declarative access control (Android permission model inspired)", "Policy enforcement engine (no server modifications)", "Automated policy generation from source code (80.9% accuracy)", "MCP server dataset (296 most popular)", "ACM FSE 2026 publication"]
composition: "Access control framework: source code analysis → automated policy generation (80.9%) → declarative policy enforcement engine wraps MCP servers without modification → blocks malicious behavior at negligible overhead."
reproducibility: "Open-sourced on GitHub (dortort/agent-bound). 296 most popular MCP servers evaluated. Published at ACM FSE 2026."
rating: 9
---

# AgentBound: Declarative Access Control for MCP Servers

**Origin:** USI Lugano, Switzerland (arXiv:2510.21236)
**Venue:** ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (FSE 2026)
**GitHub:** https://github.com/dortort/agent-bound

## Overview

AgentBound is the first access control framework for **MCP servers**. As the Model Context Protocol has become the de facto standard for connecting AI agents with external resources, thousands of MCP servers execute with unrestricted access to host systems, creating a broad attack surface. AgentBound addresses this by adapting the proven Android permission model to MCP server security.

## Two-Component Architecture

1. **Declarative policy mechanism** — Inspired by the Android permission model:
   - MCP servers declare required permissions (file access, network, process execution, etc.)
   - Permissions are granted at runtime (user-mediated or policy-mediated)
   - Least-privilege by design

2. **Policy enforcement engine** — Contains malicious behavior without requiring MCP server modifications:
   - Wraps MCP servers in a policy enforcement layer
   - Blocks unauthorized resource access at runtime
   - Negligible performance overhead

## Key Results

| Metric | Result |
|--------|--------|
| MCP servers analyzed | 296 (most popular) |
| Automated policy generation accuracy | 80.9% from source code |
| Threat blocking | Majority of security threats blocked |
| Performance overhead | Negligible |
| Server modifications required | None |

## Key Innovations

- **Android permission model for MCP** — Adapts the proven, widely-deployed Android permission system to MCP servers
- **Automated policy generation** — Source code → declarative policies with 80.9% accuracy, reducing manual effort
- **Non-invasive enforcement** — Wraps MCP servers without requiring changes to the servers themselves
- **Software engineering rigor** — Published at FSE 2026, bringing SE access control discipline to agent infrastructure

## Context Elements

- **Declarative access control policies** — Permission declarations (Android-inspired formal model)
- **Policy enforcement engine** — Runtime sandboxing/containment layer
- **Source code analysis** — Automated policy generation from MCP server code
- **MCP server dataset** — 296 most popular servers (benchmark for policy generation)

## Relation to Skill Bundle Patterns

AgentBound extends skill bundle security to the **MCP protocol layer** — the infrastructure that connects skills to resources.

- Complements [[skillguard-permission-framework]] (skill-level permissions vs. MCP-server-level permissions)
- Related to [[skillfortify-formal-verification-supply-chain]] (formal supply chain — AgentBound is runtime infrastructure)
- Different layer from [[skillspector-nvidia-security-scanner]] (static scanning vs. runtime access control)
- Addresses the infrastructure layer defined by [[agent-skills-spec]] and MCP
- Connects to [[externalization-llm-agents-unified-review]] (harness engineering = governed execution)

## Key Insight

MCP servers are the connective tissue between agents and resources, yet thousands run with unrestricted access. AgentBound demonstrates that the Android permission model — proven across billions of devices — can be adapted to MCP server security with automated policy generation and non-invasive enforcement. This brings software engineering access control discipline to agent infrastructure.

[[backlinks]]
