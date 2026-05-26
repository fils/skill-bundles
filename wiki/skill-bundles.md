# Skill Bundles: A Living Catalog

**Primary Publication** — Last major update: 2026-05-26 (Iteration 11)

## TL;DR

Skill bundles are reusable packages that combine agent skills with formal context artifacts (validation, mapping, rules, vocabularies, taxonomies, and ontologies).

## Documented Examples (40 Total)

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

### Security Governance Frameworks (NEW)
- **OWASP Agentic Skills Top 10 (AST10)** — First dedicated security risk framework: 10-class vulnerability taxonomy, Lethal Trifecta, Universal Skill Format
- **Agentic Trust Framework (CSA)** — Zero Trust governance: 4-level maturity model (Intern→Principal), 5 promotion gates, compliance mapping
- **arXiv Agent Skills Survey** — First comprehensive academic survey: 26.1% vulnerability rate, 4-axis analysis (architecture, acquisition, deployment, security)

### Platform Skill Systems
- **Anthropic Official Skills** — Canonical reference: spec, templates, production document skills (140k stars)
- **Ylang Labs Agent Skills** — Definitive overview: "recipes vs kitchen" metaphor, 3-level progressive disclosure
- **Claude API Integration** — Container parameter, version pinning, 8 skills/request, 30MB limit
- OpenAI Codex Agent Skills — Progressive disclosure, MCP dependency declarations
- VS Code Copilot Agent Skills — Cross-platform agentskills.io implementation

### Enterprise Platform Implementations (NEW)
- **Microsoft Agent Framework Skills** — Enterprise platform: 3 implementation types (file/inline/class), script approval, DI support, multi-source composition
- **Spring AI Generic Agent Skills** — Java ecosystem: LLM-agnostic, 3-core-tool architecture, Claude Code compatible

### Distribution & Marketplaces (NEW)
- **Chris Ayers Plugin Ecosystem** — 3-layer model (Skills → Plugins → Marketplaces); cross-tool compatibility matrix proving SKILL.md universal portability
- **Agensi Marketplace Landscape** — 8-marketplace comparison: skills.sh (2k), SkillsMP (800k), Agensi (200+, 8-point security scan); consolidation trends

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

## State of Research (After Iteration 11)

Iteration 11 marks a **qualitative shift** in the catalog: the addition of two formal security governance frameworks ([[owasp-agentic-skills-top-10]], [[agentic-trust-framework-csa]]) and one comprehensive academic survey ([[arxiv-agent-skills-survey]]) moves us from *empirical observation* of security issues to *formalized governance* with risk taxonomies, maturity models, and compliance mappings.

The catalog grows from 34 to **40 documented examples**. Three new categories emerge:

1. **Security Governance Frameworks** — OWASP AST10 provides a 10-class vulnerability taxonomy with Universal Skill Format; ATF provides a 4-level Zero Trust maturity model; the arXiv survey validates both with a 26.1% vulnerability rate finding
2. **Enterprise Platform Implementations** — [[microsoft-agent-framework-skills]] (3 implementation types, DI, script approval) and [[spring-ai-agent-skills]] (LLM-agnostic Java integration) signal enterprise readiness
3. **Distribution & Marketplaces** — [[chris-ayers-plugin-ecosystem]] (3-layer model) and the Agensi marketplace landscape document the emerging distribution infrastructure

**Key convergence finding:** The [[arxiv-agent-skills-survey]]'s composition patterns (single → pipeline → hierarchical → mesh → swarm) mirror the [[sc25-autonomous-science-workflows|SC '25 paper]]'s framework, confirming cross-domain convergence between agent skills research and scientific workflow evolution.

**Cross-tool portability confirmation:** Chris Ayers' compatibility matrix proves SKILL.md works identically across 5 major tools (Copilot CLI, VS Code, Claude Code, Codex CLI, Gemini CLI) — the strongest evidence yet for skills as the universal portable unit.

**Security governance maturation:** Iteration 10 had scattered security advice (Mondoo patterns, PurpleBox taxonomy). Iteration 11 has two formal frameworks and one academic survey — a step-change from empiricism to formalization.

## Emerging Patterns

1. **Skills + Declarative Context Files** (ubiquitous across all platforms)
2. **Skills + Ontology** (growing — 8 examples)
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
18. **Skill Security Governance Stack** (new — 4-layer model: AST10 risk taxonomy → ATF maturity model → empirical data → technical controls; see [[skill-security-governance]])
19. **SKILL.md as Universal Portable Unit** (new — confirmed identical operation across 5 major tools)
20. **Enterprise Platform Convergence** (new — Microsoft + Spring AI both shipping production-grade implementations)

## Context Element Coverage

| Context Element | Examples | Status |
|-----------------|----------|--------|
| SHACL Validation | 7 | **Strong** |
| Constraint Rules | 6 | **Strong** |
| Rules / Authorization | 5 | **Strong** |
| Ontology / Taxonomy | 8 | **Strong** |
| Governance / Verification | 8 | **Strong** (+3: OWASP AST10, ATF, arXiv survey) |
| Security Framework / Certification | 3 | **Growing** (NEW — OWASP AST10, ATF, arXiv) |
| Platform Implementation | 5 | **Growing** (+2: Microsoft, Spring AI) |
| Plugin / Distribution | 2 | **Emerging** (NEW — Chris Ayers Plugins, Agensi) |
| Academic Survey | 1 | **Emerging** (NEW — arXiv 2602.12430) |
| Universal Skill Format | 1 | **Emerging** (NEW — OWASP proposed) |
| Dependency Graphs | 2 | **Stable** |
| YAML Configuration | 8+ | Ubiquitous |
| MCP Dependencies | 3 | Emerging |
| SSSOM Mapping | 4 | **Mature** |
| Supply Chain / Provenance | 3 | Growing |
| Benchmarking | 1 | Emerging |

See also: [[skill-security-governance]] for the complete governance stack synthesis.
