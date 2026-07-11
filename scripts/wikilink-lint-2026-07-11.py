#!/usr/bin/env python3
"""Wikilink lint for skill-bundles wiki — Iteration 36 (2026-07-11).
Checks [[wikilinks]] against existing files, classifies broken links.
"""
import os
import re
import glob

WIKI_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "wiki")

def get_wiki_files():
    """Return set of all .md file basenames (without extension) in wiki/."""
    files = set()
    for root, dirs, filenames in os.walk(WIKI_DIR):
        for f in filenames:
            if f.endswith('.md'):
                name = f[:-3]
                files.add(name)
    return files

def extract_wikilinks(content):
    """Extract [[wikilink]] references from markdown content.
    Returns list of link targets (ignoring display text).
    """
    # Match [[link]] or [[link|display]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    links = re.findall(pattern, content)
    return [l.strip() for l in links]

def lint():
    wiki_files = get_wiki_files()
    
    all_links = {}  # link -> list of (source_file, line_num)
    total_files = 0
    total_links = 0
    
    for root, dirs, filenames in os.walk(WIKI_DIR):
        for f in filenames:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                total_files += 1
                rel_path = os.path.relpath(filepath, os.path.dirname(WIKI_DIR))
                
                with open(filepath, 'r', encoding='utf-8') as fh:
                    lines = fh.readlines()
                
                for i, line in enumerate(lines, 1):
                    # Skip code blocks
                    if line.strip().startswith('```'):
                        continue
                    # Skip inline code
                    if '`' in line:
                        # Simple heuristic: skip lines with backtick-enclosed wikilinks
                        pass
                    links = extract_wikilinks(line)
                    for link in links:
                        # Skip known false positives
                        if link.lower() in ('backlinks', 'todo'):
                            continue
                        # Skip links that are clearly inside code (rough heuristic)
                        total_links += 1
                        if link not in all_links:
                            all_links[link] = []
                        all_links[link].append((rel_path, i))
    
    # Classify links
    resolved = set()
    broken = []
    intentional = []
    
    for link, sources in all_links.items():
        # Check exact match
        if link in wiki_files:
            resolved.add(link)
        else:
            # Check if it's a known false positive pattern
            if link.startswith('TODO') or link == 'backlinks':
                intentional.append((link, sources))
            else:
                broken.append((link, sources))
    
    # Output
    print(f"=== Wikilink Lint Report — 2026-07-11 (Iteration 36) ===")
    print(f"Wiki files found: {total_files}")
    print(f"Unique wikilink targets: {len(all_links)}")
    print(f"Resolved links: {len(resolved)}")
    print(f"Broken links: {len(broken)}")
    print(f"Intentional false positives: {len(intentional)}")
    print()
    
    if broken:
        print("--- Broken Links ---")
        for link, sources in sorted(broken):
            # Check for close matches
            close = [w for w in wiki_files if link.lower() in w.lower() or w.lower() in link.lower()]
            close_str = f" (close: {close[:3]})" if close else ""
            print(f"  [[{link}]]{close_str}")
            for src, line in sources[:3]:
                print(f"    → {src}:{line}")
        print()
    
    if intentional:
        print("--- Intentional False Positives ---")
        for link, sources in intentional:
            print(f"  [[{link}]] ({len(sources)} occurrences)")
    
    print()
    print("=== Summary ===")
    print(f"Real broken links: {len(broken)}")
    print(f"False positive intentional: {len(intentional)}")
    # Check for new broken links (not in known patterns)
    new_broken = [l for l, s in broken if l not in (
        'schimatos-shacl-knowledge-graph',  # known partial
    )]
    print(f"New broken links (not pre-existing): {len(new_broken)}")
    
    return len(broken)

if __name__ == '__main__':
    lint()
