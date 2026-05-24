# Complex Q&A — Skill Bundles Wiki

**Date:** 2026-05-24 (Iteration 8)

---

## Q1: Which bundles combine skills with SHACL validation AND SSSOM-style mappings?

**Answer:** The closest example is [[open-ontologies-paper]] (Open Ontologies by Rovai), which combines:
- SHACL validation (built-in `shacl` tool for RDF validation)
- Ontology alignment via stable matching (six-signal similarity scoring)
- While not using SSSOM TSV format directly, the alignment mechanism operates at the same semantic level — mapping terms between ontologies with confidence scores and provenance

The newly added [[xpshacl-explainable-shacl]] focuses on validation explainability but doesn't incorporate mapping. True SHACL+SSSOM bundles remain a gap — the pieces exist (SHACL validation + SSSOM standard) but no single example combines them.

## Q2: What ontology patterns appear most frequently alongside agent skills?

**Answer:** From 20 documented examples:
1. **Ontology/Taxonomy** appears in 8 examples (40%) — the most common formal context element
2. **RDF/SHACL integration** appears in 6 examples — growing strongly
3. **OWL reasoning** appears in 3 examples (Open Ontologies)
4. **Clinical crosswalks** (ICD-10, SNOMED, MeSH) appear in 2 examples

The dominant pattern is: skills use an ontology to provide structured domain knowledge, then validate their outputs against SHACL shapes for that ontology.

## Q3: How do successful bundles handle rule integration?

**Answer:** Three distinct patterns emerged:
1. **Authorization kernel** ([[veto-agent-authorization]], [[tool-use-firewall]]) — binary allow/block decisions on tool calls
2. **Graph-based policy enforcement** ([[graphguard-os-guardrails]]) — SHACL shapes (structural) + Cypher policies (behavioral) validated against a knowledge graph
3. **Framework taxonomy** ([[claude-skills-ecosystem-1116]]) — skills organized under MITRE/NIST frameworks, inheriting rule semantics from the taxonomy

GraphGuard's approach (SHACL + Cypher + Shadow Policy Manager) is the most sophisticated, enabling safe rule evolution without production risk.

## Q4: What gaps remain in the catalog?

**Answer:**
- **Rules engines** beyond authorization: no examples of skills using Drools, N3 rules, or SWRL
- **SSSOM in practice:** specification documented but no agent skill that reads/writes SSSOM files
- **Skill composition:** how do multiple skills in a bundle coordinate? No examples of skill-to-skill protocols
- **Performance metrics:** few examples benchmark skill execution time or context usage
- **Skill versioning:** `gh skill` introduces pinning, but no systematic versioning schema across bundles
