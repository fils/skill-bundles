# Supply Chain Security Meets the Agentic Factory

**Source:** https://medium.com/@rbean_3467/supply-chain-security-meets-the-agentic-factory-5a770c34369b (Medium, 19 Mar 2026)
**Author:** ralphbean (Red Hat / Konflux team)
**GitHub:** https://github.com/konflux-ci/fullsend
**Date Ingested:** 2026-07-11
**Signal Rating:** 8/10

## Key Ideas

- **New trust boundary:** The supply chain is no longer just `source → binary`. With AI agents writing code, it's now `intent → source → binary`. The first half (intent → source) is largely unexamined from a supply chain security perspective.
- **Existing supply chain security stack** (Konflux/Red Hat):
  - **Provenance:** signed in-toto attestations capturing what happened during build (task images, parameters, dependencies, digests)
  - **Neutral observer pattern:** Tekton Chains watches build pipelines from outside; signs attestations with credentials the build never touches (SLSA Build Level 3)
  - **Hermetic builds:** Hermeto pre-fetches all dependencies, runs build with network disabled → complete manifest of ingredients
  - **Contextual SBOMs:** hierarchical relationships (DESCENDANT_OF, BUILD_TOOL_OF) trace every component to origin
  - **Policy gates:** Conforma policy engine evaluates attestations against machine-readable rules before release
- **Threat model for agentic development:**
  1. External prompt injection (manipulate agent inputs — issues, PRs, web content)
  2. Insider threats / compromised credentials
  3. Agent drift (gradually lower-quality code as context accumulates)
  4. Supply chain attacks on the agent itself (compromised models, poisoned training data)
- **Key insight:** An attack on the code-generation model leaves traces in logs/training process (opaque), NOT in build attestations. Traditional supply chain attacks leave traces in build attestations. This is a fundamentally new attack surface.
- **fullsend project:** Konflux community exploring fully autonomous agentic engineering with security-focused confidence. Missing from industry: formal intent verification, zero-trust inter-agent review, autonomous merge with security-grade attestation, agent governance frameworks, provenance for code generation step.

## Quotes

> "The supply chain isn't just source → binary anymore. It's: intent → source → binary."

> "A provenance attestation that only tells you the source commit and the build system is like a medical record that only tells you the patient's name and the hospital."

> "An attack on the code-generation model leaves traces in logs of the agent's operation (or in the model's training process), which are both largely opaque."

## Skill Bundle Context Elements

- **in-toto attestations** — cryptographic provenance for build processes (extensible to skill packages)
- **SLSA framework** — supply chain levels for software artifacts (gap identified for intent→source)
- **Policy gates** — Conforma engine evaluates attestations against rules before release
- **Hermetic builds** — pre-fetch dependencies, disable network → complete ingredient manifest
- **Neutral observer pattern** — separation of signing credentials from build process

## Impact for Skill Bundles

This is the first concrete proposal to extend **SLSA/in-toto provenance** to the agentic code generation pipeline. For skill bundles specifically:
- Skills distributed via marketplaces need provenance attestations (who created them, how, with what model)
- The "intent → source" gap applies directly to skill authoring — a compromised model could generate malicious skills that pass superficial review
- The neutral observer pattern could be applied to skill verification (external verifier signs off on skill quality)
- Policy gates map to skill validation frameworks (SHACL shapes, validate-skill GitHub Actions)
- The fullsend project provides a concrete framework for "provenance for the transformation itself"

## Links

- [[purplebox-supply-chain-security]] — supply chain for skills
- [[skill-security-governance]] — governance framework
- [[sok-agentic-skills-beyond-tool-use]] — ClawHavoc case study (marketplace supply chain attack)
- [[three-layer-validation-stack]] — validation layers
- [[validate-skill-github-action]] — policy gate equivalent
