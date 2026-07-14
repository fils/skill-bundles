# NVIDIA-Verified Agent Skills: Capability Governance for AI Agents

**Source:** NVIDIA Developer Blog (https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/)
**Date:** May 19, 2026
**Authors:** Moshe Abramovitch, Michael Boone, Sayali Kandarkar, Daniel Major, Nir Paz (NVIDIA)
**GitHub:** https://github.com/NVIDIA/skills
**Signal Rating:** 8/10

## Summary

NVIDIA-verified agent skills are portable instruction sets that help developers understand, trust, and safely deploy AI agent capabilities by providing transparency, provenance, security scanning, and cryptographic signing. They build on the agentskills.io open skills specification, so the same SKILL.md works across Claude Code, Codex, and Cursor.

## Verification Flow

1. **Daily catalog updates** — synced from NVIDIA product teams
2. **Automated + human review** — scanning for software and agent-native risks
3. **Security scanning** — using SkillSpector for risk detection
4. **Cryptographic signing** — detached skill.oms.sig signature verified post-download
5. **Documentation** — machine-readable skill cards detailing ownership, dependencies, limitations, and verification status

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

## Skill Bundle Context

- Skill card = formal metadata document (context element for trust/governance)
- Cryptographic signing = provenance/authenticity verification
- SkillSpector = security scanning tool (automated risk detection)
- Daily catalog sync = governance lifecycle for skill maintenance
- Cross-platform SKILL.md = portability across agent harnesses
- Verification status = trust metadata for skill bundles

## Relevance to Skill Bundles

NVIDIA-verified skills represent the industry productionization of skill bundle governance. The skill card is a formal context element that centralizes trust metadata. The cryptographic signing extends supply chain provenance from code packages to agent skills. This is the commercial/enterprise counterpart to SkillGuard's permission framework and SkillFortify's formal verification — focusing on the publication/distribution layer rather than runtime enforcement or static analysis.
