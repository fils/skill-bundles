# NVIDIA Verified Agent Skills — Capability Governance

Source: https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/

NVIDIA introduced **Verified Agent Skills** to provide structural transparency and operational integrity for autonomous AI agents. Portable instruction sets for NVIDIA CUDA-X libraries, AI Blueprints, and platform tools.

## Key Features
- **Cataloged:** Synced daily from NVIDIA product teams
- **Scanned:** SkillSpector scans for software and agent-native risks
- **Signed:** Cryptographically signed with OpenSSF Model Signing (skill.oms.sig)
- **Documented:** Machine-readable Skill Card (SKILLCARD.yaml)

## Signature Verification
```bash
model_signing verify certificate SKILL_DIR \
  --signature SKILL_DIR/skill.oms.sig \
  --certificate-chain nv-agent-root-cert.pem \
  --ignore-unsigned-files
```

## The Skill Card (SKILLCARD.yaml)
Machine-readable trust metadata including:
- Authorship/Creator
- Licensing terms
- Dependencies
- Known limitations
- Data flow description

## Verification Pipeline
1. Source Repo → 2. Review → 3. SkillSpector Scan → 4. Evaluate → 5. Skill Card → 6. Sign → 7. Catalog & Sync

## Security Coverage (SkillSpector)
- Software Risks: vulnerable dependencies, suspicious scripts, credential access
- Agent Risks: hidden instructions, prompt injection, trigger abuse, tool poisoning
- Governance: OWASP Top 10 for LLM/Agentic AI, MITRE ATLAS

## Bundle Context Elements
- **OpenSSF Model Signing** (cryptographic provenance)
- **SKILLCARD.yaml** (machine-readable trust metadata)
- **SkillSpector** (automated security scanning)
- **Verification certificate chain** (nv-agent-root-cert.pem)
