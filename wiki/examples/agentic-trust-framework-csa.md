# Agentic Trust Framework (ATF) — Zero Trust Governance for Skill Bundles

**Source:** https://cloudsecurityalliance.org/blog/2026/02/02/the-agentic-trust-framework-zero-trust-governance-for-ai-agents
**Repository:** https://github.com/massivescale-ai/agentic-trust-framework
**Date Added:** 2026-05-26 (Iteration 11)
**Author:** Josh Woodruff, MassiveScale.AI
**License:** CC BY 4.0
**Bundle Type:** Identity · Behavior · Data Governance · Segmentation · Incident Response — Governance Framework
**Confidence:** 9/10

## Name & Origin

The **Agentic Trust Framework (ATF)** is an open governance specification from the Cloud Security Alliance that applies Zero Trust principles to autonomous AI agents. Published February 2026, it provides a maturity model, promotion gates, and implementation phases for governing agent skills and capabilities.

**Core Principle:** *"No AI agent should be trusted by default… Trust must be earned through demonstrated behavior and continuously verified."*

## Skills Included

- **Identity management** — Authentication, authorization, session management for agent skills
- **Behavioral monitoring** — Observability, anomaly detection, intent analysis during skill execution
- **Data governance** — Input validation, PII protection, output governance for skill inputs/outputs
- **Segmentation controls** — Access control, resource boundaries, policy enforcement per skill
- **Incident response** — Circuit breakers, kill switches, containment for rogue skill behavior

## Context Elements

- **Agent Maturity Model (4 Levels):** Intern (observe) → Junior (recommend) → Senior (act) → Principal (autonomous) — maps directly to skill autonomy levels
- **Five Promotion Gates:** Performance thresholds, security validation, business value, incident record, governance sign-off — each with escalating criteria
- **Implementation Phases (Crawl-Walk-Run):** 2-3 week MVP (JWT, logging, schema validation) → 4-6 week Production (OAuth2, RBAC, PII detection) → 8-12 week Enterprise (policy-as-code, streaming anomaly detection)
- **Compliance Mapping:** SOC 2, ISO 27001, NIST AI RMF, EU AI Act mapped to 7 ATF requirements
- **Build Order (Week-by-Week):** Identity → Data Governance → Behavioral Monitoring → Segmentation → Incident Response

## How Context Elements Support Skills

ATF provides **guardrails for skill deployment** at every maturity level:

1. **Identity (skills provenance):** Every skill must have a verifiable publisher identity — aligns with [[nvidia-verified-agent-skills]]'s certificate chain
2. **Behavior (skill monitoring):** When a skill executes, its behavior must be observable — logging every file access, network call, and state change
3. **Data Governance (skill I/O):** Skills handling PII or credentials require input validation and output filtering — maps to [[veto-agent-authorization]] patterns
4. **Segmentation (skill isolation):** Skills must run in resource-bounded environments — aligns with [[nemoclaw-security-scanner]] and [[graphguard-os-guardrails]]
5. **Incident Response (skill fail-safe):** Circuit breakers and kill switches for skills behaving unexpectedly

## Composition Notes

ATF and [[owasp-agentic-skills-top-10]] are **complementary frameworks**:

| Dimension | OWASP AST10 | ATF |
|-----------|-------------|-----|
| Focus | Risk classification | Governance process |
| Output | Vulnerability taxonomy | Maturity model |
| Target | Skill developers/registries | Enterprise agent deployments |
| Approach | Reactive (classify risks) | Proactive (mature gradually) |
| Timeline | Q2-Q4 2026 roadmap | Phased 2-12 week implementation |

Together they form a complete governance story: AST10 identifies *what* can go wrong; ATF defines *how* to prevent it.

The maturity model is particularly powerful for skill bundles — it suggests **progressive autonomy** based on demonstrated reliability, not static permission sets.

## Reproducibility

High — open specification on CSA blog under CC BY 4.0, full GitHub repository with implementation code. The MVP phase (2-3 weeks) is designed to be immediately actionable.

## Bundle Links
- [[owasp-agentic-skills-top-10]] — Complementary risk classification framework
- [[nvidia-verified-agent-skills]] — Implements ATF's identity + signing requirements
- [[graphguard-os-guardrails]] — Implements ATF's segmentation + incident response
- [[mondoo-agent-skills-security]] — Provides empirical behavior data for ATF monitoring
