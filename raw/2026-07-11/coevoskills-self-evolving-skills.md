# CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification

**Source:** https://arxiv.org/abs/2604.01687 (arXiv:2604.01687v2, 12 Apr 2026)
**Project Page:** https://zhang-henry.github.io/CoEvoSkills/
**Authors:** Hanrong Zhang, Shicheng Fan, Henry Peng Zou, Yankai Chen, Zhenting Wang, Jiayu Zhou, Chengze Li, Wei-Chieh Huang, Yifei Yao, Kening Zheng, Xue Liu, Xiaoxiao Li, Philip S. Yu
**Institutions:** UIC, MBZUAI, McGill, Columbia, Zhejiang U, UBC
**License:** CC BY 4.0
**Date Ingested:** 2026-07-11
**Signal Rating:** 9/10

## Key Ideas

- **Core problem:** Agent skills (Anthropic concept) are structured bundles of interdependent multi-file artifacts (workflow instructions, scripts, domain references), not simple tool functions. Manual authoring is labor-intensive and suffers from **human–machine cognitive misalignment** — human-intuitive workflows don't match how LLMs process context, leading to degraded performance (e.g., Natural Science domain on SkillsBench).
- **Tool–skill gap:** Existing self-evolving methods designed for tools cannot be applied to skills because skills are multi-file packages, not single functions. CoEvoSkills is the first to address this gap.
- **Framework:** CoEvoSkills couples a **Skill Generator** (iteratively refines skill packages) with a **Surrogate Verifier** (co-evolves to provide informative, actionable feedback **without ground-truth test content**).
- **Results:** On SkillsBench, CoEvoSkills achieves highest pass rate among 5 baselines on both Claude Code and Codex. Strong generalization to 6 additional LLMs. Surpasses human-curated skills within 5 evolution iterations.

## Quotes

> "A tool is a single, self-contained function, whereas a skill is a structured bundle of interdependent multi-file artifacts."

> "Human-curated skills yield highly uneven gains: while certain domains benefit substantially, others, such as Natural Science, even exhibit degraded performance after skill integration. We hypothesize that a key driver of this inconsistency is human–machine cognitive misalignment."

> "Existing self-evolving methods designed for tools cannot be directly applied to skills due to their increased complexity."

## Skill Bundle Context Elements

- **Multi-file skill packages** — workflow instructions + executable scripts + domain references
- **Co-evolutionary verification** — generator + surrogate verifier co-evolve without ground-truth
- **SkillsBench evaluation** — benchmark-validated effectiveness
- **Progressive disclosure** — YAML frontmatter (name, description) + constraints + workflow + edge cases + scripts/

## Impact for Skill Bundles

CoEvoSkills is the first framework to formally address the **tool–skill gap** in autonomous skill generation. It validates the skill bundle concept (skills = multi-file packages, not atomic tools) and introduces co-evolutionary verification as a new context element for skill bundles — the verifier itself is a formal artifact that constrains and improves skill quality.

## Links

- [[skillsbench-agent-skills-benchmark]] — evaluation benchmark used
- [[arxiv-agent-skills-survey]] — cited for skill definition
- [[skill-bundle-patterns]] — multi-file bundle structure
