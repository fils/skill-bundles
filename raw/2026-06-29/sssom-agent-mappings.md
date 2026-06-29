# SSSOM + Agent / Mapping Skills

**Sources:**
- mapping-commons/sssom (https://github.com/mapping-commons/sssom/)
- SSSOM dev spec (https://mapping-commons.github.io/sssom/dev/)
- PyPI sssom package (latest release 2026-05-23)
- arXiv paper on SSSOM mapping browser (2025)

**Key Ideas:**
- SSSOM = Simple Standard for Sharing Ontological Mappings (TSV + rich metadata).
- Metadata includes creator (can be an agent), curation_rule (condition executed by an agent), mapping_date, confidence, etc.
- Toolkit supports parsing, conversion to OWL, curation workflows.
- Explicitly designed for agent-driven curation and safe exchange of mappings.

**Composition Notes:**
- SSSOM mapping sets can be produced/curated by agents.
- Provides provenance and rules layer that complements skill definitions.

**Relevance to Skill Bundles:** Strong example of mapping/ontology context element (SSSOM) used alongside or to support agent skills.