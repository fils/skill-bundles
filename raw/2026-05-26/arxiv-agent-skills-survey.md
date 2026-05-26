# Agent Skills for LLMs: Architecture, Acquisition, Security — Survey (arXiv:2602.12430)

**Source:** https://arxiv.org/html/2602.12430v3
**Authors:** Renjun Xu, Yang Yan (Zhejiang University)
**License:** CC BY-NC-ND 4.0
**Repo:** https://github.com/scienceaix/agentskills
**Date:** Feb 17, 2026

## Key Contributions
First comprehensive survey of Agent Skills, organized along 4 axes:
1. **Architectural foundations** — SKILL.md, progressive disclosure, MCP integration
2. **Skill acquisition** — RL, autonomous discovery, compositional synthesis
3. **Deployment at scale** — Computer-use agent stack, benchmarks
4. **Security** — 26.1% of community skills contain vulnerabilities

## Timeline
- Oct 2025: Anthropic launches Agent Skills across Claude
- Dec 2025: Released as open standard (agentskills.io); 62k+ GitHub stars
- Dec 2025: MCP donated to Linux Foundation's Agentic AI Foundation

## Skill Engineering Paradigm Shift
| Paradigm | Period | Characteristic |
|----------|--------|---------------|
| Prompt Engineering | 2022-2023 | Ephemeral, non-modular, hard to version |
| Tool Use / Function Calling | 2023-2024 | Atomic functions, no task reshaping |
| Skill Engineering | 2025-present | Bundled instructions, workflow, scripts |

## Skills vs MCP
| Dimension | Agent Skills | MCP |
|-----------|--------------|-----|
| Primary role | Procedural knowledge | Tool connectivity |
| Unit | Directory with SKILL.md | Server with endpoints |
| Loaded by | Agent on trigger | Client on config |
| Modifies | Context + permissions | Available tools/data |
| Persistence | Filesystem-based | Session-based |

## Key Finding: Skill modifications are contextual
Skills modify agent **preparation** not output — distinct from function calls. A skill "resembles putting together an onboarding guide for a new hire."

## Security Finding
26.1% of community-contributed skills contain vulnerabilities. Proposes **Skill Trust and Lifecycle Governance Framework** with four-tier, gate-based permission model.

## Progressive Disclosure (3 levels)
| Level | Content | Token Cost |
|-------|---------|-----------|
| 1 | Metadata (name, description) | ~50 tokens |
| 2 | Full instructions/workflow | ~2000 tokens |
| 3 | Scripts, reference docs | Up to 15k tokens |
