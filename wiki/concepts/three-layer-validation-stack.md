# Three-Layer Validation Stack for Skill Bundles

**Date Added:** 2026-06-01 (Iteration 13)
**Confidence:** 9/10

## Definition

A **three-layer validation stack** is the emerging pattern where skill bundles are validated at three different points in the lifecycle, by three different tools, each with a different scope and threat model:

| Layer | Where | Tool (catalog) | Scope | Cost |
|---|---|---|---|---|
| **1. Pre-commit** | Local dev, before commit | [[skill-validator-cli]] (Go binary, 13 platform hooks) | Structure + content + contamination + link rot + LLM-as-judge | Seconds to minutes |
| **2. CI/CD** | PR pipelines, GitHub Actions | [[validate-skill-github-action]] (YAML Action) | Structure + spec compliance + reference checking | < 1 second |
| **3. Registry** | Marketplace / install time | [[agentskill-sh-ags-security-scoring]] (12-category threat scan) | Security (12 threat categories) + content SHA versioning + quality rating | Continuous |

## Why This Pattern Matters

Each layer catches what the others miss:

- **Pre-commit (CLI)** catches deep quality issues (LLM-as-judge scoring on clarity/actionability/novelty, contamination detection, link rot) but is opt-in and requires local install.
- **CI/CD (Action)** catches structural regressions on every PR automatically but doesn't run LLM-as-judge and doesn't know about cross-skill threats.
- **Registry (ags)** catches threats the skill author didn't intend (malicious payloads, supply chain attacks, social engineering) but only at install time and only for skills in the registry.

## Composition With Other Catalog Bundles

- **[[owasp-agentic-skills-top-10]]** — Defines *what* vulnerabilities to scan for at layer 3
- **[[agentic-trust-framework-csa]]** — Defines the *maturity levels* each layer can achieve
- **[[mondoo-agent-skills-security]]** — Provides skills-as-scanners that can plug into layer 1 or 2
- **[[purplebox-supply-chain-security]]** — Defines the 6 supply chain attack vectors layer 3 must catch
- **[[nvidia-verified-agent-skills]]** — Provides the OpenSSF signing that supplements layer 3's hash-based provenance

## Cross-Domain Analogy

This three-layer pattern is well-established in **software supply chain security**:

| Software supply chain | Skill bundles |
|---|---|
| Pre-commit linters (eslint, golangci-lint) | skill-validator CLI |
| CI/CD linters + scanners (CodeQL, Snyk) | Validate Skill GitHub Action |
| Registry-level scanners (npm audit, Snyk DB) | agentskill.sh 12-category scanner |

The skill ecosystem is approximately 2-3 years behind the npm/PyPI ecosystem in terms of supply chain maturity, but the convergence on this three-layer pattern is clear.

## Open Questions

1. **Attestation chaining:** Can the three layers share a SLSA-style provenance attestation? (Currently they produce independent signals.)
2. **Cross-platform consistency:** Layer 1 has 13 platform-specific hooks; do layers 2 and 3 cover the same platforms? (Layer 3 currently best-supported on Claude Code, others via CLI.)
3. **Bundle-level validation:** All three layers validate individual skills — but skills in a bundle may interact. Bundle-level validation is an open problem.

## Related Concepts
- [[skill-bundle-patterns]] — Foundation patterns
- [[skill-security-governance]] — Why each layer exists
- [[sssom-mapping-as-context]] — Mappings as a form of validation
- [[constraint-rules-as-context]] — Rules as a form of validation
