---
title: "SkillSpector: NVIDIA Security Scanner for AI Agent Skills"
date: 2026-07-15
sources: ["https://github.com/nvidia/skillspector", "https://docs.nvidia.com/skills/scanning-agent-skills"]
skills_included: ["YARA-based malicious pattern detection", "OWASP/MITRE-aligned security scanning", "Batch scanning", "CI/CD integration", "MCP least-privilege analysis", "Multi-provider LLM semantic analysis"]
context_elements: ["YARA rules (pattern-based detection)", "OWASP LLM guidance alignment", "MITRE threat framework alignment", "CI/CD pipeline integration", "Docker containerization", "Plugin extensions system"]
composition: "Security scanner: YARA rule engine + LLM semantic analysis + OWASP/MITRE framework alignment. Scans skills before installation. Part of NVIDIA-Verified ecosystem (catalog → scan → sign → document → distribute)."
reproducibility: "Open-sourced on GitHub (NVIDIA/SkillSpector, 13.2k stars, 1.1k forks, Apache 2.0). 1312 unit tests. v2.3.13. Active development (286 commits, latest Jul 14, 2026)."
rating: 10
---

# SkillSpector: NVIDIA Security Scanner for AI Agent Skills

**Origin:** NVIDIA (GitHub: nvidia/skillspector)
**Stars:** 13.2k | Forks: 1.1k | Contributors: 38
**License:** Apache 2.0
**Version:** 2.3.13 (Jul 14, 2026)

## Overview

SkillSpector is NVIDIA's open-source security scanner for AI agent skills. It detects vulnerabilities, malicious patterns, and security risks before installing agent skills. It is the scanning component of the NVIDIA-Verified Agent Skills ecosystem — the operational implementation of the "scan" step in the governance pipeline: catalog → **scan** → sign → document → distribute.

## Detection Capabilities

1. **YARA-based pattern matching** — Uses YARA rules (1.1% of codebase) for known malicious code patterns
2. **OWASP + MITRE alignment** — Scanning coverage grounded in recognized AI security governance frameworks
3. **LLM semantic analysis** — Multi-provider support (Anthropic direct + Vertex proxy, Bedrock) for semantic threat analysis
4. **MCP least-privilege analysis** — Analyzes MCP server permissions for over-privilege
5. **Batch scanning** — `contrib/batch_scan` module for scanning multiple skills at once
6. **CI/CD integration** — GitHub Actions workflows for automated scanning in pipelines

## Architecture

- `src/skillspector/` — Core scanner logic
- `extensions/` — Plugin system (includes CI scan tool)
- `contrib/batch_scan/` — Batch scanning utilities
- `tests/` — Comprehensive test suite (1312 unit tests passing)
- `.github/workflows/` — CI/CD (lint, unit tests, Docker smoke, OSS release sync)
- Internal-to-OSS release pipeline (`scripts/create-oss-release.sh`)

## Context Elements

- **YARA rules** — Pattern-based malicious code detection (formal rule definitions)
- **OWASP LLM guidance** — Security framework alignment
- **MITRE frameworks** — Threat modeling alignment
- **Skill cards** — Trust metadata (from NVIDIA-verified ecosystem)
- **Cryptographic signing** — skill.oms.sig (from NVIDIA-verified ecosystem)
- **CI/CD integration** — Automated scanning as deployment gate

## Relation to Skill Bundle Patterns

SkillSpector operationalizes the scanning step of the [[nvidia-verified-agent-skills-governance]] pipeline. It is the industry-grade, productionized counterpart to academic detection frameworks.

- Operationalizes [[nvidia-verified-agent-skills-governance]] (scanning step)
- Complements [[skillsieve-malicious-skill-detection]] (three-layer LLM-based triage — SkillSpector adds YARA + CI integration)
- Related to [[skillfortify-formal-verification-supply-chain]] (formal supply chain analysis — SkillSpector is the practical scanner)
- Related to [[skillguard-permission-framework]] (runtime governance — SkillSpector is pre-installation)
- Defense counterpart to [[maltool-malicious-tool-attacks]], [[badskill-backdoor-model-in-skill]], [[skillject-automated-prompt-injection]]
- Related to [[nemoclaw-security-scanner]] (earlier NVIDIA scanner, SkillSpector is the successor)

## Key Insight

Production-grade skill security scanning requires both pattern-based detection (YARA) and semantic analysis (LLM). SkillSpector combines both with industry-standard frameworks (OWASP, MITRE) and integrates directly into CI/CD pipelines, making pre-installation scanning a first-class deployment gate rather than an afterthought.

[[backlinks]]
