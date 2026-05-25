# Skill Bundles: A Living Catalog

**Primary Publication** — Last major update: 2026-05-24 (Iteration 8)

## TL;DR

Skill bundles are reusable packages that combine agent skills with formal context artifacts (validation, mapping, rules, vocabularies, taxonomies, and ontologies).

## Documented Examples (28 Total)

### Research & Workflow
- NORA — Autonomous research agent with orchestrated skills
- Agentic Engineering Workflow Skills — Multi-skill workflow patterns
- NemoClaw — Secure agent sandboxing and policy management (23 skills)
- **Superpowers** — Engineering discipline as skills: Iron Laws, Red Flags, methodology cycle (14 skills)
- **NORA Paper** — Harness-engineered autonomous research agent (21 skills + 9 sub-agents, arXiv 2605.02092)

### Ontology & Knowledge
- Ontologizer — OpenClaw ontology skill
- OpenClaw PKB Skill — Personal knowledge base
- RDF Ontologies — SHACL + SPARQL integration
- Open Ontologies MCP — Full ontology lifecycle (43 tools, SHACL validation, 32 stored ontologies)
- Open Ontologies Paper — Stable matching alignment algorithm (OAEI F1=0.832, P=0.963)
- Open Ontologies GitHub — Production Rust MCP server with onto_align tool, 32 standard ontologies
- Going Meta: Agent Skills for Ontologies — Video series on skills for ontology work

### Validation & Rules
- Veto — Authorization Kernel
- Tool-Use Firewall
- Schimatos — SHACL knowledge graph validation
- Agent Audit — Security scanning
- GraphGuard OS — SHACL + Cypher guardrails + Shadow Policy Manager
- xpSHACL — Explainable SHACL validation with RAG + Violation Knowledge Graph (99.48% cache hit)
- SHACL Data Quality — 69 data quality metrics mapped to SHACL shapes
- **NemoClaw Security Scanner** — LLM-assisted vulnerability detection for skill definitions

### Governance & Verification
- NVIDIA Verified Agent Skills — OpenSSF signing, SkillSpector scanning, SKILLCARD.yaml
- NVIDIA Skills Repository — 140+ skills across 13 product areas with governance pipeline
- GitHub CLI Skill Management — Supply chain integrity (immutability, pinning, provenance)
- **Mondoo Security Analysis** — 14 attack patterns, 25%+ vulnerable skills, ClawHavoc campaign

### Platform Skill Systems
- **Anthropic Official Skills** — Canonical reference: spec, templates, production document skills (140k stars)
- **Claude API Integration** — Container parameter, version pinning, 8 skills/request, 30MB limit
- OpenAI Codex Agent Skills — Progressive disclosure, MCP dependency declarations
- VS Code Copilot Agent Skills — Cross-platform agentskills.io implementation

### Security Taxonomy
- Claude Skills Ecosystem (1,116) — 754 cybersecurity skills mapped to MITRE/NIST frameworks

### Framework-Specific
- **DSPy Agent Skills Bundle** — Three-repo bundle: 80 validation tests, AST checking, GEPA benchmarks, orchestration skill
- **Skills+DSPy SDK** — SkillsReActAgent with firejail, meta-tools, YAML config for sandbox

### Specification
- Agent Skills Specification — The open standard (agentskills.io)
- SSSOM Mapping Protocol — Simple Standard for Sharing Ontological Mappings
- SHACL 1.2 Core — W3C Shapes Constraint Language specification

### Dependency & Retrieval
- **Graph of Skills (GoS)** — DAG-based skill composition, PageRank ranking, prerequisite resolution

### Benchmarking & Catalogs
- **SkillsBench** — First agent skills benchmark: +16.2pp avg improvement, Healthcare +51.9pp
- **Awesome Agent Skills Catalogs** — Ecosystem mapping: 1000+ skills, 44k+ marketplace

## State of Research (After Iteration 9)

Iteration 9 expanded the catalog from 20 to 28 examples and introduced three new categories: **Framework-Specific** (DSPy skills), **Dependency & Retrieval** (Graph of Skills), and **Benchmarking** (SkillsBench). The most significant conceptual addition is the **Constraint Rules as Context** pattern — skills that encode prohibitions (Iron Laws, Red Flags, SHACL guardrails, cryptographic signing) alongside procedural instructions.

The **Graph of Skills (GoS)** paper provides the first formal dependency-aware composition model for skill bundles, explaining why patterns like the [[dspy-agent-skills-bundle]]'s orchestrator skill and [[superpowers-engineering-discipline-skills]]'s methodology cycle work. GoS constructs a DAG from SKILL.md dependencies and uses reverse-weighted PageRank for bundle retrieval.

**SkillsBench** provides the first quantitative benchmark for skill effectiveness: +16.2pp average improvement across domains, +51.9pp in healthcare. This enables empirical quality claims for individual bundles.

**Mondoo's security analysis** reveals a critical gap: 25%+ of public skills have vulnerabilities. The 14-pattern attack taxonomy maps directly to needed context elements: scanning (NemoClaw), signing (NVIDIA), verification (Veto), and internal catalogs.

The [[anthropic-official-skills-repo]] (140k stars) is the canonical reference — spec, templates, working production skills. The [[claude-api-skills-integration]] documents the official API contract: container parameter, version pinning, 8-skill limit.

SSSOM mapping coverage remains at 2 (spec + algorithm). The dependency graph category is new at 2 (GoS + GraphGuard OS).

## Emerging Patterns

1. **Skills + Declarative Context Files** (ubiquitous across all platforms)
2. **Skills + Ontology** (growing — 7 examples)
3. **Skills + Validation + Explainability** (SHACL + RAG + Violation KG, AST validation)
4. **Skills + Guardrails via Interceptor** (SHACL + Cypher + Shadow testing)
5. **Skills + Supply Chain Provenance** (immutability, pinning, content-addressed detection)
6. **Skills + Taxonomy at Scale** (754 skills mapped to MITRE/NIST)
7. **Skills + Mapping/Alignment** (emerging — 2 examples)
8. **Skills + Rules/Governance** (strong — 5 examples)
9. **Skills + SHACL Validation** (strong — 7 examples)
10. **Skills + MCP Dependencies** (emerging — 3 examples)
11. **Skills + Constraint Rules** (new — Iron Laws, Red Flags, SHACL, crypto signing, authorization)
12. **Skills + Dependency Graphs** (new — DAG-based composition, PageRank ranking)
13. **Skills + Benchmarking** (new — paired evaluation, delta metrics)
14. **Orchestrator Pattern** (new — a skill that activates and sequences other skills)
## Context Element Coverage

| Context Element | Examples | Status |
|-----------------|----------|--------|
| SHACL Validation | 7 | **Strong** |
| Constraint Rules | 6 | **Strong** (new) |
| Rules / Authorization | 5 | **Strong** |
| Ontology / Taxonomy | 8 | **Strong** |
| Governance / Verification | 5 | **Strong** |
| Dependency Graphs | 2 | **Strong** (new) |
| YAML Configuration | 8+ | Ubiquitous |
| MCP Dependencies | 3 | Emerging |
| SSSOM Mapping | 2 | Emerging |
| Supply Chain / Provenance | 2 | Emerging |
| Benchmarking | 1 | Emerging (new) |

See the dedicated state document: [[skill-bundles-research-state]]
