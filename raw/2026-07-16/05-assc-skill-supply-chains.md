# Skills Are Not Islands: Agent Skill Supply Chains (ASSCs)

**Source:** https://arxiv.org/abs/2607.01136 | https://arxiv.org/html/2607.01136v1
**Date:** Jul 1 2026 | Peking University (Jia, Zhao, He, Zhou)
**Signal rating:** 10/10

## Key ideas
- Skills are **dependency-bearing artifacts** (skill + package + service channels) with opaque implicit deps.
- **SDA (SkillDepAnalyzer)** recovers natural-language dependency evidence → SkillBOM (SBOM-compatible).
- Scale: **1.43 million skills** analyzed; SKILL-DEP benchmark F1=0.95 metadata+deps.
- Patterns: activation-ready but governance-poor metadata; 58.73% name collisions; deps: skills 8.92% / packages 15.48% / services 22.25%; 71–73% of package deps hidden via transitive skill reuse; 30.41% of roots in dependency clusters.
- Security: 60–78% of security-relevant skill deps and 93–98% of some package/service risks are **transitive only** — root-skill inspection insufficient.
- Recommendations: typed multi-channel dependency manifests, dependency-cluster management, risk-warning audit commands, **lockfile-like records**.

## Why skill-bundles
Highest-signal supply-chain work since SkillFortify/ClawHavoc: operationalizes SBOM/lockfile for skills at ecosystem scale; fills versioning/dependency gap flagged by SWE-Skills-Bench and Skill OS.
