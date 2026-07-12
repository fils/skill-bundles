# SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?

**Source:** https://arxiv.org/abs/2603.00718
**Date:** 2026-07-12
**Authors:** Shiqi Chen, Jingze Gai, Ruochen Zhou, Jinghan Zhang, Tongyao Zhu, Junlong Li, Kangrui Wang, Zihan Wang, Zhengyu Chen, Klara Kaleb, Ning Miao, Siyang Gao, Cong Lu, Manling Li, Junxian He, Yee Whye Teh
**Submitted:** 28 Feb 2026 (v1), revised 10 Mar 2026 (v2)
**Signal:** 9/10

## Abstract

Real-world tool-using agents operate over long-horizon workflows with recurring structure and diverse demands, where effective behavior requires not only invoking atomic tools but also abstracting and reusing higher-level tool compositions. Existing benchmarks mainly measure instance-level success under static tool sets, offering limited insight into agents' ability to acquire such reusable skills.

### SkillCraft Benchmark
- Explicitly stress-tests agent ability to **form and reuse higher-level tool compositions** (called "Skills")
- Realistic, highly compositional tool-use scenarios
- Difficulty scaled along both **quantitative** and **structural** dimensions
- Designed to elicit skill abstraction and cross-task reuse

### Lightweight Evaluation Protocol
- Agents **auto-compose atomic tools into executable Skills**
- **Cache and reuse** Skills inside and across tasks
- Improves efficiency while accumulating a **persistent library** of reusable skills

### Key Results
- Token usage reduced by up to **80%** by skill saving and reuse
- Success rate strongly correlates with tool composition ability at test time
- Compositional skill acquisition is a **core capability**

## Relevance to Skill Bundles

SkillCraft is a foundational benchmark for **skill composition and reuse**:
1. **Skill = higher-level tool composition** — formalizes the concept that skills are composed from atomic tools
2. **Auto-composition protocol** — agents autonomously create skills from tools, the inverse of static skill bundles
3. **Persistent skill library** — accumulated through task execution, cached and reused cross-task
4. **80% token savings** — quantifies the efficiency benefit of skill reuse
5. **Compositional ability as core capability** — links skill composition to agent success

This directly validates the skill bundle thesis: **composing tools into reusable skills dramatically improves efficiency**.

## Key Quotes

> "Effective behavior requires not only invoking atomic tools but also abstracting, and reusing higher-level tool compositions"

> "Token usage reduced by up to 80% by skill saving and reuse"

> "Success rate strongly correlates with tool composition ability at test time, underscoring compositional skill acquisition as a core capability"

## Links
- PDF: https://arxiv.org/pdf/2603.00718
- Code: https://github.com/shiqichen17/SkillCraft
- Project page: https://skillcraft-website.github.io/page
- Cited by 20
