# A Survey of Agent Skills: Toward Procedural Infrastructure for LLM Agents

**Source:** https://www.preprints.org/manuscript/202605.1276 (Preprints.org, 19 May 2026)
**GitHub:** https://github.com/DataArcTech/Awesome-Agent-Skill-Papers (12 stars)
**Authors:** Cehao Yang, Xiaojun Wu, Honghao Liu, Xueyuan Lin, Chengjin Xu, Xuhui Jiang, Yuanliang Sun, Wenjie Zhang, Zhichao Shi, Yijie Xu, Jia Li, Hui Xiong, Jian Guo
**License:** CC BY 4.0
**Date Ingested:** 2026-07-11
**Signal Rating:** 9/10

## Key Ideas

- **Six-layer taxonomy** for agent skills:
  1. **Ontology** — what a skill is, relationship to memory, cognition, compression, reusable procedural knowledge
  2. **Representation and Packaging** — how skills are written, structured, serialized, distributed, packaged
  3. **Lifecycle** — acquisition, storage, retrieval, execution, refinement, retirement, internalization
  4. **Runtime Integration** — terminal interfaces, tool interfaces, multi-agent systems, agent harnesses
  5. **Governance** — security, governance risks, trusted deployment mechanisms
  6. **Applications** — robotics, games, web agents, GUI/mobile/OS agents, software engineering

- **Marketplace scale data** (as of April 2, 2026):
  - SkillsMP: 425,000+ skills
  - LobeHub Skills: 169,739 skills
  - agentskill.sh: 110,000+ skills
  - skills.sh: ~87,000 unique skills
  - ClawHub: 20,000+ skills

- **Paradigm arc:** prompt engineering → context engineering → harness engineering. Skills are the key externalization structure.
- **Skill definition:** "reusable procedural abstractions that connect memory, human expertise, and execution" — compress recurring patterns of successful behavior into operational artifacts.
- **Skill representations covered:** natural-language guidance, executable code snippets, decision graphs, filesystem-based packages (SKILL.md), structured skill records.
- **Selective internalization:** skills can be internalized into model behavior (beyond just runtime loading).

## Paper List (from GitHub repo)

The Awesome-Agent-Skill-Papers repo catalogs papers including:
- SkillsBench, CoEvoSkills, Graph-of-Skills
- EffiSkill (code efficiency optimization)
- Scaling Coding Agents via Atomic Skills
- SkillMOO (Multi-Objective Optimization for SE)
- Supply-chain poisoning attacks
- SoK: Agentic Skills

## Quotes

> "Skills compress recurring patterns of successful behavior into operational artifacts that can guide future action."

> "Practical agent engineering has moved through a recognizable arc: from prompt engineering, to context engineering, and now toward harness engineering."

> "Agent skills are rapidly becoming a new ecosystem layer which is already substantial."

## Impact for Skill Bundles

This survey provides the most comprehensive **six-layer taxonomy** for the skill bundle domain, directly mapping to our wiki structure:
- Ontology → concepts/
- Representation/Packaging → examples/ (SKILL.md format)
- Lifecycle → concepts/skill-bundle-patterns
- Runtime Integration → tools/
- Governance → concepts/skill-security-governance
- Applications → examples/ (domain-specific bundles)

The marketplace scale data quantifies the ecosystem size — 800K+ total skills across marketplaces.

## Links

- [[arxiv-agent-skills-survey]] — complementary survey (4-axis)
- [[sok-agentic-skills-beyond-tool-use]] — SoK (7 patterns + lifecycle)
- [[skill-bundle-patterns]] — pattern taxonomy
- [[skillsbench-agent-skills-benchmark]] — benchmark
- [[coevoskills-self-evolving-skills]] — self-evolving
