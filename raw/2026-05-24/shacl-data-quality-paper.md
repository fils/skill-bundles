# "Is SHACL Suitable for Data Quality Assessment?" — Research Paper

**Source:** https://arxiv.org/abs/2507.22305
**Date Accessed:** 2026-05-24
**Authors:** Carolina Cortés, Lisa Ehrlinger, Lorena Etcheverry, Felix Naumann
**Venue:** Proc. WOP-HAIBRIDGE 2025 (co-located with ISWC 2025)

---

## Key Ideas
- Maps 69 data quality metrics to SHACL shapes
- Prototype automatically instantiates SHACL shapes and computes quality measures
- Evaluates SHACL across intrinsic, contextual, representational dimensions
- Strengths: Excellent for intrinsic dimensions (syntactic validity, consistency)
- Challenges: Contextual dimensions (relevancy, timeliness) may require external metadata
- Computational overhead for massive KGs with complex shapes

## Bundle Context Elements
- **SHACL Validation:** 69 metrics operationalized as SHACL shapes
- **Data Quality Framework:** Zaveri et al. dimensions mapped to constraints
- **Prototype Code:** Open-source SHACL shape generator

## Relevance to Skill Bundles
This paper provides a comprehensive set of SHACL shapes for data quality assessment. An agent skill that uses these shapes could automatically validate knowledge graph quality as part of its workflow — a clear skill bundle pattern (validation + data quality framework + shape library).

## Confidence: 9/10
