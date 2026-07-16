#!/usr/bin/env python3
"""
DEPRECATED: Pre-OKF Obsidian wikilink linter.

The wiki/ tree is now an OKF v0.1 Knowledge Bundle.
Use scripts/okf-lint.py instead.
"""
import runpy
import sys
from pathlib import Path

print(
    "NOTE: wikilink-lint.py is deprecated. Delegating to okf-lint.py "
    "(wiki uses relative markdown links, not [[wikilinks]]).",
    file=sys.stderr,
)
sys.argv[0] = str(Path(__file__).with_name("okf-lint.py"))
runpy.run_path(str(Path(__file__).with_name("okf-lint.py")), run_name="__main__")
