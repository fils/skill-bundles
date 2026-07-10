# Scientific Agent Skills (K-Dense-AI/scientific-agent-skills)

**Source:** https://github.com/K-Dense-AI/scientific-agent-skills  
**Stars:** ~30.6k (2026-07-10)  
**Version:** 2.53.0 · **Skills:** 148 · MIT  
**Standard:** agentskills.io compatible  
**Signal rating:** 9/10 (strongest science-domain skill bundle after ClawBio; security scan CI + 100+ databases)

## Summary

Domain skill library that turns any Agent Skills–compatible agent into an "AI Scientist." Covers biology, chemistry, medicine, drug discovery, materials, geospatial, clinical ML, lab automation, and scientific communication. Used by claimed 160,000+ scientists; sponsors Agent Skills '26 workshop.

## Bundle composition

- **148 skills** with SKILL.md + examples + references
- **100+ scientific databases** via unified database-lookup skill (PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov, etc.) + BioServices, BioPython, gget
- **70+ optimized Python package skills** (RDKit, Scanpy, OpenMM, scikit-learn, …)
- **9 scientific platform integrations** (Benchling, DNAnexus, LatchBio, OMERO, Protocols.io, Ginkgo Cloud Lab, LabArchives, Opentrons, Open Notebook)
- **Security Scan** GitHub Action workflow (badge + SECURITY.md)
- **scan_skills.py / scan_pr_skills.py** — PR/skill security scanning scripts
- Companion: K-Dense BYOK desktop co-scientist

## Domain categories (taxonomy as context)

Bioinformatics, Cheminformatics, Proteomics, Clinical Research, Healthcare AI, Medical Imaging, ML/AI, Materials, Physics/Astronomy, Engineering/Simulation, Data Viz, Geospatial, Lab Automation, Scientific Communication, Multi-omics, Protein Engineering, Agent Platforms, Research Methodology

## Context elements

| Element | Present? | Notes |
|---------|----------|-------|
| Skills | Yes | 148 |
| Domain taxonomy | Yes | Multi-category science taxonomy |
| Database/ontology proxies | Yes | UniProt/ChEMBL/PubChem etc. as living controlled data sources |
| Security scanning | Yes | CI security-scan.yml + PR scanners |
| agentskills.io standard | Yes | Explicit badge + install paths |
| SHACL / SSSOM | Not primary | Science DBs are semantic layer proxies |
| Reproducibility artifacts | Partial | Examples + package pinning culture |

## Comparison to ClawBio

- ClawBio: bioinformatics-native (Galaxy tools, Corpasome, high validation pass rate)
- K-Dense: broader "AI Scientist" stack across many science domains + explicit multi-platform Agent Skills packaging
- Both reinforce **domain specialization + formal data sources** as high-density bundle pattern

## Composition notes

Pattern: **domain mega-bundle = skills + curated DBs + package skills + security CI + standard compliance**. High bundle density without SHACL/SSSOM by substituting scientific databases and package docs as context elements.
