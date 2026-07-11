# Graph-of-Skills v3: SkillsBench Leaderboard Results & SkillsBench v1.1 Update

**Sources:**
- https://arxiv.org/abs/2604.05333 (v3, 27 May 2026)
- https://skillsbench.ai/ (v1.1, 87 tasks)
- https://github.com/benchflow-ai/skillsbench
**Date Ingested:** 2026-07-11
**Signal Rating:** 8/10

## Graph-of-Skills (GoS) v3 Update

- **GoS** (Graph-of-Skills, arXiv:2604.05333) updated to v3 with concrete SkillsBench results:
  - Peak reward increase: **+25.55%** on SkillsBench using GPT-5.2 Codex
  - Token savings: **-56.72%** total tokens vs vanilla full skill-loading baseline
  - Consistent improvements across Claude Sonnet 4.5, MiniMax M2.7, GPT-5.2 Codex
  - Scales from 200 to 2,000 skills
- **Method:** Offline skill graph construction → hybrid semantic-lexical seeding → reverse-aware Personalized PageRank → context-budgeted hydration
- **Key insight:** Retrieving a bounded, dependency-aware skill bundle is both more effective AND more efficient than loading all skills or using flat semantic retrieval

## SkillsBench v1.1 Update

- Now **87 tasks** across 8 domains (up from 86/11 domains in v1.0)
- **Leaderboard** (24 model-harness configurations):
  - #1: GPT-5.5 OpenHands — 51.5% → 67.3% (+15.8, g=32.6%)
  - #2: GPT-5.5 Codex — 46.8% → 66.5% (+19.7, g=37.0%)
  - #3: Opus 4.7 Claude Code — 43.0% → 61.2% (+18.2, g=31.9%)
  - #4: Gemini 3.1 Pro Gemini CLI — 36.0% → 60.8% (+24.8, g=38.7%)
  - #5: GLM 5.1 OpenHands — 32.7% → 58.4% (+25.7, g=38.1%)
- **Normalized gain metric (g):** Measures skill effectiveness relative to room for improvement
- **Three abstraction layers:** Skills (applications) → Agent Harness (OS) → Models (CPUs)
- **Professional domains:** Software Engineering, Industrial & Physical Systems, Natural Science, Office & White Collar, Finance & Economics, Mathematics & OR, Cybersecurity, Media & Content Production
- **Trend:** Fleet mean resolution rate 49.2% with skills, improving +2.2 pts/month across model releases

## Impact for Skill Bundles

- GoS v3 provides **concrete benchmark evidence** that dependency-aware skill bundle retrieval outperforms flat retrieval — validating the skill bundle composition thesis
- SkillsBench v1.1 leaderboard quantifies skill augmentation value across 24 model configurations
- The three-layer abstraction (Skills/Harness/Models) maps to our wiki structure (examples/tools/concepts)
- Token savings of 56.72% from GoS demonstrates that **dependency-aware retrieval** is not just better for quality but also for efficiency — a key argument for skill bundle composition over flat catalogs

## Links

- [[graph-of-skills-dependency-retrieval]] — existing wiki entry (needs update with v3 results)
- [[skillsbench-agent-skills-benchmark]] — existing wiki entry (needs update with v1.1 leaderboard)
