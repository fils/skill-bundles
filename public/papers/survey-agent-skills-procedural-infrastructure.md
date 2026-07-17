---
type: Paper
title: 'A Survey of Agent Skills: Toward Procedural Infrastructure for LLM Agents'
description: The most comprehensive **six-layer taxonomy** of agent skills, covering ontology, representation/packaging, lifecycle, runtime integration, governance, and applications.
resource: https://www.preprints.org/manuscript/202605.1276
timestamp: '2026-07-11T00:00:00Z'
date: '2026-07-11'
---

# A Survey of Agent Skills: Toward Procedural Infrastructure for LLM Agents

**Source:** https://www.preprints.org/manuscript/202605.1276 (19 May 2026)
**GitHub:** https://github.com/DataArcTech/Awesome-Agent-Skill-Papers
**Date Added:** 2026-07-11 (Iteration 36)
**Authors:** Cehao Yang, Xiaojun Wu, Honghao Liu, Xueyuan Lin, et al. (13 authors)
**License:** CC BY 4.0
**Bundle Type:** Academic Survey · Six-Layer Taxonomy · Paper Catalog
**Confidence:** 9/10

## Name & Origin

The most comprehensive **six-layer taxonomy** of agent skills, covering ontology, representation/packaging, lifecycle, runtime integration, governance, and applications. Accompanied by a curated GitHub catalog of agent skill papers.

## Skills Included (as taxonomy layers)

1. **Ontology** — what a skill is; relationship to memory, cognition, compression, reusable procedural knowledge
2. **Representation & Packaging** — natural-language guidance, executable code, decision graphs, filesystem packages (SKILL.md), structured records
3. **Lifecycle** — acquisition, storage, retrieval, usage, maintenance, selective internalization into model behavior
4. **Runtime Integration** — terminal interfaces, tool interfaces, multi-agent systems, agent harnesses (Claude Code, Codex, OpenClaw, Hermes Agent)
5. **Governance** — security risks, trusted deployment, marketplace governance
6. **Applications** — robotics, games, web agents, GUI/mobile/OS agents, software engineering

## Context Elements

- **Six-layer taxonomy** — the most comprehensive structural framework for skill bundle analysis
- **Marketplace scale data** (as of April 2, 2026):
  - SkillsMP: 425,000+ skills
  - LobeHub Skills: 169,739 skills
  - agentskill.sh: 110,000+ skills
  - skills.sh: ~87,000 unique skills
  - ClawHub: 20,000+ skills
- **Paradigm arc:** prompt engineering → context engineering → **harness engineering**
- **Selective internalization** — skills can be internalized into model weights (beyond runtime loading)
- **Paper catalog** — Awesome-Agent-Skill-Papers GitHub repo with curated paper list

## How Context Elements Support Skills

The six-layer taxonomy maps directly to our wiki structure:

| Survey Layer | Wiki Mapping |
|-------------|-------------|
| Ontology | [skill bundle patterns](../concepts/skill-bundle-patterns.md) |
| Representation/Packaging | [agent skills spec](../examples/agent-skills-spec.md), SKILL.md format |
| Lifecycle | [skill bundle patterns](../concepts/skill-bundle-patterns.md) |
| Runtime Integration | [agensi marketplace landscape](../tools/agensi-marketplace-landscape.md) |
| Governance | [skill security governance](../concepts/skill-security-governance.md) |
| Applications | Domain-specific examples (see wiki/examples/) |

The marketplace data quantifies the ecosystem at **800K+ total skills** across major marketplaces — a scale that makes governance and validation critical.

## Composition Notes

This survey is complementary to [arxiv agent skills survey](../examples/arxiv-agent-skills-survey.md) (4-axis: architecture, acquisition, security, deployment) and [sok agentic skills beyond tool use](sok-agentic-skills-beyond-tool-use.md) (7 patterns + lifecycle). Together, these three surveys provide overlapping but non-redundant coverage:
- **This survey:** 6-layer taxonomy (most comprehensive structure)
- **arXiv survey:** 4-axis (architecture + security focus)
- **SoK:** 7 patterns + formal definition (design patterns focus)

## Reproducibility

High — preprint on Preprints.org (CC BY 4.0), GitHub repo with paper list and taxonomy image.

## Bundle Links

- [arxiv agent skills survey](../examples/arxiv-agent-skills-survey.md) — complementary 4-axis survey
- [sok agentic skills beyond tool use](sok-agentic-skills-beyond-tool-use.md) — SoK (7 patterns + lifecycle)
- [skill bundle patterns](../concepts/skill-bundle-patterns.md) — pattern taxonomy
- [skillsbench agent skills benchmark](../examples/skillsbench-agent-skills-benchmark.md) — benchmark
- [coevoskills self evolving skills](../examples/coevoskills-self-evolving-skills.md) — self-evolving
- [awesome agent skill papers catalog](../examples/awesome-agent-skill-papers-catalog.md) — paper catalog

## Sources

- https://www.preprints.org/manuscript/202605.1276
- https://github.com/DataArcTech/Awesome-Agent-Skill-Papers
