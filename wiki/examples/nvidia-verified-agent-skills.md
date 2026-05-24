# NVIDIA Verified Agent Skills — Governance & Verification

**Date:** 2026-05-23  
**Sources:**
- https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/
- https://github.com/NVIDIA/skills
**Confidence:** 5/5 (Official NVIDIA blog + GitHub repo)

## Name & Origin
NVIDIA Verified Agent Skills — a governed catalog of portable instruction sets for AI agents to interact with NVIDIA CUDA-X libraries, AI Blueprints, and platform tools. Published in the NVIDIA/skills GitHub repository with ~140 skills across 13 product areas.

## Skills Included
140+ verified skills covering:
- CUDA-Q (quantum), cuOpt (optimization), DALI (data loading)
- DeepStream (vision AI), Megatron-Bridge/Core (distributed training)
- Model-Optimizer (quantization), NeMo Evaluator/RL (LLM eval/training)
- NemoClaw (sandboxing/policy), TensorRT-LLM (inference optimization)
- RAG Blueprint, Video Search

## Context Elements
- **OpenSSF Model Signing (OMS)**: Cryptographic signatures (skill.oms.sig) cover every file in the skill directory, ensuring post-publication integrity
- **SKILLCARD.yaml**: Machine-readable trust metadata including authorship, licensing, dependencies, limitations, and data flow
- **SkillSpector**: Automated security scanner covering:
  - Software risks: vulnerable dependencies, suspicious scripts, credential access
  - Agent risks: hidden instructions, prompt injection, trigger abuse, tool poisoning
  - Governance alignment: OWASP Top 10 for LLM/Agentic AI, MITRE ATLAS
- **Certificate chain**: nv-agent-root-cert.pem trust anchor for local verification
- **Automated sync pipeline**: Daily GitHub Actions sync ensures skills match verified product sources

## Verification Process
```bash
model_signing verify certificate SKILL_DIR \
  --signature SKILL_DIR/skill.oms.sig \
  --certificate-chain nv-agent-root-cert.pem \
  --ignore-unsigned-files
```

## How Context Elements Support Skills
This is the most comprehensive example of formal governance in the skill bundle ecosystem:
- Cryptographic signing ensures skills haven't been tampered with
- SkillSpector scanning validates safety before publication
- SKILLCARD.yaml provides machine-readable provenance for automated tooling
- The verification pipeline creates an auditable chain from source to publication

## Composition Notes
This represents the gold standard for skill governance:
1. **Source authenticity**: OpenSSF cryptographic signatures
2. **Content safety**: Automated scanning (SkillSpector)
3. **Metadata transparency**: Machine-readable skill cards
4. **Distribution integrity**: Automated sync pipeline
5. **Multi-agent compatibility**: Works across Claude Code, Codex, Cursor, Kiro

## Reproducibility
High — public GitHub repo with CLI installation (npx skills add nvidia/skills), verification commands documented, trust anchor available.
