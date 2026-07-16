#!/usr/bin/env python3
"""
OKF v0.1 conformance linter for the wiki/ Knowledge Bundle.

Required checks (OKF §9):
1. Every non-reserved .md file has parseable YAML frontmatter
2. Every frontmatter has non-empty `type`
3. Reserved files index.md / log.md follow structure when present

Soft checks:
- Relative markdown links resolve
- No remaining [[wikilinks]]
- Recommended title/description present
- Primary catalog (skill-bundles.md) bullets without links under Documented Examples
- Examples with low inbound degree (≤1, typically only examples/index.md)
- Examples missing from skill-bundles.md link graph

Usage:
  python3 scripts/okf-lint.py
  python3 scripts/okf-lint.py --strict   # soft failures → exit 1
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import yaml

REPO = Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"
RESERVED = {"index.md", "log.md"}

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
MD_LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`]+`")


def strip_code(text: str) -> str:
    """Remove fenced and inline code so anti-examples like [[wikilink]] don't hard-fail."""
    text = FENCE_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    return text


def load_fm(text: str) -> tuple[dict[str, Any] | None, str, str | None]:
    """Return (fm|None, body, error)."""
    if not text.startswith("---"):
        return None, text, "missing frontmatter delimiter"
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text, "missing frontmatter delimiter"
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text, "unclosed frontmatter"
    raw = "".join(lines[1:end])
    body = "".join(lines[end + 1 :])
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        return None, body, f"YAML parse error: {e}"
    if data is None:
        data = {}
    if not isinstance(data, dict):
        return None, body, "frontmatter is not a mapping"
    return data, body, None


def is_external(url: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="fail on soft issues")
    args = parser.parse_args()

    if not WIKI.is_dir():
        print("wiki/ not found", file=sys.stderr)
        return 1

    hard: list[str] = []
    soft: list[str] = []

    md_files = sorted(WIKI.rglob("*.md"))
    # Ignore README.md as non-OKF helper files
    concept_files = [
        f for f in md_files if f.name not in RESERVED and f.name != "README.md"
    ]
    reserved_files = [f for f in md_files if f.name in RESERVED]

    for path in concept_files:
        rel = path.relative_to(REPO)
        text = path.read_text(encoding="utf-8")
        fm, body, err = load_fm(text)
        if err or fm is None:
            hard.append(f"{rel}: {err or 'missing frontmatter'}")
            continue
        typ = fm.get("type")
        if not typ or not str(typ).strip():
            hard.append(f"{rel}: missing required frontmatter field `type`")
        if not fm.get("title"):
            soft.append(f"{rel}: missing recommended `title`")
        if not fm.get("description"):
            soft.append(f"{rel}: missing recommended `description`")

        for m in WIKILINK_RE.finditer(strip_code(text)):
            hard.append(f"{rel}: residual wikilink [[{m.group(1)}]]")

        for m in MD_LINK_RE.finditer(body):
            url = m.group(2).strip()
            # strip title in quotes
            if " " in url and not url.startswith("<"):
                url = url.split(" ", 1)[0]
            url = url.strip("<>")
            if is_external(url) or url.startswith("#") or url.startswith("mailto:"):
                continue
            if url.startswith("/"):
                soft.append(
                    f"{rel}: absolute link {url!r} (prefer relative for GitHub + monorepo)"
                )
                # still try resolve from wiki root
                target = (WIKI / url.lstrip("/")).resolve()
            else:
                target = (path.parent / unquote(url.split("#")[0])).resolve()
            try:
                target.relative_to(REPO.resolve())
            except ValueError:
                soft.append(f"{rel}: link escapes repo: {url}")
                continue
            if not target.exists():
                soft.append(f"{rel}: broken link -> {url}")

    for path in reserved_files:
        rel = path.relative_to(REPO)
        text = path.read_text(encoding="utf-8")
        is_root_index = path.resolve() == (WIKI / "index.md").resolve()
        fm, body, err = load_fm(text)

        if path.name == "index.md":
            if is_root_index:
                if fm is not None:
                    # only okf_version expected
                    extra = set(fm.keys()) - {"okf_version"}
                    if extra:
                        soft.append(
                            f"{rel}: root index frontmatter has non-okf keys: {sorted(extra)}"
                        )
                    if fm.get("okf_version") != "0.1":
                        soft.append(f"{rel}: recommend okf_version: \"0.1\"")
                else:
                    soft.append(f"{rel}: recommend okf_version frontmatter")
            else:
                if fm is not None and err is None:
                    soft.append(f"{rel}: subdir index should not have frontmatter")
            # structure: should have some markdown links
            if not MD_LINK_RE.search(text):
                soft.append(f"{rel}: index has no markdown links")
        elif path.name == "log.md":
            if fm is not None and err is None and list(fm.keys()):
                soft.append(f"{rel}: log.md should not have concept frontmatter")
            if not re.search(r"(?m)^##\s+\d{4}-\d{2}-\d{2}", text):
                soft.append(f"{rel}: log date headings should be ## YYYY-MM-DD")

        for m in WIKILINK_RE.finditer(strip_code(text)):
            hard.append(f"{rel}: residual wikilink [[{m.group(1)}]]")

    # --- Soft graph / catalog coverage checks ---
    soft.extend(_soft_link_coverage())

    print(f"OKF lint — concepts: {len(concept_files)}, reserved: {len(reserved_files)}")
    print(f"Hard failures: {len(hard)}")
    for h in hard[:50]:
        print(f"  HARD: {h}")
    if len(hard) > 50:
        print(f"  ... and {len(hard) - 50} more")
    print(f"Soft issues: {len(soft)}")
    for s in soft[:40]:
        print(f"  SOFT: {s}")
    if len(soft) > 40:
        print(f"  ... and {len(soft) - 40} more")

    if hard:
        print("FAIL (conformance)")
        return 1
    if args.strict and soft:
        print("FAIL (strict soft issues)")
        return 1
    print("PASS" + (" (with soft issues)" if soft else ""))
    return 0


def _is_external(url: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url))


def _soft_link_coverage() -> list[str]:
    """Catalog completeness + inbound degree soft checks."""
    issues: list[str] = []
    examples_dir = WIKI / "examples"
    if not examples_dir.is_dir():
        return issues

    examples = [
        p
        for p in examples_dir.glob("*.md")
        if p.name not in RESERVED and p.name != "README.md"
    ]
    example_paths = {p.resolve() for p in examples}

    # Inbound degree for every wiki md → examples
    inbound: dict[Path, set[Path]] = defaultdict(set)
    for src in WIKI.rglob("*.md"):
        text = src.read_text(encoding="utf-8", errors="replace")
        for m in MD_LINK_RE.finditer(text):
            url = m.group(2).strip().split()[0].strip("<>")
            if _is_external(url) or url.startswith("#"):
                continue
            path_part = unquote(url.split("#")[0])
            if not path_part or path_part.endswith("/"):
                continue
            if path_part.startswith("/"):
                tgt = (WIKI / path_part.lstrip("/")).resolve()
            else:
                tgt = (src.parent / path_part).resolve()
            if tgt in example_paths and src.resolve() != tgt:
                inbound[tgt].add(src.resolve())

    low_inbound = []
    for p in examples:
        deg = len(inbound.get(p.resolve(), set()))
        if deg <= 1:
            sources = sorted(
                str(s.relative_to(WIKI.resolve()))
                for s in inbound.get(p.resolve(), set())
            )
            low_inbound.append((p.name, deg, sources))
    if low_inbound:
        issues.append(
            f"examples with inbound degree ≤1: {len(low_inbound)} "
            f"(often only examples/index.md) — e.g. {', '.join(x[0] for x in low_inbound[:8])}"
            + ("..." if len(low_inbound) > 8 else "")
        )

    # skill-bundles.md: Documented Examples bullets should be linked
    pub = WIKI / "skill-bundles.md"
    if pub.exists():
        text = pub.read_text(encoding="utf-8")
        in_catalog = False
        unlinked_bullets = 0
        linked_example_stems: set[str] = set()
        for line in text.splitlines():
            if line.startswith("## Documented Examples"):
                in_catalog = True
                continue
            if in_catalog and line.startswith("## ") and not line.startswith("###"):
                if "Documented" not in line:
                    in_catalog = False
            if not in_catalog:
                continue
            if not line.startswith("- "):
                continue
            if "](" not in line:
                # intentional external-only mentions are annotated
                if "no local wiki page" in line.lower():
                    continue
                unlinked_bullets += 1
            for m in MD_LINK_RE.finditer(line):
                url = m.group(2).split("#")[0]
                if "examples/" in url or url.endswith(".md"):
                    linked_example_stems.add(Path(url).stem)

        if unlinked_bullets:
            issues.append(
                f"wiki/skill-bundles.md: {unlinked_bullets} Documented Examples "
                f"bullet(s) still lack markdown links"
            )

        missing_from_pub = sorted(
            p.stem for p in examples if p.stem not in linked_example_stems
        )
        # Meta / research-state notes not required in the living catalog bullets
        allow_missing = {
            "skill-bundles-research-state",
        }
        missing_from_pub = [s for s in missing_from_pub if s not in allow_missing]
        if missing_from_pub:
            issues.append(
                f"wiki/skill-bundles.md does not link {len(missing_from_pub)} example(s): "
                + ", ".join(missing_from_pub[:10])
                + ("..." if len(missing_from_pub) > 10 else "")
            )

    # examples/index must list all examples
    idx = examples_dir / "index.md"
    if idx.exists():
        idx_text = idx.read_text(encoding="utf-8")
        listed = {Path(m.group(2).split("#")[0]).stem for m in MD_LINK_RE.finditer(idx_text)}
        missing_idx = sorted(p.stem for p in examples if p.stem not in listed)
        if missing_idx:
            issues.append(
                f"wiki/examples/index.md missing {len(missing_idx)} example(s): "
                + ", ".join(missing_idx[:10])
            )

    return issues


if __name__ == "__main__":
    raise SystemExit(main())
