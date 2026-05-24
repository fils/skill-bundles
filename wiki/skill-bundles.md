# Skill Bundles: A Living Catalog

**Primary Publication** — Last major update: 2026-05-23 (Iteration 6)

## TL;DR

Skill bundles are reusable packages that combine agent skills with formal context artifacts (validation, mapping, rules, vocabularies, taxonomies, and ontologies).

## Documented Examples (14 Total)

### Research & Workflow
- NORA — Autonomous research agent with orchestrated skills
- Agentic Engineering Workflow Skills — Multi-skill workflow patterns
- NemoClaw — Secure agent sandboxing and policy management (23 skills)

### Ontology & Knowledge
- Ontologizer — OpenClaw ontology skill
- OpenClaw PKB Skill — Personal knowledge base
- RDF Ontologies — SHACL + SPARQL integration
- Open Ontologies MCP — Full ontology lifecycle (43 tools, SHACL validation, 32 stored ontologies)

### Validation & Rules
- Veto — Authorization Kernel
- Tool-Use Firewall
- Schimatos — SHACL knowledge graph validation
- Agent Audit — Security scanning

### Governance & Verification (NEW)
- **NVIDIA Verified Agent Skills** — OpenSSF signing, SkillSpector scanning, SKILLCARD.yaml
- **NVIDIA Skills Repository** — 140+ skills across 13 product areas with governance pipeline

### Platform Skill Systems
- **OpenAI Codex Agent Skills** — Progressive disclosure, MCP dependency declarations
- **VS Code Copilot Agent Skills** — Cross-platform agentskills.io implementation
- Anthropic Skills — Plugin marketplace, multi-language API guides

### Specification
- Agent Skills Specification — The open standard (agentskills.io)

## State of Research (Iteration 6)

After six iterations, **Governance/Verification** and **Ontology** layers now show the strongest adoption. **Rules & Authorization** remain well-covered. **SHACL validation** has grown from 1 to 3 examples. Formal semantic mapping (**SSSOM**) remains the only category with zero examples.

See the dedicated state document: [[skill-bundles-research-state]]

## Emerging Patterns

1. **Skills + Declarative Context Files** (most common across all platforms)
2. **Skills + Ontology** (growing — 5 examples)
3. **Skills + Rules/Governance** (emerging strongly — 4 examples)
4. **Skills + SHACL Validation** (still rare but present — 3 examples)
5. **Skills + Governance Pipeline** (NVIDIA model: signing, scanning, metadata)
6. **Skills + MCP Dependencies** (emerging — external tool server declarations)

## Context Element Coverage

| Context Element | Examples | Status |
| Rules / Authorization | 4 | Strong |
| Ontology / Taxonomy | 5 | Strong |
| Governance / Verification | 3 | Strong |
| YAML Configuration | 8+ | Ubiquitous |
| SHACL Validation | 3 | Emerging |
| MCP Dependencies | 2 | Emerging |
| SSSOM Mapping | 0 | None |
