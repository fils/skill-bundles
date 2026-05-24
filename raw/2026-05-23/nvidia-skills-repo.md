# NVIDIA Skills Repository — Public Catalog

Source: https://github.com/NVIDIA/skills

## Overview
Centralized, public catalog of official, NVIDIA-verified skills for AI agents. Portable instruction sets enabling AI agents to utilize NVIDIA CUDA-X libraries, AI Blueprints, and platform tools.

## Installation
```bash
npx skills add nvidia/skills
npx skills add nvidia/skills --skill cuopt-numerical-optimization-api-python --agent claude-code
```

## Skill Catalog (140+ skills across 13 product areas)
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
| NemoClaw | Secure agent sandboxing, policy management | 23 |
| TensorRT-LLM | LLM inference optimization | 25 |
| RAG Blueprint | RAG pipeline deployment | 1 |
| Video Search | Video summarization | 10 |

## Security & Trust
- **Verification:** Trust anchor (nv-agent-root-cert.pem) for signatures
- **Scanning:** Automated security scanning for instruction safety and supply-chain integrity
- **Governance:** Automated daily sync ensures skills match verified product sources

## Agent Skills Specification Compliance
- Portable directories with SKILL.md root
- YAML frontmatter (name + description)
- Progressive disclosure pattern

## Bundle Context Elements
- **Automated sync pipeline** (GitHub Actions) for governance
- **Security scanning** (SkillSpector integration)
- **Trust anchor certificates** for cryptographic verification
- **Multi-agent compatibility** (Claude Code, Codex, Cursor, Kiro)
