---
type: Skill Bundle Example
title: 'NVIDIA-Verified Agent Skills: Capability Governance for AI Agents'
description: NVIDIA-verified agent skills are portable instruction sets that help developers understand, trust, and safely deploy AI agent capabilities by providing **transparency, provenance, security scanning, and cryptographic...
resource: https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/
timestamp: '2026-07-14T00:00:00Z'
date: 2026-07-14
sources:
- https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/
- https://github.com/NVIDIA/skills
skills_included:
- SkillSpector security scanning
- Cryptographic skill signing
- Skill cards (trust metadata)
- Daily catalog sync
- Verification flow (automated + human review)
context_elements:
- Skill cards (ownership, dependencies, limitations, verification status)
- Cryptographic signing (skill.oms.sig)
- Security scanning (SkillSpector)
- agentskills.io spec compliance
- Cross-platform portability (Claude Code, Codex, Cursor)
composition: 'Verification pipeline: daily catalog sync → SkillSpector scanning → automated + human review → cryptographic signing → skill card documentation. Same SKILL.md works across agent harnesses.'
reproducibility: 'GitHub: NVIDIA/skills. Built on agentskills.io open specification. Production system with daily updates.'
rating: 8
---

# NVIDIA-Verified Agent Skills: Capability Governance for AI Agents

**Origin:** NVIDIA (Developer Blog, May 19, 2026)
**GitHub:** https://github.com/NVIDIA/skills

## Overview

NVIDIA-verified agent skills are portable instruction sets that help developers understand, trust, and safely deploy AI agent capabilities by providing **transparency, provenance, security scanning, and cryptographic signing**. They build on the agentskills.io open skills specification, so the same SKILL.md works across Claude Code, Codex, and Cursor.

## Verification Flow

1. **Daily catalog updates** — synced from NVIDIA product teams
2. **Automated + human review** — scanning for software and agent-native risks
3. **Security scanning** — SkillSpector for risk detection
4. **Cryptographic signing** — detached skill.oms.sig signature, verifiable post-download
5. **Documentation** — machine-readable skill cards

## Skill Cards

Skill cards centralize trust metadata:
- Ownership information
- Dependencies
- Limitations
- Verification status
- Cryptographic signatures for authenticity and integrity

## Evaluation Layer (Planned)

Next layer will add standardized quality metrics:
- Trigger accuracy
- Task completion rate
- Token efficiency
Measured against a common harness.

## Context Elements

- **Skill cards** — formal metadata document (trust/governance context element)
- **Cryptographic signing** — provenance/authenticity verification
- **SkillSpector** — security scanning tool (automated risk detection)
- **Daily catalog sync** — governance lifecycle for skill maintenance
- **Cross-platform SKILL.md** — portability across agent harnesses
- **Verification status** — trust metadata for skill bundles

## Relation to Skill Bundle Patterns

NVIDIA-verified skills represent the **industry productionization** of skill bundle governance:
- Complements [skillguard permission framework](skillguard-permission-framework.md) (runtime) and [skillfortify formal verification supply chain](skillfortify-formal-verification-supply-chain.md) (static analysis) — NVIDIA focuses on publication/distribution layer
- Skill cards extend [prov agent unified provenance](prov-agent-unified-provenance.md) (provenance) to commercial skill distribution
- Cryptographic signing parallels [supply chain agentic factory in toto](supply-chain-agentic-factory-in-toto.md) (SLSA/in-toto) for skills
- Built on [agent skills spec](agent-skills-spec.md) — same SKILL.md across harnesses
- SkillSpector = automated security scanning (complements [skillsieve malicious skill detection](skillsieve-malicious-skill-detection.md))

## Key Insight

Production skill governance requires a multi-layer approach: publication (catalog + sync), security (scanning), authenticity (cryptographic signing), and documentation (skill cards). NVIDIA's verification flow is the enterprise/industry counterpart to academic frameworks — focusing on the distribution layer rather than runtime enforcement or static analysis. Cross-platform SKILL.md compatibility ensures skills work reliably across Claude Code, Codex, and Cursor.

