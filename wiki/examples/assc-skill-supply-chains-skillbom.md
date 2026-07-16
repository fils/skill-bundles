---
type: Skill Bundle Example
title: 'ASSCs: Agent Skill Supply Chains & SkillBOM'
description: '**Skills Are Not Islands** argues skills have become **dependency-bearing artifacts** with mixed skill–package–service dependencies that remain largely implicit.'
resource: https://arxiv.org/abs/2607.01136
timestamp: '2026-07-16T00:00:00Z'
date: 2026-07-16
sources:
- arXiv:2607.01136
skills_included:
- SDA dependency recovery
- SkillBOM serialization
- Multi-channel dep graphs
context_elements:
- Agent Skill Supply Chains (ASSCs)
- SkillDepAnalyzer (SDA)
- SkillBOM (SBOM-compatible)
- Typed multi-channel deps (skill/package/service)
- Lockfile-like records
- Transitive risk propagation
composition: SDA extracts NL dependency evidence → typed skill/package/service graph → recursive expansion → SkillBOM; applied to 1.43M skills for ecosystem ASSC analysis.
reproducibility: arXiv:2607.01136 Jul 2026; SKILL-DEP benchmark F1=0.95; 1.43M-skill study with reported malicious-skill reporting.
rating: 10
---

# ASSCs: Agent Skill Supply Chains & SkillBOM

**Origin:** Peking University (Jia, Zhao, He, Zhou), arXiv:2607.01136, Jul 1 2026

## Overview

**Skills Are Not Islands** argues skills have become **dependency-bearing artifacts** with mixed skill–package–service dependencies that remain largely implicit. It introduces **Agent Skill Supply Chains (ASSCs)**, the **SkillDepAnalyzer (SDA)** tool, and **SkillBOM** (SBOM-compatible skill bills of materials), then analyzes **1.43 million** skills.

## Architecture (SDA)

1. Recover dependency candidates from front matter + skill bodies (NL evidence)
2. Confidence-score candidates; high-confidence → typed scanners (skill / package / service)
3. Recursively resolve transitive skill + package deps → ASSC graph
4. Serialize as **SkillBOM** (SBOM-IR compatible for existing toolchains)

## Ecosystem Findings (1.43M skills)

| Pattern | Evidence |
|---------|----------|
| Governance-poor metadata | Deps/license/version sparse; activation-ready names/descriptions |
| Name collisions | **58.73%** non-unique names |
| Multi-channel deps | Skills 8.92% · Packages 15.48% · Services 22.25% |
| Hidden package inventory | **71.87% npm / 73.33% PyPI** packages via transitive skill reuse only |
| Dependency clusters | **30.41%** of dependency-bearing roots in workflow clusters |
| Transitive security | **60–78%** security-relevant skill deps transitive-only; **93–98%** of some package/service risks invisible at root |

## Recommendations

- Typed multi-channel dependency manifests (source + version)
- First-class **dependency-cluster** management
- Risk-warning audit commands for registries/package managers
- **Lockfile-like** records for skill developers

## Context Elements

- **ASSC graph** — directed multi-channel supply chain model
- **SkillBOM** — machine-readable skill inventory bridging SBOM practice
- **Transitive risk axiom** — root-skill inspection is insufficient
- **Lockfiles for skills** — operationalizes SkillFortify-style integrity at ecosystem scale

## Relation to Skill Bundle Patterns

- Extends [skillfortify formal verification supply chain](skillfortify-formal-verification-supply-chain.md) (lockfile semantics, ADG) to **1.43M-skill** empirical supply chains
- Complements [clawhavoc marketplace attack](clawhavoc-marketplace-attack.md), [maltool malicious tool attacks](maltool-malicious-tool-attacks.md), [skillsieve malicious skill detection](skillsieve-malicious-skill-detection.md)
- Complements [supply chain agentic factory in toto](supply-chain-agentic-factory-in-toto.md) (SLSA/in-toto for intent→source)
- Addresses versioning gaps from [swe skills bench utility benchmark](swe-skills-bench-utility-benchmark.md) and [skill os skills as apps](skill-os-skills-as-apps.md)
- Aligns with [nvidia verified agent skills governance](nvidia-verified-agent-skills-governance.md) and [prov agent unified provenance](prov-agent-unified-provenance.md)

## Key Insight

Skill bundles inherit software supply-chain physics. Without typed manifests, SkillBOM, and lockfiles, **most risk and most packages live in the transitive dark**. Governance that only scans the root `SKILL.md` is structurally blind.

