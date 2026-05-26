# OWASP Agentic Skills Top 10 (AST10) — Security Risk Framework for Skill Bundles

**Source:** https://owasp.org/www-project-agentic-skills-top-10/
**Date Added:** 2026-05-26 (Iteration 11)
**Project Lead:** Ken Huang (OWASP AIVSS Lead)
**License:** CC-BY-SA-4.0
**Bundle Type:** Security Risk Taxonomy · Universal Skill Format · Governance Framework
**Confidence:** 9/10

## Name & Origin

The **OWASP Agentic Skills Top 10 (AST10)** is the first dedicated security risk framework for the agent skill ecosystem, analogous to OWASP's Top 10 for web applications and LLM applications. Published in Q1 2026, it identifies the 10 most critical security risks in the skill execution layer of AI agents.

**Mental Model:** *"MCP = how the model talks to tools; AST10 = what those tools actually do."*

## Skills Included

- Risk classification and assessment methodology for skill inventory
- **Universal Skill Format** with permissions, risk tiers, and cryptographic signatures
- Scanning pipeline recommendations (semantic + behavioral multi-tool)
- Governance controls (immutable pinning, hash verification, least-privilege manifests)

## Context Elements

- **Risk Taxonomy (10-class):** AST01–AST10 covering malicious skills, supply chain compromise, over-privileged skills, insecure metadata, unsafe deserialization, weak isolation, update drift, poor scanning, no governance, cross-platform reuse
- **Lethal Trifecta:** Formal risk model combining (private data access) × (untrusted content exposure) × (external communication) = high-risk classification
- **Universal Skill Format (YAML):** Proposed standard with `permissions.files`, `permissions.network`, `risk_tier`, `signature`, `content_hash`
- **Security Checklist:** 12-item checklist for users/security teams and developers

## How Context Elements Support Skills

AST10 provides the **security specification** that skill bundle validation tools should enforce:

1. **Malicious Skills (AST01):** Merkle root signing + registry scanning — directly complements [[nvidia-verified-agent-skills]]'s OpenSSF signing
2. **Supply Chain (AST02):** Registry transparency + provenance tracking — maps to [[purplebox-supply-chain-security]]'s 6-vector taxonomy
3. **Over-Privileged (AST03):** Least-privilege manifests + schema validation — reinforces [[veto-agent-authorization]] pattern
4. **Weak Isolation (AST06):** Containerization + Docker sandboxing — aligns with [[graphguard-os-guardrails]] and [[nemoclaw-security-scanner]]

The **Lethal Trifecta** formalizes what [[mondoo-agent-skills-security]] found empirically: skills with data access + untrusted content + network egress are the highest risk.

## Composition Notes

This is a **meta-governance bundle** — it defines the rules by which other skill bundles should be evaluated:

1. **Specification Layer:** The Universal Skill Format provides a machine-readable standard for permissions, risk tiers, and signatures
2. **Scanning Layer:** AST08 (Poor Scanning) defines requirements for multi-tool scanning pipelines
3. **Governance Layer:** AST09 (No Governance) mandates skill inventories and agentic identity controls
4. **Compliance Layer:** The framework maps to existing security standards (OWASP LLM Top 10, MITRE ATLAS)

The framework is uniquely **evidence-based** — built on real incident data:
- 36.8% of 3,984 scanned skills contain flaws
- 1,184 malicious skills in ClawHavoc campaign
- 135,000+ exposed OpenClaw instances
- CVE-2026-28363 (ClawJacked) CVSS 9.9

## Reproducibility

High — published on OWASP's official website as an open project under CC-BY-SA-4.0. Full write-ups for AST01–AST06 expected Q2 2026.

## Bundle Links
- [[mondoo-agent-skills-security]] — Empirical basis for many AST10 risk categories
- [[nvidia-verified-agent-skills]] — Provides the signing/certificate chain AST10 recommends
- [[purplebox-supply-chain-security]] — Supply chain attack taxonomy maps to AST02
- [[nemoclaw-security-scanner]] — Fills the scanning pipeline gap (AST08)
