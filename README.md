# Skill Bundles Research

## About

This is a repo with a focus on the creation of an Agent-managed Personal Knowledge Graph for **Skill Bundles**.

**Research Focus:** Collections of skills combined with supporting context elements including validation (SHACL), mapping (SSSOM), rules, vocabularies, taxonomies, and ontologies.

The goal is to discover, document, and analyze real-world examples of reusable, composable skill bundles that pair agent capabilities with formal semantic and validation layers.

## Components

### raw/

Source documents ingested daily by the agent. Organized by date (`raw/YYYY-MM-DD/`). Outside the OKF bundle (ingestion staging).

### wiki/ — OKF Knowledge Bundle

The compiled, LLM-maintained publication. **Primary entry point:** [`wiki/index.md`](wiki/index.md).

`wiki/` is an [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) Knowledge Bundle:

- Every concept document has YAML frontmatter with a required `type` field
- Cross-links use **relative markdown links** (OKF §5.2) so they work on GitHub and in OKF consumers
- Reserved files: `index.md` (progressive disclosure), `log.md` (update history)
- Concept ID = path under `wiki/` without `.md` (e.g. `examples/skill0-skill-internalization`)
- Local format summary for agents: [`wiki/concepts/okf-knowledge-bundle.md`](wiki/concepts/okf-knowledge-bundle.md)
- Daily agent contract: [`PLAN.md`](PLAN.md) (Karpathy-style research *loop*; OKF *document format*)

### resources/

A directory for JSON-LD documents using schema.org types (Dataset, DigitalObject, etc.) to record information about resources indexed from sources.

### scripts/

Automation for OKF conformance and maintenance. See [`scripts/README.md`](scripts/README.md).

```bash
python3 scripts/okf-lint.py          # OKF §9 conformance
python3 scripts/convert-to-okf.py    # one-shot / re-migration helper
```

## Approaches

All changes are done in a branch of master that is then submitted as a pull request.
No changes directly to master are done.

## Key References

- [Open Knowledge Format (OKF) SPEC](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [Agent Skills](https://agentskills.io/)
- [NORA (Night Owl Research Agent)](https://github.com/GRIND-Lab-Core/night_owl_research_agent)
- [Agents at Conferences](https://github.com/cecat/agents-at-conferences)
