---
title: "SkillFortify: Formal Analysis and Supply Chain Security for Agentic AI Skills"
date: 2026-07-14
sources: ["arXiv:2603.00195", "https://www.varunpratap.com/products/skillfortify"]
skills_included: ["DY-Skill attacker model", "Sound static analysis (abstract interpretation)", "Capability-based sandboxing", "Agent Dependency Graph (SAT resolution)", "Trust score algebra", "SkillFortifyBench"]
context_elements: ["Formal verification (5 mathematical theorems)", "Dolev-Yao attacker model for skill lifecycle", "Agent Dependency Graph with lockfile semantics", "Trust score algebra with monotonicity", "SHA-256 integrity hashing"]
composition: "Six-contribution framework: DY-Skill threat model → sound static analysis → capability sandboxing with confinement proof → dependency graph with SAT resolution + lockfile → trust score algebra → benchmark (540 skills)."
reproducibility: "arXiv paper (298K chars). Supports 22 agent frameworks. 540-skill benchmark. Product available at varunpratap.com."
rating: 9
---

# SkillFortify: Formal Analysis and Supply Chain Security for Agentic AI Skills

**Origin:** Independent Research (arXiv:2603.00195, February 2026)
**Product:** https://www.varunpratap.com/products/skillfortify

## Overview

SkillFortify is the **first formal analysis framework** for agent skill supply chains. Unlike the 12+ reactive security tools that emerged after ClawHavoc (Snyk agent-scan, Cisco skill-scanner, ToolShield — all heuristic), SkillFortify provides **formal guarantees** through mathematical proofs. If SkillFortify says a skill is safe, it provably cannot exceed its declared capabilities.

## Six Contributions

1. **DY-Skill attacker model** — Dolev-Yao adaptation to the five-phase skill lifecycle (authorship → registry → installation → execution → persistence) with maximality proof
2. **Sound static analysis** — grounded in abstract interpretation (provable, not heuristic)
3. **Capability-based sandboxing** — with a confinement proof
4. **Agent Dependency Graph** — SAT-based resolution with lockfile semantics (deterministic ordering, dependency resolution, trust scores, SHA-256 integrity hash)
5. **Trust score algebra** — formal monotonicity property
6. **SkillFortifyBench** — 540-skill benchmark

## Key Results

| Metric | Result |
|--------|--------|
| F1 score | 96.95% (95% CI: [95.1%, 98.4%]) |
| Precision | 100% |
| False positive rate | 0% |
| SAT resolution (1,000-node graphs) | <100ms |
| Agent frameworks supported | 22 |
| Malicious tools catalogued (MalTool) | 6,487 |

## Context: CVE-2026-25253

On January 27, 2026, Ethiack disclosed CVE-2026-25253 — RCE in OpenClaw skill runtime, the first CVE assigned to an agentic AI system. ClawHavoc exploited this to infiltrate 1,200+ malicious skills. 42,447 skills analyzed: 26.1% have ≥1 security vulnerability.

## Lockfile Semantics

The lockfile provides:
- Deterministic ordering (alphabetical by skill name)
- Dependency resolution (constraint satisfaction)
- Trust scores at lock time (temporal comparison)
- Analysis status (critical blocks, warning recorded)
- SHA-256 integrity hash (tamper detection)
- Byte-identical output on repeated invocations

## Context Elements

- **Formal verification** — 5 mathematical theorems guaranteeing soundness
- **DY-Skill attacker model** — formal threat model for skill lifecycle
- **Agent Dependency Graph** — dependency resolution (like npm/PyPI but for skills)
- **Lockfile semantics** — reproducible skill installations with integrity verification
- **Trust score algebra** — formal trust scoring with monotonicity
- **Capability-based sandboxing** — runtime confinement with proof

## Relation to Skill Bundle Patterns

SkillFortify provides the **formal verification layer** for skill bundle supply chains:
- Complements [[skillguard-permission-framework]] (runtime permission governance) — SkillFortify governs supply chain, SkillGuard governs runtime
- Complements [[skillsieve-malicious-skill-detection]] (heuristic detection) — SkillFortify provides formal guarantees, SkillSieve provides probabilistic detection
- Extends [[supply-chain-agentic-factory-in-toto]] (SLSA/in-toto provenance) — SkillFortify adds formal analysis to provenance
- Agent Dependency Graph parallels [[orca-cognitive-runtime]]'s DAG composition but for dependency resolution
- Lockfile semantics = package management pattern adapted for skills

## Key Insight

The agent skill ecosystem reproduces the trust pathologies of traditional package ecosystems (npm, PyPI) but with amplified risk — skills execute with broad system privileges in the context of a powerful LLM. Heuristic detection is necessary but insufficient: "no findings does not mean no risk" (Cisco). Formal analysis with mathematical proofs provides the missing guarantee layer.

[[backlinks]]
