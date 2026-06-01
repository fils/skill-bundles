# citiususc/text2shacl — Multi-Agent LangGraph Pipeline for SHACL Generation

**Extracted:** 2026-06-01
**Source:** https://github.com/citiususc/text2shacl
**License:** Apache-2.0 | **Stars:** 8 | **Forks:** 0 | **Latest Release:** v1.0 (May 8, 2026)
**Topics:** `shacl` · `knowledge-graphs` · `llm`
**Language:** HTML 96.3% / Python 3.1% / Other 0.6%

## What It Is

`text2shacl` is an **ontology-driven multi-agent system for extracting SHACL shapes from text**, focused on the ERA (European Union Agency for Railways) ontology and RINF Application Guide. It uses a LangGraph multi-agent pipeline with RAG over the ontology + technical docs to generate SHACL constraints in Turtle format.

This is the inverse of the typical SHACL workflow: instead of **validating** RDF against existing shapes, it **generates** shapes from natural-language requirements docs.

## Pipeline (4 Stages)

1. **HTML preprocessing** — RINF Application Guide cleaned, split into semantic chunks. Text + tables + images extracted.
2. **RAG indexing** — Text/table chunks summarized by LLM; images described by vision model. Summaries stored in **Chroma** (vector index). Original chunks in **Redis** (document store).
3. **SHACL generation** — For each ontology property, a **LangGraph multi-agent workflow** gathers evidence from: ontology, optional Astrea baseline, RAG context. Outputs SHACL shapes in Turtle.
4. **Post-processing & merging** — Shapes validated, cleaned, optionally merged with Astrea baseline using `priority-llm` or `restrictive` strategies.

## Models Evaluated

- Gemma 3 12B
- GPT-OSS 120B
- Llama 3.3 70B
- Mixtral 8x7B
- Qwen3-Next 80B-A3B

## Inputs

- RINF Application Guide **v3.1.0** (native HTML) and **v1.6.1** (PDF→HTML)
- ERA OWL ontology (`ontology.ttl`)
- Astrea baseline shapes (`astrea-shapes.ttl`)
- Gold standard (`era-shapes.ttl`)

## Outputs

- Generated SHACL shapes in Turtle
- Merged shapes via two strategies (`priority-llm`, `restrictive`)
- Bar+line charts and heatmaps comparing model performance
- Results CSV

## Why It Matters for the Catalog

This is a **bidirectional SHACL↔LLM bridge**:
- **Forward:** Natural-language requirements → SHACL shapes
- **Reverse:** Existing SHACL shapes → natural-language explanations (covered by `xpshacl` in catalog)

It also demonstrates a **multi-agent composition pattern** where the agents operate over different knowledge sources (ontology vs. docs vs. RAG summaries) — a composition that resembles the SC '25 paper's pipeline→hierarchical pattern.

## Cross-references in Catalog

- `xpshacl-explainable-shacl` — the reverse direction (SHACL → natural language)
- `shacl-1-2-spec` — the spec these shapes conform to
- `shacl-data-quality-69-metrics` — the shape-quality dimensions
- `dspy-agent-skills-bundle` — another multi-agent + validation bundle
- SC '25 paper — autonomous science workflows (cataloged as `sc25-autonomous-science-workflows`)

## Bundle Density

- Skills: 4-pipeline (preprocess / RAG / generate / merge)
- Context elements: SHACL shapes (output), OWL ontology (input), Astrea baseline, gold standard, RAG context
- Composition: LangGraph multi-agent + RAG + Chroma + Redis + multiple LLMs
- Evaluation: 5 LLMs × 2 input versions × 2 merge strategies

## Reproducibility Assessment

**Very High.** Apache-2.0 license, conda environment file, full source code, public evaluation results (results.csv, figures), gold standard published.

## Gap It Fills in the Wiki

We've had **validation** (xpSHACL, SHACL DQ) and **shape consumption** (Mondoo, GraphGuard OS), but no **shape generation** from natural language. This fills the input-side gap and makes the SHACL story complete in the catalog.
