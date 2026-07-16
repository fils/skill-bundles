---
title: "Inside the Skill Market: SE Activities as Reusable Skills"
date: 2026-07-16
sources: ["arXiv:2607.09065"]
skills_included: ["11,497 SE marketplace skills", "Lifecycle-mapped SE activity skills"]
context_elements: ["SE activity→skill mapping", "Lifecycle coverage analysis", "Skill versioning statistics", "Five-component skill structure", "Marketplace evaluation gap"]
composition: "Activity-centric empirical study of SE skills in public markets: map SDLC activities to skill packages; measure coverage, versioning, and evaluation practices."
reproducibility: "arXiv:2607.09065 Jul 10 2026; 11,497 unique SE-related skills from public repositories/marketplaces."
rating: 8
---

# Inside the Skill Market: SE Activities as Reusable Skills

**Origin:** Cao, Yan, Chen, Lu, Liu, Cheung et al., arXiv:2607.09065, Jul 10 2026

## Overview

First **activity-centric** large-scale study of software-engineering skills in public skill markets. Asks: which SE lifecycle activities are being encapsulated as reusable agent skills, and how evenly is the SDLC covered?

## Scope

- **11,497** unique SE-related skills from public repositories and marketplaces
- Maps skills to SE activities across the development lifecycle
- Analyzes evolution/versioning and evaluation mechanisms

## Key Findings

1. **Unit of reuse is shifting** — Beyond code/libraries/services, **SE activities themselves** are packaged as skills
2. **Uneven lifecycle coverage** — Construction/coding-heavy; high-context stages (requirements analysis, design) underrepresented
3. **Versioning immaturity** — ClawHub analysis: majority single-version (969 observed); max 72 versions; version count ≠ maturity
4. **Evaluation gap** — Marketplace evaluation practices lag true reuse effectiveness in real SE contexts
5. **Five-component model** — Metadata · Instructions · Resources · optional executables · supplementary docs

## Context Elements

- **Activity→skill taxonomy** — Reuse map for SDLC stages
- **Coverage gaps** as research/product targets (requirements/design skills hard)
- **Version semantics weakness** — no reliable maturity signal from version counts
- **Marketplace structure** — composition/reuse patterns at ecosystem level

## Relation to Skill Bundle Patterns

- SE-domain counterpart to [[registry-to-repository-skill-maintenance]]
- Versioning evidence supports [[swe-skills-bench-utility-benchmark]] version-mismatch findings
- Complements [[assc-skill-supply-chains-skillbom]] (dependency/version manifests)
- Aligns with [[skill-os-skills-as-apps]] (global management, no maturity indicators)
- Complements engineering mega-bundles: [[addyosmani-engineering-skills]], [[superpowers-engineering-discipline-skills]], [[vercel-labs-agent-skills]]

## Key Insight

Skill markets are already turning **SE activities into distributeable artefacts**, but coverage is skewed toward construction and versioning/evaluation infrastructure is weak. Closing the gap means better skill structure, recommendation, and encapsulation of high-context lifecycle stages — not only more code-generation skills.

[[backlinks]]
