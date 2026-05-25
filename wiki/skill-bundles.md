# Skill Bundles: A Living Catalog

**Primary Publication** — Last major update: 2026-05-25 (Iteration 10)

## TL;DR

Skill bundles are reusable packages that combine agent skills with formal context artifacts (validation, mapping, rules, vocabularies, taxonomies, and ontologies).

## Documented Examples (34 Total)

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
- **OxO2 Mapping Service** — SSSOM-compliant service with CLAUDE.md agent context (EBISPOT)
- **Onto-LLM-Mapping** — SSSOM mapping generation via LLM+RAG pipeline

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
- **PurpleBox Security Analysis** — Supply chain risk: 12% infection rate, 6-vector attack taxonomy, CVE-2026-25253
- GitHub CLI Skill Management — Supply chain integrity (immutability, pinning, provenance)
- **Mondoo Security Analysis** — 14 attack patterns, 25%+ vulnerable skills, ClawHavoc campaign

### Platform Skill Systems
- **Anthropic Official Skills** — Canonical reference: spec, templates, production document skills (140k stars)
- **Ylang Labs Agent Skills** — Definitive overview: "recipes vs kitchen" metaphor, 3-level progressive disclosure
- **Claude API Integration** — Container parameter, version pinning, 8 skills/request, 30MB limit
- OpenAI Codex Agent Skills — Progressive disclosure, MCP dependency declarations
- VS Code Copilot Agent Skills — Cross-platform agentskills.io implementation

### Security Taxonomy
- Claude Skills Ecosystem (1,116) — 754 cybersecurity skills mapped to MITRE/NIST frameworks
- **Awesome OpenClaw Skills** — 179 CLI utilities with implicit security/memory/development bundles

### Framework-Specific
- **DSPy Agent Skills Bundle** — Three-repo bundle: 80 validation tests, AST checking, GEPA benchmarks, orchestration skill
- **DSPy Agent Skills v0.2.3** — Updated bundle for DSPy 3.2.x, +19.53pp RAG improvement, dual-platform install
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

## State of Research (After Iteration 10)

Iteration 10 expanded the catalog from 28 to 34 examples and completed the **SSSOM lifecycle** — we now have 4 examples covering define (spec), generate (Onto-LLM-Mapping), serve (OxO2), and align (Open Ontologies). The SSSOM category jumps from 2 to 4 examples, making it a mature context element type.

The **PurpleBox Security analysis** reveals that within 7 weeks of the Agent Skills standard release, 12% of marketplace skills were malicious — a 6-vector attack taxonomy that maps directly to defense patterns already in our catalog (signing → NVIDIA, scanning → Mondoo, sandboxing → GraphGuard, authorization → Veto). This creates a complete "attack → defense" matrix across our examples.

[[oxo2-sssom-mapping-service]] from EMBL-EBI is significant because it combines SSSOM compliance with a `CLAUDE.md` agent context file — the first production system where ontology mapping and AI assistant documentation coexist as formal context artifacts.

[[onto-llm-mapping]] demonstrates a multi-stage LLM pipeline (expand → vectorize → retrieve → rank → SSSOM) that shows how LLMs themselves can generate the formal mappings that skills use for cross-ontology reasoning.

[[awesome-openclaw-skills-catalog]] reveals that skill bundles can be **implicitly discovered** by grouping skills across a taxonomy catalog — 4+ related security skills form a security bundle even without explicit declaration. This is a new composition pattern.

[[dspy-agent-skills-v023]] updates our DSPy entry to v0.2.3 with DSPy 3.2.x validation and measured GEPA optimization improvements (+19.53pp on RAG tasks), providing empirical evidence of bundle effectiveness.

Ylang Labs' article provides the definitive reference explanation of the Agent Skills format, with the "recipes vs kitchen" metaphor (Skills = recipes, MCP = kitchen) that clarifies the composition relationship between procedural knowledge and tool access.

The [[ylang-labs-agent-skills-overview]] article documents the three-level progressive disclosure pattern that explains the architecture of multiple bundles in our catalog.

**SSSOM mapping coverage is now at 4** (spec, generator, server, aligner) — a complete lifecycle. The security taxonomy category is at 5 examples (Mondoo, PurpleBox, NVIDIA Verified, Awesome OpenClaw, Claude Ecosystem).

## Emerging Patterns

1. **Skills + Declarative Context Files** (ubiquitous across all platforms)
2. **Skills + Ontology** (growing — 9 examples)
3. **Skills + Validation + Explainability** (SHACL + RAG + Violation KG, AST validation)
4. **Skills + Guardrails via Interceptor** (SHACL + Cypher + Shadow testing)
5. **Skills + Supply Chain Provenance** (immutability, pinning, content-addressed detection)
6. **Skills + Taxonomy at Scale** (754 skills mapped to MITRE/NIST)
7. **Skills + Mapping/Alignment** (mature — 4 examples: SSSOM lifecycle complete)
8. **Skills + Rules/Governance** (strong — 5 examples)
9. **Skills + SHACL Validation** (strong — 7 examples)
10. **Skills + MCP Dependencies** (emerging — 3 examples)
11. **Skills + Constraint Rules** (new — Iron Laws, Red Flags, SHACL, crypto signing, authorization)
12. **Skills + Dependency Graphs** (new — DAG-based composition, PageRank ranking)
13. **Skills + Benchmarking** (new — paired evaluation, delta metrics)
14. **Orchestrator Pattern** (new — a skill that activates and sequences other skills)
15. **Implicit Bundle Discovery** (new — bundles discovered by grouping related skills across taxonomy catalogs)
16. **Attack → Defense Mapping** (new — PurpleBox attack vectors map directly to defense bundles)
17. **Agent Context as Documentation** (new — CLAUDE.md + CONTEXT.md + ADR as living context)
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
