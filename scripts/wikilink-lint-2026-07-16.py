#!/usr/bin/env python3
"""
Wikilink lint for skill-bundles wiki (2026-07-16).
Checks for broken [[wikilinks]] vs existing files.
Handles pipe aliases: [[link|Display Text]] -> target = link (before pipe).
Classifies [[backlinks]] as intentional false-positive.
Also checks path-style links: [[concepts/name]] -> base name.
Run: python3 scripts/wikilink-lint-2026-07-16.py
"""
import os
import re
from pathlib import Path

WIKI_DIR = Path("wiki")

def find_md_files():
    return list(WIKI_DIR.rglob("*.md"))

def extract_wikilinks(text):
    return re.findall(r'\[\[([^\]]+)\]\]', text)

def get_link_target(link):
    # Split on pipe for display alias
    target = link.split('|')[0].strip()
    # Remove path prefix if present (e.g., [[concepts/name]] -> name)
    if '/' in target:
        target = target.split('/')[-1].strip()
    return target

def main():
    INTENTIONAL = 0
    BROKEN = []
    md_files = find_md_files()
    all_titles = {f.stem for f in md_files}
    all_titles.add("backlinks")  # intentional marker

    for f in md_files:
        content = f.read_text()
        links = extract_wikilinks(content)
        for link in links:
            if link == "backlinks":
                INTENTIONAL += 1
                continue
            target = get_link_target(link)
            if target == "backlinks":
                INTENTIONAL += 1
                continue
            if target not in all_titles and not target.startswith("TODO"):
                BROKEN.append((f, link, target))

    print(f"Total markdown files: {len(md_files)}")
    print(f"Intentional [[backlinks]] markers: {INTENTIONAL}")
    print(f"New real broken wikilinks: {len(BROKEN)}")
    if BROKEN:
        for f, link, target in BROKEN[:20]:
            print(f"  BROKEN: {f.name} -> [[{link}]] (target: {target})")
    else:
        print("No new real broken wikilinks found (0 real new broken links).")
    print("Lint complete. [[backlinks]] and pipe-aliased links classified per convention.")

if __name__ == "__main__":
    main()
