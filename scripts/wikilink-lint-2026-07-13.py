#!/usr/bin/env python3
"""Wikilink lint script for skill-bundles wiki.
Scans all .md files in wiki/ for [[wikilinks]] and checks if they resolve.
Classifies false positives: [[backlinks]], code-example links, path-style links.
"""
import os
import re
import sys
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent / "wiki"

def get_all_wiki_files():
    """Get all .md files in wiki/ (recursive)."""
    files = []
    for root, dirs, filenames in os.walk(WIKI_DIR):
        for f in filenames:
            if f.endswith('.md'):
                rel = os.path.relpath(os.path.join(root, f), WIKI_DIR)
                files.append(rel)
    return set(files)

def get_wiki_basenames():
    """Get base names (without .md) of all wiki files."""
    files = get_all_wiki_files()
    basenames = set()
    for f in files:
        name = f.replace('.md', '')
        basenames.add(name)
        # Also add just the filename without directory
        basename_only = os.path.basename(f).replace('.md', '')
        basenames.add(basename_only)
    return basenames

def extract_wikilinks(content):
    """Extract all [[wikilinks]] from content, excluding code blocks."""
    # Remove code blocks
    lines = content.split('\n')
    in_code = False
    clean_lines = []
    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
            continue
        if not in_code:
            clean_lines.append(line)
    clean_content = '\n'.join(clean_lines)
    
    # Find all [[...]] patterns
    pattern = r'\[\[([^\]]+)\]\]'
    raw_matches = re.findall(pattern, clean_content)
    # Handle pipe aliases: [[name|display text]] → use only 'name' part
    matches = []
    for m in raw_matches:
        if '|' in m:
            name = m.split('|')[0].strip()
            matches.append(name)
        else:
            matches.append(m)
    return matches

def is_false_positive(link):
    """Classify known false positives."""
    # [[backlinks]] is intentional
    if link == 'backlinks':
        return True, "intentional backlinks marker"
    
    # Path-style links (contain /)
    if '/' in link:
        return True, "path-style reference (directory/category)"
    
    # Links inside backticks (code examples) - already filtered by code block removal
    # but also check for links that look like code
    if link.startswith('concepts/') or link.startswith('examples/') or link.startswith('tools/') or link.startswith('papers/'):
        return True, "path-prefixed directory reference"
    
    return False, None

def main():
    basenames = get_wiki_basenames()
    all_files = get_all_wiki_files()
    
    total_links = 0
    broken_links = []
    false_positives = []
    files_scanned = 0
    
    for root, dirs, filenames in os.walk(WIKI_DIR):
        for f in filenames:
            if not f.endswith('.md'):
                continue
            filepath = os.path.join(root, f)
            rel_path = os.path.relpath(filepath, WIKI_DIR)
            files_scanned += 1
            
            with open(filepath, 'r') as fh:
                content = fh.read()
            
            links = extract_wikilinks(content)
            for link in links:
                total_links += 1
                is_fp, reason = is_false_positive(link)
                if is_fp:
                    false_positives.append((rel_path, link, reason))
                elif link not in basenames:
                    broken_links.append((rel_path, link))
    
    print(f"=== Wikilink Lint Report (2026-07-13) ===")
    print(f"Files scanned: {files_scanned}")
    print(f"Total wikilinks found: {total_links}")
    print(f"False positives (intentional/path-style): {len(false_positives)}")
    print(f"Broken links (real): {len(broken_links)}")
    
    if broken_links:
        print(f"\n--- Broken Links (real, need fixing) ---")
        for filepath, link in broken_links:
            print(f"  {filepath}: [[{link}]]")
    
    if false_positives:
        print(f"\n--- False Positives (intentional, skip) ---")
        seen = set()
        for filepath, link, reason in false_positives:
            key = (link, reason)
            if key not in seen:
                seen.add(key)
                print(f"  [[{link}]] — {reason}")
    
    # Summary
    print(f"\n=== Summary ===")
    print(f"Real broken links: {len(broken_links)}")
    print(f"False positives: {len(false_positives)}")
    if len(broken_links) == 0:
        print("✅ No real broken links found!")
    else:
        print(f"⚠️  {len(broken_links)} broken links need attention")
    
    return 0 if len(broken_links) == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
