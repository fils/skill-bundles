#!/usr/bin/env python3
"""
Simple wikilink lint for skill-bundles wiki.
Checks for broken [[wikilinks]] vs existing files.
Classifies [[backlinks]] as intentional false-positive.
Run: python3 scripts/wikilink-lint.py
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
            if link == "backlinks":
                INTENTIONAL += 1
                continue
            if link not in all_titles and not link.startswith("TODO"):
                BROKEN.append((f, link))

    print(f"Total markdown files: {len(md_files)}")
    print(f"Intentional [[backlinks]] markers: {INTENTIONAL}")
    print(f"New real broken wikilinks: {len(BROKEN)}")
    if BROKEN:
        for f, link in BROKEN[:10]:
            print(f"  BROKEN: {f} -> [[{link}]]")
    else:
        print("No new real broken wikilinks found (0 real new broken links).")
    print("Lint complete. [[backlinks]] classified as false-positive per convention.")

if __name__ == "__main__":
    main()