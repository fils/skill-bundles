# OWASP Agentic Skills Top 10 (AST10) — 2026 Edition

**Source:** https://owasp.org/www-project-agentic-skills-top-10/
**Fetched:** 2026-05-26
**License:** CC-BY-SA-4.0
**Project Lead:** Ken Huang (OWASP AIVSS Lead)

## Key Statistics (Q1 2026)
- 36.8% of scanned skills (1,467 out of 3,984) contain security flaws
- 13.4% of skills contain critical-level issues
- 1,184 malicious skills in ClawHavoc campaign (Antiy CERT)
- 135,000+ OpenClaw instances publicly exposed
- 25%+ of skills across all registries contain at least one vulnerability

## Top 10 Risks (AST10)
1. **AST01: Malicious Skills** (Critical) — Merkle root signing, registry scanning
2. **AST02: Supply Chain Compromise** (Critical) — Registry transparency, provenance tracking
3. **AST03: Over-Privileged Skills** (High) — Least-privilege manifests, schema validation
4. **AST04: Insecure Metadata** (High) — Static analysis, manifest linting
5. **AST05: Unsafe Deserialization** (High) — Safe parsers, sandboxed loading
6. **AST06: Weak Isolation** (High) — Containerization, Docker sandboxing
7. **AST07: Update Drift** (Medium) — Immutable pinning, hash verification
8. **AST08: Poor Scanning** (Medium) — Semantic + behavioral multi-tool pipeline
9. **AST09: No Governance** (Medium) — Skill inventories, agentic identity controls
10. **AST10: Cross-Platform Reuse** (Medium) — Universal YAML format adoption

## Lethal Trifecta
A skill is high-risk when it simultaneously has:
1. Access to private data (SSH keys, API credentials, wallets)
2. Exposure to untrusted content (emails, memory files, instructions)
3. Ability to communicate externally (network egress, webhooks, curl)

## Proposed Universal Skill Format
```yaml
name: example-skill
version: 1.0.0
permissions:
  files:
    read: [ "~/.config/app.json" ]
    deny_write: [ "SOUL.md", "MEMORY.md" ]
  network:
    allow: [ "api.example.com" ]
    deny: "*"
risk_tier: L1  # L0=safe to L3=destructive
signature: "ed25519:ABCDEF1234567890..."
content_hash: "sha256:abcdef1234..."
```

## Incident Timeline (2026)
- Jan 2026: ClawHavoc Campaign — 1,184 malicious skills
- Feb 2026: ToxicSkills Report — Snyk, 76 malicious payloads
- Feb 14, 2026: OpenClaw Log Poisoning patched
- Feb 25, 2026: Claude Code CVE-2025-59536 (CVSS 8.7)
- Feb 26, 2026: CVE-2026-28363 "ClawJacked" (CVSS 9.9)

## Roadmap
- Q2 2026: AST01–AST06 full write-ups
- Q3 2026: Universal Skill Format v1.0, AST07–AST10
- Q4 2026: Flagship project submission
