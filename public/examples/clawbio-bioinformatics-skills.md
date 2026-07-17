---
type: Skill Bundle Example
title: 'ClawBio: Bioinformatics-Native AI Agent Skill Library'
description: '**ClawBio** is the first **bioinformatics-native skill library** for AI agents.'
resource: https://github.com/ClawBio/ClawBio
timestamp: '2026-06-09T00:00:00Z'
date: '2026-06-09'
---

# ClawBio: Bioinformatics-Native AI Agent Skill Library

**Source:** https://github.com/ClawBio/ClawBio  \
**Date Added:** 2026-06-09  \
**Bundle Type:** Domain-Specific Skill Library (Bioinformatics/Genomics)  \
**Raw Source:** [clawbio clawbio](../../raw/2026-06-09/clawbio-clawbio.md)

## Overview

**ClawBio** is the first **bioinformatics-native skill library** for AI agents. Built on **OpenClaw**, it provides a **local-first, privacy-focused, and reproducible** framework for genomic analysis with **88 skills** (29 production-ready) and access to **8,000+ Galaxy tools**. It bridges the gap between stochastic LLM reasoning and rigorous bioinformatics execution.

## Skills Included (88 Total, 29 Production-Ready)

| Skill | Category | Description |
|-------|----------|-------------|
| **Bio Orchestrator** | Infrastructure | Automatically routes inputs (files/text) to the correct skill |
| **PharmGx Reporter** | Personal | Analyzes 12 genes/51 drugs for personalized dosage (CPIC guidelines) |
| **Drug Photo** | Personal | Identifies meds from photos (Telegram/Discord) and checks against genotype |
| **GWAS Lookup** | Population | Queries 9 databases (gnomAD, ClinVar, GTEx, etc.) for variant data |
| **Ancestry PCA** | Population | PCA vs SGDP reference panel with publication-quality figures |
| **UKB Navigator** | Research | Semantic search across 22,000+ UK Biobank fields |
| **Galaxy Bridge** | Research | Search and run 8,000+ tools from usegalaxy.org via CLI |
| **nf-core Wrappers** | Pipeline | Production wrappers for `scrnaseq`, `rnaseq`, `sarek` (variant calling) |
| **Genomic Intelligence (gi-*)** | AI/ML | Six skills wrapping transformer-based DNA language model predictions |

## Context Elements (Rich Formal Artifacts)

### 1. Specification Layer (Machine-Readable Contracts)
- **`SKILL.md` files for every skill** — domain expertise encoded in structured markdown, not model weights
- **Specification-First philosophy**: *"Instead of allowing an LLM to improvise code (which leads to hallucinations in critical areas like dosage), ClawBio uses a machine-readable contract."*

### 2. Validation & Benchmarking Infrastructure (v0.5.0, April 2026)
- **AD Ground Truth:** 34 Alzheimer's genes across 3 evidence tiers
- **Mock API Server:** Deterministic endpoints for offline CI testing
- **Public Leaderboard:** **92.3% (168/182) tests passing** across audited skills
- Systematic validation as part of the release process

### 3. Reproducibility Bundles (Generated Per Execution)
Each skill execution generates a `reproducibility/` bundle containing:
- `commands.sh`: The exact replay command
- `environment.yml`: Conda environment snapshot
- `checksums.sha256`: SHA-256 verification for outputs
- **This is a formal reproducibility artifact — a key context element type**

### 4. Reference Genome: The Corpasome (Real, Fully Open Human Genome)
- **23andMe SNP chip:** ~600K variants
- **30x Illumina WGS:** ~4M SNPs, 600K indels, structural variants (GRCh37)
- **DOI:** 10.5281/zenodo.19297389
- Used for **all demo data** — ensures deterministic, reproducible testing

### 5. Developer Tooling & AI-Ready Artifacts
- **Scaffolding:** `python scaffold_skill.py` for creating new skills
- **Testing:** `uv run pytest` suite
- **`llms.txt`** (token-optimized summary for LLM context)
- **`AGENTS.md`** (universal guide for AI coding agents)
- **Hosted Inference:** Six `gi-*` skills wrap Genomic Intelligence platform

### 6. Conversational Interfaces (Agent Access Layers)
1. **RoboTerri:** Telegram/Discord messaging agent (handles VCF, FASTQ, 23andMe uploads, medication photos)
2. **OpenClaw Gateway:** Self-hosted browser/webchat interface
3. **Claude Code:** Uses `CLAUDE.md` to teach agent how to route requests to local skills

## Composition Notes

ClawBio demonstrates **advanced bundle composition patterns**:

1. **Domain-focused cohesion**: All 88 skills serve bioinformatics/genomics — high semantic coherence
2. **Specification layer as validation**: Machine-readable `SKILL.md` contracts prevent hallucination in critical domains (dosage, genetics)
3. **Reproducibility as a generated artifact**: Every execution produces a formal reproducibility bundle — this is a **context element type** (reproducibility contract)
4. **Multi-modal agent interfaces**: CLI, chat (Telegram/Discord), web (OpenClaw), IDE (Claude Code) — same skills, different access patterns
5. **Reference data as bundle asset**: The Corpasome genome is bundled with the library for deterministic testing
6. **Validation leaderboard**: Public, quantitative quality metric (92.3% pass rate) — a **governance/monitoring artifact**
7. **Galaxy Bridge**: Access to 8,000+ external tools — demonstrates **external tool registry mapping** as a context element

## Installation & Distribution

- **Claude Code:** `/plugin marketplace add ClawBio/ClawBio`
- **Manual:** `git clone https://github.com/ClawBio/ClawBio.git && cd ClawBio && uv sync`
- **No pip package** — must clone repository
- **Agent-agnostic:** Works with Claude, ChatGPT, or local models (Ollama)

## Confidence

9/10 — Well-documented GitHub repo with clear architecture, validation infrastructure, reference genome, and multiple access layers. Production-ready skills with real users.

## Sources

- https://github.com/ClawBio/ClawBio
- https://clawbio.ai/
- Raw: [clawbio clawbio](../../raw/2026-06-09/clawbio-clawbio.md)
