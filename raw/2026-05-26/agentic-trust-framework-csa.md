# Agentic Trust Framework (ATF) — Zero Trust Governance for AI Agents

**Source:** https://cloudsecurityalliance.org/blog/2026/02/02/the-agentic-trust-framework-zero-trust-governance-for-ai-agents
**Author:** Josh Woodruff, MassiveScale.AI
**Published:** 2026-02-02
**License:** CC BY 4.0
**Repository:** https://github.com/massivescale-ai/agentic-trust-framework

## Core Principle
"No AI agent should be trusted by default… Trust must be earned through demonstrated behavior and continuously verified."

## Five Core Elements
1. **Identity** — Authentication, authorization, session management
2. **Behavior** — Observability, anomaly detection, intent analysis
3. **Data Governance** — Input validation, PII protection, output governance
4. **Segmentation** — Access control, resource boundaries, policy enforcement
5. **Incident Response** — Circuit breakers, kill switches, containment

## Agent Maturity Model (4 Levels)
| Level | Name | Autonomy Level |
|-------|------|---------------|
| 1 | Intern | Observe + Report (continuous oversight) |
| 2 | Junior | Recommend + Approve (human approves all) |
| 3 | Senior | Act + Notify (post-action notification) |
| 4 | Principal | Autonomous (strategic oversight only) |

## Five Promotion Gates (escalating criteria)
- Gate 1: Performance (min time at level: 2wk/4wk/8wk; accuracy >95%/99%)
- Gate 2: Security Validation (pen testing, adversarial testing)
- Gate 3: Business Value (ROI, stakeholder sign-off)
- Gate 4: Incident Record (zero critical incidents)
- Gate 5: Governance Sign-off (technical + security + business + risk)

## Implementation Phases
- Phase 1 MVP (2-3wk): JWT auth, structured logging, schema validation, circuit breaker
- Phase 2 Production (4-6wk): OAuth2/OIDC, RBAC/ABAC, PII/PHI detection, rate limiting
- Phase 3 Enterprise (8-12wk): Policy-as-code, streaming anomaly detection, API gateway, IR platform

## Compliance Mapping
SOC 2, ISO 27001, NIST AI RMF, EU AI Act mapped to ATF requirements.

## Complementary Relationship
- MAESTRO (threat modeling) → "What could go wrong?"
- ATF (governance) → "How do we maintain control?"
