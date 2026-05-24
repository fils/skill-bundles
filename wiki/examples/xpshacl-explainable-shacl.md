# xpSHACL — Explainable SHACL Validation with RAG and LLMs

**Source:** https://arxiv.org/abs/2507.08432  
**Date Added:** 2026-05-24 (Iteration 8)  
**Authors:** Gustavo Correa Publio (University of Leipzig), José Emilio Labra Gayo (University of Oviedo)  
**Bundle Type:** SHACL Validation + RAG + Violation Knowledge Graph  
**Confidence:** 9/10

## Name & Origin

xpSHACL is an open-source system that solves the "interpretability gap" in RDF data validation. While traditional SHACL engines provide terse, technical reports, xpSHACL combines rule-based justification trees, Retrieval-Augmented Generation (RAG), and LLMs to generate human-readable explanations and actionable correction suggestions.

## Skills Included

- Extended SHACL validation (built on pyshacl)
- Justification tree construction for violations
- Context retrieval via RAG (ontology fragments, shape documentation, similar cases, domain rules)
- Natural language explanation generation (multi-language)
- Violation signature caching for cost efficiency

## Context Elements

- **SHACL Validation:** Core validation via pyshacl, extended to extract granular violation details (focus node, property path, constraint component, actual value)
- **Violation Knowledge Graph:** Persistent cache that stores "violation signatures" (MD5 hashes of constraint type + property path + violation type). 99.48% cache hit rate on 868 Linked Open Vocabularies (LOV) vocabularies.
- **RAG Context Retrieval:** SPARQL queries to retrieve ontology fragments, shape documentation (`rdfs:comment`), similar violation cases, and domain business rules linked via custom properties (`xsh:appliesToProperty`)
- **Justification Trees:** Logic trace connecting SHACL shape definitions → data graph facts → violation inference

## How Context Elements Support Skills

The system demonstrates a sophisticated skill bundle pattern where:
1. **SHACL** provides the validation engine and constraint definitions
2. **Violation KG** acts as a reusable cache (dramatically reducing LLM API costs)
3. **RAG** enriches validation context with domain knowledge
4. **LLM** synthesizes explanations and suggestions

This is a prime example of how validation (SHACL) can be augmented with a knowledge layer (RAG + Violation KG) to produce actionable outputs rather than technical error reports.

## Composition Notes

xpSHACL exemplifies a "validation + explanation" bundle pattern. The key insight is that **validation alone is insufficient** — the Violation KG that caches explanations makes repeated validation runs cost-effective. This caching pattern is generalizable: any skill that performs expensive LLM-based analysis of structured data could benefit from a signature-based cache.

**Performance:** Initial run ~65 seconds (LLM calls + KG population); cached run ~20 seconds; baseline pyshacl ~4 seconds. The caching amortizes the explanation cost over time.

## Reproducibility

High — built on pyshacl, supports OpenAI/Gemini/Claude/Ollama. Open source with published evaluation on 868 vocabularies. The Violation KG caching mechanism is described in detail and could be adapted for other validation contexts.

## Key Insight

> "Only 12 unique signatures required new LLM generation for 145,910 violations."

This demonstrates that in practice, most validation violations fall into a small number of patterns — making signature caching extremely effective.

## Limitations

- Computational overhead vs. raw validation (4× slower for initial run)
- 49.7% parsing success rate on LOV vocabularies (failures due to dead links/parsing errors in source data)
- Future work: integrating high-performance query engines (QLever) to reduce overhead
