# Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

**Source:** arXiv:2604.08224 (cs.SE, cs.MA)
**Authors:** Chenyu Zhou, Huacan Chai, Wenteng Chen, Zihan Guo, Rong Shan, Yuanyi Song, Tianyi Xu, Yingxuan Yang, Aofan Yu, Weiming Zhang, Congming Zheng, Jiachen Zhu, Zeyu Zheng, Zhuosheng Zhang, Xingyu Lou, Changwang Zhang, Zhihui Fu, Jun Wang, Weiwen Liu, Jianghao Lin, Weinan Zhang (21 authors)
**Submitted:** Apr 9, 2026
**Citations:** 35
**Pages:** 54
**Signal Rating:** 10/10

## Abstract

LLM agents are increasingly built less by changing model weights than by reorganizing the runtime around them. Capabilities that earlier systems expected the model to recover internally are now externalized into memory stores, reusable skills, interaction protocols, and the surrounding harness that makes these modules reliable in practice.

This paper reviews that shift through the lens of **externalization**. Drawing on the idea of **cognitive artifacts**, it argues that agent infrastructure matters not merely because it adds auxiliary components, but because it transforms hard cognitive burdens into forms that the model can solve more reliably.

## Core Framework

Under the externalization view:

| Form | What it externalizes |
|------|---------------------|
| **Memory** | State across time |
| **Skills** | Procedural expertise |
| **Protocols** | Interaction structure |
| **Harness engineering** | Unification layer that coordinates them into governed execution |

## Historical Progression

**Weights → Context → Harness**

1. **Weights era** — Capabilities baked into model parameters
2. **Context era** — Capabilities externalized into prompts, memory, skills
3. **Harness era** — Capabilities coordinated by surrounding infrastructure (governed execution)

## Key Ideas

1. **Cognitive artifacts lens** — Agent infrastructure (memory, skills, protocols, harness) are cognitive artifacts that transform hard cognitive burdens into tractable forms.
2. **Three coupled forms of externalization** — Memory, skills, and protocols are distinct but coupled. They interact inside a larger agent system.
3. **Harness as unification layer** — Harness engineering is not just "glue code" but the coordination layer that makes memory + skills + protocols reliable in practice.
4. **Parametric vs. externalized trade-off** — There's a fundamental trade-off between capabilities baked into model weights vs. those externalized into runtime infrastructure.
5. **Self-evolving harnesses** — Emerging direction: harnesses that improve themselves over time.
6. **Shared agent infrastructure** — Emerging direction: shared/collective agent infrastructure (cf. SkillClaw's shared skill repository).
7. **Open challenges** — Evaluation, governance, long-term co-evolution of models and external infrastructure.

## Context Elements

- **Cognitive artifacts framework** — Theoretical lens for understanding externalization
- **Four-form taxonomy** — Memory, skills, protocols, harness (unified classification)
- **Weights→Context→Harness progression** — Historical development framework
- **Parametric/externalized trade-off** — Design space for capability placement

## Relation to Existing Wiki

- **Theoretical foundation** for the entire skill bundles wiki — provides the systems-level framework for why skills matter
- Skills = "externalized procedural expertise" — formal definition
- Harness engineering connects to [[skillguard-permission-framework]] (governance), [[skillfortify-formal-verification-supply-chain]] (formal verification)
- Self-evolving harnesses → [[skillclaw-collective-skill-evolution]], [[coevoskills-self-evolving-skills]]
- Shared agent infrastructure → [[skillclaw-collective-skill-evolution]] (shared skill repository)
- Related to [[arxiv-agent-skills-survey]] (prior survey, this is more systems-level)
- Related to [[skill-os-skills-as-apps]] (OS abstraction = harness engineering)
- Provides theoretical backing for [[swe-skills-bench-utility-benchmark]] findings (skills as externalized procedural expertise can fail when expertise doesn't match context)
