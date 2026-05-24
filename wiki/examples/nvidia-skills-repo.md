# NVIDIA Skills Repository — Multi-Product Catalog

**Date:** 2026-05-23  
**Sources:**
- https://github.com/NVIDIA/skills
- https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/

**Confidence:** 5/5 (Official GitHub repo + blog)

## Name & Origin
NVIDIA Skills Repository — A centralized, public catalog of official, NVIDIA-verified skills for AI agents. Contains ~140 skills across 13 product areas including CUDA-Q, cuOpt, Megatron, NeMo, and TensorRT.

## Skills Included
| Product | Description | Skills Count |
| CUDA-Q | Quantum applications, GPU simulation | 1 |
| cuOpt | GPU-accelerated optimization (VRP, LP) | 12 |
| DALI | GPU-accelerated data loading | 1 |
| DeepStream | Vision AI development | 2 |
| Megatron-Bridge | Data processing, model conversion | 29 |
| Megatron-Core | Distributed training | 12 |
| Model-Optimizer | Quantization, sparsity, distillation | 8 |
| NeMo Evaluator | LLM evaluation | 4 |
| NeMo-RL | RLHF training (GRPO, DPO, SFT) | 14 |
| NemoClaw | Secure agent sandboxing | 23 |
| TensorRT-LLM | Inference optimization | 25 |
| RAG Blueprint | RAG pipeline deployment | 1 |
| Video Search | Video summarization | 10 |

## Context Elements
- **Automated sync pipeline**: GitHub Actions for daily sync from product team repos
- **Security scanning**: Automated validation for instruction safety and supply-chain integrity
- **Trust anchor certificates**: nv-agent-root-cert.pem for cryptographic verification
- **Multi-agent compatibility**: Designed for Claude Code, Codex, Cursor, Kiro via agentskills.io standard
- **CLI distribution**: npx skills add nvidia/skills for installation

## How Context Elements Support Skills
The automated sync pipeline ensures skills stay current with product updates. The multi-agent compatibility demonstrates adherence to the open agent skills specification, enabling cross-platform usage.

## Composition Notes
This represents a large-scale, production skill catalog with governance infrastructure. The verification pipeline (detailed in [[nvidia-verified-agent-skills]]) provides the trust layer for this distribution.

## Reproducibility
High — public GitHub repo with standardized CLI installation.
