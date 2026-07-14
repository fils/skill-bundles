# SkillFortify: Formal Analysis and Supply Chain Security for Agentic AI Skills

**Source:** arXiv:2603.00195 (https://arxiv.org/html/2603.00195v1)
**Date:** Submitted 27 Feb 2026
**Author:** Varun Pratap Bhardwaj (Independent Research)
**Product:** https://www.varunpratap.com/products/skillfortify
**Signal Rating:** 9/10

## Summary

SkillFortify is the first formal analysis framework for agent skill supply chains. Unlike the 12+ reactive security tools that rely on heuristic methods (Snyk agent-scan, Cisco skill-scanner, ToolShield), SkillFortify provides formal guarantees through mathematical proofs.

## Six Contributions

1. **DY-Skill attacker model** — Dolev-Yao adaptation to the five-phase skill lifecycle with a maximality proof
2. **Sound static analysis** — grounded in abstract interpretation (formal guarantees, not heuristics)
3. **Capability-based sandboxing** — with a confinement proof
4. **Agent Dependency Graph** — SAT-based resolution with lockfile semantics (deterministic ordering, dependency resolution, trust scores, integrity hash)
5. **Trust score algebra** — formal monotonicity property
6. **SkillFortifyBench** — 540-skill benchmark

## Results

- 96.95% F1 (95% CI: [95.1%, 98.4%])
- 100% precision, 0% false positive rate on 540 skills
- SAT-based resolution handles 1,000-node dependency graphs in <100ms
- Lockfile with SHA-256 integrity hash for tamper detection
- Supports 22 agent frameworks
- 6,487 malicious tools catalogued (from MalTool benchmark)

## Context: CVE-2026-25253

On January 27, 2026, Ethiack disclosed CVE-2026-25253 — remote code execution in OpenClaw skill runtime, the first CVE assigned to an agentic AI system. ClawHavoc exploited this to infiltrate 1,200+ malicious skills. MalTool benchmarked 6,487 malicious tools. 42,447 skills analyzed: 26.1% have ≥1 security vulnerability.

## Skill Bundle Context

- Agent Dependency Graph = formal dependency resolution (like package lockfiles but for skills)
- Lockfile semantics = reproducible skill installations with integrity verification
- Trust score algebra = formal trust scoring for skill provenance
- Capability-based sandboxing = runtime enforcement with confinement proof
- DY-Skill attacker model = formal threat model for skill lifecycle
- Abstract interpretation = sound static analysis (provable, not heuristic)

## Relevance to Skill Bundles

SkillFortify provides the formal verification layer that skill bundles need for supply chain security. The Agent Dependency Graph with lockfile semantics is a direct parallel to package management (npm, PyPI) but adapted for skill bundles. The DY-Skill attacker model formalizes the threat surface across the entire skill lifecycle (authorship → registry → installation → execution → persistence). This is the "formal verification" complement to SkillGuard's "permission framework" and SkillSieve's "detection" approach.
