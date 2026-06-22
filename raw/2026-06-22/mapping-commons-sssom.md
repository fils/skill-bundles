# mapping-commons/sssom — Simple Standard for Sharing Ontology Mappings (context element exemplar)

**Source**: https://github.com/mapping-commons/sssom/ (and https://mapping-commons.github.io/sssom/)
**Date ingested**: 2026-06-22
**Signal rating**: 9/10 — Canonical example of a formal context element (ontology mapping standard) that can be bundled with agent skills.

## Key Ideas
- TSV-based standard for ontology term mappings with rich metadata (30+ elements).
- Required: subject_id, predicate_id, object_id, mapping_justification, labels.
- Supports provenance, curation rules, license, creator.
- Translation to OWL; used in bioinformatics (OBO Foundry).
- Active 2026 updates (derived_from slot, pronunciation docs).

## Quotes & Excerpts
- "A comprehensive set of standard metadata elements to describe mappings."
- "curation_rule: A curation rule is a (potentially) complex condition executed by an agent..."

## Composition Notes
- Perfect for bundling with agent skills that do ontology work, data integration, or semantic reasoning.
- Provides vocabulary + rules (mapping_justification, curation_rule) + provenance metadata.

## Reproducibility
High — BSD license, examples/, specification, LinkML project.