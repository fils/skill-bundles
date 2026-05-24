# Validator + Explanation Bundle Pattern

**Date:** 2026-05-24 (Discovered Iteration 8)

## Summary

The Validator + Explanation pattern addresses a fundamental problem: **validation reports alone are not actionable**. Technical validation output (e.g., SHACL violation reports) is too terse for humans to understand and act on. The pattern couples a validation engine with an explanation layer that converts failures into natural language guidance.

## Core Components

1. **Validation Engine** — Deterministic constraint checking (e.g., SHACL/pyshacl)
2. **Explanation Generator** — LLM-based natural language synthesizer
3. **Context Retriever** — RAG system that fetches relevant ontology fragments, shape documentation, similar cases
4. **Violation Cache** — Signature-based storage (MD5 hash) of previously explained violations

## Examples

- **[[xpshacl-explainable-shacl]]** — Full implementation: pyshacl + justification trees + RAG + Violation KG. 99.48% cache hit rate across 868 vocabularies.
- **[[shacl-data-quality-69-metrics]]** — 69 data quality metrics as SHACL shapes; prototype computes numerical quality scores from violations.

## Why This Pattern Works

The key insight from xpSHACL is that **validation errors are highly repetitive**: only 12 unique violation signatures needed new LLM explanations for 145,910 total violations. A signature-based cache makes explainable validation practical — initial run costs ~65 seconds, subsequent runs ~20 seconds (vs. 4 seconds for raw validation).

## Applicability to Skill Bundles

Any skill that produces or consumes structured data can benefit from this pattern:
1. Skill generates or modifies RDF/knowledge graph data
2. SHACL validation runs against quality/structure shapes
3. Violations are explained in natural language with actionable suggestions
4. Repeated violations hit the cache, minimizing LLM API costs

## Related Patterns

- **[[skill-bundle-patterns]]** — SHACL + Cypher Rules + Shadow Testing (GraphGuard OS)
- [[sssom-mapping-protocol]] — SSSOM standard can be paired with explainable validation for multi-ontology scenarios
