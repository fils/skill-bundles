#!/usr/bin/env python3
"""
Phase 0: Update metadata only (files already in raw/YYYY-MM-DD/ via writes)
Adjust ROOT, today date, and daily_sources before running.
"""
import json
from pathlib import Path

ROOT = "/home/hermes/projects/YOUR_PROJECT_NAME"
META = Path(f"{ROOT}/raw/metadata.json")

today = "YYYY-MM-DD"
daily_count = 0  # set to # new sources ingested

with open(META) as f:
    meta = json.load(f)

meta["date"] = today
meta["daily_sources"] = daily_count
meta["total_sources"] = meta.get("total_sources", 0) + daily_count

with open(META, "w") as f:
    json.dump(meta, f, indent=2)

print(f"[Phase 0] metadata updated: {today}, +{daily_count} sources, total={meta['total_sources']}")
