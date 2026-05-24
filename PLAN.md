# PLAN.md: Agentic Daily Online Research & Publication — Skill Bundles

**Research Topic:** Skill Bundles  
**Focus:** Collections of skills combined with supporting context elements (validation/SHACL, mapping/SSSOM, rules, vocabularies, taxonomies, and ontologies)  
**Inspired by:** 
- Andrej Karpathy's "LLM Knowledge Bases" (Apr 2026)
- NORA (Night Owl Research Agent) — https://github.com/GRIND-Lab-Core/night_owl_research_agent
- Agent Skills specification — https://agentskills.io/
- Agents at Conferences patterns
- ClawBio-style domain research agents

**Core Idea:** Use LLMs to discover, ingest, and synthesize examples of *skill bundles* — reusable, composable collections of agent skills plus the surrounding formal artifacts (SHACL shapes, SSSOM mappings, rules, controlled vocabularies, taxonomies, and ontologies) that give those skills reliable context and guardrails.

**Mission:** Run a persistent, self-improving research agent that performs **daily online research** to find, document, and analyze real-world examples of skill bundles. The agent maintains a living publication (structured wiki) that compounds knowledge about how skills are packaged with validation, mapping, rules, and semantic layers.

**Output Artifact:** A growing project directory (`wiki/`, `raw/`, `resources/`) that serves as both the research target and the publication. Primary publication file: `wiki/skill-bundles.md`.

---

## 1. High-Level Goals (Measurable)

- **Daily:** Ingest 3–8 high-signal sources; add/update ≥2 wiki articles or bundle examples; produce 1 daily digest.
- **Weekly:** Full wiki lint + gap analysis; 1 major synthesized article on bundle patterns; update top-level publication.
- **Monthly:** Wiki reaches ~80+ well-documented bundle examples; surface non-obvious composition patterns; propose workflow or taxonomy improvements.
- **Long-term:** The publication becomes the reference catalog for how skills are bundled with formal context artifacts. Track "bundle density" (skills + context elements per example) and reuse patterns.

**Success Metrics (tracked in `wiki/metrics.md`):**
- Number of documented skill bundle examples (cumulative + daily)
- Wiki word count / article count / backlink density
- Coverage of context element types (SHACL, SSSOM, rules, vocabularies, taxonomies, ontologies)
- Quality of bundle descriptions (clarity, reproducibility, composition notes)
- External references and citations

---

## 2. Directory Structure (Enforced by Agent)

```
/home/hermes/projects/skill-bundles/
├── raw/                  # Untouched sources (GitHub repos, papers, docs, skill definitions)
│   ├── YYYY-MM-DD/       # Daily subdirs
│   └── metadata.json     # Auto-generated index
├── wiki/                 # The compiled, LLM-maintained publication (Obsidian-ready)
│   ├── index.md          # Master entry point + table of contents + daily summary
│   ├── skill-bundles.md  # **Primary publication file** — catalog of examples + patterns
│   ├── concepts/         # Atomic notes on bundle patterns, composition rules, etc.
│   ├── examples/         # Individual well-documented skill bundle case studies
│   ├── tools/            # Skill frameworks, bundlers, validators
│   ├── papers/           # Summarized relevant papers and specifications
│   ├── daily-digests/    # One .md per day (or weekly rollups)
│   ├── visualizations/   # Diagrams of bundle architectures, composition graphs
│   └── metrics.md        # Tracked KPIs + progress
├── resources/            # JSON-LD / schema.org descriptions of bundles and artifacts
├── scripts/              # Helper tools (metadata updater, bundle linter, etc.)
├── images/               # Downloaded visuals
└── PLAN.md               # This file
```

**Rule:** The LLM agent owns everything in `wiki/`. Human only touches `PLAN.md`, `raw/`, or high-level config.

---

## 3. Daily Workflow (Run Every 24h)

### Phase 1: Discovery & Ingestion (45–75 min)
**Goal:** Find fresh, high-signal examples of skill bundles.

**Actions:**
1. **Web & GitHub searches** (use `web_search` tool, prioritize recent):
   - `"skill bundle" OR "agent skills" OR "claude skills" OR "agent skills catalog"`
   - `SHACL` + skills / agents
   - `SSSOM` + skills / mapping + agents
   - For GitHub-specific searches, prefer the `gh` CLI via `terminal` when possible (e.g. `gh search repos "skill bundle"`)
   - Specific follow-ups from NORA, agentskills.io, ClawBio, Agents at Conferences patterns

2. **Browse & Save** top results (use `browser` or `web_search` tools as appropriate):
   - Extract skill definitions, accompanying SHACL shapes, SSSOM mappings, rule sets, vocabularies, taxonomies, or ontologies.
   - Save full content or clean .md version to `raw/YYYY-MM-DD/`.
   - Note composition patterns (how skills reference or depend on context artifacts).
   - For JavaScript-heavy sites, fall back to the browser automation tool if standard search results are insufficient.

3. **Quick triage prompt**:
   > "Review these new sources. Rate signal-to-noise for skill bundle examples (1-10). Recommend which 3–5 to fully ingest today and why. Suggest 2 new search queries for tomorrow based on gaps in context element coverage (SHACL, SSSOM, rules, vocabularies, etc.)."

**Output:** Updated `raw/` + `raw/metadata.json`.

### Phase 2: Incremental Compilation (60–90 min)
**Goal:** Compile new bundle examples into the wiki using consistent structure.

**Core Prompt (use every time):**
```
You are an expert cataloger of Agent Skill Bundles.

Existing wiki summary (read first):
[PASTE current wiki/index.md + last 3 daily digests + concepts/ summaries]

New sources to integrate (from raw/ today):
[PASTE or reference paths + cleaned text]

Task:
1. Create or update entries in wiki/examples/ for each clear skill bundle.
2. Maintain consistent frontmatter: date, sources, skills included, context elements (SHACL/SSSOM/rules/vocab/taxonomy/ontology), composition notes, reproducibility.
3. Use wikilinks [[concept-name]] heavily.
4. Add to index.md and relevant parent articles in concepts/.
5. Generate 1 daily-digest/YYYY-MM-DD.md summarizing today's bundles and patterns discovered.
6. Never delete — prefer append + backlink.

Current date: [TODAY]
```

**Post-compilation:** Verify all new wikilinks resolve. Fix broken ones.

### Phase 3: Publication Editing & Synthesis (45–60 min)
**Goal:** Actively edit the main publication (`wiki/skill-bundles.md`) and synthesize patterns.

**Actions:**
1. Update master publication with new examples and emerging patterns.
2. Synthesize cross-bundle insights (e.g., "Common ways skills are validated with SHACL").
3. Generate visualizations of bundle architectures when useful.
4. File everything back into `wiki/` with proper links.

### Phase 4: Q&A, Exploration & Gap Analysis (30–45 min)
**Goal:** Use the growing catalog to discover composition patterns and gaps.

**Actions:**
1. Run complex queries against the wiki:
   - "Which bundles combine skills with both SHACL validation and SSSOM mappings?"
   - "What ontology patterns appear most frequently alongside agent skills?"
   - "How do successful bundles handle rule integration?"
2. Linting pass for consistency, missing context elements, and new research questions.

### Phase 5: Tooling & Automation (as needed)
- Vibe-code small scripts in `scripts/` when repeated tasks become painful.
- Update `PLAN.md` only after validating improvements.

---

## 4. Recurring Search Queries & Sources to Monitor

**Daily Core Queries (rotate):**
1. "agent skills" OR "claude code skills" OR "skill bundle" github
2. SHACL + (agent OR skills OR "claude code")
3. SSSOM + (agent OR skills OR mapping)
4. "skill catalog" OR "agentskills.io" OR "agent skills specification"
5. NORA OR "night owl research" skills
6. "agents at conferences" skills OR bundles
7. DSPy OR dspy (skills OR "agent skills" OR bundles OR "skill bundle") github
8. "dspy-agent-skills" OR "dspy skills" OR DSPy agent framework skills

**High-Priority Sources:**
- https://agentskills.io/ and related GitHub org
- https://github.com/GRIND-Lab-Core/night_owl_research_agent
- https://github.com/cecat/agents-at-conferences
- https://clawbio.ai/
- https://github.com/intertwine/dspy-agent-skills (example DSPy-based agent skills bundle — prime target for discovery)
- arXiv papers on agent skills, tool-use formalization, semantic agent frameworks
- GitHub searches for `skills/` directories containing validation, mapping, or ontology files

---

## 5. Key LLM Prompts Library

**Bundle Documentation Prompt** (use when creating `wiki/examples/` entries):
```
Document this skill bundle with the following structure:
- Name & origin
- Skills included
- Context elements (list each SHACL shape, SSSOM mapping, rule set, vocabulary, taxonomy, ontology with links)
- How the context elements support or constrain the skills
- Composition notes / reusability patterns
- Reproducibility assessment
```

**Pattern Synthesis Prompt:**
```
From the examples added today and previously documented bundles, identify 2–3 emerging patterns in how skills are bundled with formal context artifacts. Write a short concept article for each pattern.
```

---

## 6. Weekly & Monthly Rituals

**Every Sunday:**
- Full wiki lint + consistency pass across all bundle examples.
- Generate "Weekly Synthesis" on bundle composition patterns.
- Review metrics and adjust search focus.

**Monthly:**
- Major publication refresh.
- Evaluate taxonomy of context element types and propose improvements.

---

## 7. Risk Mitigation & Best Practices

- **Contamination:** Keep raw sources clearly separated from synthesized wiki content.
- **Hallucination:** Every claim must trace to ≥1 raw source. Use confidence scores.
- **Scope Creep:** Focus only on bundles that include both skills *and* at least one formal context element (validation/mapping/rules/vocab/taxonomy/ontology).
- **Token Efficiency:** Use hierarchical summaries.
- **Human Override:** Revert via git if needed.
- **Backup:** Daily snapshots recommended.

---

## 8. Getting Started (First Run Instructions)

1. Ensure directory structure exists.
2. Seed `raw/` with initial high-quality examples from the links above.
3. Run Phase 2 bootstrap prompt to generate initial wiki structure.
4. Manually create skeleton `wiki/skill-bundles.md` if needed.
5. Set up daily scheduling.

**Bootstrap Prompt:**
> "Create the complete initial wiki structure and content for 'Skill Bundles' based on the seed sources. Include index.md, master publication, 8–10 core concept articles, examples/ directory with 5–10 documented bundles, and tools/ section. Use proper wikilinks and backlinks. Make it immediately useful for discovering composition patterns."

---

## 9. Evolution of This Plan

This PLAN.md is part of the knowledge base. The agent is encouraged to log execution notes, propose improvements as new concept articles, and after 30 days ask: "What would make this daily loop 2× more effective?"

**Version:** 1.2 (Tool usage clarified)  
**Last Edited:** 2026-05-23  
**Next Review:** After first full week of runs
