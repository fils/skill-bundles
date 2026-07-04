# SSSOM — Simple Standard for Sharing Ontology Mappings (agent curation context)

**Source:** https://mapping-commons.github.io/sssom/dev/ + GitHub mapping-commons/sssom
**Date ingested:** 2026-07-04
**Type:** Mapping standard + tooling

**Key content:**
- TSV-based format for ontology term mappings with rich metadata (38 fields).
- Includes creator_id, mapping_date, curation_rule, confidence, match types.
- curation_rule can be complex conditions executed by an agent.
- Python library (sssom-py) and CLI for working with mapping sets.
- Used for data integration, interoperability, and agent-curated knowledge graphs.

**Context elements present:**
- Formal mapping metadata vocabulary
- Curation rules (agent-executable)
- LinkML schema, JSON-LD/RDF export options

**Relevance to skill bundles:** Provides the mapping/SSSOM layer that frequently accompanies skill bundles when they involve ontology or taxonomy alignment.