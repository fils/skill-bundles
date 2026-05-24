# xpSHACL: Explainable SHACL Validation using RAG and LLMs

**Source:** https://arxiv.org/abs/2507.22305 (arXiv:2507.08432)
**Date Accessed:** 2026-05-24
**Authors:** Gustavo Correa Publio (University of Leipzig), José Emilio Labra Gayo (University of Oviedo)

---

## Key Ideas
- xpSHACL combines rule-based justification trees, RAG, and LLMs to generate human-readable explanations for SHACL validation violations
- Creates a persistent Violation KG that caches "violation signatures" (MD5 hashes of constraint type, property path, violation type)
- 99.48% cache hit rate on 868 vocabularies from Linked Open Vocabularies (LOV) repository
- Addresses the interpretability gap: raw SHACL output is terse and technical; xpSHACL adds natural language explanations

## Bundle Context Elements
- **SHACL Validation:** Core validation layer via pyshacl
- **Knowledge Graph:** Violation KG for caching explanations
- **RAG:** Context retrieval (ontology fragments, shape documentation, similar cases, domain rules)
- **Ontology Integration:** SPARQL queries for domain rules linked via custom properties

## Composition Notes
This is a prime example of a skill bundle: SHACL validation + RAG context retrieval + LLM explanation generation, all tied together with a cached Knowledge Graph. The Violation KG functions as a reusable artifact that other skills could consume.

## Quotes
> "The system merges symbolic reasoning (Justification Trees) with neural generation (LLMs)."

## Reproducibility
- High: Built on pyshacl, supports OpenAI/Gemini/Claude/Ollama
- Cache-first design keeps costs low after initial run

## Confidence: 9/10
