#!/usr/bin/env python3
"""Wikilink linter for skill-bundles wiki."""
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

WIKI_DIR = Path("/home/hermes/projects/skill-bundles/wiki")
EXAMPLES_DIR = WIKI_DIR / "examples"
CONCEPTS_DIR = WIKI_DIR / "concepts"
PAPERS_DIR = WIKI_DIR / "papers"
TOOLS_DIR = WIKI_DIR / "tools"

# Collect all wiki files (basenames without .md)
wiki_files = set()
for d in [EXAMPLES_DIR, CONCEPTS_DIR, PAPERS_DIR, TOOLS_DIR]:
    if d.exists():
        for f in d.glob("*.md"):
            wiki_files.add(f.stem)

# Also collect top-level wiki files
for f in WIKI_DIR.glob("*.md"):
    wiki_files.add(f.stem)

print(f"Total wiki files found: {len(wiki_files)}")

# Pattern for wikilinks: [[link]] or [[link|display]]
WIKILINK_RE = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')

# Known false-positive patterns
FALSE_POSITIVE_PATTERNS = [
    "backlinks",  # intentional marker
    "TODO",
]

# Path-style wikilinks (directory prefixes that don't resolve)
PATH_PREFIXES = ["concepts/", "examples/", "tools/", "papers/", "qa/", "daily-digests/"]

broken_links = defaultdict(list)  # link -> [files that reference it]
false_positives = defaultdict(list)
path_style_links = defaultdict(list)
code_example_links = defaultdict(list)

# Scan all wiki files
all_md_files = []
for d in [EXAMPLES_DIR, CONCEPTS_DIR, PAPERS_DIR, TOOLS_DIR, WIKI_DIR]:
    if d.exists():
        all_md_files.extend(d.glob("*.md"))

for md_file in sorted(all_md_files):
    try:
        content = md_file.read_text()
    except Exception:
        continue
    
    for match in WIKILINK_RE.finditer(content):
        link = match.group(1).strip()
        
        # Skip known false positives
        if link in FALSE_POSITIVE_PATTERNS:
            false_positives[link].append(md_file.name)
            continue
        
        # Check for code-example context (inside backticks)
        start = max(0, match.start() - 100)
        context = content[start:match.end() + 10]
        if '`' in context[:100]:
            code_example_links[link].append(md_file.name)
            continue
        
        # Check for path-style links
        is_path_style = False
        for prefix in PATH_PREFIXES:
            if link.startswith(prefix):
                # Try stripping the prefix
                base_name = link[len(prefix):]
                if base_name in wiki_files:
                    path_style_links[link].append(md_file.name)
                    is_path_style = True
                    break
        
        if is_path_style:
            continue
        
        # Check if link resolves
        if link not in wiki_files:
            broken_links[link].append(md_file.name)

print(f"\n=== LINT RESULTS ===")
print(f"Total wiki files: {len(wiki_files)}")
print(f"Files scanned: {len(all_md_files)}")
print(f"False positives (intentional): {sum(len(v) for v in false_positives.values())} references to {len(false_positives)} links")
print(f"Code-example links (false positive): {sum(len(v) for v in code_example_links.values())} references to {len(code_example_links)} links")
print(f"Path-style links (fixable): {sum(len(v) for v in path_style_links.values())} references to {len(path_style_links)} links")
print(f"Broken links (real): {sum(len(v) for v in broken_links.values())} references to {len(broken_links)} links")

if path_style_links:
    print(f"\n--- PATH-STYLE LINKS (should fix inline) ---")
    for link, files in sorted(path_style_links.items()):
        print(f"  [[{link}]] — referenced by: {', '.join(sorted(set(files)))}")

if broken_links:
    print(f"\n--- BROKEN LINKS (real) ---")
    for link, files in sorted(broken_links.items()):
        print(f"  [[{link}]] — referenced by: {', '.join(sorted(set(files)))}")

if false_positives:
    print(f"\n--- FALSE POSITIVES (intentional) ---")
    for link, files in sorted(false_positives.items()):
        print(f"  [[{link}]] — {len(files)} references")

if code_example_links:
    print(f"\n--- CODE-EXAMPLE LINKS (false positive) ---")
    for link, files in sorted(code_example_links.items()):
        print(f"  [[{link}]] — {len(files)} references")

print(f"\n=== SUMMARY ===")
real_broken = len(broken_links)
path_broken = len(path_style_links)
print(f"Real broken links: {real_broken}")
print(f"Path-style (fixable): {path_broken}")
print(f"False positives: {len(false_positives) + len(code_example_links)}")
if real_broken == 0 and path_broken == 0:
    print("✓ All wikilinks resolve correctly")
elif real_broken == 0:
    print("✓ No real broken links (only path-style to fix)")
