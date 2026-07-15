# AgentBound: Securing Execution Boundaries of AI Agents

**Source:** arXiv:2510.21236 (cs.CR, cs.AI, cs.SE)
**Authors:** Christoph Bühler, Matteo Biagiola, Luca Di Grazia, Guido Salvaneschi
**Submitted:** Oct 24, 2025 (v1); revised Apr 24, 2026 (v3)
**Venue:** ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (FSE 2026)
**GitHub:** https://github.com/dortort/agent-bound
**Signal Rating:** 9/10

## Abstract

LLMs have evolved into AI agents that interact with external tools and environments. The Model Context Protocol (MCP) has become the de facto standard for connecting agents with such resources, but security has lagged behind: thousands of MCP servers execute with unrestricted access to host systems, creating a broad attack surface.

**AgentBound** is the first access control framework for MCP servers. It combines:

1. **Declarative policy mechanism** — Inspired by the Android permission model.
2. **Policy enforcement engine** — Contains malicious behavior without requiring MCP server modifications.

## Key Results

- **Dataset:** 296 most popular MCP servers
- **Automated policy generation:** 80.9% accuracy from source code analysis
- **Threat blocking:** Blocks the majority of security threats in malicious MCP servers
- **Performance:** Negligible overhead from policy enforcement engine

## Key Ideas

1. **Android permission model for MCP** — Adapts the proven Android permission system (declarative permissions, runtime grants, least privilege) to MCP servers.
2. **Source code → policy automation** — Policies can be generated automatically from MCP server source code with 80.9% accuracy.
3. **No server modifications needed** — The enforcement engine wraps MCP servers without requiring changes to the servers themselves.
4. **MCP as de facto standard** — Acknowledges MCP as the standard protocol for agent-resource connection, making MCP security critical infrastructure.
5. **Software engineering venue** — Published at FSE 2026, bringing SE rigor (access control, policy enforcement) to agent security.

## Context Elements

- **Declarative access control policies** — Permission declarations (Android-inspired)
- **Policy enforcement engine** — Runtime sandboxing/containment
- **Source code analysis** — Automated policy generation from MCP server code
- **MCP server dataset** — 296 most popular servers (benchmark)

## Relation to Existing Wiki

- Complements [[skillguard-permission-framework]] (skill-level permissions) with MCP-server-level permissions
- Related to [[skillfortify-formal-verification-supply-chain]] (formal supply chain security)
- Extends security beyond skills to the MCP protocol layer
- Different layer from [[skillspector-nvidia-security-scanner]] (static scanning vs. runtime access control)
- Addresses the infrastructure layer that [[agent-skills-spec]] and MCP define
