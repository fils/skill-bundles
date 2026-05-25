# OxO2 — SSSOM-Compliant Ontology Mapping Service

**Source:** https://github.com/EBISPOT/oxo2/blob/dev/CLAUDE.md
**Date:** 2026-05-25
**Signal:** 9/10

## Key Finding
OxO2 is a production SSSOM-compliant ontology mapping service from EMBL-EBI's EBISPOT team. It includes a `CLAUDE.md` file — demonstrating the **agent skills pattern applied to AI assistant context** for a real bioinformatics service.

## Architecture
- **Backend:** Java 25, Maven, Spring Boot 3.4.1
- **Frontend:** React 19, TypeScript, Vite, Tailwind CSS
- **Data Store:** Apache Solr 9.9.0
- **Inference Engine:** Nemo v0.9.1 (rules + explanations)
- **Pipeline:** Nextflow for data loading

## SSSOM Compliance
OxO2 downloads SSSOM mappings, converts to JSON, and serves them via REST API. It is a direct implementation of the SSSOM standard for ontology mapping — connecting to the OLS (Ontology Lookup Service) and O×O (Ontology Xref Ontology).

## Agent Context Pattern
The project uses `CLAUDE.md` at root + `CONTEXT.md` per module + `docs/adr/` for architectural decisions. This is a **formalized context artifact pattern** — agent instructions as living documentation.

## Issue Management
GitHub Issues via `gh` CLI with triage labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`.
