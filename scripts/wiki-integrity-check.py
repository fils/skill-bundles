#!/usr/bin/env python3
"""Wiki integrity + backlink analysis for skill-bundles."""
import re
from pathlib import Path
from collections import defaultdict

WIKI = Path('wiki')
files = list(WIKI.rglob('*.md'))

# Find all wikilink references
target_refs = defaultdict(list)
for f in files:
    content = f.read_text()
    for m in re.finditer(r'\[\[([^\]\|#]+)', content):
        target = m.group(1).strip().lower()
        target_refs[target].append(str(f.relative_to(WIKI)))

# Identify orphans
examples = [f for f in files if 'examples/' in str(f)]
concepts = [f for f in files if 'concepts/' in str(f)]

orphan_examples = [f.stem for f in examples if not target_refs.get(f.stem.lower())]
orphan_concepts = [f.stem for f in concepts if not target_refs.get(f.stem.lower())]

print(f'Examples: {len(examples)} | Orphan (no inbound): {len(orphan_examples)}')
for o in orphan_examples: print(f'  - {o}')
print(f'\nConcepts: {len(concepts)} | Orphan (no inbound): {len(orphan_concepts)}')
for o in orphan_concepts: print(f'  - {o}')

# Top referenced
print('\n--- Top 15 most-referenced targets ---')
for t, refs in sorted(target_refs.items(), key=lambda x: -len(x[1]))[:15]:
    print(f'  {len(refs):3d}  {t}')

# New examples' backlink counts
print('\n--- Backlink counts for new Iteration 13 examples ---')
new_examples = [
    'ai4curation-curation-skills',
    'skill-validator-cli',
    'agentskill-sh-ags-security-scoring',
    'validate-skill-github-action',
    'text2shacl-multi-agent-shacl',
]
for ex in new_examples:
    refs = target_refs.get(ex, [])
    print(f'  {len(refs):2d}  {ex}')

# New concepts
print('\n--- Backlink counts for new Iteration 13 concepts ---')
new_concepts = [
    'three-layer-validation-stack',
    'bidirectional-shacl-llm-bridge',
]
for c in new_concepts:
    refs = target_refs.get(c, [])
    print(f'  {len(refs):2d}  {c}')

# Wikilink resolution check
basenames = {f.stem.lower() for f in files}
basenames.update({re.sub(r'\(.*?\)', '', l.strip()).strip().lower().replace(' ', '-')
                  for f in files for l in f.read_text().split('\n')[:3]
                  if l.startswith('# ')})

unresolved = sorted(t for t in target_refs
                    if t not in basenames
                    and t.replace(' ', '-') not in basenames
                    and not t.startswith('../'))
print(f'\nUnresolved wikilinks (excluding relative ../ paths): {len(unresolved)}')
for t in unresolved:
    print(f'  - {t}')
