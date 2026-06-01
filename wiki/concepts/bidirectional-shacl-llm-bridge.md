# Bidirectional SHACL ↔ LLM Bridge

**Date Added:** 2026-06-01 (Iteration 13)
**Confidence:** 8/10

## Definition

A **bidirectional SHACL ↔ LLM bridge** is a bundle that uses LLMs to translate between natural-language requirements and SHACL shapes in both directions:

- **Forward direction:** Natural-language requirements → SHACL shapes (validation rules in Turtle)
- **Reverse direction:** Existing SHACL shapes → natural-language explanations

The catalog now has examples of both directions, which together form a complete bridge.

## Forward Direction: text2shacl

[[text2shacl-multi-agent-shacl]] (added Iteration 13) demonstrates forward generation:

- Input: HTML/PDF technical requirements (RINF Application Guide) + OWL ontology
- Pipeline: 4 stages — preprocessing → RAG indexing → SHACL generation (LangGraph multi-agent) → post-processing/merging
- Output: SHACL shapes in Turtle, validated and cleaned, optionally merged with baseline (Astrea)
- Evaluation: 5 LLMs compared empirically, gold standard for comparison

The merge step implements explicit conflict-resolution policy:
- `priority-llm` — favors LLM-generated shapes when sources conflict
- `restrictive` — keeps only constraints that all sources agree on

## Reverse Direction: xpSHACL

[[xpshacl-explainable-shacl]] (already in catalog from Iteration 8) demonstrates reverse explanation:

- Input: SHACL shapes + RDF data
- Output: Natural-language explanations of why validation passes/fails
- Method: Logic-based + LLM-based hybrid explanation

## Why The Bridge Matters

Together, the two directions enable a **closed-loop workflow**:

```
Natural-language requirements
        ↓ (forward: text2shacl)
SHACL shapes
        ↓ (apply to data)
Validation results
        ↓ (reverse: xpSHACL)
Natural-language explanation
        ↓ (back to requirements authors for review)
Natural-language requirements (refined)
```

This is the kind of closed loop that makes SHACL accessible to non-RDF-experts — a long-standing usability barrier for SHACL adoption.

## Composition Notes

- **Multi-agent architecture:** The forward direction uses LangGraph's multi-agent pattern, the reverse uses logic-based + LLM hybrid — different patterns, same goal.
- **Ontology grounding:** Both directions are *ontology-grounded* — the SHACL shapes use ontology terms, not free-text predicates. This grounds the entire bridge in formal semantics.
- **Gold standard requirement:** Forward direction needs a manually curated gold standard for evaluation. Reverse direction needs user studies to validate explanation quality.

## Cross-References in the Catalog

- [[shacl-1-2-spec]] — The spec both directions target
- [[shacl-data-quality-69-metrics]] — Shape-quality dimensions the forward direction can optimize for
- [[xpshacl-explainable-shacl]] — The reverse direction
- [[dspy-agent-skills-bundle]] — LLM-as-judge pattern useful for evaluating forward generation quality
- [[sc25-autonomous-science-workflows]] — Closed-loop autonomous pattern this resembles

## Open Questions

1. **Round-trip consistency:** If you generate shapes from text (forward) then explain the same shapes back to text (reverse), do you get the original text? (Probably not exactly, but should be close.)
2. **Co-evolution:** As the underlying ontology evolves, how do generated shapes stay in sync? (Active research area.)
3. **Partial shapes:** Forward generation often produces *partial* shapes — a constraint for some properties but not all. The reverse direction should be able to explain "this shape doesn't constrain property X" — does it?

## Related Concepts
- [[validator-explanation-pattern]] — The reverse direction
- [[sssom-mapping-as-context]] — Mapping as a parallel bridge pattern
- [[skill-bundle-patterns]] — Foundation patterns
