# Mondoo: Agent Skills — Real Power, Real Risk

**URL:** https://mondoo.com/blog/agent-skills-real-power-real-risk
**Author:** Christoph Hartmann (CTO, Mondoo)
**Date Retrieved:** 2026-05-24

Key findings:
- 14 distinct attack patterns identified (prompt injection, data exfiltration, privilege escalation)
- ClawHavoc campaign: 341 malicious skills in 3 days
- Persistence: skills writing malicious instructions to agent memory files
- Ransomware via modified legitimate skills (MedusaLocker)
- No version pinning, no npm-audit equivalent
- Recommendations: least privilege, internal catalogs, LLM-assisted review

Attack vectors documented:
1. Credential harvesting via disguised telemetry scripts
2. Hidden HTML comments / Unicode invisible instructions in SKILL.md
3. Registry flooding + supply chain compromise
