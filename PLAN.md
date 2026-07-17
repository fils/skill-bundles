# PLAN.md: Agentic Daily Online Research & Publication — Skill Bundles

**Research Topic:** Skill Bundles  
**Focus:** Collections of skills combined with supporting context elements (validation/SHACL, mapping/SSSOM, rules, vocabularies, taxonomies, and ontologies)

**Document format (authoritative):** `wiki/` is an **Open Knowledge Format (OKF) v0.1** Knowledge Bundle.  
- Spec: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md  
- Local summary: `wiki/concepts/okf-knowledge-bundle.md`  
- Conformance gate: `python3 scripts/okf-lint.py` (only; ignore dated `wikilink-lint-*.py` scripts)  
- Every concept `.md` needs YAML frontmatter with required `type`  
- Cross-links: **relative standard markdown only** — e.g. `[Title](../examples/foo.md)`  
- **Never** use Obsidian/Karpathy-era `[[wikilink]]` syntax in `wiki/`  
- `raw/` may contain any notes; do **not** copy wikilink style into `wiki/`

**Workflow inspiration (not document format):**
- Andrej Karpathy's "LLM Knowledge Bases" (Apr 2026) — daily compound research loop; **format is OKF, not Obsidian**
- NORA (Night Owl Research Agent) — https://github.com/GRIND-Lab-Core/night_owl_research_agent
- Agent Skills specification — https://agentskills.io/
- Agents at Conferences patterns
- ClawBio-style domain research agents
- **"The (R)evolution of Scientific Workflows in the Agentic AI Era"** (ACM SC '25) — state-machine framework for autonomous science, agent composition patterns (Single→Pipeline→Hierarchical→Mesh→Swarm)
- **"The Beginning of scAInce"** (Frontiers in AI, PMC12426084) — agentic models + lab automation, co-pilot→lab-pilot transition, skill taxonomy for scientific workflows

**Core Idea:** Use LLMs to discover, ingest, and synthesize examples of *skill bundles* — reusable, composable collections of agent skills plus the surrounding formal artifacts (SHACL shapes, SSSOM mappings, rules, controlled vocabularies, taxonomies, and ontologies) that give those skills reliable context and guardrails.

**Mission:** Run a persistent, self-improving research agent that performs **daily online research** to find, document, and analyze real-world examples of skill bundles. The agent maintains a living **OKF knowledge bundle** under `wiki/` that compounds knowledge about how skills are packaged with validation, mapping, rules, and semantic layers.

**Output Artifact:** A growing project directory (`wiki/`, `raw/`, `resources/`) that serves as both the research target and the publication. Primary publication file: `wiki/skill-bundles.md`.

---

## 1. High-Level Goals (Measurable)

- **Daily:** Ingest 3–8 high-signal sources; add/update ≥2 wiki articles or bundle examples; produce 1 daily digest.
- **Weekly:** Full OKF lint (`python3 scripts/okf-lint.py`) + gap analysis; 1 major synthesized article on bundle patterns; update top-level publication.
- **Monthly:** Wiki reaches ~80+ well-documented bundle examples; surface non-obvious composition patterns; propose workflow or taxonomy improvements.
- **Long-term:** The publication becomes the reference catalog for how skills are bundled with formal context artifacts. Track "bundle density" (skills + context elements per example) and reuse patterns.

**Success Metrics (tracked in `wiki/metrics.md`):**
- Number of documented skill bundle examples (cumulative + daily)
- Wiki word count / article count / cross-link density (relative markdown links between concepts)
- Coverage of context element types (SHACL, SSSOM, rules, vocabularies, taxonomies, ontologies)
- Quality of bundle descriptions (clarity, reproducibility, composition notes)
- External references and citations
- OKF lint clean: `python3 scripts/okf-lint.py` exits 0

---

## 2. Directory Structure (Enforced by Agent)

```
/home/hermes/projects/skill-bundles/
├── raw/                  # Untouched sources (GitHub repos, papers, docs, skill definitions)
│   ├── YYYY-MM-DD/       # Daily subdirs
│   └── metadata.json     # Auto-generated index
├── wiki/                 # OKF v0.1 Knowledge Bundle (LLM-maintained publication)
│   ├── index.md          # Bundle root (okf_version) + progressive disclosure
│   ├── log.md            # Chronological update log (OKF reserved)
│   ├── skill-bundles.md  # **Primary publication** — catalog of examples + patterns
│   ├── concepts/         # Atomic notes (+ index.md); includes okf-knowledge-bundle.md
│   ├── examples/         # Skill bundle case studies (+ index.md)
│   ├── tools/            # Skill frameworks, bundlers, validators (+ index.md)
│   ├── papers/           # Summarized papers (+ index.md)
│   ├── daily-digests/    # One .md per day (+ index.md)
│   ├── qa/               # Q&A passes (+ index.md)
│   ├── visualizations/   # Diagrams of bundle architectures, composition graphs
│   └── metrics.md        # Tracked KPIs + progress
│
│   # Format: OKF v0.1 — not Obsidian, not bare Karpathy wiki markup
│   # https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
├── resources/            # JSON-LD / schema.org descriptions of bundles and artifacts
├── scripts/              # okf-lint.py (gate), convert-to-okf.py, helpers
├── images/               # Downloaded visuals
└── PLAN.md               # This file (agent workflow contract)
```

**Rule:** The LLM agent owns everything in `wiki/`. Human only touches `PLAN.md`, `raw/`, or high-level config.  
**Lint rule:** Always use `python3 scripts/okf-lint.py`. Do **not** run dated `scripts/wikilink-lint-*.py` copies (legacy Obsidian checks).

---

## 3. Daily Workflow (Run Every 24h)

### Pre-flight (always run first, before Phase 1)

**Mandatory.** Do not skip. Output these four lines at the top of every run report.

```bash
cd /home/hermes/projects/skill-bundles
git status -sb                              # any untracked / modified files?
ls -la raw/$(date +%Y-%m-%d)/               # does today's raw dir exist? has content?
git log --oneline -5                        # what was the last commit?
ls wiki/daily-digests/ | tail -3            # are daily digests current?
```

**Rules derived from the pre-flight:**
- If `git status` shows uncommitted `raw/<old-date>/` content from a previous run, **process it first** as part of today's Phase 2–4. Do not leave it for a future run.
- If today's `raw/$(date +%Y-%m-%d)/` does not exist, Phase 1 must create it.
- If the most recent `wiki/daily-digests/` entry is older than 48 hours, the previous run(s) failed; flag this and prioritize closing the gap.

**When is [SILENT] allowed?**
Only when ALL of these are simultaneously true:
  (a) `git status -sb` shows a clean working tree, AND
  (b) `raw/$(date +%Y-%m-%d)/` exists with ≥1 file committed today, AND
  (c) `wiki/daily-digests/$(date +%Y-%m-%d).md` exists and is committed.

Otherwise, you MUST proceed through Phases 1–5 and push, even if it is a small run. A 1-source day is better than a silent no-op.

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
The wiki/ directory is an Open Knowledge Format (OKF) v0.1 Knowledge Bundle.
Spec: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
Local rules: wiki/concepts/okf-knowledge-bundle.md

Existing wiki summary (read first):
[PASTE current wiki/index.md + last 3 daily digests + concepts/ summaries]

New sources to integrate (from raw/ today):
[PASTE or reference paths + cleaned text]

Task:
1. Create or update entries in wiki/examples/ for each clear skill bundle.
2. Every concept document MUST have YAML frontmatter with required field `type`
   (use: Skill Bundle Example | Concept | Paper | Tool | Daily Digest | Q&A | Publication | Metrics).
   Also include recommended fields when known: title, description, resource, tags, timestamp.
   Producer extensions are allowed: date, sources, skills_included, context_elements,
   composition, reproducibility, rating.
3. Cross-link with **relative standard markdown links** only, e.g.
   [SkillOpt](../examples/skillopt-trainable-skill-parameters.md)
   Do NOT use Obsidian/wikilink syntax [[like-this]].
   Prefer relative paths so links work on GitHub and in OKF consumers.
4. Update wiki/examples/index.md (and other relevant index.md files) plus parent concept articles.
5. Generate 1 daily-digest/YYYY-MM-DD.md summarizing today's bundles and patterns discovered
   (type: Daily Digest). Prefer a # Citations section for external sources.
6. Never delete — prefer append + add relative markdown cross-links from related concepts.

Current date: [TODAY]
```

**Post-compilation:** Run `python3 scripts/okf-lint.py`. Fix any hard failures (missing `type`, residual `[[wikilinks]]`, unparseable frontmatter). Do not use legacy wikilink linters.

### Phase 3: Publication Editing & Synthesis (45–60 min)
**Goal:** Actively edit the main publication (`wiki/skill-bundles.md`) and synthesize patterns.

**Actions:**
1. Update master publication with new examples and emerging patterns (keep OKF frontmatter; `type: Publication`).
2. Synthesize cross-bundle insights (e.g., "Common ways skills are validated with SHACL").
3. Generate visualizations of bundle architectures when useful.
4. File everything back into `wiki/` using **relative markdown links** only (same rules as Phase 2 / OKF §5.2). No `[[wikilinks]]`.
5. Refresh affected `index.md` listings when titles/descriptions change.

### Phase 4: Q&A, Exploration & Gap Analysis (30–45 min)
**Goal:** Use the growing catalog to discover composition patterns and gaps.

**Actions:**
1. Run complex queries against the wiki:
   - "Which bundles combine skills with both SHACL validation and SSSOM mappings?"
   - "What ontology patterns appear most frequently alongside agent skills?"
   - "How do successful bundles handle rule integration?"
2. Write Q&A notes under `wiki/qa/` with OKF frontmatter (`type: Q&A`) and relative markdown links.
3. **OKF lint pass:** `python3 scripts/okf-lint.py` — fix missing context elements, broken relative links, and any residual `[[wikilinks]]`.

### Phase 5: Tooling, Report & Git — **MANDATORY, UNCONDITIONAL**

**This phase runs every single day, including maintenance days and days with zero new sources. Skipping it is the failure mode that lost us 3 days of pushes in late May 2026. Do not skip.**

1. Vibe-code small scripts in `scripts/` when repeated tasks become painful.
2. Update `PLAN.md` only after validating improvements.
3. Diff changes since last run.
4. **Always run exactly one of these terminal commands:**

```bash
# Normal case: there are file changes
git add . && git commit -m "Daily update $(date +%Y-%m-%d): <short summary>" && git push origin master

# Maintenance case: no file changes (zero new sources, all clean)
git add . && git commit --allow-empty -m "Daily research $(date +%Y-%m-%d): maintenance run (no new sources)" && git push origin master
```

5. **Report section is mandatory** and must include:
   - "Pre-flight:" line (from the pre-flight section above)
   - "Phases 1–5:" summary of what ran, including source count
   - "Git & Delivery:" with the commit hash AND `git log --oneline origin/master..HEAD` output (should be empty after a successful push), e.g. `Pushed: 5477a86..bbcb67f master -> master`
   - Any errors must be reported explicitly, not silently swallowed

Verify (always run before writing the report):
```bash
ls -1 raw/ | wc -l
ls -1 wiki/*.md
git status -sb
git log --oneline -3
```

**Hard rule:** if `git push` fails for any reason (auth, network, non-fast-forward, etc.), report the exact error in the report and do NOT mark the run as successful. A failed push is a critical alert.

### Phase 6: Post-Processing & Visualization (MANDATORY after successful Phase 5)

**Only run this phase after a successful git push in Phase 5.**  
Load the `skill-bundles-postprocess` skill and execute both steps below.

**Order is critical:** `kiso-cli` rebuilds/clears `public/` (it removed `viz.html` when run after visualize in dry-run 2026-07-17). Always run kiso **first**, then visualize.

#### Step 1: Static OKF Site Build
```bash
cd ~
./bin/kiso-cli-linux-x64 build \
  -s=./projects/skill-bundles/wiki \
  -d=./projects/skill-bundles/public
```

#### Step 2: Interactive Visualization
```bash
cd /home/hermes/src/visualize-okf/src
python3 -m visualize_okf \
  --bundle ~/projects/skill-bundles/wiki \
  --out ~/projects/skill-bundles/public/viz.html \
  --name "Skill Bundle"
```

**Verification (always perform):**
- Confirm `public/index.html` (and related site files) exist after kiso.
- Confirm `public/viz.html` exists and is non-empty **after** visualize (not only before kiso).
- Report file sizes and any errors/warnings.
- If either command fails, report the exact error — do **not** mark the run as successful.

**Reporting requirement:** Include a short “Phase 6” subsection in the final report with the commands run and verification output.

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
- **Seeded Papers (manually added):**
- https://dl.acm.org/doi/full/10.1145/3731599.3767580 — "The (R)evolution of Scientific Workflows in the Agentic AI Era" (SC '25 Workshops): state-machine framework for autonomous science, agent composition patterns
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12426084/ — "The Beginning of scAInce" (Frontiers in AI, 2025): agentic models + lab automation, co-pilot→lab-pilot transition

**arXiv papers on agent skills, tool-use formalization, semantic agent frameworks**
- GitHub searches for `skills/` directories containing validation, mapping, or ontology files

---

## 5. Key LLM Prompts Library

**Bundle Documentation Prompt** (use when creating `wiki/examples/` entries):
```
Create or update a wiki/examples/<slug>.md concept document under OKF v0.1
(spec: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).

Required YAML frontmatter (example):
---
type: Skill Bundle Example
title: <Human-readable name>
description: <One sentence summary>
resource: <canonical URL if any>
tags: [skill-bundles, ...]
timestamp: <ISO 8601 datetime>
date: YYYY-MM-DD
sources: [<urls or raw/ paths>]
skills_included: [...]
context_elements: [...]
composition: <how parts fit together>
reproducibility: <how to verify>
rating: <1-10 optional>
---

Body structure:
- Name & origin
- Skills included
- Context elements (list each SHACL shape, SSSOM mapping, rule set, vocabulary, taxonomy, ontology)
- How the context elements support or constrain the skills
- Composition notes / reusability patterns
- Reproducibility assessment
- # Citations (external sources)

Linking rules:
- Use relative markdown links only, e.g. [Three-layer validation](../concepts/three-layer-validation-stack.md)
- Never use [[wikilink]] / Obsidian syntax
- Update wiki/examples/index.md with title + description
```

**Pattern Synthesis Prompt:**
```
From the examples added today and previously documented bundles, identify 2–3 emerging patterns
in how skills are bundled with formal context artifacts. Write a short concept article for each
pattern under wiki/concepts/ with OKF frontmatter (type: Concept), relative markdown links to
related examples, and update wiki/concepts/index.md. Spec:
https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
```

---

## 6. Weekly & Monthly Rituals

**Every Sunday:**
- Full OKF lint (`python3 scripts/okf-lint.py`) + consistency pass across all bundle examples.
  (Lint ignores fenced/inline code anti-examples; do not "fix" docs that only mention `[[wikilinks]]` as forbidden.)
- Generate "Weekly Synthesis" on bundle composition patterns (OKF concept docs + relative links).
- Review metrics and adjust search focus.
- Refresh `wiki/log.md` if not auto-maintained.

**Monthly:**
- Major publication refresh (`wiki/skill-bundles.md`, still OKF `type: Publication`).
- Evaluate taxonomy of context element types and propose improvements.
- Spot-check against OKF SPEC (frontmatter, indexes, link style).

---

## 7. Risk Mitigation & Best Practices

- **Format drift:** Never reintroduce Obsidian `[[wikilinks]]` or drop required `type` frontmatter. Gate with `okf-lint.py`.
- **Contamination:** Keep raw sources clearly separated from synthesized wiki content. `raw/` is not part of the OKF bundle.
- **Hallucination:** Every claim must trace to ≥1 raw source. Use confidence scores. Prefer `# Citations`.
- **Scope Creep:** Focus only on bundles that include both skills *and* at least one formal context element (validation/mapping/rules/vocab/taxonomy/ontology).
- **Token Efficiency:** Use hierarchical summaries and `index.md` progressive disclosure (OKF §6).
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
> "Create the complete initial wiki structure and content for 'Skill Bundles' based on the seed sources, as an OKF v0.1 Knowledge Bundle (https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md). Include index.md with okf_version, master publication, 8–10 core concept articles, examples/ with 5–10 documented bundles, tools/, and per-directory index.md files. Every concept needs YAML frontmatter with required type. Use relative markdown cross-links only — never [[wikilinks]]. Make it immediately useful for discovering composition patterns."

---

## 9. Evolution of This Plan

This PLAN.md is the agent workflow contract (outside the OKF bundle). The agent may propose PLAN improvements after validating them; knowledge content belongs in `wiki/` as OKF concept documents. After major format changes, re-run `python3 scripts/okf-lint.py` and confirm the Document format section above still matches the SPEC.

**Version:** 2.0 (OKF v0.1 document format; Karpathy workflow only)  
**Last Edited:** 2026-07-16  
**Next Review:** After first full week of OKF-aligned daily runs
