---
type: Skill Bundle Example
title: 'ClawHavoc Campaign: 1,184 Malicious Skills on ClawHub'
description: ClawHavoc is a coordinated supply-chain attack that poisoned **ClawHub** (the official skill marketplace for OpenClaw, an open-source AI agent framework) with approximately **1,184–1,200 malicious skills** over approx...
resource: https://arxiv.org/abs/2602.20867
timestamp: '2026-07-11T00:00:00Z'
date: '2026-07-11'
---

# ClawHavoc Campaign: 1,184 Malicious Skills on ClawHub

**Sources:**
- https://arxiv.org/abs/2602.20867 (SoK case study)
- https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting
- https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/
- https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/
**Date Added:** 2026-07-11 (Iteration 36)
**Bundle Type:** Security Case Study · Supply-Chain Attack · Marketplace Poisoning
**Confidence:** 9/10

## Name & Origin

ClawHavoc is a coordinated supply-chain attack that poisoned **ClawHub** (the official skill marketplace for OpenClaw, an open-source AI agent framework) with approximately **1,184–1,200 malicious skills** over approximately 6 weeks. The campaign exfiltrated API keys, cryptocurrency wallets, and browser credentials at scale. It is the canonical real-world case study for skill marketplace supply-chain attacks, anchored in the [SoK: Agentic Skills](../papers/sok-agentic-skills-beyond-tool-use.md) paper.

## Skills Included (malicious patterns)

- **Dual-vector attack:** 100% of malicious skills combined prompt injection + shell access (Snyk ToxicSkills)
- **SKILL.md shell access:** Malicious skills exploit SKILL.md's ability to include executable scripts — "From SKILL.md to Shell Access in Three Lines of Markdown" (Snyk)
- **Credential exfiltration:** API keys, crypto wallets, browser credentials stolen at scale

## Context Elements

- **Supply-chain attack pattern** — marketplace-distributed malicious skills
- **Dual-vector attack** — prompt injection + shell access in SKILL.md
- **Marketplace trust failure** — ~13% malicious rate (341 of 2,632 audited skills)
- **Detection framework** — hierarchical triage (arXiv:2604.06550)
- **Trust tier model** — response: graduated trust levels for skills

## How Context Elements Support Skills

ClawHavoc demonstrates the **critical need for formal context elements** in skill bundles:

1. **Provenance attestation** — without in-toto/SLSA provenance, malicious skills are indistinguishable from legitimate ones (see [supply chain agentic factory in toto](supply-chain-agentic-factory-in-toto.md))
2. **Validation gates** — the attack validates the need for [three layer validation stack](../concepts/three-layer-validation-stack.md) and [validate skill github action](validate-skill-github-action.md)
3. **Trust tiers** — the SoK's trust-tiered execution model directly responds to this attack pattern
4. **Security scanning** — validates [nemoclaw security scanner](nemoclaw-security-scanner.md) and [mondoo agent skills security](mondoo-agent-skills-security.md) approaches
5. **OWASP AST01** — [owasp agentic skills top 10](owasp-agentic-skills-top-10.md) uses ClawHavoc as its primary real-world evidence

## Composition Notes

- **Detection by the target:** Koi Security's bot detected the malicious skills that were targeting it — "found by the bot they were targeting"
- **Scale:** ~1,184 poisoned skills over 6 weeks; 341 confirmed malicious out of 2,632 audited (13% rate)
- **Industry response:** Antiy CERT, Palo Alto Unit 42, Snyk, OWASP all published analyses
- **Academic anchor:** Used as case study in [sok agentic skills beyond tool use](../papers/sok-agentic-skills-beyond-tool-use.md) (arXiv:2602.20867)
- **Hierarchical triage:** arXiv:2604.06550 proposes a formal detection framework validated on ClawHavoc data

## Reproducibility

High — multiple independent security firm analyses (Koi, Antiy CERT, Unit 42, Snyk), academic paper with case study, OWASP documentation.

## Bundle Links

- [sok agentic skills beyond tool use](../papers/sok-agentic-skills-beyond-tool-use.md) — primary case study
- [owasp agentic skills top 10](owasp-agentic-skills-top-10.md) — AST01 (Malicious Skills)
- [purplebox supply chain security](purplebox-supply-chain-security.md) — supply chain security
- [skill security governance](../concepts/skill-security-governance.md) — governance framework
- [supply chain agentic factory in toto](supply-chain-agentic-factory-in-toto.md) — SLSA/in-toto provenance
- [nemoclaw security scanner](nemoclaw-security-scanner.md) — security scanning
- [three layer validation stack](../concepts/three-layer-validation-stack.md) — validation layers
- [mondoo agent skills security](mondoo-agent-skills-security.md) — security analysis

## Sources

- https://arxiv.org/abs/2602.20867
- https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting
- https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/
- https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/
- https://snyk.io/articles/skill-md-shell-access/
- https://arxiv.org/abs/2604.06550 (hierarchical triage framework)
