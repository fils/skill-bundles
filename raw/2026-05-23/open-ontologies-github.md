# Open Ontologies - GitHub Repository

**Source:** https://github.com/fabio-rovai/open-ontologies
**Author:** Fabio Rovai
**Date Accessed:** 2026-05-23
**License:** MIT

## Overview

Open Ontologies is a high-performance, Rust-based Model Context Protocol (MCP) server and desktop Studio designed for AI-native ontology engineering. It enables LLMs like Claude to build, validate, query, and reason over RDF/OWL ontologies without requiring a JVM or Protégé.

## Key Features & Capabilities

- **43 Specialized Tools:** Exposes `onto_*` tools for the full ontology lifecycle (build, diff, lint, version, align, and reason).
- **In-Memory Performance:** Powered by the **Oxigraph** triple store (pure Rust) and a native **OWL2-DL tableaux reasoner**.
- **Terraform-style Management:** Includes `plan`, `apply`, `lock`, and `drift` tools for knowledge graph governance.
- **Marketplace:** Instant access to **32 standard ontologies** (Schema.org, BFO, FOAF, SKOS, etc.).
- **IES Support:** Full support for the **Information Exchange Standard (IES)** 4D/BORO patterns used in Digital Twin programs.
- **Clinical Intelligence:** Includes crosswalks for ICD-10, SNOMED, and MeSH.
- **Neuro-Symbolic Alignment:** Hybrid alignment engine using structural signals and LLM adjudication.

## Quick Start (MCP / CLI)

### Installation

```bash
# macOS (Apple Silicon)
curl -LO https://github.com/fabio-rovai/open-ontologies/releases/latest/download/open-ontologies-aarch64-apple-darwin
chmod +x open-ontologies-aarch64-apple-darwin && mv open-ontologies-aarch64-apple-darwin /usr/local/bin/open-ontologies

# Docker
docker pull ghcr.io/fabio-rovai/open-ontologies:latest
docker run -i ghcr.io/fabio-rovai/open-ontologies:latest serve
```

### Connecting to Claude Desktop

```json
{
  "mcpServers": {
    "open-ontologies": {
      "command": "/path/to/open-ontologies",
      "args": ["serve"]
    }
  }
}
```

## Studio (Desktop App)

The Studio is a native Tauri-based application that provides a visual environment for the engine.

- **Virtualized Tree:** Handles 1,500+ classes with zero lag by only rendering visible rows.
- **AI Agent Chat:** Features `/build` (13-step deep pipeline) and `/sketch` (3-step prototype) commands.
- **Property Inspector:** Protégé-style inline triple editor for real-time graph updates.
- **Lineage Viewer:** Full audit trail of every action taken by the AI or user.

## Benchmarks & Performance

### Reasoning Speed (vs. HermiT)

| Axioms | Open Ontologies | HermiT | Speedup |
| :--- | :--- | :--- | :--- |
| 10,000 | 14ms | 1,200ms | **86×** |
| 50,000 | 15ms | 24,490ms | **1,633×** |

### Build Modes: `/sketch` vs `/build`

| Metric | `/sketch` (~2 min) | `/build` (~15 min) |
| :--- | :--- | :--- |
| **Classes** | 95 | **1,433** |
| **Object Properties** | 15 | **218** |
| **Hierarchy Depth** | 5 | **11** |

### Axiom Identification (OntoAxiom)

- **Bare Claude Opus:** 0.431 F1
- **MCP Extraction:** **0.717 F1** (+264% vs paper best)

## Architecture

The system is split into a **Rust Engine** and a **Studio Frontend**:

- **Engine:** Uses **Oxigraph** for RDF, **SQLite** for lineage/versioning, and **tract-onnx** for semantic embeddings.
- **Studio:** Built with **React 19** and **Tauri 2**. It communicates with the engine via a sessionless REST API for reads and MCP for agent-driven writes.

### Tool Categories

- **Core:** `query`, `stats`, `diff`, `lint`, `convert`.
- **Lifecycle:** `plan`, `apply`, `drift`, `monitor`, `lineage`.
- **Data:** `ingest` (CSV/JSON to RDF), `shacl` (validation), `reason`.
- **Advanced:** `align` (cross-ontology matching), `embed` (semantic search).

## Technical Stack

- **Language:** Rust (Edition 2024), TypeScript, Python.
- **Triple Store:** Oxigraph 0.4.
- **Database:** SQLite (rusqlite).
- **Frontend:** React 19, Vite 7, Tailwind CSS 4, Zustand 5.
- **License:** MIT.
