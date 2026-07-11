# SoK: Agentic Skills — Beyond Tool Use in LLM Agents

**Source:** https://arxiv.org/abs/2602.20867 (arXiv:2602.20867v1, 24 Feb 2026)
**Authors:** Yanna Jiang, Delong Li, Haiyu Deng, Baihe Ma, Xu Wang, Qin Wang, Guangsheng Yu
**License:** CC BY 4.0
**Date Ingested:** 2026-07-11
**Signal Rating:** 10/10

## Key Ideas

- **Formal definition:** Skill S = (C, π, T, R) where C = applicability conditions, π = execution policy, T = termination criteria, R = reusable interface. Skills are simultaneously **executable, reusable, and governable** — distinct from tools (atomic primitives), plans (one-time), and episodic memory.
- **Skill lifecycle model:** 7 stages — discovery, practice, distillation, storage, composition, evaluation, update. First full lifecycle model for skills.
- **Seven design patterns** (system-level taxonomy):
  1. Metadata-driven progressive disclosure (SKILL.md)
  2. Executable code skills
  3. Workflow enforcement
  4. Self-evolving libraries
  5. Marketplace distribution
  6. (two more in full paper)
  7. (pattern 7)
- **Representation × Scope taxonomy:** What skills ARE (natural language, code, policy, hybrid) × What environments they operate over (web, OS, software engineering, robotics).
- **ClawHavoc case study:** ~1,200 malicious skills infiltrated a major agent marketplace (ClawHub), exfiltrating API keys, crypto wallets, browser credentials at scale. Anchored in the security analysis.
- **Key finding:** Curated skills substantially improve agent success rates, but self-generated skills may **degrade** performance (echoes CoEvoSkills finding on cognitive misalignment).

## Security & Governance

- Supply-chain risks (marketplace-distributed skills)
- Prompt injection via skill payloads
- Trust-tiered execution model
- Pattern-specific risk matrix
- ClawHavoc as anchor case study for supply-chain attack on skills

## Six Contributions

1. Unified definition of agentic skills S=(C,π,T,R)
2. Skill lifecycle model (7 stages)
3. Seven-pattern design taxonomy
4. Representation × Scope taxonomy
5. Security/governance analysis with ClawHavoc case study
6. Evaluation framework with benchmark mapping

## Quotes

> "Skills are simultaneously executable, reusable, and governable. A skill carries its own applicability conditions, termination criteria, and callable interface, making it a first-class unit of procedural knowledge."

> "Nearly 1,200 malicious skills infiltrated a major agent marketplace, exfiltrating API keys, cryptocurrency wallets, and browser credentials at scale."

> "Curated skills can substantially improve agent success rates while self-generated skills may degrade them."

## Impact for Skill Bundles

This SoK provides the **formal theoretical foundation** for skill bundle research:
- The S=(C,π,T,R) definition gives us a formal vocabulary for bundle analysis
- The 7 design patterns map to existing wiki examples
- The ClawHavoc case study quantifies supply-chain risk for skill marketplaces
- The lifecycle model provides a framework for tracking bundle evolution
- The "self-generated skills degrade performance" finding validates the need for formal context elements (verification, validation)

## Links

- [[skill-bundle-patterns]] — design patterns taxonomy
- [[skill-security-governance]] — security analysis
- [[three-layer-validation-stack]] — trust tier model
- [[owasp-agentic-skills-top-10]] — security threats
- [[purplebox-supply-chain-security]] — supply chain
- [[coevoskills-self-evolving-skills]] — self-evolving skills (Pattern 4)
- [[agentskills-workshop-2026]] — workshop venue
