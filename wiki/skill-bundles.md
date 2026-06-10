# Skill Bundles: A Living Catalog

**Primary Publication** — Last major update: 2026-06-09 (Iteration 14)

## TL;DR

Skill bundles are reusable packages that combine agent skills with formal context artifacts (validation, mapping, rules, vocabularies, taxonomies, and ontologies).

## Documented Examples (50 Total)

### Research & Workflow
- NORA — Autonomous research agent with orchestrated skills
- Agentic Engineering Workflow Skills — Multi-skill workflow patterns
- NemoClaw — Secure agent sandboxing and policy management (23 skills)
- **Superpowers** — Engineering discipline as skills: Iron Laws, Red Flags, methodology cycle (14 skills)
- **NORA Paper** — Harness-engineered autonomous research agent (21 skills + 9 sub-agents, arXiv 2605.02092)
- **ai4curation/curation-skills** — Chris Mungall's ontology/biocuration bundle (7 skills: OAK, ROBOT, DOSDP, OBO editing). Production users: Mondo, Cell Ontology, Uberon, EFO
- **ClawBio** (NEW Iteration 14) — Bioinformatics-native library: 88 skills (29 production), 8,000+ Galaxy tools, reproducibility bundles, Corpasome reference genome (DOI: 10.5281/zenodo.19297389), 92.3% validation pass rate
- **Addy Osmani Agent Skills** (NEW Iteration 14) — 23 production-grade engineering workflow skills across full SDLC, 3 specialist personas, 7 slash commands, Iron Laws/Red Flags constraint rules, Google engineering culture

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
- **text2shacl** — Multi-agent LangGraph pipeline for SHACL generation from text; 5 LLMs evaluated, two merge strategies (priority-llm, restrictive)
- **skill-validator CLI** — Go-based lifecycle-mapped validator: 7 commands, 13 platform pre-commit hooks, LLM-as-judge, contamination detection (151 stars)
- **Validate Skill GitHub Action** — Lightweight CI/CD layer: structural spec compliance, JSON outputs, 4 inputs/2 outputs

### Governance & Verification
- NVIDIA Verified Agent Skills — OpenSSF signing, SkillSpector scanning, SKILLCARD.yaml
- NVIDIA Skills Repository — 140+ skills across 13 product areas with governance pipeline
- **PurpleBox Security Analysis** — Supply chain risk: 12% infection rate, 6-vector attack taxonomy, CVE-2026-25253
- GitHub CLI Skill Management — Supply chain integrity (immutability, pinning, provenance)
- **Mondoo Security Analysis** — 14 attack patterns, 25%+ vulnerable skills, ClawHavoc campaign
- **agentskill.sh / ags** — Registry-level security scoring: 12-category threat taxonomy, 100k+ skills scanned, 0-100 security score, content-SHA versioning, 10-dim quality scoring

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
- **agentskill.sh** — 100k+ skill registry with 12-category threat scanning, content-SHA versioning, auto-rate feedback loop

### Infrastructure & Participation
- **Agents at Conferences** (NEW Iteration 14) — Infrastructure for AI agent conference participation: 6-component protocol (registration, feeds, communication, moderation, benchmarking, memory), capability schema taxonomy, SciFM26 target: 50 agents

### Security Taxonomy
- Claude Skills Ecosystem (1,116) — 754 cybersecurity skills mapped to MITRE/NIST frameworks
- **Awesome OpenClaw Skills** — 179 CLI utilities with implicit security/memory/development bundles

### Framework-Specific
- **DSPy Agent Skills Bundle** — Three-repo bundle: 34+ validation tests, AST checking, GEPA benchmarks, orchestration skill, exact DSPy 3.2.1 pinning
- **DSPy Agent Skills v0.2.3** — Updated bundle for DSPy 3.2.x, +19.53pp RAG improvement, dual-platform install, committed benchmark artifacts
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

## State of Research (After Iteration 14)

Iteration 14 adds **4 new examples** spanning **domain-specialized bioinformatics**, **production-grade engineering workflows**, **conference participation infrastructure**, and an **updated DSPy optimization bundle** — plus two foundational papers on autonomous scientific workflows.

### Domain-Specialized Bioinformatics Skill Bundle (NEW)
[[clawbio-bioinformatics-skills]] is the richest domain-coherent bundle in the catalog: **88 skills** (29 production) serving genomics/bioinformatics with:
- **Specification layer** as machine-readable contracts preventing hallucination in dosage/genetics
- **Per-execution reproducibility bundles** (commands + environment + checksums) — a new context element type
- **Reference genome asset** (Corpasome, DOI: 10.5281/zenodo.19297389) for deterministic testing
- **Validation leaderboard** (92.3% pass rate) as public governance artifact
- **Multi-modal access**: CLI, Telegram/Discord, web gateway, Claude Code
- **Galaxy Bridge** to 8,000+ external tools — external tool registry mapping

### Process-as-Skill Engineering Discipline Bundle (NEW)
[[addyosmani-engineering-skills]] encodes the **full SDLC as 23 skills** with:
- **Anti-rationalization tables**: Explicit agent failure modes + required corrections
- **Verification gates**: Non-negotiable evidence (tests, logs, runtime data)
- **7 slash commands** mapping 1:1 to phases — a command taxonomy
- **Specialist personas** that activate relevant skill subsets
- **Reference checklists** (Testing, Security, Performance, Accessibility) as standards artifacts
- **Google engineering culture** (Hyrum's Law, Chesterton's Fence) as normative artifacts
- **Session hooks** for cross-cutting concerns (citation caching)

### Conference Participation Infrastructure as Skill Bundle (NEW)
[[agents-at-conferences-infrastructure]] defines **6 core infrastructure capabilities** as agent skills:
- **Capability schema** (`capabilities[]`, `model_backbone`) as skill taxonomy for registration
- **Protocol contracts** (WebSocket + REST in `ARCHITECTURE.md`) as interface specifications
- **Benchmark arena** (GPQA, AAAR, LAB-Bench) as continuous evaluation harness
- **Communication bus** with rate limiting as coordination protocol
- **Moderation layer** as human-in-the-loop governance
- **Output aggregation** (PDF + JSON API) as knowledge persistence + inter-agent queryability

### DSPy Bundle Deepening (v0.2.3)
[[dspy-agent-skills-bundle]] now includes:
- **Exact dependency pinning** (DSPy 3.2.1 via `check_dspy_surface.py`) — prevents API drift
- **34+ pytest validators** for SKILL.md frontmatter, JSON schemas, Python AST
- **GEPA gotchas documented** as protocol constraints
- **Committed performance benchmarks** with specific model names and deltas
- **Offline validation** (`--dry-run`) for smoke testing

### Three-Layer Validation Stack (Iteration 13, reinforced)
The skill ecosystem is converging on a three-layer architecture:
- **Layer 1 (Pre-commit):** [[skill-validator-cli]] — deep quality + contamination + LLM-as-judge
- **Layer 2 (CI/CD):** [[validate-skill-github-action]] — structural spec compliance
- **Layer 3 (Registry):** [[agentskill-sh-ags-security-scoring]] — 12-category security scanning

This mirrors the **software supply chain** three-layer pattern (linters → CI scanners → registry audits) and is approximately 2-3 years behind the npm/PyPI ecosystem in maturity. See [[three-layer-validation-stack]].

### Bidirectional SHACL ↔ LLM Bridge (Iteration 13, reinforced)
With [[text2shacl-multi-agent-shacl]] (forward generation) added, the catalog now has a complete bridge:
- **Forward:** text2shacl turns natural-language requirements into SHACL shapes via multi-agent LangGraph pipeline with RAG
- **Reverse:** [[xpshacl-explainable-shacl]] turns SHACL shapes into natural-language explanations

Together they form a closed loop: requirements → shapes → validation → explanation → refined requirements. See [[bidirectional-shacl-llm-bridge]].

### Autonomous Science Workflow Framework (Seeded Papers)
Two foundational papers provide theoretical grounding:
- **SC25 Revolution paper:** Two-dimensional evolution matrix (Intelligence × Composition) with state machine abstraction. Maps directly to skill composition patterns (Single→Pipeline→Hierarchical→Mesh→Swarm) and skill sophistication levels (Static→Adaptive→Learning→Optimizing→Intelligent).
- **scAInce paper:** Co-pilot → Lab-pilot transition; self-driving laboratories (SDLs) as ultimate skill bundles; information-gain scoring for experiment prioritization; governance frameworks (EU AI Act, ISO 42001, PRISMA-AI, STARD-AI).

## Emerging Patterns

1. **Skills + Declarative Context Files** (ubiquitous across all platforms)
2. **Skills + Ontology** (strong — 10 examples, +ai4curation, +ClawBio OBO tooling)
3. **Skills + Validation + Explainability** (strong — 8 examples, +text2shacl forward direction)
4. **Skills + Guardrails via Interceptor** (SHACL + Cypher + Shadow testing)
5. **Skills + Supply Chain Provenance** (immutability, pinning, content-addressed detection)
6. **Skills + Taxonomy at Scale** (754 skills mapped to MITRE/NIST)
7. **Skills + Mapping/Alignment** (mature — 4 examples: SSSOM lifecycle complete)
8. **Skills + Rules/Governance** (strong — 6 examples, +Iron Laws/Red Flags)
9. **Skills + SHACL Validation** (strong — 7 examples, +text2shacl generation)
10. **Skills + MCP Dependencies** (emerging — 4 examples, +conference feed API)
11. **Skills + Constraint Rules** (strong — Iron Laws, Red Flags, SHACL, crypto signing, authorization)
12. **Skills + Dependency Graphs** (stable — DAG-based composition, PageRank ranking)
13. **Skills + Benchmarking** (emerging — paired evaluation, delta metrics, GEPA benchmarks)
14. **Orchestrator Pattern** (strong — a skill that activates and sequences other skills: DSPy, NORA, Addy Osmani)
15. **Implicit Bundle Discovery** (new — bundles discovered by grouping related skills across taxonomy catalogs)
16. **Attack → Defense Mapping** (new — PurpleBox attack vectors map directly to defense bundles)
17. **Agent Context as Documentation** (new — CLAUDE.md + CONTEXT.md + ADR as living context)
18. **Skill Security Governance Stack** (new — 4-layer model: AST10 risk taxonomy → ATF maturity model → empirical data → technical controls; see [[skill-security-governance]])
19. **SKILL.md as Universal Portable Unit** (new — confirmed identical operation across 5 major tools)
20. **Enterprise Platform Convergence** (new — Microsoft + Spring AI both shipping production-grade implementations)
21. **Three-Layer Validation Stack** (Iteration 13 — pre-commit → CI/CD → registry; see [[three-layer-validation-stack]])
22. **Bidirectional SHACL↔LLM Bridge** (Iteration 13 — text → shapes → explanation → text; see [[bidirectional-shacl-llm-bridge]])
23. **Registry-Level Security Scanning** (Iteration 13 — 12-category threat taxonomy + content-SHA provenance + auto-rate feedback)
24. **Domain-Specific Ontology Skills** (Iteration 13 — OBO Foundry skills for ontology/biocuration work; OAK, ROBOT, DOSDP)
25. **Domain-Coherent Bioinformatics Bundle** (NEW Iteration 14 — 88 skills, reproducibility bundles, reference genome asset, validation leaderboard, multi-modal access; see [[clawbio-bioinformatics-skills]])
26. **Process-as-Skill SDLC Coverage** (NEW Iteration 14 — 23 skills spanning full lifecycle with anti-rationalization, verification gates, personas; see [[addyosmani-engineering-skills]])
27. **Infrastructure-as-Agent-Capabilities** (NEW Iteration 14 — 6-component protocol for conference participation: registration, feeds, communication, moderation, benchmarking, memory; see [[agents-at-conferences-infrastructure]])
28. **Exact Dependency Pinning + Offline Validation** (NEW Iteration 14 — DSPy 3.2.1 pinned, 34+ validators, --dry-run smoke tests, committed benchmarks; see [[dspy-agent-skills-bundle]])
29. **Autonomous Science Workflow Theory** (NEW Iteration 14 — State machine abstraction, Intelligence×Composition matrix, co-pilot→lab-pilot, SDLs as skill bundles; see [[sc25-autonomous-science-workflows]], [[scaince-ai-lab-automation]])

## Context Element Coverage

| Context Element | Examples | Status |
|-----------------|----------|--------|
| SHACL Validation | 7 | **Strong** |
| Constraint Rules | 7 | **Strong** (+1: Iron Laws/Red Flags) |
| Rules / Authorization | 5 | **Strong** |
| Ontology / Taxonomy | 10 | **Strong** (+1: ai4curation OBO tooling, +1: ClawBio bioinformatics) |
| Governance / Verification | 9 | **Strong** (+1: conference moderation layer) |
| Security Framework / Certification | 4 | **Growing** |
| Platform Implementation | 6 | **Growing** (+1: Addy Osmani cross-platform) |
| Plugin / Distribution | 3 | **Emerging** |
| Academic Survey | 1 | **Emerging** |
| Universal Skill Format | 1 | **Emerging** |
| Dependency Graphs | 2 | **Stable** |
| YAML Configuration | 9+ | **Ubiquitous** |
| MCP Dependencies | 4 | **Emerging** (+1: conference feed API) |
| SSSOM Mapping | 4 | **Mature** |
| Supply Chain / Provenance | 5 | **Growing** (+1: content-SHA versioning, +1: reproducibility bundles) |
| Benchmarking | 2 | **Emerging** (+1: DSPy GEPA benchmarks) |
| LLM-as-Judge Quality Scoring | 1 | **NEW** (skill-validator) |
| Multi-Agent SHACL Generation | 1 | **NEW** (text2shacl) |
| Content-Addressed Versioning | 1 | **NEW** (agentskill.sh) |
| Pre-commit Multi-Platform Hooks | 1 | **NEW** (skill-validator, 13 platforms) |
| **Reproducibility Bundles** | **2** | **NEW** (ClawBio per-execution, DSPy pinned deps + benchmarks) |
| **Reference Data Assets** | **2** | **NEW** (Corpasome genome, DSPy benchmark datasets) |
| **Infrastructure Protocols** | **1** | **NEW** (Agents at Conferences 6-component protocol) |
| **Specification Layer Contracts** | **2** | **NEW** (ClawBio SKILL.md contracts, Addy Osmani Iron Laws) |

See also:
- [[skill-security-governance]] — Complete governance stack synthesis
- [[three-layer-validation-stack]] — The validation architecture pattern
- [[bidirectional-shacl-llm-bridge]] — The SHACL↔LLM closed loop
- [[skill-bundle-patterns]] — Foundation patterns
- [[sssom-mapping-as-context]] — Mappings as context
- [[constraint-rules-as-context]] — Rules as context
- [[validator-explanation-pattern]] — Validation + explanation pattern
