# Skill Bundles: A Living Catalog

**Primary Publication** — Last major update: 2026-06-01 (Iteration 13)

## TL;DR

Skill bundles are reusable packages that combine agent skills with formal context artifacts (validation, mapping, rules, vocabularies, taxonomies, and ontologies).

## Documented Examples (45 Total)

### Research & Workflow
- NORA — Autonomous research agent with orchestrated skills
- Agentic Engineering Workflow Skills — Multi-skill workflow patterns
- NemoClaw — Secure agent sandboxing and policy management (23 skills)
- **Superpowers** — Engineering discipline as skills: Iron Laws, Red Flags, methodology cycle (14 skills)
- **NORA Paper** — Harness-engineered autonomous research agent (21 skills + 9 sub-agents, arXiv 2605.02092)
- **ai4curation/curation-skills** (NEW Iteration 13) — Chris Mungall's ontology/biocuration bundle (7 skills: OAK, ROBOT, DOSDP, OBO editing). Production users: Mondo, Cell Ontology, Uberon, EFO

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
- **text2shacl** (NEW Iteration 13) — Multi-agent LangGraph pipeline for SHACL generation from text; 5 LLMs evaluated, two merge strategies (priority-llm, restrictive)
- **skill-validator CLI** (NEW Iteration 13) — Go-based lifecycle-mapped validator: 7 commands, 13 platform pre-commit hooks, LLM-as-judge, contamination detection (151 stars)
- **Validate Skill GitHub Action** (NEW Iteration 13) — Lightweight CI/CD layer: structural spec compliance, JSON outputs, 4 inputs/2 outputs

### Governance & Verification
- NVIDIA Verified Agent Skills — OpenSSF signing, SkillSpector scanning, SKILLCARD.yaml
- NVIDIA Skills Repository — 140+ skills across 13 product areas with governance pipeline
- **PurpleBox Security Analysis** — Supply chain risk: 12% infection rate, 6-vector attack taxonomy, CVE-2026-25253
- GitHub CLI Skill Management — Supply chain integrity (immutability, pinning, provenance)
- **Mondoo Security Analysis** — 14 attack patterns, 25%+ vulnerable skills, ClawHavoc campaign
- **agentskill.sh / ags** (NEW Iteration 13) — Registry-level security scoring: 12-category threat taxonomy, 100k+ skills scanned, 0-100 security score, content-SHA versioning, 10-dim quality scoring

### Security Governance Frameworks
- **OWASP Agentic Skills Top 10 (AST10)** — First dedicated security risk framework: 10-class vulnerability taxonomy, Lethal Trifecta, Universal Skill Format
- **Agentic Trust Framework (CSA)** — Zero Trust governance: 4-level maturity model (Intern→Principal), 5 promotion gates, compliance mapping
- **arXiv Agent Skills Survey** — First comprehensive academic survey: 26.1% vulnerability rate, 4-axis analysis (architecture, acquisition, deployment, security)

### Platform Skill Systems
- **Anthropic Official Skills** — Canonical reference: spec, templates, production document skills (140k stars)
- **Ylang Labs Agent Skills** — Definitive overview: "recipes vs kitchen" metaphor, 3-level progressive disclosure
- **Claude API Integration** — Container parameter, version pinning, 8 skills/request, 30MB limit
- OpenAI Codex Agent Skills — Progressive disclosure, MCP dependency declarations
- VS Code Copilot Agent Skills — Cross-platform agentskills.io implementation

### Enterprise Platform Implementations
- **Microsoft Agent Framework Skills** — Enterprise platform: 3 implementation types (file/inline/class), script approval, DI support, multi-source composition
- **Spring AI Generic Agent Skills** — Java ecosystem: LLM-agnostic, 3-core-tool architecture, Claude Code compatible

### Distribution & Marketplaces
- **Chris Ayers Plugin Ecosystem** — 3-layer model (Skills → Plugins → Marketplaces); cross-tool compatibility matrix proving SKILL.md universal portability
- **Agensi Marketplace Landscape** — 8-marketplace comparison: skills.sh (2k), SkillsMP (800k), Agensi (200+, 8-point security scan); consolidation trends
- **agentskill.sh** (NEW Iteration 13) — 100k+ skill registry with 12-category threat scanning, content-SHA versioning, auto-rate feedback loop

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

## State of Research (After Iteration 13)

Iteration 13 adds **5 new examples** that establish the **three-layer validation stack** and complete the **bidirectional SHACL↔LLM bridge**.

### Three-Layer Validation Stack (NEW)
The skill ecosystem is converging on a three-layer architecture:
- **Layer 1 (Pre-commit):** [[skill-validator-cli]] — deep quality + contamination + LLM-as-judge
- **Layer 2 (CI/CD):** [[validate-skill-github-action]] — structural spec compliance
- **Layer 3 (Registry):** [[agentskill-sh-ags-security-scoring]] — 12-category security scanning

This mirrors the **software supply chain** three-layer pattern (linters → CI scanners → registry audits) and is approximately 2-3 years behind the npm/PyPI ecosystem in maturity. See [[three-layer-validation-stack]] for the full analysis.

### Bidirectional SHACL ↔ LLM Bridge (NEW)
With [[text2shacl-multi-agent-shacl]] (forward generation) added, the catalog now has a complete bridge:
- **Forward:** text2shacl turns natural-language requirements into SHACL shapes via multi-agent LangGraph pipeline with RAG
- **Reverse:** [[xpshacl-explainable-shacl]] turns SHACL shapes into natural-language explanations

Together they form a closed loop: requirements → shapes → validation → explanation → refined requirements. See [[bidirectional-shacl-llm-bridge]].

### Ontology-Grounded Domain Skill Bundle (NEW)
[[ai4curation-curation-skills]] is the cleanest example in the catalog of skills operating on formal artifacts (OBO ontologies). 7 skills provide a natural-language interface to a sophisticated ontology toolkit. Production users: Mondo, Cell Ontology, Uberon, EFO. Companion `ai-blame` tool provides line-level attribution for AI-assisted edits.

## Emerging Patterns

1. **Skills + Declarative Context Files** (ubiquitous across all platforms)
2. **Skills + Ontology** (strong — 9 examples, +ai4curation)
3. **Skills + Validation + Explainability** (strong — 8 examples, +text2shacl forward direction)
4. **Skills + Guardrails via Interceptor** (SHACL + Cypher + Shadow testing)
5. **Skills + Supply Chain Provenance** (immutability, pinning, content-addressed detection)
6. **Skills + Taxonomy at Scale** (754 skills mapped to MITRE/NIST)
7. **Skills + Mapping/Alignment** (mature — 4 examples: SSSOM lifecycle complete)
8. **Skills + Rules/Governance** (strong — 5 examples)
9. **Skills + SHACL Validation** (strong — 7 examples, +text2shacl generation)
10. **Skills + MCP Dependencies** (emerging — 3 examples)
11. **Skills + Constraint Rules** (new — Iron Laws, Red Flags, SHACL, crypto signing, authorization)
12. **Skills + Dependency Graphs** (new — DAG-based composition, PageRank ranking)
13. **Skills + Benchmarking** (new — paired evaluation, delta metrics)
14. **Orchestrator Pattern** (new — a skill that activates and sequences other skills)
15. **Implicit Bundle Discovery** (new — bundles discovered by grouping related skills across taxonomy catalogs)
16. **Attack → Defense Mapping** (new — PurpleBox attack vectors map directly to defense bundles)
17. **Agent Context as Documentation** (new — CLAUDE.md + CONTEXT.md + ADR as living context)
18. **Skill Security Governance Stack** (new — 4-layer model: AST10 risk taxonomy → ATF maturity model → empirical data → technical controls; see [[skill-security-governance]])
19. **SKILL.md as Universal Portable Unit** (new — confirmed identical operation across 5 major tools)
20. **Enterprise Platform Convergence** (new — Microsoft + Spring AI both shipping production-grade implementations)
21. **Three-Layer Validation Stack** (NEW — pre-commit → CI/CD → registry; see [[three-layer-validation-stack]])
22. **Bidirectional SHACL↔LLM Bridge** (NEW — text → shapes → explanation → text; see [[bidirectional-shacl-llm-bridge]])
23. **Registry-Level Security Scanning** (NEW — 12-category threat taxonomy + content-SHA provenance + auto-rate feedback)
24. **Domain-Specific Ontology Skills** (NEW — OBO Foundry skills for ontology/biocuration work; OAK, ROBOT, DOSDP)

## Context Element Coverage

| Context Element | Examples | Status |
|-----------------|----------|--------|
| SHACL Validation | 7 | **Strong** (+1: text2shacl forward generation) |
| Constraint Rules | 6 | **Strong** |
| Rules / Authorization | 5 | **Strong** |
| Ontology / Taxonomy | 9 | **Strong** (+1: ai4curation OBO tooling) |
| Governance / Verification | 8 | **Strong** |
| Security Framework / Certification | 4 | **Growing** (+1: ags 12-category threat model) |
| Platform Implementation | 5 | **Growing** |
| Plugin / Distribution | 3 | **Emerging** (+1: agentskill.sh marketplace) |
| Academic Survey | 1 | **Emerging** |
| Universal Skill Format | 1 | **Emerging** |
| Dependency Graphs | 2 | **Stable** |
| YAML Configuration | 8+ | Ubiquitous |
| MCP Dependencies | 3 | Emerging |
| SSSOM Mapping | 4 | **Mature** |
| Supply Chain / Provenance | 4 | **Growing** (+1: content-SHA versioning) |
| Benchmarking | 1 | Emerging |
| LLM-as-Judge Quality Scoring | 1 | **NEW** (skill-validator) |
| Multi-Agent SHACL Generation | 1 | **NEW** (text2shacl) |
| Content-Addressed Versioning | 1 | **NEW** (agentskill.sh) |
| Pre-commit Multi-Platform Hooks | 1 | **NEW** (skill-validator, 13 platforms) |

See also:
- [[skill-security-governance]] — Complete governance stack synthesis
- [[three-layer-validation-stack]] — The validation architecture pattern
- [[bidirectional-shacl-llm-bridge]] — The SHACL↔LLM closed loop
- [[skill-bundle-patterns]] — Foundation patterns
- [[sssom-mapping-as-context]] — Mappings as context
- [[constraint-rules-as-context]] — Rules as context
- [[validator-explanation-pattern]] — Validation + explanation pattern
