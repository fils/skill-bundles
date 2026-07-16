#!/usr/bin/env python3
"""
One-shot migration: Karpathy/Obsidian LLM wiki → OKF v0.1 Knowledge Bundle.

- Ensures YAML frontmatter with required `type` on every concept document
- Converts [[wikilinks]] to relative standard markdown links
- Generates subdirectory index.md files and optional root log.md
- Adds okf_version to root wiki/index.md

Usage:
  python3 scripts/convert-to-okf.py           # apply changes
  python3 scripts/convert-to-okf.py --dry-run # report only
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"
RESERVED = {"index.md", "log.md"}

TYPE_BY_DIR = {
    "examples": "Skill Bundle Example",
    "concepts": "Concept",
    "papers": "Paper",
    "tools": "Tool",
    "daily-digests": "Daily Digest",
    "qa": "Q&A",
    "case-studies": "Case Study",
    "visualizations": "Visualization",
}

TYPE_BY_ROOT_FILE = {
    "skill-bundles.md": "Publication",
    "metrics.md": "Metrics",
}

# Known broken/alias stems → canonical file stem
STEM_ALIASES = {
    "addyosmani-agent-skills": "addyosmani-engineering-skills",
    "agent-skills-catalogs": "awesome-agent-skills-catalogs",
    "agentskills-io-specification": "agent-skills-spec",
    "agentskills-spec": "agent-skills-spec",
    "agentskills.io": "agent-skills-spec",
    "anthropic-official-skills": "anthropic-official-skills-repo",
    "nemo-claw": "nemoclaw-security-scanner",
    "nora-night-owl-research-agent": "nora-gis-research-agent",
    "nvidia-verified-skills": "nvidia-verified-agent-skills",
    "volt-agent-awesome-agent-skills": "awesome-agent-skills-catalogs",
    "shacl-agent-instruction": "shacl-1-2-spec",
    "shacl": "shacl-1-2-spec",
    "sssom": "sssom-mapping-protocol",
    "concepts": None,  # drop / plain text
    "examples": None,
    "examples/": None,
}

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
H1_RE = re.compile(r"^#\s+(.+)$", re.M)
DATE_BOLD_RE = re.compile(
    r"\*\*Date(?:\s+Added)?:\*\*\s*(\d{4}-\d{2}-\d{2})", re.I
)
DATE_FIELD_RE = re.compile(r"(?m)^date:\s*[\"']?(\d{4}-\d{2}-\d{2})")
URL_RE = re.compile(r"https?://[^\s\)\]\"']+")
ARXIV_RE = re.compile(r"(?:arXiv:|arxiv\.org/(?:abs|pdf)/)(\d{4}\.\d{4,5})", re.I)


def load_yaml_frontmatter(text: str) -> tuple[dict[str, Any] | None, str]:
    """Return (frontmatter_dict or None, body)."""
    if not text.startswith("---"):
        return None, text
    # Must be --- on first line
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text
    raw_fm = "".join(lines[1:end])
    body = "".join(lines[end + 1 :])
    try:
        data = yaml.safe_load(raw_fm) or {}
        if not isinstance(data, dict):
            data = {"_raw": data}
    except yaml.YAMLError:
        # Keep unparsed as opaque; rebuild later with type only
        data = {}
    return data, body


def dump_frontmatter(data: dict[str, Any]) -> str:
    # Prefer readable block style for lists; keep key order roughly logical
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
        if key in data and data[key] is not None:
            ordered[key] = data[key]
    for key, val in data.items():
        if key not in ordered and val is not None:
            ordered[key] = val
    dumped = yaml.safe_dump(
        ordered,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).strip()
    return f"---\n{dumped}\n---\n"


def infer_type(path: Path) -> str:
    rel = path.relative_to(WIKI)
    if path.name in TYPE_BY_ROOT_FILE:
        return TYPE_BY_ROOT_FILE[path.name]
    if len(rel.parts) > 1:
        return TYPE_BY_DIR.get(rel.parts[0], "Reference")
    return "Reference"


def extract_title(fm: dict[str, Any], body: str, path: Path) -> str:
    if fm.get("title"):
        return str(fm["title"]).strip()
    m = H1_RE.search(body)
    if m:
        return m.group(1).strip()
    return path.stem.replace("-", " ").title()


def extract_description(fm: dict[str, Any], body: str) -> str | None:
    existing = fm.get("description")
    if existing:
        desc = str(existing).strip()
        bad = (
            not desc
            or "[[" in desc
            or desc.startswith("- http")
            or re.match(r"^\d+\.?$", desc)
            or len(desc) < 12
        )
        if not bad:
            return desc
        # Fall through to re-derive if description is polluted / placeholder
    # First non-empty prose paragraph after headings/bold meta
    lines = body.splitlines()
    buf: list[str] = []
    started = False
    for line in lines:
        s = line.strip()
        if not s:
            if started and buf:
                break
            continue
        if s.startswith("#") or s.startswith("|") or s.startswith("!") or s.startswith("---"):
            if started and buf:
                break
            continue
        if s.startswith("**") and s.endswith("**") and len(s) < 80:
            continue
        if re.match(r"^\*\*[^*]+:\*\*", s):
            continue
        # Skip bare URL / source list lines / thin numbered placeholders
        if s.startswith("- http") or s.startswith("http") or s.startswith("> **"):
            continue
        if re.match(r"^\d+\.$", s) or re.match(r"^\d+\.\s*$", s):
            continue
        if s.startswith("- ") and ("http" in s or s.startswith("- **")):
            # Prefer real overview later; skip meta bullets
            if "http" in s or re.match(r"^- \*\*[^*]+\*\*", s):
                continue
        # Prefer digest source lines / overview paragraphs over bare numbers
        if re.match(r"^\d+\.\s+\*\*", s):
            # Daily digest source entry — take the substance after em dash if present
            if "—" in s:
                s = s.split("—", 1)[1].strip()
            elif " - " in s:
                s = s.split(" - ", 1)[1].strip()
            else:
                s = re.sub(r"^\d+\.\s+\*\*[^*]+\*\*\s*", "", s).strip(" —-")
        started = True
        buf.append(s)
        if len(" ".join(buf)) > 160:
            break
    if not buf:
        if existing and str(existing).strip() not in {"1.", "1"}:
            return str(existing).strip()
        return None
    desc = " ".join(buf)
    # Single sentence preference
    if ". " in desc:
        desc = desc.split(". ")[0] + "."
    if len(desc) > 220:
        desc = desc[:217].rstrip() + "..."
    return desc


def sanitize_fm_value(val: Any, source: Path, stem_index: dict[str, Path]) -> Any:
    """Convert residual [[wikilinks]] inside frontmatter strings/lists."""
    if isinstance(val, str):
        new, _ = convert_wikilinks(val, source, stem_index)
        # Descriptions should be plain text — strip markdown links to display text
        return new
    if isinstance(val, list):
        return [sanitize_fm_value(v, source, stem_index) for v in val]
    if isinstance(val, dict):
        return {k: sanitize_fm_value(v, source, stem_index) for k, v in val.items()}
    return val


def plain_description(text: str) -> str:
    """Turn markdown links in a description into plain display text for index snippets."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_resource(fm: dict[str, Any], body: str) -> str | None:
    if fm.get("resource"):
        return str(fm["resource"])
    # Prefer arxiv abs URL
    sources = fm.get("sources") or fm.get("source")
    candidates: list[str] = []
    if isinstance(sources, list):
        candidates.extend(str(s) for s in sources)
    elif isinstance(sources, str):
        candidates.append(sources)
    if fm.get("arxiv"):
        candidates.append(f"https://arxiv.org/abs/{fm['arxiv']}")
    candidates.extend(URL_RE.findall(body[:3000]))
    for c in candidates:
        m = ARXIV_RE.search(c)
        if m:
            return f"https://arxiv.org/abs/{m.group(1)}"
    for c in candidates:
        if c.startswith("http"):
            return c
    return None


def extract_timestamp(fm: dict[str, Any], body: str, path: Path) -> str | None:
    if fm.get("timestamp"):
        return str(fm["timestamp"])
    date_val = fm.get("date")
    if date_val:
        s = str(date_val)[:10]
        if re.match(r"\d{4}-\d{2}-\d{2}", s):
            return f"{s}T00:00:00Z"
    m = DATE_FIELD_RE.search(yaml.safe_dump(fm) if fm else "")
    if m:
        return f"{m.group(1)}T00:00:00Z"
    m = DATE_BOLD_RE.search(body)
    if m:
        return f"{m.group(1)}T00:00:00Z"
    # daily digests / qa filenames
    m = re.match(r"(\d{4}-\d{2}-\d{2})", path.stem)
    if m:
        return f"{m.group(1)}T00:00:00Z"
    return None


def ensure_date_field(fm: dict[str, Any], timestamp: str | None) -> None:
    if fm.get("date") or not timestamp:
        return
    fm["date"] = timestamp[:10]


def build_stem_index() -> dict[str, Path]:
    """stem -> absolute path for concept files (unique)."""
    index: dict[str, Path] = {}
    for f in WIKI.rglob("*.md"):
        if f.name in RESERVED or f.name == "README.md":
            continue
        if f.stem in index:
            raise SystemExit(f"Stem collision: {f.stem}: {index[f.stem]} vs {f}")
        index[f.stem] = f
    return index


def resolve_wikilink_target(
    raw: str, source: Path, stem_index: dict[str, Path]
) -> tuple[str | None, str]:
    """
    Returns (relative_url or None if drop, display_text).
    None url means remove link markup and keep display text only.
    """
    inner = raw.strip()
    display = None
    target = inner
    if "|" in inner:
        target, display = inner.split("|", 1)
        target, display = target.strip(), display.strip()
    # anchors
    anchor = ""
    if "#" in target and not target.startswith("../") and not target.startswith("./"):
        # only split if not a path with weirdness — still allow path#anchor
        parts = target.split("#", 1)
        target, anchor = parts[0], "#" + parts[1]

    if target.lower() == "backlinks" or target == "backlinks":
        return None, ""

    # Path-like targets (raw files, dirs)
    if target.startswith("../") or target.startswith("./") or target.startswith("/"):
        display = display or Path(target).stem.replace("-", " ")
        # Normalize paths that intended to point at repo raw/ from wiki/**
        m_raw = re.search(r"(raw/.+)$", target)
        if m_raw:
            abs_raw = REPO / m_raw.group(1)
            if abs_raw.exists():
                rel = os_relpath(abs_raw, source.parent).replace("\\", "/")
                return rel + (anchor if anchor else ""), display
        cand = (source.parent / target).resolve()
        if cand.exists():
            rel = os_relpath(cand, source.parent).replace("\\", "/")
            return rel + (anchor if anchor else ""), display
        # Keep original relative form even if missing
        return target + (anchor if anchor else ""), display

    if "/" in target:
        # e.g. concepts/ontology-as-skill-context
        candidate = WIKI / f"{target}.md"
        if candidate.exists():
            rel = os_relpath(candidate, source.parent).replace("\\", "/")
            display = display or candidate.stem.replace("-", " ")
            return rel + anchor, display
        # directory
        if (WIKI / target.rstrip("/")).is_dir():
            display = display or target.rstrip("/")
            rel = os_relpath(WIKI / target.rstrip("/"), source.parent).replace("\\", "/")
            return rel + "/", display
        display = display or target
        return None, display

    # Alias map
    mapped = STEM_ALIASES.get(target, STEM_ALIASES.get(target.lower(), "UNSET"))
    if mapped != "UNSET":
        if mapped is None:
            return None, display or target.replace("-", " ")
        target = mapped

    dest = stem_index.get(target)
    if dest is None:
        # try case-insensitive
        lower_map = {k.lower(): v for k, v in stem_index.items()}
        dest = lower_map.get(target.lower())
    if dest is None:
        return None, display or target.replace("-", " ")

    rel = os_relpath(dest, source.parent).replace("\\", "/")
    if display is None:
        # prefer title from file later — use stem humanized for speed
        display = dest.stem.replace("-", " ")
    return rel + anchor, display


def os_relpath(target: Path, start: Path) -> str:
    import os

    return os.path.relpath(str(target), str(start))


def convert_wikilinks(text: str, source: Path, stem_index: dict[str, Path]) -> tuple[str, list[str]]:
    unresolved: list[str] = []

    def repl(m: re.Match[str]) -> str:
        raw = m.group(1)
        url, display = resolve_wikilink_target(raw, source, stem_index)
        if url is None:
            if not display:
                return ""
            unresolved.append(raw)
            return display
        # Check destination exists for non-external
        if not url.startswith("http"):
            dest_path = (source.parent / url.split("#")[0]).resolve()
            if not dest_path.exists() and not str(url).endswith("/"):
                unresolved.append(raw)
        # Escape display brackets
        display = display.replace("[", "\\[").replace("]", "\\]")
        return f"[{display}]({url})"

    return WIKILINK_RE.sub(repl, text), unresolved


def convert_concept_file(
    path: Path, stem_index: dict[str, Path], dry_run: bool
) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    fm, body = load_yaml_frontmatter(text)
    if fm is None:
        fm = {}

    original = text
    fm["type"] = fm.get("type") or infer_type(path)
    title = extract_title(fm, body, path)
    fm["title"] = title
    # Convert body first so description extraction can use clean prose if we re-derive
    new_body, unresolved = convert_wikilinks(body, path, stem_index)
    new_body = re.sub(r"[ \t]+\n", "\n", new_body)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)

    desc = extract_description(fm, new_body)
    if desc:
        # Prefer plain-text descriptions (no nested wikilinks / heavy markup)
        desc = plain_description(desc)
        desc, _ = convert_wikilinks(desc, path, stem_index)
        fm["description"] = plain_description(desc)
    resource = extract_resource(fm, new_body)
    if resource:
        fm["resource"] = resource
    ts = extract_timestamp(fm, new_body, path)
    if ts:
        fm["timestamp"] = ts
        ensure_date_field(fm, ts)

    # Sanitize any remaining wikilinks in extension fields
    for key in list(fm.keys()):
        fm[key] = sanitize_fm_value(fm[key], path, stem_index)

    new_text = dump_frontmatter(fm) + (new_body if new_body.startswith("\n") else "\n" + new_body)
    if not new_text.endswith("\n"):
        new_text += "\n"

    changed = new_text != original
    if changed and not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return {
        "path": str(path.relative_to(REPO)),
        "changed": changed,
        "type": fm["type"],
        "unresolved": unresolved,
    }


def convert_index_file(path: Path, stem_index: dict[str, Path], dry_run: bool) -> dict[str, Any]:
    """Indexes: convert wikilinks; root index may keep/add okf_version only."""
    text = path.read_text(encoding="utf-8")
    original = text
    is_root = path.resolve() == (WIKI / "index.md").resolve()

    fm, body = load_yaml_frontmatter(text)
    if is_root:
        # Only okf_version allowed in root index frontmatter per OKF §11
        content = body if fm is not None else text
        new_body, unresolved = convert_wikilinks(content, path, stem_index)
        new_text = dump_frontmatter({"okf_version": "0.1"}) + (
            new_body if new_body.startswith("\n") else "\n" + new_body
        )
    else:
        # Subdir index: no frontmatter
        content = body if fm is not None else text
        new_body, unresolved = convert_wikilinks(content, path, stem_index)
        new_text = new_body.lstrip("\n")
        if not new_text.endswith("\n"):
            new_text += "\n"

    if not new_text.endswith("\n"):
        new_text += "\n"
    changed = new_text != original
    if changed and not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return {
        "path": str(path.relative_to(REPO)),
        "changed": changed,
        "type": "index",
        "unresolved": unresolved,
    }


def read_title_desc(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    fm, body = load_yaml_frontmatter(text)
    fm = fm or {}
    title = str(fm.get("title") or "").strip() or extract_title({}, body, path)
    desc = str(fm.get("description") or "").strip()
    if not desc or "[[" in desc:
        d = extract_description({}, body)
        desc = d or desc
    desc = plain_description(desc)
    return title, desc


def generate_subdir_indexes(dry_run: bool) -> list[str]:
    written: list[str] = []
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
        files = sorted(
            [f for f in d.glob("*.md") if f.name not in RESERVED and f.name != "README.md"],
            key=lambda p: p.name,
            reverse=(dirname in ("daily-digests", "qa")),
        )
        lines = [f"# {heading}", "", "Progressive disclosure listing for this directory.", ""]
        for f in files:
            title, desc = read_title_desc(f)
            entry = f"* [{title}]({f.name})"
            if desc:
                entry += f" - {desc}"
            lines.append(entry)
        lines.append("")
        content = "\n".join(lines)
        out = d / "index.md"
        if not dry_run:
            out.write_text(content, encoding="utf-8")
        written.append(str(out.relative_to(REPO)))
        # Fold digests README into index; leave README as pointer if present
        readme = d / "README.md"
        if readme.exists() and not dry_run:
            readme.write_text(
                f"# {heading}\n\nSee [index.md](index.md) for the OKF directory listing.\n",
                encoding="utf-8",
            )
    return written


def generate_log(dry_run: bool) -> str:
    """Thin log from daily digests, newest first."""
    digests = sorted(
        (WIKI / "daily-digests").glob("*.md"),
        key=lambda p: p.name,
        reverse=True,
    )
    digests = [d for d in digests if d.name not in RESERVED and d.name != "README.md"]
    lines = ["# Directory Update Log", ""]
    for d in digests:
        date = d.stem[:10]
        if not re.match(r"\d{4}-\d{2}-\d{2}", date):
            continue
        title, desc = read_title_desc(d)
        lines.append(f"## {date}")
        summary = desc or title
        rel = f"daily-digests/{d.name}"
        lines.append(f"* **Update**: [{title}]({rel}) — {summary}")
        lines.append("")
    content = "\n".join(lines)
    out = WIKI / "log.md"
    if not dry_run:
        out.write_text(content if content.endswith("\n") else content + "\n", encoding="utf-8")
    return str(out.relative_to(REPO))


def augment_root_index_catalog(dry_run: bool) -> None:
    """Ensure root index has progressive-disclosure sections for subdirs."""
    path = WIKI / "index.md"
    text = path.read_text(encoding="utf-8")
    catalog = """
## Knowledge Catalog (OKF)

This directory is an [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) Knowledge Bundle. Cross-links use relative markdown paths so they work on GitHub and in OKF consumers.

# Bundle sections

* [Skill Bundle Examples](examples/) - Documented real-world skill bundle case studies
* [Concepts](concepts/) - Atomic notes on patterns, composition, and governance
* [Papers](papers/) - Summarized papers and workshop notes
* [Tools](tools/) - Frameworks, marketplaces, and tooling landscape
* [Daily Digests](daily-digests/) - Chronological research digests
* [Q&A](qa/) - Structured exploration and gap analysis
* [Primary Publication](skill-bundles.md) - Living catalog of examples and patterns
* [Metrics](metrics.md) - KPIs and coverage tracking
* [Update Log](log.md) - Chronological change history

"""
    if "## Knowledge Catalog (OKF)" in text:
        return
    # Insert after Quick Links section if present, else after frontmatter/overview
    if "## Quick Links" in text:
        # append catalog after quick links block (before ## Current Status)
        if "## Current Status" in text:
            text = text.replace("## Current Status", catalog + "## Current Status", 1)
        else:
            text = text.rstrip() + "\n" + catalog
    else:
        fm, body = load_yaml_frontmatter(text)
        if fm is not None:
            text = dump_frontmatter(fm) + "\n" + catalog + body.lstrip("\n")
        else:
            text = catalog + text
    if not dry_run:
        path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not WIKI.is_dir():
        print("wiki/ not found", file=sys.stderr)
        return 1

    stem_index = build_stem_index()
    print(f"Concept files: {len(stem_index)} unique stems")

    results = []
    for path in sorted(WIKI.rglob("*.md")):
        if path.name == "README.md":
            # Convert wikilinks if any; leave as non-concept
            text = path.read_text(encoding="utf-8")
            new_text, _ = convert_wikilinks(text, path, stem_index)
            if new_text != text and not args.dry_run:
                path.write_text(new_text if new_text.endswith("\n") else new_text + "\n")
            continue
        if path.name in RESERVED:
            results.append(convert_index_file(path, stem_index, args.dry_run))
        else:
            results.append(convert_concept_file(path, stem_index, args.dry_run))

    # Indexes need titles from converted files — regenerate after conversion
    if not args.dry_run:
        written = generate_subdir_indexes(args.dry_run)
        log_path = generate_log(args.dry_run)
        # Re-process root index for okf_version + wikilinks (in case indexes added later)
        convert_index_file(WIKI / "index.md", stem_index, args.dry_run)
        augment_root_index_catalog(args.dry_run)
        print(f"Generated indexes: {len(written)}")
        for w in written:
            print(f"  {w}")
        print(f"Generated {log_path}")
    else:
        print("Dry-run: skipping index/log generation writes")

    changed = sum(1 for r in results if r["changed"])
    unresolved_total = []
    for r in results:
        for u in r["unresolved"]:
            unresolved_total.append((r["path"], u))

    print(f"Files processed: {len(results)}")
    print(f"Files changed: {changed}")
    print(f"Unresolved wikilink targets left as plain text: {len(unresolved_total)}")
    # unique unresolved
    uniq = sorted({u for _, u in unresolved_total})
    for u in uniq[:40]:
        print(f"  unresolved: [[{u}]]")
    if args.dry_run:
        print("Dry-run complete (no writes).")
    else:
        print("Conversion complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
