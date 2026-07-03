# SSSOM - Simple Standard for Sharing Ontology Mappings

**Source:** https://mapping-commons.github.io/sssom/dev/ and GitHub mapping-commons/sssom
**Date ingested:** 2026-07-03
**Type:** Standard + tooling

## Key Ideas
- SSSOM: TSV-based representation for ontology term mappings with rich metadata (up to 38 fields).
- Supports curation_rule, curation_rule_text, creator (agent or person), license, etc.
- Python library (sssom) for parsing, CLI operations, pandas integration.
- Explicitly models "curation rules" executed by agents.

## Quotes / Highlights
- "A curation rule is a (potentially) complex condition executed by an agent that led to the establishment of a mapping."
- Mapping sets associated with metadata including license and description.

## Relevance to Skill Bundles
SSSOM provides the mapping + curation context layer for skill bundles. Skills can be mapped across ontologies/taxonomies using SSSOM; curation rules can be agent-driven. Strong "skills + SSSOM" pattern example.

**Tags:** SSSOM, ontology-mapping, curation, agent-driven, TSV

**Metadata update note:** 5 new sources ingested 2026-07-03.