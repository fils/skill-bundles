# A Simple Standard for Sharing Ontology Mappings (SSSOM) — Dev

**Source:** https://mapping-commons.github.io/sssom/dev/  
**Ingested:** 2026-06-25

## Key Ideas
- SSSOM provides TSV-based representation for ontology term mappings with rich metadata (38+ elements).
- Supports curation rules executed by agents; `curation_rule` and `curation_rule_text` fields explicitly mention agent involvement.
- Standard translation to OWL; enhances consistency, quality, discoverability for data integration.
- Maintained by mapping-commons GitHub org; multiple implementations (sssom-py, sssom-js).

## Relevance to Skill Bundles
Core mapping standard that can be bundled with agent skills for ontology alignment. Explicit "agent" metadata fields make it a natural fit for agentic skill bundles involving semantic mapping + validation (SHACL/SSSOM combinations).