# Randall Ye — Astro research homepage

Local redesign based on `../CODEX_HOMEPAGE_PLAN.md`. Read `docs/homepage-plan-v2.md`, `docs/progress.md` and `docs/content-inventory.md` before integrating. The checkout is a local clone of the user-supplied repository, on `redesign/astro` based on upstream commit `4544eec`. Original source files are retained and 17 legacy assets are preserved under `public/` with checksums.

Use Node >=22.23.4. Astro 7.4.5 was the registry's stable version at the audit. No client framework, backend, remote fonts or analytics.

```sh
cd astro-redesign
npm ci
npm run check
npm test
npm run build
npm run check:links
npm run check:demo
npm run check:posts
npm run check:talks
npm run check:publications
npm run check:history
npm run check:routes
npm run dev
```

The dependency lockfile is committed; use `npm ci` for reproducible installations. Node 24.22.2 has been used successfully for build and type checks. Local browser preview may still be restricted by the execution environment.

`src/components/` contains shared UI, `src/data/` contains source-based publication/research records, and `src/content/demos/` stores schema-validated demonstrations. The publications collection validates canonical IDs, research metadata and links to demos. `public/` is reserved for preserved legacy paths. Use two spaces, descriptive component names and strict TypeScript. There is no formatter or linter configured yet; avoid claiming otherwise.

Root deployment configuration is static and targets https://randallye.github.io. Test project-path previews separately:

```sh
ASTRO_BASE=/research-preview/ npm run build
ASTRO_BASE=/research-preview/ npm run check:links
ASTRO_BASE=/research-preview/ npm run check:demo
ASTRO_BASE=/research-preview/ npm run check:posts
ASTRO_BASE=/research-preview/ npm run check:talks
ASTRO_BASE=/research-preview/ npm run check:publications
npm run preview
```

`local()` prefixes internal links with Astro's base; canonical URLs include the generated path. After preview checks, rebuild without ASTRO_BASE for production. Do not copy preview output to production.

Before release, perform the browser checklist in `docs/progress.md`, verify the real video, review legacy URL aliases, and obtain explicit user approval. The manual preview workflow packages a verified build artifact; it does not deploy. See `docs/preview-review.md`. Do not push, change Pages settings or deploy as part of local development.

## Historical resources

Selected original resources from the read-only `old_entry` export are preserved under `public/old_entry/`, including nine recordings for current/future migration. `docs/old-entry-assets.json` records their audit hashes and source-page dependencies; generated theme files and example pages are excluded. The preserved historical CV is separate from the primary current CV.

To verify/copy resources again from the supplied archive (existing mismatched files are never overwritten):

```sh
python3 scripts/preserve-old-entry.py /home/rye/workspace/web/old_entry
npm test
```

Recovered showcases are `/tools/probabilistic-relations/`, `/tools/robochart-prism/`, `/tools/robochart-chemical-detector/`, `/tools/robochart-patrol-robot/` and the engineering case study `/tools/line-following-robot/`; their original site paths redirect locally. Local videos use controls and `preload="none"`; media header checks do not establish actual browser playback. See `docs/progress.md` for verification gaps and remaining history migration.

## Selected posts

Only two blogs from `old_entry` are in scope: Temporal Logic and Steady State Probabilities. The latest-site SEFM/DataMod report is also migrated at `/posts/sefm-datamod-report/`. The original report source remains preserved and its content hash is in `src/data/posts.json`; `python3 scripts/migrate-sefm-report.py` refreshes the extracted post from that preserved HTML. The old-entry post hashes, bodies and dates are also in `src/data/posts.json`; `python3 scripts/migrate-selected-posts.py /home/rye/workspace/web/old_entry` refreshes only the two selected old-entry articles.

Archived publication abstracts, BibTeX versions and preprint resources are attached to canonical records. To refresh source-backed abstracts from the supplied old-entry export, run `python3 scripts/enrich-publications.py /home/rye/workspace/web/old_entry`, then run `npm run check:publications` after a build.

KaTeX is a pinned build dependency and outputs native MathML without client scripts or remote fonts. Run `npm run check:posts` after a successful build, with the same ASTRO_BASE value as that build. The steady-state post visibly identifies historical scientific-review issues while retaining the source notes.

## News

Announcements are written as one Markdown note per item in `src/content/news/<slug>.md`. `npm run build:news` compiles them into `src/data/news.json`, which the validated `news` collection reads. `npm run build` and `npm test` run the compiler first, so an out-of-date JSON file fails the test suite instead of shipping stale news, and `astro dev` recompiles on every note change (an invalid note is reported in the dev log and the previous data stays published).

```md
---
title: New journey in industry at IOHK
date: 2025-11-24
summary: One or two sentences.
resources:
  - label: IOHK
    url: https://iohk.io/
---

Optional longer text. It appears behind a “More details” disclosure on `/news/`.
```

`eventDate` and `eventEndDate` (YYYY-MM-DD) may be added for dated events, and `provenance` uses the same `- field: value` list shape for material migrated from a source file:

```md
provenance:
  - source: old_entry
    path: news/20221011_robostar_industry_exhibition/index.html
    sha256: <64 hex chars>
```

The filename is the id, so it must be a lowercase slug (`^[a-z0-9]+(-[a-z0-9]+)*$`); it also becomes the page anchor. `title`, `date` and `summary` are required; everything else is optional. Order does not matter: both the archive and the homepage sort by date. Frontmatter is a small YAML subset — `key: value` lines plus `key:` + indented `- field: value` lists — so plain text values need no quotes.

## Complete local verification

Run `npm run verify` to check both root and preview base paths and restore a root build. `npm run check:routes` checks the complete 84-page route disposition report and exact-case aliases; `npm run audit:routes` refreshes that report after mapping changes. Browser/playback/external-resource acceptance is tracked separately in `docs/preview-review.md`.

## Research content

`src/data/research-areas.json` contains the four validated research areas and 13 contributions. Each contribution links canonical publications, demonstrations, projects and software resources. The overview and homepage theme cards share these summaries. `docs/research-content-map.md` records the source authority and scope qualifications. `npm run check:research` verifies research navigation, coverage, diagrams and attribution after a build; it also runs within `npm run verify`.
