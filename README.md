# Skill Bundles Research

## About

This is a repo with a focus on the creation of an Agent-managed Personal Knowledge Graph for **Skill Bundles**.

**Research Focus:** Collections of skills combined with supporting context elements including validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

The goal is to discover, document, and analyze real-world examples of reusable, composable skill bundles that pair agent capabilities with formal semantic and validation layers.

## Components

### raw/

Source documents ingested daily by the agent. Organized by date (`raw/YYYY-MM-DD/`).

### wiki/

The compiled, LLM-maintained publication. Primary entry point: `wiki/index.md`.

### resources/

A directory for JSON-LD documents using schema.org types (Dataset, DigitalObject, etc.) to record information about resources indexed from sources.

## Approaches

All changes are done in a branch of master that is then submitted as a pull request.
No changes directly to master are done.

## Key References

- [Agent Skills](https://agentskills.io/)
- [NORA (Night Owl Research Agent)](https://github.com/GRIND-Lab-Core/night_owl_research_agent)
- [Agents at Conferences](https://github.com/cecat/agents-at-conferences)


