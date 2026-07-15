# SkillSpector: Security Scanner for AI Agent Skills

**Source:** NVIDIA/SkillSpector (GitHub)
**URL:** https://github.com/nvidia/skillspector
**Docs:** https://docs.nvidia.com/skills/scanning-agent-skills
**Stars:** 13.2k | Forks: 1.1k | Contributors: 38
**License:** Apache 2.0
**Language:** Python 98.2%, YARA 1.1%
**Version:** 2.3.13 (Jul 14, 2026)
**Signal Rating:** 10/10

## Overview

SkillSpector is NVIDIA's security scanner for AI agent skills. It detects vulnerabilities, malicious patterns, and security risks before installing agent skills. It is the scanning component of the NVIDIA-Verified Agent Skills ecosystem (catalog → **scan** → sign → document → distribute).

## Key Features

1. **YARA-based rule engine** — Uses YARA rules (1.1% of codebase) for pattern matching against known malicious patterns in skill code.
2. **OWASP + MITRE alignment** — Scanning coverage grounded in OWASP guidance for LLM/agentic AI risks and MITRE frameworks.
3. **Batch scanning** — `contrib/batch_scan` module for scanning multiple skills at once.
4. **CI integration** — GitHub Actions workflows for automated scanning in CI pipelines.
5. **Docker support** — Dockerfile + .dockerignore for containerized scanning.
6. **Multi-provider LLM support** — Supports Anthropic (direct + Vertex proxy), Bedrock, and other LLM providers for semantic analysis.
7. **MCP least-privilege** — Includes MCP least-privilege formatting/analysis.
8. **Extensions** — Plugin system for extending detection capabilities.
9. **Comprehensive test suite** — 1312 unit tests passing, 12 skipped, 34 deselected, 6 xfailed.

## Architecture

- `src/skillspector/` — Core scanner logic
- `extensions/` — Plugin extensions (includes SkillSpector scan tool for CI)
- `contrib/batch_scan/` — Batch scanning utilities
- `docs/` — Documentation
- `tests/` — Test suite (1312+ tests)
- `.github/workflows/` — CI/CD (lint, unit tests, Docker smoke checks, OSS release sync)

## Context Elements

- **YARA rules** — Pattern-based malicious code detection
- **OWASP LLM guidance** — Security framework alignment
- **MITRE frameworks** — Threat modeling alignment
- **Skill cards** — Trust metadata (from NVIDIA-verified ecosystem)
- **Cryptographic signing** — skill.oms.sig (from NVIDIA-verified ecosystem)
- **CI/CD integration** — Automated scanning in deployment pipelines

## Relation to Existing Wiki

- Operationalizes the scanning step of [[nvidia-verified-agent-skills-governance]]
- Complements [[skillsieve-malicious-skill-detection]] (three-layer triage)
- Related to [[skillfortify-formal-verification-supply-chain]] (formal supply chain analysis)
- Related to [[skillguard-permission-framework]] (runtime permission governance)
- Defense counterpart to [[clawhavoc-marketplace-attack]] (malicious skill attacks)

## Notable

- Released as open source (Apache 2.0) with internal-to-OSS release pipeline (`scripts/create-oss-release.sh`)
- Active development: 286 commits, latest commit Jul 14, 2026 (10 hours before this extraction)
- 38 contributors including Claude AI as co-author
- Part of the broader NVIDIA skills ecosystem (NVIDIA/skills repo)
