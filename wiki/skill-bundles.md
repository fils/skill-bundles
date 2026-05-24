# Skill Bundles: A Living Catalog

**Primary Publication** — Last major update: 2026-05-24 (Iteration 8)

## TL;DR

Skill bundles are reusable packages that combine agent skills with formal context artifacts (validation, mapping, rules, vocabularies, taxonomies, and ontologies).

## Documented Examples (20 Total)

### Research & Workflow
- NORA — Autonomous research agent with orchestrated skills
- Agentic Engineering Workflow Skills — Multi-skill workflow patterns
- NemoClaw — Secure agent sandboxing and policy management (23 skills)

### Ontology & Knowledge
- Ontologizer — OpenClaw ontology skill
- OpenClaw PKB Skill — Personal knowledge base
- RDF Ontologies — SHACL + SPARQL integration
- Open Ontologies MCP — Full ontology lifecycle (43 tools, SHACL validation, 32 stored ontologies)
- **Open Ontologies Paper — Stable matching alignment algorithm for ontology mapping (OAEI F1=0.832, P=0.963)**
- **Open Ontologies GitHub — Production Rust MCP server with onto_align tool, marketplace of 32 standard ontologies**
- **Going Meta: Agent Skills for Ontologies** — Video series on skills for ontology work

### Validation & Rules
- Veto — Authorization Kernel
- Tool-Use Firewall
- Schimatos — SHACL knowledge graph validation
- Agent Audit — Security scanning
- **GraphGuard OS** — SHACL + Cypher guardrails + Shadow Policy Manager for coordinated agents
- **xpSHACL** — Explainable SHACL validation with RAG + Violation Knowledge Graph (99.48% cache hit)
- **SHACL Data Quality** — 69 data quality metrics mapped to SHACL shapes

### Governance & Verification
- **NVIDIA Verified Agent Skills** — OpenSSF signing, SkillSpector scanning, SKILLCARD.yaml
- **NVIDIA Skills Repository** — 140+ skills across 13 product areas with governance pipeline
- **GitHub CLI Skill Management** — Supply chain integrity (immutability, pinning, provenance)

### Platform Skill Systems
- **OpenAI Codex Agent Skills** — Progressive disclosure, MCP dependency declarations
- **VS Code Copilot Agent Skills** — Cross-platform agentskills.io implementation
- Anthropic Skills — Plugin marketplace, multi-language API guides

### Security Taxonomy
- **Claude Skills Ecosystem (1,116)** — 754 cybersecurity skills mapped to MITRE/NIST frameworks

### Specification
- Agent Skills Specification — The open standard (agentskills.io)
- **SSSOM Mapping Protocol** — Simple Standard for Sharing Ontological Mappings
- **SHACL 1.2 Core** — W3C Shapes Constraint Language specification

## State of Research (After Iteration 8)

Iteration 8 significantly strengthened SHACL validation coverage (3 → 6 examples) and expanded into supply chain/provenance as a new context element category. The [[xpshacl-explainable-shacl]] paper demonstrates that SHACL validation paired with RAG explanation and a Violation KG cache (99.48% hit rate) makes validation actionable. [[graphguard-os-guardrails]] introduces the "interceptor + SHACL + Cypher" pattern for deterministic agent guardrails.

SSSOM mapping coverage grew to 2 with the addition of the [[sssom-mapping-protocol]] standard specification. Combined with [[open-ontologies-paper]] (stable matching alignment), we now have both the mapping algorithm and the mapping format.

The [[claude-skills-ecosystem-1116]] survey revealed 754 cybersecurity skills systematically mapped to MITRE/NIST frameworks — the largest taxonomy-driven bundle found in this research.

`gh skill` CLI introduces package-manager semantics for skill distribution: install, update, pin, publish with supply chain integrity (content-addressed detection, version pinning, portable provenance).

## Emerging Patterns

1. **Skills + Declarative Context Files** (ubiquitous across all platforms)
2. **Skills + Ontology** (growing — 7 examples)
3. **Skills + Validation + Explainability** (new: SHACL + RAG + Violation KG)
4. **Skills + Guardrails via Interceptor** (new: SHACL + Cypher + Shadow testing)
5. **Skills + Supply Chain Provenance** (new: immutability, pinning, content-addressed detection)
6. **Skills + Taxonomy at Scale** (new: 754 skills mapped to MITRE/NIST)
7. **Skills + Mapping/Alignment** (emerging — 2 examples)
8. **Skills + Rules/Governance** (strong — 5 examples)
9. **Skills + SHACL Validation** (strong — 6 examples)
10. **Skills + MCP Dependencies** (emerging — 3 examples)

## Context Element Coverage

| Context Element | Examples | Status |
| SHACL Validation | 6 | **Strong** |
| Rules / Authorization | 5 | **Strong** |
| Ontology / Taxonomy | 7 | **Strong** |
| Governance / Verification | 4 | **Strong** |
| YAML Configuration | 8+ | Ubiquitous |
| MCP Dependencies | 3 | Emerging |
| SSSOM Mapping | 2 | Emerging |
| Supply Chain / Provenance | 2 | Emerging |

See the dedicated state document: [[skill-bundles-research-state]]
