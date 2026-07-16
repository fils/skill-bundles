---
type: Skill Bundle Example
title: Claude Skills Ecosystem — 1,116 Skills from 500+ Repos
description: A comprehensive survey and mapping of 1,116 unique Claude Code Skills discovered across 500+ repositories.
resource: https://growthexe.substack.com/p/i-found-1116-claude-code-skills-from
timestamp: '2026-05-24T00:00:00Z'
date: '2026-05-24'
---

# Claude Skills Ecosystem — 1,116 Skills from 500+ Repos

**Source:** https://growthexe.substack.com/p/i-found-1116-claude-code-skills-from
**Date Added:** 2026-05-24 (Iteration 8)
**Author:** GrowthExe (Substack)
**Bundle Type:** Mega Collection + Security Taxonomy
**Confidence:** 8/10

## Name & Origin

A comprehensive survey and mapping of 1,116 unique Claude Code Skills discovered across 500+ repositories. The most thorough inventory of the Claude skills ecosystem to date.

## Skills Included (Major Collections)

- **obra/superpowers** (166k stars): TDD, systematic debugging, verification-before-completion, brainstorming, planning, dispatching parallel agents
- **alirezarezvani/claude-skills** (235 skills): Engineering (37), Marketing (44), C-Level Advisory (34), Regulatory (14)
- **wshobson/agents** (150 skills): General-purpose agents
- **Microsoft** (133 skills): .NET (25), Python (40+), TypeScript (22), Azure services
- **Anthropic-Cybersecurity-Skills** (754 skills): MITRE/NIST framework mapping
- **Trail of Bits** (29 skills): Static/variant analysis, Semgrep rule creation
- **Unity-Skills** (543 skills): Game development
- **Sentry** (30 SDK skills): Error tracking

## Context Elements

- **YAML Configuration:** SKILL.md frontmatter standard across all skills
- **MCP Dependencies:** Multiple skills declare MCP tool integrations (Composio plugin for 78+ SaaS apps)
- **Security Taxonomy:** 754 cybersecurity skills mapped to MITRE ATT&CK and NIST frameworks — this is a **taxonomy + rules** pattern
- **Skill Specification:** agentskills.io compatible across the ecosystem

## How Context Elements Support Skills

The **Anthropic-Cybersecurity-Skills** collection (754 skills mapped to MITRE/NIST) represents a formal taxonomy driving skill organization. This is the most significant taxonomy-based bundle pattern found outside of formal ontology/mapping work. The MITRE framework provides:
1. A hierarchical taxonomy of attack techniques
2. Standardized naming and categorization
3. Cross-referencing between skills and framework nodes

## Composition Notes

The three-layer architecture (MCP connection → Tools actions → Skills workflow/guardrails) observed across this ecosystem reinforces the pattern that skills are the **workflow layer** that sits above MCP connections and individual tools.

The Composio plugin pattern — a single MCP connection providing access to 78+ SaaS apps — demonstrates a **dependency consolidation** pattern: instead of declaring individual MCP dependencies per skill, a central plugin provides the tool layer.

## Reproducibility

Medium — this is a survey document, not a single tool. Individual skills are reproducible per their own docs.

## Key Insight

The 754 cybersecurity skills mapped to MITRE/NIST frameworks represent a formally **taxonomized skill collection** — the largest taxonomy-driven bundle found in this research. This provides a counterpoint to ontology-based bundles: instead of formal ontologies (OWL, RDF), it uses established security frameworks as the organizing structure.
