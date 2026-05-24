# Verified Skill Governance Patterns

**Date:** 2026-05-23  
**Type:** Concept article

## Overview

NVIDIA's Verified Agent Skills represent the most comprehensive example of formal governance in the skill bundle ecosystem. This concept article synthesizes the governance patterns found in [[nvidia-verified-agent-skills]] and [[nvidia-skills-repo]].

## Governance Pyramid

### Layer 1: Source Authenticity
- OpenSSF Model Signing (OMS) creates cryptographic signatures
- Covers every file in the skill directory
- Verifiable locally via model_signing CLI
- Trust anchor: nv-agent-root-cert.pem

### Layer 2: Content Safety
- **SkillSpector** scans for:
  - Software risks: vulnerable dependencies, suspicious scripts
  - Agent risks: hidden instructions, prompt injection, tool poisoning
- Aligned with OWASP Top 10 for LLM/Agentic AI and MITRE ATLAS

### Layer 3: Metadata Transparency
- **SKILLCARD.yaml**: Machine-readable trust metadata
- Includes: authorship, licensing, dependencies, limitations, data flow
- Enables automated tooling to assess skill trustworthiness

### Layer 4: Distribution Integrity
- Automated sync pipeline (GitHub Actions)
- Daily sync from product team repositories
- Ensures published skills match verified sources

## Comparison with Other Governance Approaches

| Approach | Auth | Safety | Metadata | Distribution |
|--|--|--|--|--|
| NVIDIA Verified | OpenSSF signing | SkillSpector | SKILLCARD.yaml | GitHub Actions |
| VS Code Copilot | Frontmatter schema | N/A | Frontmatter fields | Extensions |
| OpenAI Codex | Scope hierarchy | N/A | openai.yaml config | Installer |
| Anthropic Skills | Plugin marketplace | N/A | Frontmatter | Plugin system |

## Implications for Skill Bundles

The NVIDIA governance model suggests a trajectory where skill bundles will need:
1. **Provenance layer**: Cryptographic signatures to verify skill origin
2. **Safety layer**: Automated scanning for agent-specific risks
3. **Metadata layer**: Machine-readable trust information
4. **Distribution layer**: Automated synchronization for freshness

This aligns with the broader trend toward formal context elements (SHACL, SSSOM) but applies them to skill distribution rather than semantic content.
