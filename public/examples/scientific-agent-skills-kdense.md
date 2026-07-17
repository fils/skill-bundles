---
type: Skill Bundle Example
title: Scientific Agent Skills (K-Dense)
description: 148 ready-to-use scientific/research skills across bioinformatics, cheminformatics, proteomics, clinical research, medical imaging, materials, geospatial, lab automation, scientific communication, multi-omics, protein...
resource: https://github.com/K-Dense-AI/scientific-agent-skills
timestamp: '2026-07-10T00:00:00Z'
date: 2026-07-10
sources:
- raw/2026-07-10/scientific-agent-skills-kdense.md
- https://github.com/K-Dense-AI/scientific-agent-skills
skills_included: 148
context_elements:
- domain-taxonomy
- scientific-databases
- package-skills
- security-ci
- agentskills-io-standard
composition_notes: Domain mega-bundle combining skills with 100+ DBs, package docs, platform integrations, and security scanning CI.
reproducibility: High — MIT, versioned releases (v2.53.0), scan scripts, agentskills.io install paths
---

# Scientific Agent Skills (K-Dense)

**Origin:** [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) (~30.6k stars, 2026-07-10)

## Skills included

148 ready-to-use scientific/research skills across bioinformatics, cheminformatics, proteomics, clinical research, medical imaging, materials, geospatial, lab automation, scientific communication, multi-omics, protein engineering, and research methodology.

## Context elements

- **Domain taxonomy** — multi-category science skill taxonomy
- **Scientific databases** — unified lookup over PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov, etc. (100+); BioServices / BioPython / gget packages
- **Package skills** — 70+ curated Python package skills (RDKit, Scanpy, OpenMM, …)
- **Platform integrations** — Benchling, DNAnexus, LatchBio, OMERO, Ginkgo Cloud Lab, Opentrons, etc.
- **Security CI** — `security-scan.yml`, `scan_skills.py`, `scan_pr_skills.py`, SECURITY.md
- **Standard compliance** — agentskills.io badge and multi-host install (Cursor, Claude Code, Codex, Antigravity, Pi)

## How context supports skills

Scientific databases and package documentation act as a **living semantic layer**: skills are not free-floating prompts but grounded in curated tools and data sources. Security scanning enforces supply-chain hygiene at PR and repo level (see [three layer validation stack](../concepts/three-layer-validation-stack.md)).

## Composition notes / reusability

- Parallel to [clawbio bioinformatics skills](clawbio-bioinformatics-skills.md) but broader "AI Scientist" scope
- Sponsors [agentskills workshop 2026](../papers/agentskills-workshop-2026.md) (Agent Skills '26) — research community alignment
- Companion product: K-Dense BYOK desktop co-scientist

## Reproducibility assessment

**High.** Versioned releases, MIT, explicit standard, CI scanners, documented install paths.

## Related

- [clawbio bioinformatics skills](clawbio-bioinformatics-skills.md)
- [three layer validation stack](../concepts/three-layer-validation-stack.md)
- [skill bundle patterns](../concepts/skill-bundle-patterns.md)
- [agentskills workshop 2026](../papers/agentskills-workshop-2026.md)

