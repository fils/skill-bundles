# ClawHavoc Campaign: 1,184 Malicious Skills on ClawHub

**Source:** https://arxiv.org/abs/2602.20867 (SoK paper case study), https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting
**Related:** https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/, https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/
**Date Ingested:** 2026-07-11
**Signal Rating:** 9/10

## Key Ideas

- **ClawHavoc** is a coordinated supply-chain attack that poisoned ClawHub (official skill marketplace for OpenClaw, an open-source AI agent framework) with **~1,184–1,200 malicious skills** over ~6 weeks.
- **Koi Security audit:** Of 2,632–2,857 skills audited on ClawHub, **341 were found malicious** (335 from ClawHavoc campaign alone). That's a **~13% malicious rate** in the marketplace.
- **Attack vectors:** Malicious skills exfiltrated API keys, cryptocurrency wallets, and browser credentials at scale. Combined prompt injection + shell access (Snyk ToxicSkills: 100% of malicious skills combined both attack vectors).
- **Detection:** Koi Security's own bot detected the malicious skills that were targeting it — "found by the bot they were targeting."
- **Industry response:** Antiy CERT documented the campaign within days. OWASP AST01 (Malicious Skills) uses ClawHavoc as primary case study. Palo Alto Unit 42 published analysis of OpenClaw supply chain risk.
- **Hierarchical triage:** arXiv:2604.06550 proposes a hierarchical triage framework for detecting malicious AI agent skills, validated on the ClawHavoc dataset.

## Quotes (from SoK paper)

> "Nearly 1,200 malicious skills infiltrated a major agent marketplace, exfiltrating API keys, cryptocurrency wallets, and browser credentials at scale."

> (Koi Security) "We audited all 2632 skills on ClawHub and found 341 were malicious - 335 from a single campaign we're calling ClawHavoc."

## Skill Bundle Context Elements

- **Supply-chain attack pattern** — marketplace-distributed malicious skills
- **Dual-vector attack** — prompt injection + shell access in SKILL.md
- **Marketplace trust failure** — 13% malicious rate in a major marketplace
- **Detection framework** — hierarchical triage (arXiv:2604.06550)
- **Trust tier model** — response to attack: graduated trust levels for skills

## Impact for Skill Bundles

ClawHavoc is the **canonical real-world case study** for skill bundle supply-chain attacks:
- Quantifies the threat: ~13% of marketplace skills can be malicious
- Demonstrates the dual-vector pattern (prompt injection + shell access)
- Validates the need for [[three-layer-validation-stack]] and [[skill-security-governance]]
- Grounds the SoK paper's security analysis in real exploitation
- Motivates SLSA/in-toto provenance for skill packages (see [[supply-chain-agentic-factory-in-toto]])
- Connects to OWASP AST01 and the broader agentic security ecosystem

## Links

- [[sok-agentic-skills-beyond-tool-use]] — primary case study in the SoK
- [[owasp-agentic-skills-top-10]] — AST01 (Malicious Skills)
- [[purplebox-supply-chain-security]] — supply chain security
- [[skill-security-governance]] — governance framework
- [[nemoclaw-security-scanner]] — security scanning
- [[supply-chain-agentic-factory-in-toto]] — SLSA/in-toto provenance
