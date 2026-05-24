# Open Ontologies: Tool-Augmented Ontology Engineering with Stable Matching Alignment

**Source:** https://arxiv.org/html/2605.09184v1
**Author:** Fabio Rovai (The Tesseract Academy, London)
**Date Accessed:** 2026-05-23

## Executive Summary

Open Ontologies is a Rust-based, open-source system designed to bridge the gap between LLMs and formal ontology engineering. It integrates LLM-driven construction with formal OWL reasoning and alignment via the Model Context Protocol (MCP).

### Primary Findings

- **Stable Matching is King:** In ontology alignment, the *matching strategy* (1-to-1 assignment) is more critical than the *similarity function* (signal weights).
- **Structure > Raw Data:** LLMs perform significantly better when accessing ontologies through structured tools (SPARQL/MCP) than when reading raw OWL files. In fact, reading raw syntax can *decrease* LLM performance compared to using no file at all.

## Core System Architecture

The system is a single Rust binary (~17,400 LOC) with no JVM or Python dependencies, targeting LLM-orchestrated workflows.

- **Core Engine:** Uses **Oxigraph** for in-memory SPARQL 1.1.
- **Reasoner:** Native Rust implementation featuring:
  - OWL-RL forward-chaining for triple materialization.
  - Partial SHIQ tableaux for consistency checking.
- **Lifecycle Management:** Adopts an "Infrastructure-as-Code" approach (Plan, Enforce, Apply, Monitor, Drift) with an append-only lineage trail.
- **Interface:** Exposes all tools via **MCP**, allowing LLMs to interact with the ontology symbolically rather than textually.

## Ontology Alignment & Stable Matching

The alignment module computes similarity based on six signals (labels, properties, parents, instances, restrictions, and neighborhood).

### The "Stable Matching" Breakthrough

The study found that applying **stable 1-to-1 matching** (sorting candidates by confidence and retaining only the top-scoring unique pairs) is the dominant factor in quality.

> "Ablation across five weight configurations shows that signal weights are irrelevant when stable matching is applied (F1 varies by less than 0.004), while removing stable matching drops F1 to 0.728."

### OAEI Anatomy Track Results

| System | Precision (P) | Recall (R) | F1 Score |
| :--- | :--- | :--- | :--- |
| AML | 0.950 | **0.922** | **0.936** |
| **Open Ontologies** | **0.963** | 0.733 | 0.832 |

*Note: Open Ontologies achieved the highest precision of any reported system, though recall was lower due to a conservative label penalty.*

## Tool-Augmented Interaction (The "Structure" Effect)

The research evaluated how LLMs (Claude 4) interact with ontologies using the **OntoAxiom** benchmark.

### Key Comparison

| Condition | Input Modality | F1 Score |
| :--- | :--- | :--- |
| **B** | LLM, no tools (Name lists only) | 0.431 |
| **D** | LLM + Raw OWL File (Turtle syntax) | **0.323** |
| **C** | LLM + MCP Tools (SPARQL access) | **0.717** |

### Insight: Why Raw Files Hurt Performance

Condition D (Raw File) performed **25% worse** than Condition B (No File).

- **Parsing Noise:** LLMs struggle with Turtle syntax ambiguity (confusing property IRIs with class IRIs).
- **Hallucination vs. Extraction:** The LLM's internal training knowledge is often more accurate than its ability to parse complex, multi-line axiom blocks in raw text.
- **The Solution:** Structured tools provide a "qualitatively different mode of access" that eliminates parsing errors.

## Performance & Benchmarks

- **Reasoning Speed:** OWL-RL forward chaining is significantly faster than HermiT (e.g., 15ms vs 24,490ms for 50,000 axioms), though it is incomplete for OWL-DL.
- **Construction Efficiency:** The system built a 91-class "Pizza" ontology (based on the Manchester tutorial) in **under 5 minutes** with 96% class coverage.
- **Conference Track:** Achieved F1 = 0.438. Precision remained high (0.693), but recall suffered due to heterogeneous modeling styles in conference ontologies.

## Key Excerpts & Formulas

### Similarity Scoring Formula

score(c_s, c_t) = Σ(w_i × s_i(c_s, c_t)) for i=1..6

Signals: labels, properties, parents, instances, restrictions, neighborhood.

### On Tool Access

> "The improvement from B to C (+66% F1) combines two factors: richer input and structured tool access... structured tools provide +122% over raw file access. MCP tools are not merely 'richer input'; they provide a qualitatively different access modality."

### On Alignment Strategy

> "For ontologies with limited structural metadata, the assignment constraint [stable matching] matters more than the similarity function."

## Limitations & Future Work

- **Recall Gap:** Needs domain-specific background knowledge (like UMLS) to improve recall on matches with low label similarity.
- **Evaluation:** Results are measured against reference alignments but have not yet been independently evaluated by external benchmarks.
