#!/usr/bin/env python3
"""
Improve cross-link coverage in the OKF wiki:

1. Link skill-bundles.md catalog bullets → examples/ and papers/
2. Regenerate examples/index.md (and other subdir indexes)
3. Ensure each daily digest links that day's new example files
4. Link Q&A pages from digests + root index
5. (Soft checks live in okf-lint.py — this script only mutates content)

Usage:
  python3 scripts/link-catalog-and-digests.py
  python3 scripts/link-catalog-and-digests.py --dry-run
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"

# Manual aliases: catalog name fragment (lowercase) → example/paper stem
ALIASES: dict[str, str] = {
    "nora": "nora-gis-research-agent",
    "nora paper": "nora-gis-research-agent",
    "agentic engineering workflow skills": "agentic-engineering-workflow-skills",
    "nemoclaw": "nemoclaw-security-scanner",
    "nemoclaw security scanner": "nemoclaw-security-scanner",
    "superpowers": "superpowers-engineering-discipline-skills",
    "ai4curation/curation-skills": "ai4curation-curation-skills",
    "ai4curation": "ai4curation-curation-skills",
    "clawbio": "clawbio-bioinformatics-skills",
    "addy osmani agent skills": "addyosmani-engineering-skills",
    "scientific agent skills (k-dense)": "scientific-agent-skills-kdense",
    "scientific agent skills": "scientific-agent-skills-kdense",
    "k-dense": "scientific-agent-skills-kdense",
    "openmontage": "openmontage-video-production-skills",
    "coevoskills": "coevoskills-self-evolving-skills",
    "skillmoo": "skillmoo-multi-objective-optimization",
    "effiskill": "effiskill-code-efficiency-optimization",
    "skillcraft": "skillcraft-benchmark",
    "evoskill": "evoskill-automated-skill-discovery",
    "skillopt": "skillopt-trainable-skill-parameters",
    "aspire": "aspire-robotics-skill-discovery",
    "memento-skills": "memento-skills-agent-designing-agent",
    "memento": "memento-skills-agent-designing-agent",
    "skill1": "skill1-unified-skill-evolution-rl",
    "exif": "exif-automated-skill-discovery",
    "skillclaw": "skillclaw-collective-skill-evolution",
    "skill0": "skill0-skill-internalization",
    "openclaw-skill / csts": "openclaw-skill-csts-tree-search",
    "openclaw-skill": "openclaw-skill-csts-tree-search",
    "csts": "openclaw-skill-csts-tree-search",
    "ontologizer": "ontologizer-openclaw-ontology-skill",
    "openclaw pkb skill": "openclaw-pkb-skill",
    "rdf ontologies": "rdf-ontologies-skill",
    "open ontologies mcp": "open-ontologies-github",
    "open ontologies paper": "open-ontologies-paper",
    "open ontologies github": "open-ontologies-github",
    "oxo2 mapping service": "oxo2-sssom-mapping-service",
    "oxo2": "oxo2-sssom-mapping-service",
    "onto-llm-mapping": "onto-llm-mapping",
    "veto": "veto-agent-authorization",
    "tool-use firewall": "tool-use-firewall",
    "schimatos": "schimatos-shacl-knowledge-graph",
    "graphguard os": "graphguard-os-guardrails",
    "xpshacl": "xpshacl-explainable-shacl",
    "shacl data quality": "shacl-data-quality-69-metrics",
    "text2shacl": "text2shacl-multi-agent-shacl",
    "skill-validator cli": "skill-validator-cli",
    "validate skill github action": "validate-skill-github-action",
    "nvidia verified agent skills": "nvidia-verified-agent-skills",
    "nvidia-verified agent skills": "nvidia-verified-agent-skills-governance",
    "nvidia skills repository": "nvidia-skills-repo",
    "purplebox security analysis": "purplebox-supply-chain-security",
    "github cli skill management": "github-cli-skill-management",
    "mondoo security analysis": "mondoo-agent-skills-security",
    "agentskill.sh / ags": "agentskill-sh-ags-security-scoring",
    "agentskill.sh": "agentskill-sh-ags-security-scoring",
    "clawhavoc campaign": "clawhavoc-marketplace-attack",
    "clawhavoc": "clawhavoc-marketplace-attack",
    "supply chain agentic factory": "supply-chain-agentic-factory-in-toto",
    "skillsieve": "skillsieve-malicious-skill-detection",
    "prov-agent": "prov-agent-unified-provenance",
    "skillguard": "skillguard-permission-framework",
    "skillfortify": "skillfortify-formal-verification-supply-chain",
    "skillspector": "skillspector-nvidia-security-scanner",
    "agentbound": "agentbound-mcp-access-control",
    "owasp agentic skills top 10 (ast10)": "owasp-agentic-skills-top-10",
    "owasp agentic skills top 10": "owasp-agentic-skills-top-10",
    "agentic trust framework (csa)": "agentic-trust-framework-csa",
    "agentic trust framework": "agentic-trust-framework-csa",
    "arxiv agent skills survey": "arxiv-agent-skills-survey",
    "sok: agentic skills": "sok-agentic-skills-beyond-tool-use",
    "skillreducer": "skillreducer-token-efficiency",
    "maltool": "maltool-malicious-tool-attacks",
    "badskill": "badskill-backdoor-model-in-skill",
    "skillject": "skillject-automated-prompt-injection",
    "anthropic official skills": "anthropic-official-skills-repo",
    "ylang labs agent skills": "ylang-labs-agent-skills-overview",
    "claude api integration": "claude-api-skills-integration",
    "openai codex agent skills": "openai-codex-skills",
    "vs code copilot agent skills": "vscode-copilot-skills",
    "vercel labs agent skills": "vercel-labs-agent-skills",
    "microsoft agent framework skills": "microsoft-agent-framework-skills",
    "spring ai generic agent skills": "spring-ai-agent-skills",
    "chris ayers plugin ecosystem": "chris-ayers-plugin-ecosystem",
    "agensi marketplace landscape": "agensi-marketplace-landscape",  # tools/
    "agentic awesome skills library": "agentic-awesome-skills-library",
    "awesome-agent-skill-papers": "awesome-agent-skill-papers-catalog",
    "marketplace landscape 2026": "marketplace-landscape-2026",
    "skillmigrator": "skillmigrator-cross-domain-transfer",
    "asscs / skills are not islands": "assc-skill-supply-chains-skillbom",
    "asscs": "assc-skill-supply-chains-skillbom",
    "from registry to repository": "registry-to-repository-skill-maintenance",
    "inside the skill market": "inside-skill-market-se-activities",
    "agents at conferences": "agents-at-conferences-infrastructure",
    "claude skills ecosystem (1,116)": "claude-skills-ecosystem-1116",
    "claude skills ecosystem": "claude-skills-ecosystem-1116",
    "awesome openclaw skills": "awesome-openclaw-skills-catalog",
    "dspy agent skills bundle": "dspy-agent-skills-bundle",
    "dspy agent skills v0.2.3": "dspy-agent-skills-v023",
    "orca": "orca-cognitive-runtime",
    "skill os": "skill-os-skills-as-apps",
    "skillgenbench": "skillgenbench-skill-generation-benchmark",
    "agent skills specification": "agent-skills-spec",
    "sssom mapping protocol": "sssom-mapping-protocol",
    "shacl 1.2 core": "shacl-1-2-spec",
    "ai-km": "ai-km-ontology-skills",
    "graph of skills (gos)": "graph-of-skills-dependency-retrieval",
    "graph of skills": "graph-of-skills-dependency-retrieval",
    "r3-skill": "r3-skill-compatibility-routing",
    "skillsbench": "skillsbench-agent-skills-benchmark",
    "swe-skills-bench": "swe-skills-bench-utility-benchmark",
    "wildclawbench": "wildclawbench-native-runtime-evaluation",
    "awesome agent skills catalogs": "awesome-agent-skills-catalogs",
    "externalization in llm agents": "externalization-llm-agents-unified-review",
    "genesis skills": "genesis-skills-osti",
    "agent audit": None,  # no dedicated page known
    "going meta: agent skills for ontologies": None,
    "skills+dspy sdk": "dspy-agent-skills-bundle",
    # papers
    "sc25 revolution paper": "sc25-autonomous-science-workflows",
    "scaince paper": "scaince-ai-lab-automation",
    "sok: agentic skills (new iteration 36)": "sok-agentic-skills-beyond-tool-use",
}

MD_LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")


def load_fm(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines(keepends=True)
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text
    fm = yaml.safe_load("".join(lines[1:end])) or {}
    if not isinstance(fm, dict):
        fm = {}
    body = "".join(lines[end + 1 :])
    return fm, body


def dump_fm(fm: dict[str, Any], body: str) -> str:
    ordered: dict[str, Any] = {}
    for key in (
        "type",
        "title",
        "description",
        "resource",
        "tags",
        "timestamp",
        "date",
        "okf_version",
    ):
        if key in fm and fm[key] is not None:
            ordered[key] = fm[key]
    for k, v in fm.items():
        if k not in ordered and v is not None:
            ordered[k] = v
    dumped = yaml.safe_dump(
        ordered,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).strip()
    body = body.lstrip("\n")
    return f"---\n{dumped}\n---\n\n{body}"


def concept_index() -> dict[str, tuple[Path, str, str]]:
    """stem -> (path, title, kind) kind in examples|papers|tools|concepts."""
    out: dict[str, tuple[Path, str, str]] = {}
    for kind, sub in [
        ("examples", "examples"),
        ("papers", "papers"),
        ("tools", "tools"),
        ("concepts", "concepts"),
    ]:
        d = WIKI / sub
        if not d.is_dir():
            continue
        for p in d.glob("*.md"):
            if p.name in ("index.md", "README.md", "log.md"):
                continue
            fm, body = load_fm(p.read_text(encoding="utf-8"))
            title = str(fm.get("title") or "").strip()
            if not title:
                m = re.search(r"^#\s+(.+)$", body, re.M)
                title = m.group(1).strip() if m else p.stem
            out[p.stem] = (p, title, kind)
    return out


def norm(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[*_`]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s


def extract_catalog_name(line: str) -> str | None:
    """From a bullet line, extract the leading name before em dash / description."""
    m = re.match(r"^-\s+(.*)$", line)
    if not m:
        return None
    rest = m.group(1).strip()
    # already fully linked name? still parse
    # **Name** or Name before — or (NEW
    # Strip leading markdown link if present for re-process
    link_m = re.match(r"^\[([^\]]+)\]\([^)]+\)\s*(.*)$", rest)
    if link_m:
        return re.sub(r"[*_]", "", link_m.group(1)).strip()

    # **Name** ...
    bold = re.match(r"^\*\*([^*]+)\*\*", rest)
    if bold:
        name = bold.group(1).strip()
        # drop (NEW Iteration N)
        name = re.sub(r"\s*\(NEW Iteration \d+\)\s*$", "", name, flags=re.I).strip()
        return name

    # Name — description
    if "—" in rest:
        return rest.split("—", 1)[0].strip().strip("*")
    if " - " in rest:
        return rest.split(" - ", 1)[0].strip().strip("*")
    return rest[:80].strip("*")


def resolve_name(
    name: str, index: dict[str, tuple[Path, str, str]]
) -> tuple[str, Path, str] | None:
    """Return (stem, path, kind) or None."""
    n = norm(name)
    n = re.sub(r"\s*\(new iteration \d+\)\s*", "", n, flags=re.I).strip()
    n = re.sub(r"\s*\(iteration \d+\)\s*", "", n, flags=re.I).strip()

    # alias exact
    if n in ALIASES:
        stem = ALIASES[n]
        if stem is None:
            return None
        if stem in index:
            p, title, kind = index[stem]
            return stem, p, kind
        # tools may be only in tools/
        return None

    # stem exact
    stem_guess = re.sub(r"[^a-z0-9]+", "-", n).strip("-")
    if stem_guess in index:
        p, title, kind = index[stem_guess]
        return stem_guess, p, kind

    # title exact / startswith
    for stem, (p, title, kind) in index.items():
        tn = norm(title)
        if tn == n or tn.startswith(n) or n.startswith(tn[: max(12, len(n) // 2)]):
            if len(n) >= 4:
                return stem, p, kind

    # alias partial: longest alias key contained in name or vice versa
    best = None
    best_len = 0
    for key, stem in ALIASES.items():
        if stem is None or stem not in index:
            continue
        if key in n or n in key:
            if len(key) > best_len:
                best_len = len(key)
                best = stem
    if best and best_len >= 4:
        p, title, kind = index[best]
        return best, p, kind

    # token: first significant token matches stem start
    token = re.split(r"[\s/:]+", n)[0]
    if len(token) >= 5:
        cands = [s for s in index if s.startswith(token) or token in s]
        if len(cands) == 1:
            stem = cands[0]
            p, title, kind = index[stem]
            return stem, p, kind

    return None


def linkify_skill_bundles(dry_run: bool) -> dict[str, Any]:
    path = WIKI / "skill-bundles.md"
    text = path.read_text(encoding="utf-8")
    index = concept_index()
    # include tools agensi
    tools = WIKI / "tools" / "agensi-marketplace-landscape.md"
    if tools.exists() and "agensi-marketplace-landscape" not in index:
        fm, body = load_fm(tools.read_text())
        title = str(fm.get("title") or "Agensi Marketplace Landscape")
        index["agensi-marketplace-landscape"] = (tools, title, "tools")

    lines = text.splitlines()
    linked = 0
    unmatched: list[str] = []
    # Only transform Documented Examples section through before "## Patterns" or similar deep sections
    # Heuristic: linkify list items under "## Documented Examples" until "## Patterns" / "## Emerging" / "## Key Insights"
    in_catalog = False
    stop_headers = {
        "## Patterns Observed",
        "## Emerging Patterns",
        "## Pattern",
        "## Composition Patterns",
        "## Key Insights",
        "## Context Element",
        "## How Skill Bundles",
        "## Research Gaps",
        "## Tomorrow",
        "## Citations",
        "## Related",
    }

    new_lines: list[str] = []
    for line in lines:
        if line.startswith("## Documented Examples"):
            in_catalog = True
            new_lines.append(line)
            continue
        if in_catalog and line.startswith("## "):
            # check stop
            if any(line.startswith(h) for h in stop_headers) or (
                line.startswith("## ") and "Documented" not in line and "Paper" not in line
            ):
                # Allow ### subsections inside Documented Examples
                pass
            if line.startswith("## ") and not line.startswith("###"):
                # leaving catalog major section if not Documented
                if "Documented" not in line and "Examples" not in line:
                    in_catalog = False

        if not in_catalog or not line.startswith("- "):
            new_lines.append(line)
            continue

        # skip pattern insight bullets deep in file that aren't catalog - we're in_catalog
        if "](examples/" in line or "](papers/" in line or "](tools/" in line:
            new_lines.append(line)
            continue

        name = extract_catalog_name(line)
        if not name:
            new_lines.append(line)
            continue

        resolved = resolve_name(name, index)
        if not resolved:
            unmatched.append(line[:120])
            new_lines.append(line)
            continue

        stem, dest, kind = resolved
        rel = f"{kind}/{dest.name}"
        # rebuild line: - [**Name**](path) rest
        m = re.match(r"^-\s+(.*)$", line)
        rest = m.group(1) if m else line[2:]
        # If already has a link at start, replace target
        if rest.startswith("["):
            # replace first link target
            rest2 = re.sub(
                r"^\[([^\]]+)\]\([^)]+\)",
                lambda mm: f"[{mm.group(1)}]({rel})",
                rest,
                count=1,
            )
            new_line = f"- {rest2}"
        else:
            bold = re.match(r"^(\*\*[^*]+\*\*)(\s*.*)$", rest)
            if bold:
                label = bold.group(1)
                tail = bold.group(2)
                new_line = f"- [{label}]({rel}){tail}"
            else:
                # Name — desc
                if "—" in rest:
                    head, tail = rest.split("—", 1)
                    head = head.strip()
                    new_line = f"- [{head}]({rel}) —{tail}"
                else:
                    new_line = f"- [{name}]({rel}) — {rest[len(name):].lstrip(' —-')}"
        if new_line != line:
            linked += 1
        new_lines.append(new_line)

    new_text = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
    if not dry_run and new_text != text:
        path.write_text(new_text, encoding="utf-8")

    # Second pass: also link paper notes section if present as plain text
    return {
        "linked_bullets": linked,
        "unmatched": unmatched,
        "changed": new_text != text,
    }


def regenerate_indexes(dry_run: bool) -> list[str]:
    written = []
    sections = {
        "examples": "Skill Bundle Examples",
        "concepts": "Concepts",
        "papers": "Papers",
        "tools": "Tools",
        "daily-digests": "Daily Digests",
        "qa": "Q&A",
    }
    for dirname, heading in sections.items():
        d = WIKI / dirname
        if not d.is_dir():
            continue
        reverse = dirname in ("daily-digests", "qa")
        files = sorted(
            [f for f in d.glob("*.md") if f.name not in ("index.md", "log.md", "README.md")],
            key=lambda p: p.name,
            reverse=reverse,
        )
        lines = [f"# {heading}", "", "Progressive disclosure listing for this directory.", ""]
        for f in files:
            fm, body = load_fm(f.read_text(encoding="utf-8"))
            title = str(fm.get("title") or "").strip()
            if not title:
                m = re.search(r"^#\s+(.+)$", body, re.M)
                title = m.group(1).strip() if m else f.stem
            desc = str(fm.get("description") or "").strip()
            entry = f"* [{title}]({f.name})"
            if desc:
                # plain text desc, cap length
                desc = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", desc)
                if len(desc) > 200:
                    desc = desc[:197] + "..."
                entry += f" - {desc}"
            lines.append(entry)
        lines.append("")
        content = "\n".join(lines) + "\n"
        out = d / "index.md"
        if not dry_run:
            out.write_text(content, encoding="utf-8")
        written.append(str(out.relative_to(REPO)))
    return written


def ensure_digest_example_links(dry_run: bool) -> dict[str, Any]:
    """For each daily digest, ensure examples created that day (or listed) are linked."""
    index = concept_index()
    example_by_stem = {s: p for s, (p, t, k) in index.items() if k == "examples"}
    digests_dir = WIKI / "daily-digests"
    updated = 0
    details = []

    for digest in sorted(digests_dir.glob("*.md")):
        if digest.name in ("index.md", "README.md"):
            continue
        # date prefix
        m = re.match(r"(\d{4}-\d{2}-\d{2})", digest.stem)
        if not m:
            continue
        date = m.group(1)
        text = digest.read_text(encoding="utf-8")
        fm, body = load_fm(text)

        # Find example stems for THIS digest day — conservative matching
        candidates: set[str] = set()

        # 1) Examples whose frontmatter date matches digest date (strongest signal)
        for stem, (epath, title, kind) in index.items():
            if kind != "examples":
                continue
            efm, _ = load_fm(epath.read_text(encoding="utf-8"))
            ed = str(efm.get("date") or efm.get("timestamp") or "")[:10]
            if ed == date:
                candidates.add(stem)

        # 2) Explicit "New examples" / "Wiki Updates" lines only
        for line in body.splitlines():
            if not re.search(
                r"(?i)new examples?|wiki updates|examples created|created examples|wiki updates today",
                line,
            ):
                continue
            for stem in example_by_stem:
                if stem in line:
                    candidates.add(stem)
            for lm in MD_LINK_RE.finditer(line):
                url = lm.group(2).split("#")[0]
                if url.endswith(".md"):
                    st = Path(url).stem
                    if st in example_by_stem:
                        candidates.add(st)
            # alias keys appearing on the same line
            low = line.lower()
            for key, stem in ALIASES.items():
                if stem and stem in example_by_stem and len(key) >= 5 and key in low:
                    candidates.add(stem)

        # 3) Sources section: numbered items with distinctive product names (alias keys ≥ 6)
        in_sources = False
        for line in body.splitlines():
            if re.match(r"(?i)^##\s+sources", line):
                in_sources = True
                continue
            if in_sources and line.startswith("## "):
                in_sources = False
            if not in_sources:
                continue
            low = line.lower()
            for key, stem in ALIASES.items():
                if not stem or stem not in example_by_stem:
                    continue
                if len(key) >= 6 and key in low:
                    candidates.add(stem)

        # Already linked?
        already = set()
        for lm in MD_LINK_RE.finditer(text):
            url = lm.group(2).split("#")[0]
            if "examples/" in url or url.endswith(".md"):
                already.add(Path(url).stem)

        missing = sorted(s for s in candidates if s in example_by_stem and s not in already)
        if not missing:
            continue

        # Append a Wiki Links section if needed
        link_lines = []
        for stem in missing:
            epath, title, _ = index[stem]
            rel = f"../examples/{epath.name}"
            link_lines.append(f"- [{title}]({rel})")

        addition = "\n## Linked Examples\n\n" + "\n".join(link_lines) + "\n"
        if "## Linked Examples" in body:
            # merge into existing section
            parts = body.split("## Linked Examples", 1)
            head, tail = parts[0], parts[1]
            # find end of section
            rest_m = re.search(r"\n## ", tail[1:] if tail.startswith("\n") else tail)
            # simpler: append missing links after header
            if rest_m:
                pass
            # replace section entirely
            sec_m = re.search(
                r"(## Linked Examples\n)(.*?)(?=\n## |\Z)", body, re.S
            )
            if sec_m:
                existing = sec_m.group(0)
                new_sec = "## Linked Examples\n\n" + "\n".join(link_lines) + "\n"
                # keep any already linked plus missing
                for lm in MD_LINK_RE.finditer(existing):
                    url = lm.group(2).split("#")[0]
                    st = Path(url).stem
                    if st in example_by_stem and st not in missing:
                        epath, title, _ = index[st]
                        line = f"- [{title}](../examples/{epath.name})"
                        if line not in link_lines:
                            link_lines.insert(0, line)
                new_sec = "## Linked Examples\n\n" + "\n".join(link_lines) + "\n"
                body = body[: sec_m.start()] + new_sec + body[sec_m.end() :]
            else:
                body = body.rstrip() + addition
        else:
            body = body.rstrip() + "\n" + addition

        new_text = dump_fm(fm, body) if fm else body
        if not dry_run:
            digest.write_text(new_text if new_text.endswith("\n") else new_text + "\n", encoding="utf-8")
        updated += 1
        details.append((digest.name, missing))

    return {"digests_updated": updated, "details": details}


def link_qa_from_digests_and_index(dry_run: bool) -> dict[str, Any]:
    qa_dir = WIKI / "qa"
    qa_files = sorted(
        [p for p in qa_dir.glob("*.md") if p.name not in ("index.md", "README.md")],
        key=lambda p: p.name,
        reverse=True,
    )
    # map date -> all matching qa files
    qa_by_date: dict[str, list[Path]] = {}
    for p in qa_files:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", p.stem)
        if m:
            qa_by_date.setdefault(m.group(1), []).append(p)

    digests_updated = 0
    for digest in (WIKI / "daily-digests").glob("*.md"):
        if digest.name in ("index.md", "README.md"):
            continue
        m = re.match(r"(\d{4}-\d{2}-\d{2})", digest.stem)
        if not m:
            continue
        date = m.group(1)
        qas = list(qa_by_date.get(date, []))
        # also any qa stem containing this date not already listed
        for p in qa_files:
            if date in p.stem and p not in qas:
                qas.append(p)
        if not qas:
            continue
        text = digest.read_text(encoding="utf-8")
        fm, body = load_fm(text)
        missing_lines = []
        for qa in qas:
            rel = f"../qa/{qa.name}"
            if rel in text or qa.name in text:
                continue
            qfm, _ = load_fm(qa.read_text(encoding="utf-8"))
            qtitle = str(qfm.get("title") or qa.stem)
            missing_lines.append(f"- [{qtitle}]({rel})")
        if not missing_lines:
            continue
        if "## Q&A" in body:
            # append missing bullets into existing section
            sec_m = re.search(r"(## Q&A\n)(.*?)(?=\n## |\Z)", body, re.S)
            if sec_m:
                new_sec = sec_m.group(1) + sec_m.group(2).rstrip() + "\n" + "\n".join(missing_lines) + "\n"
                body = body[: sec_m.start()] + new_sec + body[sec_m.end() :]
            else:
                body = body.rstrip() + "\n" + "\n".join(missing_lines) + "\n"
        else:
            body = body.rstrip() + "\n\n## Q&A\n\n" + "\n".join(missing_lines) + "\n"
        new_text = dump_fm(fm, body) if fm else body
        if not dry_run:
            digest.write_text(new_text if new_text.endswith("\n") else new_text + "\n", encoding="utf-8")
        digests_updated += 1

    # Root index: ensure all Q&A files appear under Quick Links
    index_path = WIKI / "index.md"
    idx = index_path.read_text(encoding="utf-8")
    changed_idx = False
    missing_qa_lines = []
    for p in qa_files:
        if f"qa/{p.name}" not in idx:
            qfm, _ = load_fm(p.read_text(encoding="utf-8"))
            title = str(qfm.get("title") or p.stem)
            missing_qa_lines.append(f"  - [{title}](qa/{p.name})")
    if missing_qa_lines:
        block = "\n".join(missing_qa_lines)
        if "- [Q&A](qa/)" in idx:
            # insert after Q&A header line (and any existing children)
            # find Q&A block end: next non-indented list item or blank+##
            idx2 = idx
            marker = "- [Q&A](qa/)"
            pos = idx2.find(marker)
            if pos >= 0:
                # find end of indented children
                rest = idx2[pos + len(marker) :]
                lines = rest.splitlines(keepends=True)
                insert_at = 0
                for i, ln in enumerate(lines):
                    if ln.startswith("  - "):
                        insert_at = i + 1
                        continue
                    if ln.strip() == "":
                        insert_at = i
                        break
                    if ln.startswith("- ") or ln.startswith("##") or ln.startswith("* "):
                        insert_at = i
                        break
                    insert_at = i
                    break
                new_rest = (
                    "".join(lines[:insert_at])
                    + ("\n" if insert_at == 0 else "")
                    + block
                    + "\n"
                    + "".join(lines[insert_at:])
                )
                idx = idx2[: pos + len(marker)] + new_rest
                changed_idx = True
    if changed_idx and not dry_run:
        index_path.write_text(idx if idx.endswith("\n") else idx + "\n", encoding="utf-8")

    return {
        "digests_with_qa_links": digests_updated,
        "root_index_updated": changed_idx,
        "qa_count": len(qa_files),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("=== 1. Link skill-bundles.md catalog ===")
    r1 = linkify_skill_bundles(args.dry_run)
    print(f"  linked bullets: {r1['linked_bullets']}, changed={r1['changed']}")
    print(f"  unmatched: {len(r1['unmatched'])}")
    for u in r1["unmatched"][:25]:
        print(f"    ? {u}")

    print("=== 2. Regenerate subdirectory indexes ===")
    written = regenerate_indexes(args.dry_run)
    for w in written:
        print(f"  {w}")

    print("=== 3. Daily digest → example links ===")
    r3 = ensure_digest_example_links(args.dry_run)
    print(f"  digests updated: {r3['digests_updated']}")
    for name, missing in r3["details"][:15]:
        print(f"    {name}: +{len(missing)} links")

    print("=== 4. Q&A links from digests + root index ===")
    r4 = link_qa_from_digests_and_index(args.dry_run)
    print(
        f"  digests+qa: {r4['digests_with_qa_links']}, "
        f"root_index: {r4['root_index_updated']}, qa_files: {r4['qa_count']}"
    )

    print("Done." + (" (dry-run)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
