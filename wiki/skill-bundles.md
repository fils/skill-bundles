# Skill Bundles: A Living Catalog

**Primary Publication** — Last major update: 2026-07-16 (Iteration 41)

## TL;DR

Skill bundles are reusable packages that combine agent skills with formal context artifacts (validation, mapping, rules, vocabularies, taxonomies, and ontologies). This catalog tracks 97 documented examples across 41 iterations of daily research.

## Documented Examples (97 Total + 7 Paper Notes)

### Research & Workflow
- NORA — Autonomous research agent with orchestrated skills
- Agentic Engineering Workflow Skills — Multi-skill workflow patterns
- NemoClaw — Secure agent sandboxing and policy management (23 skills)
- **Superpowers** — Engineering discipline as skills: Iron Laws, Red Flags, methodology cycle (14 skills)
- **NORA Paper** — Harness-engineered autonomous research agent (21 skills + 9 sub-agents, arXiv 2605.02092)
- **ai4curation/curation-skills** — Chris Mungall's ontology/biocuration bundle (7 skills: OAK, ROBOT, DOSDP, OBO editing). Production users: Mondo, Cell Ontology, Uberon, EFO
- **ClawBio** — Bioinformatics-native library: 88 skills (29 production), 8,000+ Galaxy tools, reproducibility bundles, Corpasome reference genome (DOI: 10.5281/zenodo.19297389), 92.3% validation pass rate
- **Addy Osmani Agent Skills** — 23 production-grade engineering workflow skills across full SDLC, 3 specialist personas, 7 slash commands, Iron Laws/Red Flags constraint rules, Google engineering culture
- **Scientific Agent Skills (K-Dense)** (NEW Iteration 35) — 148 science skills, 100+ databases, package skills, security CI, agentskills.io (~30.6k★)
- **OpenMontage** (NEW Iteration 35) — Agentic video production: 500+ skills, 12 pipelines, hard human approval gates + checkpoint audit trail (~36.3k★)
- **CoEvoSkills** (NEW Iteration 36) — First self-evolving multi-file skill package framework: co-evolutionary verification (generator + surrogate verifier), surpasses human-curated skills within 5 iterations on SkillsBench (arXiv:2604.01687)
- **SkillMOO** (NEW Iteration 37) — First multi-objective skill bundle optimization: NSGA-II Pareto selection on pass rate + cost; pruning and substitution dominate successful edits; top rank on 11/12 SkillsBench tasks (arXiv:2604.09297)
- **EffiSkill** (NEW Iteration 37) — Two-tier skill hierarchy: Operator Skills (concrete transformations) + Meta Skills (strategic patterns); execution-free diagnosis; +3.69–12.52pp on EffiBench-X (arXiv:2603.27850)
- **SkillCraft** (NEW Iteration 37) — Benchmark for skill composition and reuse: agents auto-compose atomic tools into executable Skills; 80% token savings from caching; cited by 20 (arXiv:2603.00718)
- **EvoSkill** (NEW Iteration 38) — Self-evolving framework for auto-discovering agent skills via failure analysis; three-agent architecture (Executor→Proposer→Skill-Builder); Pareto frontier K=3; git-backed lineage; +7.3% OfficeQA, +12.1% SealQA; zero-shot transfer to BrowseComp (+5.3%); open-sourced (1k★) (arXiv:2603.02766)
- **SkillOpt** (NEW Iteration 38) — Treats skill files as trainable parameters; forward-backward-update in text space; frozen model + optimizer; textual learning rate + validation gating; best/tied-best on all 52 evaluation cells (6 benchmarks × 7 models × 3 modes); +23.5 points on GPT-5.5; skills transfer across model scales, harnesses, and tasks (Microsoft Research, June 2026)
- **ASPIRE** (NEW Iteration 39) — NVIDIA GEAR Lab; continual learning for robotics via code-as-policy; three components (execution engine + multimodal traces, skill library, evolutionary search); +77% LIBERO-Pro, +72% Robosuite, +32% BEHAVIOR-1K; 31% zero-shot vs 4%; sim-to-real transfer evidence; authors include Linxi "Jim" Fan, Ken Goldberg (arXiv:2607.00272)
- **Memento-Skills** (NEW Iteration 39) — Agent-designing agent; memory-based RL with stateful prompts; skills as structured markdown files = persistent evolving memory; Read-Write Reflective Learning (read = skill router, write = update library); continual learning without LLM parameter updates; +26.2% General AI Assistants, +116.2% Humanity's Last Exam; 27 citations (arXiv:2603.18743)
- **Skill1** (NEW Iteration 39) — Unified evolution of skill-augmented agents via RL; single policy co-evolves skill selection, utilization, distillation; frequency decomposition credit assignment (low-freq = selection, high-freq = distillation); ALFWorld + WebShop; outperforms baselines; 18 citations (arXiv:2605.06130)
- **EXIF** (NEW Iteration 39) — Alice-Bob dual-agent for automated skill discovery; exploration-first strategy; retrospective skill dataset from environment interaction; iterative feedback loop; self-play (Alice=Bob) enables self-evolution; Webshop + Crafter; precursor to 2026 skill discovery wave; 11 citations (arXiv:2506.04287)
- **SkillClaw** (NEW Iteration 40) — Collective skill evolution in multi-user agent ecosystems; cross-user + over-time trajectory aggregation; autonomous evolver (pattern recognition → skill update); shared synchronized repository; supports OpenClaw + Hermes; WildClawBench + Qwen3-Max; 42 citations; GitHub: AMAP-ML/SkillClaw (2.1k★) (arXiv:2604.08377)
- **SKILL0** (NEW Iteration 41) — First RL framework for skill internalization ("skills at training, zero at inference"); Dynamic Curriculum anneals skill scaffolding by on-policy helpfulness; +9.7% ALFWorld, +6.6% Search-QA, +10.1% WebShop; <0.5k tokens/step; GitHub: ZJU-REAL/SkillZero (arXiv:2604.02268)
- **OpenClaw-Skill / CSTS** (NEW Iteration 41) — Collective Skill Tree Search: multi-model candidate generation + quality/transferability assessment; builds structured transferable skill trees; Collective Skill RL multi-skill selection; addresses fragmentation, single-model bias, poor transfer (arXiv:2606.16774)

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
- **ClawHavoc Campaign** (NEW Iteration 36) — ~1,184 malicious skills on ClawHub; 13% malicious rate; dual-vector attack (prompt injection + shell access); canonical marketplace supply-chain case study
- **Supply Chain Agentic Factory** (NEW Iteration 36) — First proposal to extend SLSA/in-toto provenance to agentic code generation; "intent → source → binary" trust gap; Konflux/fullsend project (Red Hat)
- **SkillSieve** (NEW Iteration 37) — Three-layer triage for malicious skill detection: heuristic filter (86% volume) → LLM analysis (4 sub-tasks) → LLM jury (3-LLM voting+debate); F1=0.920 at $0.006/skill; 49K ClawHub skills evaluated; cross-ecosystem (ClawHub→Feishu); open-sourced (arXiv:2604.06550)
- **PROV-AGENT** (NEW Iteration 38) — Provenance model extending W3C PROV + MCP for tracking AI agent interactions in agentic workflows; agent decisions/prompts/responses as first-class provenance; near real-time capture system; cross-facility (edge/cloud/HPC); Oak Ridge + Argonne National Labs (arXiv:2508.02866)
- **SkillGuard** (NEW Iteration 39) — Permission framework for agent skills; dual-plane governance (context plane + action plane); five components (skill manifests, runtime access control, user-mediated authorization, deny-by-default, behavior monitoring); 315 real-world skills; 99.76% taxonomy coverage; 91% F1 manifest generation; attack success reduced 32%→23%; CSIRO+ANU (arXiv:2606.03024)
- **SkillFortify** (NEW Iteration 39) — First formal analysis framework for agent skill supply chains; six contributions: DY-Skill attacker model (Dolev-Yao for 5-phase lifecycle), sound static analysis (abstract interpretation), capability-based sandboxing with confinement proof, Agent Dependency Graph with SAT resolution + lockfile semantics, trust score algebra, SkillFortifyBench (540 skills); 96.95% F1, 100% precision, 0% FP; 22 frameworks; 6,487 malicious tools catalogued (arXiv:2603.00195)
- **NVIDIA-Verified Agent Skills** (NEW Iteration 39) — Industry productionization of skill governance: verified = cataloged, scanned (SkillSpector), signed (cryptographic skill.oms.sig), documented (skill cards); built on agentskills.io spec; cross-platform SKILL.md (Claude Code, Codex, Cursor); daily catalog sync; evaluation layer planned (NVIDIA, May 2026)
- **SkillSpector** (NEW Iteration 40) — NVIDIA's security scanner for AI agent skills; YARA rules + LLM semantic analysis; OWASP/MITRE alignment; batch scanning; CI/CD integration; Docker; MCP least-privilege; 1312 unit tests; v2.3.13; 13.2k★; 38 contributors; Apache 2.0; scanning step of NVIDIA-Verified ecosystem (GitHub: nvidia/skillspector)
- **AgentBound** (NEW Iteration 40) — First access control framework for MCP servers; Android permission model inspired; declarative policy + enforcement engine; 296 most popular MCP servers; 80.9% automated policy generation from source code; blocks majority of threats; negligible overhead; no server modifications; ACM FSE 2026 (arXiv:2510.21236)

### Security Governance Frameworks
- **OWASP Agentic Skills Top 10 (AST10)** — First dedicated security risk framework: 10-class vulnerability taxonomy, Lethal Trifecta, Universal Skill Format
- **Agentic Trust Framework (CSA)** — Zero Trust governance: 4-level maturity model (Intern→Principal), 5 promotion gates, compliance mapping
- **arXiv Agent Skills Survey** — First comprehensive academic survey: 26.1% vulnerability rate, 4-axis analysis (architecture, acquisition, deployment, security)
- **SoK: Agentic Skills** (NEW Iteration 36) — Formal skill definition S=(C,π,T,R); 7-stage lifecycle; 7 design patterns; ClawHavoc case study; 73 citations (arXiv:2602.20867)
- **SkillReducer** (NEW Iteration 37) — Empirical study of 55,315 skills: 26.4% lack routing, 60%+ non-actionable; two-stage optimization (delta debugging + taxonomy + progressive disclosure); 48%+39% compression with +2.8% quality (less-is-more effect); cross-model transfer (5 models, 4 families) (arXiv:2603.29919)
- **MalTool** (NEW Iteration 40) — First systematic study of malicious tool code implementations; CIA triad taxonomy for agent tools; coding-LLM-based synthesis (standalone + embedded); automated verifier (functional + diversity); 1,300 standalone + 5,727 embedded malicious tools; existing detection insufficient; UC Berkeley (Dawn Song) + Duke (arXiv:2602.12194)
- **BadSkill** (NEW Iteration 40) — Backdoor attacks via model-in-skill poisoning; semantic compositional triggers; composite training objective (classification + margin + poison); 99.5% ASR; 3% poison rate → 91.7% ASR; 8 architectures (494M–7.1B), 5 model families; 13 skills; identifies model-bearing skills as distinct supply-chain risk (arXiv:2604.09378)
- **SkillJect** (NEW Iteration 40) — First automated framework for generating poisoned skills; two-channel attack (artifact: helper script payload + instruction: front-loaded SKILL.md inducement); closed-loop multi-agent (Attack→Victim→Evaluate→refine); supports Claude Code + OpenClaw; trace-driven refinement; GitHub: jiaxiaojunQAQ/SkillJect (arXiv:2602.14211)

### Platform Skill Systems
- **Anthropic Official Skills** — Canonical reference: spec, templates, production document skills (140k stars)
- **Ylang Labs Agent Skills** — Definitive overview: "recipes vs kitchen" metaphor, 3-level progressive disclosure
- **Claude API Integration** — Container parameter, version pinning, 8 skills/request, 30MB limit
- OpenAI Codex Agent Skills — Progressive disclosure, MCP dependency declarations
- VS Code Copilot Agent Skills — Cross-platform agentskills.io implementation
- **Vercel Labs Agent Skills** (NEW Iteration 35) — Official vendor constraint-rule skills: React best practices (40+), web design (100+), writing handbook (80+), vercel-optimize (~28.9k★)

### Enterprise Platform Implementations
- **Microsoft Agent Framework Skills** — Enterprise platform: 3 implementation types (file/inline/class), script approval, DI support, multi-source composition
- **Spring AI Generic Agent Skills** — Java ecosystem: LLM-agnostic, 3-core-tool architecture, Claude Code compatible

### Distribution & Marketplaces
- **Chris Ayers Plugin Ecosystem** — 3-layer model (Skills → Plugins → Marketplaces); cross-tool compatibility matrix proving SKILL.md universal portability
- **Agensi Marketplace Landscape** — 8-marketplace comparison: skills.sh (2k), SkillsMP (800k), Agensi (200+, 8-point security scan); consolidation trends
- **agentskill.sh** — 100k+ skill registry with 12-category threat scanning, content-SHA versioning, auto-rate feedback loop
- **Agentic Awesome Skills Library** (NEW Iteration 35) — Installable mega-catalog: 1,943+ skills, npm installer, specialized plugins, schemas, security audit gates (~42.8k★, v14.1.0)
- **Awesome-Agent-Skill-Papers** (NEW Iteration 36) — Curated paper catalog accompanying six-layer taxonomy survey; discovery index for academic agent skill research (GitHub: DataArcTech)
- **Marketplace Landscape 2026** (NEW Iteration 37) — 8 major marketplaces compared: SkillsMP (800K+), LobeHub (169K+), Skills.sh (2K), Agensi (200+, 8-point security scan, 70/30 creator payments); 6.3 issues/skill avg, 36% prompt injection rate; MCP-based access predicted as default
- **SkillMigrator** (NEW Iteration 38) — Cross-domain web skill reuse via Transferable Interaction Patterns (TIP 4-tuple ⟨intent, template, slots, layout-skeleton⟩); accessibility-tree skeleton matching with Tree Edit Distance; 8-10% LLM call reduction; 35.4% cross-domain reuse rate (arXiv:2606.17645)
- **ASSCs / Skills Are Not Islands** (NEW Iteration 41) — Agent Skill Supply Chains; SDA recovers multi-channel deps (skill/package/service); SkillBOM (SBOM-compatible); 1.43M skills analyzed; 58.73% name collisions; 71–73% packages transitive-only; 60–78% security skill deps transitive; typed manifests + lockfiles recommended (arXiv:2607.01136)
- **From Registry to Repository** (NEW Iteration 41) — First empirical study of skills as engineered artefacts; 18,463 registry + 23,199 personal skills; 3,709 reuse links; 6 content themes + 6 maintenance themes; reuse = one-time copy; 53% never modified after adoption (arXiv:2607.00911)
- **Inside the Skill Market** (NEW Iteration 41) — First activity-centric SE skills study; 11,497 SE-related skills; SDLC coverage skewed to construction; versioning immature (most single-version); five-component skill model (arXiv:2607.09065)

### Infrastructure & Participation
- **Agents at Conferences** (NEW Iteration 14) — Infrastructure for AI agent conference participation: 6-component protocol (registration, feeds, communication, moderation, benchmarking, memory), capability schema taxonomy, SciFM26 target: 50 agents

### Security Taxonomy
- Claude Skills Ecosystem (1,116) — 754 cybersecurity skills mapped to MITRE/NIST frameworks
- **Awesome OpenClaw Skills** — 179 CLI utilities with implicit security/memory/development bundles

### Framework-Specific
- **DSPy Agent Skills Bundle** — Three-repo bundle: 34+ validation tests, AST checking, GEPA benchmarks, orchestration skill, exact DSPy 3.2.1 pinning
- **DSPy Agent Skills v0.2.3** — Updated bundle for DSPy 3.2.x, +19.53pp RAG improvement, dual-platform install, committed benchmark artifacts
- **Skills+DSPy SDK** — SkillsReActAgent with firejail, meta-tools, YAML config for sandbox
- **ORCA** (NEW Iteration 37) — Open Runtime for Capable Agents: 122 YAML capabilities + 36 DAG-composed skills + policy gates + provenance tracking; 184/184 canonical taxonomy coverage; MCP support; LangChain/CrewAI/Semantic Kernel adapters (Apache-2.0, 43★)
- **Skill OS** (NEW Iteration 38) — "Skills are the new Apps" position paper: surveys ~100K public skills; identifies 6 properties (phased procedures, semi-deterministic blocks, semantic equivalence, safety without enforcement, dependency fragility, no global management); argues for Skill OS abstraction (caching, env construction, global management, failure handling, security) (AgenticOS 2026 Workshop)
- **SkillGenBench** (NEW Iteration 38) — Benchmark for skill generation pipelines: 187 tasks × 8 domains; generator-executor decoupling; repository-grounded pass@3: 7-16% (extremely hard), document-grounded: 23-27%; auto-generated skills risk negative transfer (Zhou et al., 2026)

### Specification & Runtime
- Agent Skills Specification — The open standard (agentskills.io)
- SSSOM Mapping Protocol — Simple Standard for Sharing Ontological Mappings
- SHACL 1.2 Core — W3C Shapes Constraint Language specification

### Ontology-Integrated Skill Systems
- **AI-KM** (NEW Iteration 37) — Agent skills + ontology-driven knowledge modeling in closed loop: NL extraction builds formal ontologies; conversation-invokable skills + autonomous planning mode for novel tasks; knowledge→ontology→skills→knowledge feedback (SoftwareX, Sept 2026)

### Dependency & Retrieval
- **Graph of Skills (GoS)** — DAG-based skill composition, PageRank ranking, prerequisite resolution
- **R3-Skill** (NEW Iteration 41) — Query-conditional skill routing with skill compatibility; Reject-as-Resource uses LLM rejections as co-retrieval supervision; 10,246 skills; Hit@1=0.7521, NDCG@10=0.8173, Set-Compat=0.3188; Tencent R3-embedding/rerank (arXiv:2606.03565)

### Benchmarking & Catalogs
- **SkillsBench** — First agent skills benchmark: +16.2pp avg improvement, Healthcare +51.9pp
- **SWE-Skills-Bench** (NEW Iteration 40) — First requirement-driven benchmark isolating marginal utility of agent skills in SWE; 49 skills × GitHub repos × requirement docs; ~565 task instances, 6 subdomains; deterministic verification; **39/49 skills yield zero improvement**; avg gain +1.2%; token overhead up to +451%; only 7 help (up to +30%), 3 degrade (up to -10%); 34 citations (arXiv:2603.15401)
- **WildClawBench** (NEW Iteration 41) — Native-runtime long-horizon benchmark: 60 bilingual multimodal tasks in real OpenClaw / Claude Code / Codex / Hermes harnesses; hybrid grading; 19 models; best 62.2% (Opus 4.7); harness switch ±18pp; skill ablations mixed (Code Intelligence +22.4 strongest model); InternLM (arXiv:2605.10912)
- **Awesome Agent Skills Catalogs** — Ecosystem mapping: 1000+ skills, 44k+ marketplace

### Theory & Frameworks
- **Externalization in LLM Agents** (NEW Iteration 40) — Unified review of memory, skills, protocols, harness engineering; cognitive artifacts lens; four-form taxonomy (memory=state, skills=procedural expertise, protocols=interaction, harness=unification); weights→context→harness progression; parametric/externalized trade-off; self-evolving harnesses + shared infrastructure; 54 pages; 21 authors including Jun Wang (UCL), Weinan Zhang (SJTU); 35 citations (arXiv:2604.08224)

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
30. **Formal Skill Definition S=(C,π,T,R)** (NEW Iteration 36 — SoK provides canonical formal vocabulary; skills ≠ tools ≠ plans ≠ memory; simultaneously executable, reusable, governable; see [[sok-agentic-skills-beyond-tool-use]])
31. **Co-Evolutionary Verification** (NEW Iteration 36 — Dynamic verification where the verifier co-evolves with the skill generator; generalizes static validation to adaptive feedback loops; see [[coevoskills-self-evolving-skills]])
32. **SLSA/in-toto Provenance for Skills** (NEW Iteration 36 — Extending supply chain provenance to the "intent → source" gap; neutral observer pattern for skill generation; see [[supply-chain-agentic-factory-in-toto]])
33. **Marketplace Supply-Chain Attack Quantification** (NEW Iteration 36 — ClawHavoc: ~13% malicious rate; SoK: 26.1% vulnerable; workshop: 37% flaw rate; convergent quantification of marketplace risk; see [[clawhavoc-marketplace-attack]])
34. **Dependency-Aware Retrieval Validated** (NEW Iteration 36 — GoS v3: +25.55% reward, -56.72% tokens on SkillsBench; dependency-aware bundle retrieval outperforms flat in both quality and efficiency; see [[graph-of-skills-dependency-retrieval]])
35. **Six-Layer Skill Taxonomy** (NEW Iteration 36 — Ontology→Representation→Lifecycle→Runtime→Governance→Applications; comprehensive structural framework; see [[survey-agent-skills-procedural-infrastructure]])
36. **Skill Optimization Triad** (NEW Iteration 37 — Three distinct optimization approaches: SkillMOO (search/NSGA-II), CoEvoSkills (evolution), SkillReducer (content reduction); address configuration, content+verifier, and token efficiency axes; could compose; see [[skillmoo-multi-objective-optimization]], [[skillreducer-token-efficiency]])
37. **Less-Is-More Effect** (NEW Iteration 37 — Removing non-essential skill content *improves* functional quality by 2.8%; progressive disclosure (load on demand) is the architectural pattern; challenges "more context = better" assumption; see [[skillreducer-token-efficiency]])
38. **Skill Composition as Core Capability** (NEW Iteration 37 — SkillCraft validates that composing tools into reusable skills strongly correlates with agent success; 80% token savings from caching; auto-composition by agents (inverse of static bundles); see [[skillcraft-benchmark]])
39. **Hierarchical Security Triage with LLM Jury** (NEW Iteration 37 — Three-layer pipeline: heuristic→LLM analysis→LLM jury (3-LLM voting+debate); production-ready at $0.006/skill; cross-ecosystem portable; see [[skillsieve-malicious-skill-detection]])
40. **Skills + Ontology Closed Loop** (NEW Iteration 37 — Knowledge→ontology→skills→knowledge feedback; NL extraction builds ontologies; conversation-invokable skills; autonomous planning for novel tasks; see [[ai-km-ontology-skills]])
41. **DAG-Based Skill Composition Runtime** (NEW Iteration 37 — Declarative YAML capabilities composed as DAGs with policy gates, provenance, and deterministic baselines; 122 capabilities, 36 skills; see [[orca-cognitive-runtime]])
42. **Marketplace Consolidation** (NEW Iteration 37 — 8 marketplaces → 3-4 within a year; security scanning + creator payments becoming table stakes; MCP-based access replacing downloads; see [[marketplace-landscape-2026]])
43. **Skill Optimization Taxonomy Completing** (NEW Iteration 38 — Five approaches mapped: SkillMOO (search/NSGA-II), CoEvoSkills (evolution), SkillReducer (content reduction), SkillOpt (training/gradient-like text optimization), EvoSkill (failure-driven discovery); SkillOpt outperforms all on 52/52 cells; see [[skillopt-trainable-skill-parameters]], [[evoskill-automated-skill-discovery]])
44. **Skill Transfer Quantified** (NEW Iteration 38 — EvoSkill zero-shot task→task +5.3%, SkillOpt cross-harness Codex→Claude Code +59.7 + cross-model-scale, SkillMigrator cross-domain 35.4%; skills capture reusable workflow knowledge, not benchmark-specific instructions; see [[evoskill-automated-skill-discovery]], [[skillopt-trainable-skill-parameters]], [[skillmigrator-cross-domain-transfer]])
45. **Skill Generation Is the Bottleneck** (NEW Iteration 38 — SkillGenBench: 7-27% pass@3 for auto-generation; 2-3x harder than skill use; negative transfer risk; shifts research frontier from use to creation; see [[skillgenbench-skill-generation-benchmark]])
46. **Skills Need OS-Level Management** (NEW Iteration 38 — Skill OS paper: ~100K skill analysis reveals 6 properties; OS abstractions needed (caching, env construction, global management, failure handling, security); ORCA is early implementation; see [[skill-os-skills-as-apps]], [[orca-cognitive-runtime]])
47. **Provenance Standards Converging** (NEW Iteration 38 — PROV-AGENT (W3C PROV + MCP) + SLSA/in-toto + W3C Agent Protocol CG; provenance becoming standard context element for skill bundles; see [[prov-agent-unified-provenance]])
48. **Cross-Domain Transfer via Structural Layout** (NEW Iteration 38 — SkillMigrator's TIP abstraction (accessibility-tree skeleton + slot schema) enables cross-domain skill transfer by matching layout structure, not element IDs; novel architectural pattern; see [[skillmigrator-cross-domain-transfer]])

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
| Plugin / Distribution | 4 | **Growing** (+1: Agentic Awesome Skills installable mega-catalog) |
| Academic Survey | 2 | **Growing** (+1: arXiv:2602.08004; Agent Skills '26 workshop) |
| Universal Skill Format | 1 | **Emerging** |
| Dependency Graphs | 2 | **Stable** |
| YAML Configuration | 9+ | **Ubiquitous** |
| MCP Dependencies | 4 | **Emerging** (+1: conference feed API) |
| SSSOM Mapping | 4 | **Mature** |
| Supply Chain / Provenance | 6 | **Growing** (+1: OpenMontage checkpoint audit trail) |
| Benchmarking | 2 | **Emerging** (+1: DSPy GEPA; SkillsBench at workshop) |
| LLM-as-Judge Quality Scoring | 1 | **NEW** (skill-validator) |
| Multi-Agent SHACL Generation | 1 | **NEW** (text2shacl) |
| Content-Addressed Versioning | 1 | **NEW** (agentskill.sh) |
| Pre-commit Multi-Platform Hooks | 1 | **NEW** (skill-validator, 13 platforms) |
| **Reproducibility Bundles** | **2** | **NEW** (ClawBio per-execution, DSPy pinned deps + benchmarks) |
| **Reference Data Assets** | **3** | **Growing** (+1: K-Dense 100+ scientific DBs) |
| **Infrastructure Protocols** | **1** | **NEW** (Agents at Conferences 6-component protocol) |
| **Specification Layer Contracts** | **2** | **NEW** (ClawBio SKILL.md contracts, Addy Osmani Iron Laws) |
| **Human Approval Gates** | **1** | **NEW** (OpenMontage checkpoint gates) |
| **Vendor Constraint Handbooks** | **2** | **Growing** (+1: Vercel Labs rule catalogs) |
| **Co-Evolutionary Verification** | **1** | **NEW** (CoEvoSkills surrogate verifier) |
| **SLSA/in-toto Provenance** | **1** | **NEW** (Supply Chain Agentic Factory) |
| **Formal Skill Definition** | **1** | **NEW** (SoK S=(C,π,T,R)) |
| **Six-Layer Taxonomy** | **1** | **NEW** (Procedural Infrastructure survey) |
| **Paper Catalog** | **1** | **NEW** (Awesome-Agent-Skill-Papers) |
| **Multi-Objective Optimization** | **1** | **NEW** (SkillMOO NSGA-II Pareto) |
| **Delta Debugging** | **1** | **NEW** (SkillReducer adversarial delta) |
| **Progressive Disclosure** | **1** | **NEW** (SkillReducer on-demand loading) |
| **DAG Scheduler + Policy Gates** | **1** | **NEW** (ORCA runtime) |
| **Canonical Capability Taxonomy** | **1** | **NEW** (ORCA 184/184 coverage) |
| **Closed-Loop Knowledge↔Skills** | **1** | **NEW** (AI-KM) |
| **LLM Jury Voting** | **1** | **NEW** (SkillSieve 3-LLM debate) |
| **Two-Tier Skill Hierarchy** | **1** | **NEW** (EffiSkill Operator+Meta) |
| **Auto-Composition Protocol** | **1** | **NEW** (SkillCraft agent-authored) |
| **Pareto Frontier Governance** | **1** | **NEW** (EvoSkill K=3 git-backed) |
| **Textual Learning Rate** | **1** | **NEW** (SkillOpt per-step edit budget) |
| **Validation Gating + Rejected-Edit Buffer** | **1** | **NEW** (SkillOpt training-style optimization) |
| **Transferable Interaction Pattern (TIP)** | **1** | **NEW** (SkillMigrator 4-tuple) |
| **Accessibility-Tree Skeleton Matching** | **1** | **NEW** (SkillMigrator TED layout) |
| **W3C PROV + MCP Provenance** | **1** | **NEW** (PROV-AGENT) |
| **Skill OS Abstraction** | **1** | **NEW** (Skill OS 100K analysis) |
| **Generator-Executor Decoupling** | **1** | **NEW** (SkillGenBench) |
| **Negative Transfer Detection** | **1** | **NEW** (SkillGenBench auto-skill risk) |

See also:
- [[skill-security-governance]] — Complete governance stack synthesis
- [[three-layer-validation-stack]] — The validation architecture pattern
- [[bidirectional-shacl-llm-bridge]] — The SHACL↔LLM closed loop
- [[skill-bundle-patterns]] — Foundation patterns
- [[sssom-mapping-as-context]] — Mappings as context
- [[constraint-rules-as-context]] — Rules as context
- [[validator-explanation-pattern]] — Validation + explanation pattern
