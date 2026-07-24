#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path("/home/hermes/projects/skill-bundles")
WIKI = ROOT / "wiki"
DATE = "2026-07-24"
ITER = 42

# --- skill-bundles.md ---
pub = WIKI / "skill-bundles.md"
text = pub.read_text(encoding="utf-8")
text = text.replace(
    "**Primary Publication** — Last major update: 2026-07-16 (Iteration 41)",
    "**Primary Publication** — Last major update: 2026-07-24 (Iteration 42)",
)
text = text.replace(
    "This catalog tracks 97 documented examples across 41 iterations of daily research.",
    "This catalog tracks 104 documented examples across 42 iterations of daily research.",
)
text = text.replace(
    "### Documented Examples (97 Total + 7 Paper Notes)",
    "### Documented Examples (104 Total + 7 Paper Notes)",
)
# Insert new research bullets after SKILL0 / CSTS block if not present
new_block = """
- [**SkillOps**](examples/skillops-self-maintaining-skill-libraries.md) (NEW Iteration 42) — Library-time **skill technical debt** maintenance; Skill Contract (P,O,A,V,F) + HSEG; merge/repair/retire/validators; ALFWorld 79.5% (+8.8pp); plug-in +0.68–2.90pp; ~0 library-time LLM (arXiv:2605.13716)
- [**SkillRouter**](examples/skillrouter-body-aware-routing.md) (NEW Iteration 42) — Body-aware retrieve-and-rerank at ~80K; progressive-disclosure body hide −37–44pp; 1.2B Hit@1 **74.0%**; 13× smaller / 5.8× faster than strongest 16B base (arXiv:2603.22455 v5)
- [**AgentSkillOS**](examples/agentskillos-capability-tree-dag.md) (NEW Iteration 42) — Capability tree + DAG multi-skill orchestration at 200→**200K**; DAG beats flat invocation even with oracle skill set; 30 artifact tasks (arXiv:2603.02176)
- [**SkillC**](examples/skillc-contrastive-internalization.md) (NEW Iteration 42) — Contrastive Skill Credit Assignment for internalization; dual-stream advantages; +5.5% ALFWorld / +4.4% WebShop vs prior internalization RL (arXiv:2605.27899)
- [**Skill0.5**](examples/skill05-joint-internalization-utilization.md) (NEW Iteration 42) — Joint general-skill internalization + task-specific utilization via difficulty-aware mastery tiers; ID+OOD (arXiv:2605.28424)
- [**SLIM**](examples/slim-dynamic-skill-lifecycle.md) (NEW Iteration 42) — Retain–retire–expand lifecycle via leave-one-skill-out; +7.1pp; compact **non-empty** active skill boundary (arXiv:2605.10923)
- [**SkillCorpus**](examples/skillcorpus-open-ecosystem-curation.md) (NEW Iteration 42) — Curates ~821K open skills → 96,401 with 16-class taxonomy + utility/robustness/safety; +7.5pp SkillsBench; coverage+harness boundaries (arXiv:2607.15557 v4)
"""
if "skillops-self-maintaining" not in text:
    # insert after SKILL0 line if present
    anchor = "[**SKILL0**](examples/skill0-skill-internalization.md)"
    if anchor in text:
        # find end of CSTS line after SKILL0 section - insert after OpenClaw-Skill/CSTS if present
        csts = "[**OpenClaw-Skill / CSTS**](examples/openclaw-skill-csts-tree-search.md)"
        if csts in text:
            i = text.find(csts)
            j = text.find("\n", i)
            # find full line end (may be long)
            # take to next newline that starts with - or blank after the long line
            k = j
            while k < len(text) and text[k] == "\n":
                k += 1
            # the CSTS entry is one long line
            text = text[:j+1] + new_block + text[j+1:]
        else:
            i = text.find(anchor)
            j = text.find("\n", i)
            text = text[:j+1] + new_block + text[j+1:]
    else:
        text = text.replace(
            "## TL;DR\n",
            "## TL;DR\n" + new_block + "\n",
        )

# Add context element rows if section has table-like bullets at end
extra_ctx = """
| **Skill Contract (P,O,A,V,F)** | **1** | **NEW** (SkillOps) |
| **Skill Technical Debt** | **1** | **NEW** (SkillOps) |
| **Hierarchical Skill Ecosystem Graph** | **1** | **NEW** (SkillOps HSEG) |
| **Body-Aware Skill Routing** | **1** | **NEW** (SkillRouter) |
| **Capability-Tree Organization** | **1** | **NEW** (AgentSkillOS) |
| **DAG Multi-Skill Orchestration** | **1** | **NEW** (AgentSkillOS) |
| **Contrastive Skill Credit Assignment** | **1** | **NEW** (SkillC) |
| **General vs Task-Specific Skill Split** | **1** | **NEW** (Skill0.5) |
| **Leave-One-Skill-Out Lifecycle** | **1** | **NEW** (SLIM retain–retire–expand) |
| **Open Ecosystem Curation Pipeline** | **1** | **NEW** (SkillCorpus 821K→96K) |
| **Coverage + Harness Boundaries** | **1** | **NEW** (SkillCorpus) |
"""
if "Skill Technical Debt" not in text:
    # append before "See also:" if present
    if "See also:" in text:
        text = text.replace("See also:", extra_ctx + "\nSee also:")
    else:
        text = text.rstrip() + "\n" + extra_ctx + "\n"

pub.write_text(text, encoding="utf-8")

# --- index.md ---
idx = WIKI / "index.md"
it = idx.read_text(encoding="utf-8")
it = it.replace(
    "|**Last Updated:** 2026-07-16 (Iteration 41)|",
    "|**Last Updated:** 2026-07-24 (Iteration 42)|",
)
it = it.replace(
    "|**Status:** Active research — 7 new examples (WildClawBench native multi-harness eval, SKILL0 internalization, OpenClaw-Skill CSTS, R3-Skill compatibility routing, ASSC SkillBOM supply chains, Registry→Repository maintenance, Inside Skill Market SE activities)|",
    "|**Status:** Active research — 7 new examples (SkillOps library maintenance, SkillRouter body-aware 80K routing, AgentSkillOS tree+DAG, SkillC contrastive internalization, Skill0.5 hybrid, SLIM lifecycle, SkillCorpus 821K→96K)|",
)
# Update quick links digests
old_ql = "  - [2026-07-16 (Iteration 41)](daily-digests/2026-07-16.md)\n"
new_ql = "  - [2026-07-24 (Iteration 42)](daily-digests/2026-07-24.md)\n  - [2026-07-16 (Iteration 41)](daily-digests/2026-07-16.md)\n"
if "2026-07-24" not in it:
    it = it.replace(old_ql, new_ql)
# QA link
old_qa = "  - [Q&A — 2026-07-16 (Iteration 41)](qa/2026-07-16-qa.md)\n"
new_qa = "  - [Q&A — 2026-07-24 (Iteration 42)](qa/2026-07-24-qa.md)\n  - [Q&A — 2026-07-16 (Iteration 41)](qa/2026-07-16-qa.md)\n"
if "2026-07-24-qa" not in it:
    it = it.replace(old_qa, new_qa)

status_block = """## Current Status (Iteration 42 — 2026-07-24)

Catch-up after 8-day research gap (prior commits were Phase 6/Pages). Seven examples spanning library ops, scale routing/orchestration, and the internalization design space:

- **[skillops self maintaining skill libraries](examples/skillops-self-maintaining-skill-libraries.md)** — Skill technical debt; Contract (P,O,A,V,F) + HSEG; ALFWorld 79.5% (+8.8pp); plug-in gains; ~0 library-time LLM (arXiv:2605.13716)
- **[skillrouter body aware routing](examples/skillrouter-body-aware-routing.md)** — Body hide −37–44pp @~80K; 1.2B Hit@1 74.0%; e2e coding-agent transfer (arXiv:2603.22455 v5)
- **[agentskillos capability tree dag](examples/agentskillos-capability-tree-dag.md)** — Capability tree + DAG @200K; DAG > flat even with oracle skills (arXiv:2603.02176)
- **[skillc contrastive internalization](examples/skillc-contrastive-internalization.md)** — CSCA dual-stream advantages; +5.5% / +4.4% vs prior internalization (arXiv:2605.27899)
- **[skill05 joint internalization utilization](examples/skill05-joint-internalization-utilization.md)** — General-internalize + task-utilize mastery tiers (arXiv:2605.28424)
- **[slim dynamic skill lifecycle](examples/slim-dynamic-skill-lifecycle.md)** — Retain–retire–expand; +7.1pp; non-empty compact boundary (arXiv:2605.10923)
- **[skillcorpus open ecosystem curation](examples/skillcorpus-open-ecosystem-curation.md)** — 821K→96K curated corpus; +7.5pp SkillsBench; coverage+harness boundaries (arXiv:2607.15557 v4)

**Convergence signals:**
1. **Full stack emerges** — library maintain (SkillOps) · route (SkillRouter/R3) · orchestrate (AgentSkillOS) · train boundary (SLIM/SkillC/Skill0.5) · curate corpus (SkillCorpus).
2. **Body-aware routing + set-compatibility** jointly required at marketplace scale.
3. **Orchestration is not retrieval** — DAG composition is a separate unlock.
4. **Internalization is a spectrum**, not a boolean — general vs task-specific endpoints differ.
5. **Curation bounds open-ecosystem value** — raw crawl mass under-delivers without facets and harness fit.

## Iteration History (recent)

| Iteration | Date | Focus | New Examples |
|-----------|------|-------|--------------|
| **42** | **2026-07-24** | **Library ops + body-aware 80K routing + tree/DAG orchestration + internalization spectrum + open corpus curation** | **SkillOps, SkillRouter, AgentSkillOS, SkillC, Skill0.5, SLIM, SkillCorpus** |
| **41** | **2026-07-16** | **Native multi-harness eval + internalization + CSTS trees + compatibility routing + ASSC SkillBOM + maintenance science + SE market** | **WildClawBench, SKILL0, OpenClaw-Skill CSTS, R3-Skill, ASSCs, Registry→Repository, Inside Skill Market** |
"""

if "## Current Status (Iteration 42" not in it:
    # replace old current status section start through first iteration history table header area
    start = it.find("## Current Status (Iteration 41")
    if start == -1:
        start = it.find("## Current Status")
    hist = it.find("## Iteration History")
    if start != -1 and hist != -1:
        # keep old history after replacing status + prepending new history row - find end of first table rows is hard; replace status only and patch history table
        end_status = hist
        it = it[:start] + status_block + it[end_status:]
        # Remove duplicate "## Iteration History" if status_block already includes it
        # status_block ends with history header + 2 rows; old file continues with more rows - need to drop old header
        # After splice, we have status_block ending with | **41** |...| then old "## Iteration History...\n| Iteration |"
        # Fix double header
        it = it.replace(
            "| **WildClawBench, SKILL0, OpenClaw-Skill CSTS, R3-Skill, ASSCs, Registry→Repository, Inside Skill Market** |\n## Iteration History (recent)\n\n| Iteration | Date | Focus | New Examples |\n|-----------|------|-------|--------------|\n| **41** | **2026-07-16** |",
            "| **WildClawBench, SKILL0, OpenClaw-Skill CSTS, R3-Skill, ASSCs, Registry→Repository, Inside Skill Market** |\n| **41** | **2026-07-16** |",
            1,
        )
        # simpler cleanup if still duplicated
        while it.count("## Iteration History (recent)") > 1:
            first = it.find("## Iteration History (recent)")
            second = it.find("## Iteration History (recent)", first + 1)
            # remove second header and its table header lines
            rest = it[second:]
            # skip header + blank + table header + separator
            lines = rest.splitlines(keepends=True)
            skip = 0
            for n, ln in enumerate(lines[:6]):
                if n == 0 or ln.startswith("|") or ln.strip() == "":
                    skip = n + 1
                else:
                    break
            # Actually remove only the second header line and following 2 table header lines if present
            # lines[0]=header, [1]=blank?, [2]=cols, [3]=sep, [4]=maybe dup 41 row
            remove_until = 1
            if len(lines) > 1 and lines[1].strip() == "":
                remove_until = 2
            if len(lines) > remove_until and lines[remove_until].startswith("| Iteration"):
                remove_until += 1
            if len(lines) > remove_until and lines[remove_until].startswith("|---"):
                remove_until += 1
            # if next is duplicate **41** row already in status_block, skip it
            if len(lines) > remove_until and "**41**" in lines[remove_until] and "2026-07-16" in lines[remove_until]:
                remove_until += 1
            it = it[:second] + "".join(lines[remove_until:])

idx.write_text(it, encoding="utf-8")

# --- metrics.md ---
m = WIKI / "metrics.md"
mt = m.read_text(encoding="utf-8")
# Update last updated line
mt = re.sub(
    r"\|\*\*Last Updated: 2026-07-16 \(Iteration 41\)\*\*\|",
    f"|**Last Updated: {DATE} (Iteration {ITER})**|",
    mt,
)
# Replace KPI table body carefully - rewrite top KPI section
old_kpi = """| Metric | Value | Previous | Change |
|--------|-------|----------|--------|
| Documented Examples | 97 | 90 | +7 |
| Raw Sources (daily folders) | 53 days | 52 | +1 (2026-07-16) |
| Wiki Example Files | 97 | 90 | +7 |
| Paper Notes | 7 | 7 | Unchanged |
| Concept Articles | 8 | 8 | Unchanged |
| Daily Digests | +1 (2026-07-16) | — | +1 |
| Q&A Passes | +1 (2026-07-16-qa) | — | +1 |
| Context Element Types Covered | 62+ | 55+ | +7 (Native multi-harness protocol, Skill internalization/Dynamic Curriculum, Collective Skill Tree Search + transfer scoring, Skill compatibility / Reject-as-Resource, ASSC SkillBOM multi-channel deps, One-time copy reuse model, SE activity→skill mapping) |"""

# Handle double-pipe display corruption if present
# read actual file content via python
new_kpi = f"""| Metric | Value | Previous | Change |
|--------|-------|----------|--------|
| Documented Examples | 104 | 97 | +7 |
| Raw Sources (daily folders) | 54 days | 53 | +1 ({DATE}) |
| Wiki Example Files | 104 | 97 | +7 |
| Paper Notes | 7 | 7 | Unchanged |
| Concept Articles | 8 | 8 | Unchanged |
| Daily Digests | +1 ({DATE}) | — | +1 |
| Q&A Passes | +1 ({DATE}-qa) | — | +1 |
| Context Element Types Covered | 69+ | 62+ | +7 (Skill Contract/HSEG/technical debt, Body-aware routing, Capability-tree + DAG orchestration, Contrastive credit internalization, General vs task-specific skill split, LOSO retain–retire–expand lifecycle, Open ecosystem curation + coverage/harness boundaries) |"""

if "Documented Examples | 97" in mt or "Documented Examples | 97 |" in mt:
    # fuzzy: replace the KPI block by regex
    mt2 = re.sub(
        r"\| Metric \| Value \| Previous \| Change \|.*?Context Element Types Covered \|[^\n]+\n",
        new_kpi + "\n",
        mt,
        count=1,
        flags=re.S,
    )
    if mt2 == mt:
        # try with leading pipes from corrupted tables
        mt2 = re.sub(
            r"\|\| Metric \| Value \| Previous \| Change \|.*?Context Element Types Covered \|[^\n]+\n",
            new_kpi + "\n",
            mt,
            count=1,
            flags=re.S,
        )
    mt = mt2
else:
    # prepend run notes
    pass

run_notes = f"""
## {DATE} Run Notes (Iteration {ITER})

- **Gap fill:** First research content since 2026-07-16; intermediate commits were Phase 6 site/Pages only.
- **+7 examples:** SkillOps, SkillRouter, AgentSkillOS, SkillC, Skill0.5, SLIM, SkillCorpus.
- **Focus shift:** library ops + scale routing/orchestration + internalization design space + open corpus curation.
- **Anti-stagnation:** followed 07-16 priority queries (SkillOps/SkillRouter/AgentSkillOS/internalization) + fresh Jul SkillCorpus paper; avoided re-scraping OWASP (already cataloged).
- **Novel sources:** SkillCorpus (v4 Jul 23), SkillRouter v5 (Jul 20) not in prior digests.

"""
if f"## {DATE} Run Notes" not in mt:
    # insert after title / last updated
    if "## KPIs" in mt:
        mt = mt.replace("## KPIs", run_notes + "## KPIs", 1)
    else:
        mt = mt.rstrip() + "\n" + run_notes

# Coverage table additions
cov_add = """
| Skill Contract / HSEG / Technical Debt | New (SkillOps) |
| Body-Aware Large-Pool Routing | New (SkillRouter) |
| Capability Tree + DAG Orchestration | New (AgentSkillOS) |
| Contrastive Internalization Credit | New (SkillC) |
| General vs Task-Specific Skill Treatment | New (Skill0.5) |
| Dynamic External Skill Boundary (LOSO) | New (SLIM) |
| Open Ecosystem Curation + Quality Facets | New (SkillCorpus) |
"""
if "Skill Contract / HSEG" not in mt:
    mt = mt.rstrip() + "\n" + cov_add + "\n"

m.write_text(mt, encoding="utf-8")
print("Updated publication, index, metrics")
# verify counts
ex = list((WIKI/"examples").glob("*.md"))
print("example md files", len(ex), "without index", len([p for p in ex if p.name != "index.md"]))
print("digest exists", (WIKI/"daily-digests"/f"{DATE}.md").exists())
print("qa exists", (WIKI/"qa"/f"{DATE}-qa.md").exists())
