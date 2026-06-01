# citiususc/text2shacl — Multi-Agent LangGraph Pipeline for SHACL Generation

**Source:** https://github.com/citiususc/text2shacl
**Date Added:** 2026-06-01 (Iteration 13)
**License:** Apache-2.0 | **Stars:** 8 | **Forks:** 0 | **Latest Release:** v1.0 (May 8, 2026)
**Topics:** `shacl` · `knowledge-graphs` · `llm`
**Language:** HTML 96.3% / Python 3.1% / Other 0.6%
**Bundle Type:** Multi-Agent SHACL Generation · RAG · LLM Evaluation
**Confidence:** 9/10

## Name & Origin

`text2shacl` is an **ontology-driven multi-agent system for extracting SHACL shapes from text**, focused on the ERA (European Union Agency for Railways) ontology and RINF Application Guide. It uses a LangGraph multi-agent pipeline with RAG over the ontology + technical docs to generate SHACL constraints in Turtle format.

This is the **inverse** of the typical SHACL workflow: instead of **validating** RDF against existing shapes, it **generates** shapes from natural-language requirements docs.

## Skills Included (4-Stage Pipeline)

1. **HTML preprocessing** — RINF Application Guide cleaned, split into semantic chunks. Text + tables + images extracted.
2. **RAG indexing** — Text/table chunks summarized by LLM; images described by vision model. Summaries stored in **Chroma** (vector index). Original chunks in **Redis** (document store).
3. **SHACL generation** — For each ontology property, a **LangGraph multi-agent workflow** gathers evidence from ontology, optional Astrea baseline, RAG context. Outputs SHACL shapes in Turtle.
4. **Post-processing & merging** — Shapes validated, cleaned, optionally merged with Astrea baseline using `priority-llm` or `restrictive` strategies.

## Context Elements

- **Input Ontologies:** ERA OWL ontology (`ontology.ttl`)
- **Baseline Shapes:** Astrea (`astrea-shapes.ttl`) — published reference shapes
- **Gold Standard:** `era-shapes.ttl` — manually curated shapes
- **RAG Stores:** Chroma (vector index for summaries) + Redis (document store for original chunks)
- **Evaluation Framework:** 5 LLMs × 2 input versions × 2 merge strategies

## Models Evaluated

- Gemma 3 12B
- GPT-OSS 120B
- Llama 3.3 70B
- Mixtral 8x7B
- Qwen3-Next 80B-A3B

## How Context Elements Support Skills

This is a **bidirectional SHACL↔LLM bridge**:
- **Forward:** Natural-language requirements → SHACL shapes
- **Reverse:** Existing SHACL shapes → natural-language explanations (covered by [[xpshacl-explainable-shacl]])

It also demonstrates a **multi-agent composition pattern** where the agents operate over different knowledge sources (ontology vs. docs vs. RAG summaries) — a composition that resembles the SC '25 paper's pipeline→hierarchical pattern ([[sc25-autonomous-science-workflows]]).

The two merge strategies (`priority-llm` favors LLM-generated shapes when conflict; `restrictive` keeps only constraints that all sources agree on) are an example of **explicit conflict-resolution policy** — a pattern we have not seen elsewhere in the catalog.

## Composition Notes

- **Multi-source grounding:** The agents use ontology, RAG over technical docs, and a published baseline (Astrea) — three independent evidence sources.
- **Multi-model evaluation:** Same pipeline runs across 5 different LLMs to compare quality, enabling empirical model selection for this task.
- **Post-processing pipeline:** SHACL shapes are *validated, cleaned, and merged* before being declared usable — exactly the kind of post-validation pattern that [[graphguard-os-guardrails]] uses for runtime guardrails.
- **Reproducible evaluation:** Results in `results.csv`, bar+line charts and heatmaps comparing models, gold standard for comparison.

## Reproducibility

**Very High.** Apache-2.0 license, conda environment file, full source code, public evaluation results (results.csv, figures), gold standard published, two input guide versions compared.

## Bundle Links
- [[xpshacl-explainable-shacl]] — Reverse direction (SHACL → natural language)
- [[shacl-1-2-spec]] — The spec these shapes conform to
- [[shacl-data-quality-69-metrics]] — Shape-quality dimensions
- [[graphguard-os-guardrails]] — Policy-as-code pattern reference
- [[dspy-agent-skills-bundle]] — Another multi-agent + validation bundle
- [[sc25-autonomous-science-workflows]] — Autonomous science framework this resembles
- [[onto-llm-mapping]] — LLM-based ontology mapping (related LLM-for-ontologies work)
