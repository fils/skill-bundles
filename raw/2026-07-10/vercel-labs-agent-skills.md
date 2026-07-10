# Vercel Labs Agent Skills (vercel-labs/agent-skills)

**Source:** https://github.com/vercel-labs/agent-skills  
**Stars:** ~28.9k (2026-07-10)  
**Format:** agentskills.io  
**License:** MIT  
**Signal rating:** 8/10 (official vendor bundle; constraint-rules-as-skills pattern)

## Summary

Vercel's official collection of agent skills. Skills are packaged instructions + optional scripts following the Agent Skills standard. Distributed via skills.sh badge and monorepo packages.

## Skills included (documented)

1. **vercel-optimize** — Audit Vercel projects for cost, performance, reliability, caching, function usage, billing; metrics-first then file-level investigation
2. **react-best-practices** — 40+ rules across 8 categories (waterfalls, bundle size, SSR/CSR fetching, re-renders, etc.), impact-prioritized
3. **web-design-guidelines** — 100+ UI rules (a11y, focus, forms, animation, typography, images, performance, i18n, dark mode, touch)
4. **writing-guidelines** — 80+ handbook rules (voice, structure, code samples, AI workflow accountability); fetches rules from dedicated source repo at invocation
5. **react-native-guidelines** — (present; details truncated in scrape)

## Structure

```
skills/<name>/SKILL.md
scripts/ (optional)
references/ (optional)
packages/ (tooling)
AGENTS.md + CLAUDE.md symlink (universal agent compatibility)
skills.sh.json
```

## Context elements

| Element | Present? | Notes |
|---------|----------|-------|
| Constraint rules | Yes | 40+/100+/80+ rule sets as skill bodies |
| Progressive disclosure | Yes | Thin SKILL.md + remote handbook fetch pattern |
| Platform implementation | Yes | Official Vercel vendor skills |
| Distribution | Yes | skills.sh registry integration |
| Validation | Light | Structure follows agentskills.io |

## Composition pattern

**Vendor constraint-rule bundles** — encodes engineering handbooks (React performance, design, writing) as portable skills. Parallel to addyosmani Iron Laws/Red Flags and Superpowers methodology skills. Differentiator: remote-fetch handbook pattern for always-current rules.

## Quote

> "Skills follow the Agent Skills format."

## Follow-ups

- Compare writing-guidelines remote-fetch vs progressive disclosure in agentskills.io spec
- Bundle density vs addyosmani (fewer skills, denser rule catalogs)
