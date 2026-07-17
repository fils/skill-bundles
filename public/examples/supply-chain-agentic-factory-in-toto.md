---
type: Skill Bundle Example
title: Supply Chain Security Meets the Agentic Factory (SLSA/in-toto for Skills)
description: The first concrete proposal to extend **SLSA/in-toto provenance** to the agentic code generation pipeline.
resource: https://medium.com/@rbean_3467/supply-chain-security-meets-the-agentic-factory-5a770c34369b
timestamp: '2026-07-11T00:00:00Z'
date: '2026-07-11'
---

# Supply Chain Security Meets the Agentic Factory (SLSA/in-toto for Skills)

**Source:** https://medium.com/@rbean_3467/supply-chain-security-meets-the-agentic-factory-5a770c34369b (19 Mar 2026)
**GitHub:** https://github.com/konflux-ci/fullsend
**Date Added:** 2026-07-11 (Iteration 36)
**Author:** ralphbean (Red Hat / Konflux team)
**Bundle Type:** Supply Chain Framework · Provenance Model · Threat Analysis
**Confidence:** 8/10

## Name & Origin

The first concrete proposal to extend **SLSA/in-toto provenance** to the agentic code generation pipeline. Written by a Red Hat engineer on the Konflux team, it identifies the "intent → source" gap in existing supply chain security frameworks and proposes the "fullsend" project for fully autonomous agentic engineering with security-grade attestation.

## Skills Included

This is a framework/infrastructure entry, not a skill bundle per se. However, it directly informs how **skill packages** should be provenance-attested:

- **in-toto attestations** — cryptographic provenance for build processes
- **SLSA Build provenance** — structured claims about how software is produced
- **Hermeto** — hermetic build tool (pre-fetch dependencies, disable network)
- **Tekton Chains** — neutral observer that signs attestations from outside the build
- **Conforma** — policy engine that evaluates attestations against rules

## Context Elements

- **in-toto attestation framework** — specification for verifiable claims about software production
- **SLSA framework** — Supply-chain Levels for Software Artifacts (Build Level 3 achieved via neutral observer)
- **Neutral observer pattern** — signing key isolated from build process (SLSA L3)
- **Hermetic builds** — complete ingredient manifest; network disabled during build
- **Contextual SBOMs** — hierarchical relationships (DESCENDANT_OF, BUILD_TOOL_OF)
- **Policy gates** — Conforma engine evaluates attestations before release
- **Threat model** for agentic development:
  1. External prompt injection
  2. Insider threats / compromised credentials
  3. Agent drift
  4. Supply chain attacks on the agent itself

## How Context Elements Support Skills

This framework identifies a critical gap: **the supply chain is now `intent → source → binary`**, but we only have provenance for `source → binary`. For skill bundles specifically:

1. **Skill provenance:** Skills distributed via marketplaces need attestations (who created them, how, with what model)
2. **Intent verification:** The "intent → source" gap applies to skill authoring — a compromised model could generate malicious skills
3. **Neutral observer for skills:** The pattern could verify skill quality from outside the generation process (analogous to [CoEvoSkills](coevoskills-self-evolving-skills.md)' Surrogate Verifier)
4. **Policy gates for skills:** Map to [validate skill github action](validate-skill-github-action.md) and [three layer validation stack](../concepts/three-layer-validation-stack.md)
5. **Hermetic skill builds:** Pre-fetch all skill dependencies, verify no smuggling

## Composition Notes

The "fullsend" project (Konflux community) is exploring:
- Formal intent verification
- Zero-trust inter-agent review
- Autonomous merge with security-grade attestation
- Agent governance frameworks
- Provenance for the code generation step itself

This is the **infrastructure-level complement** to the academic security analysis in [sok agentic skills beyond tool use](../papers/sok-agentic-skills-beyond-tool-use.md) and [owasp agentic skills top 10](owasp-agentic-skills-top-10.md).

## Reproducibility

Medium-High — blog post with detailed technical content, GitHub project (konflux-ci/fullsend) with open problem domain documents and active PRs.

## Bundle Links

- [purplebox supply chain security](purplebox-supply-chain-security.md) — existing supply chain entry
- [skill security governance](../concepts/skill-security-governance.md) — governance framework
- [sok agentic skills beyond tool use](../papers/sok-agentic-skills-beyond-tool-use.md) — ClawHavoc case study
- [three layer validation stack](../concepts/three-layer-validation-stack.md) — validation layers
- [validate skill github action](validate-skill-github-action.md) — policy gate equivalent
- [clawhavoc marketplace attack](clawhavoc-marketplace-attack.md) — real-world supply chain attack
- [coevoskills self evolving skills](coevoskills-self-evolving-skills.md) — verifier as neutral observer analog

## Sources

- https://medium.com/@rbean_3467/supply-chain-security-meets-the-agentic-factory-5a770c34369b
- https://github.com/konflux-ci/fullsend
- https://in-toto.io/
- https://slsa.dev/
