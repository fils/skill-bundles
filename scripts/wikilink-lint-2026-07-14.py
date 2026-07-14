#!/usr/bin/env python3
"""
Wikilink lint for skill-bundles wiki (2026-07-14).
Checks for broken [[wikilinks]] vs existing files.
Handles pipe aliases ([[name|display]]) and path prefixes ([[concepts/name]]).
Classifies [[backlinks]] as intentional false-positive.
Run: python3 scripts/wikilink-lint-2026-07-14.py
"""
import os
import re
from pathlib import Path

WIKI_DIR = Path("wiki")

def find_md_files():
    return list(WIKI_DIR.rglob("*.md"))

def extract_wikilinks(text):
    return re.findall(r'\[\[([^\]]+)\]\]', text)

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
            # Handle pipe aliases: [[name|display]] -> use name
            target = link.split("|")[0].strip()
            # Handle path prefixes: [[concepts/name]] -> use basename
            if "/" in target:
                target = target.split("/")[-1].strip()
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
    print("Lint complete. [[backlinks]] classified as false-positive per convention.")

if __name__ == "__main__":
    main()
