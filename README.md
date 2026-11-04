# Randall Ye — Astro research homepage

Local redesign based on `../CODEX_HOMEPAGE_PLAN.md`. Read `docs/homepage-plan-v2.md`, `docs/progress.md` and `docs/content-inventory.md` before integrating. The checkout is a local clone of the user-supplied repository, on `redesign/astro` based on upstream commit `4544eec`. Original source files are retained and 17 legacy assets are preserved under `public/` with checksums.

Use Node >=22.23.4. Astro 7.4.5 was the registry's stable version at the audit. No client framework, backend, remote fonts or analytics.

```sh
cd astro-redesign
npm install
npm run check
npm test
npm run build
npm run check:links
npm run check:demo
npm run dev
```

The dependency lockfile is committed; use `npm ci` for reproducible installations. Node 24.22.2 has been used successfully for build and type checks. Local browser preview may still be restricted by the execution environment.

`src/components/` contains shared UI, `src/data/` contains source-based publication/research records, and `src/content/demos/` stores schema-validated demonstrations. The publications collection validates canonical IDs, research metadata and links to demos. `public/` is reserved for preserved legacy paths. Use two spaces, descriptive component names and strict TypeScript. There is no formatter or linter configured yet; avoid claiming otherwise.

Root deployment configuration is static and targets https://randallye.github.io. Test project-path previews separately:

```sh
ASTRO_BASE=/research-preview/ npm run build
ASTRO_BASE=/research-preview/ npm run check:links
ASTRO_BASE=/research-preview/ npm run check:demo
npm run preview
```

`local()` prefixes internal links with Astro's base; canonical URLs include the generated path. After preview checks, rebuild without ASTRO_BASE for production. Do not copy preview output to production.

Before release, perform the browser checklist in `docs/progress.md`, verify the real video, review legacy URL aliases, and obtain explicit user approval. There is deliberately no deployment workflow. Do not push, change Pages settings or deploy as part of local development.

## Historical resources

Selected original resources from the read-only `old_entry` export are preserved under `public/old_entry/`, including nine recordings for current/future migration. `docs/old-entry-assets.json` records their audit hashes and source-page dependencies; generated theme files and example pages are excluded. The preserved historical CV is separate from the primary current CV.

To verify/copy resources again from the supplied archive (existing mismatched files are never overwritten):

```sh
python3 scripts/preserve-old-entry.py /home/rye/workspace/web/old_entry
npm test
```

Recovered showcases are `/tools/probabilistic-relations/`, `/tools/robochart-prism/`, `/tools/robochart-chemical-detector/` and `/tools/robochart-patrol-robot/`; their original site paths redirect locally. Local videos use controls and `preload="none"`; media header checks do not establish actual browser playback. See `docs/progress.md` for verification gaps and upcoming demos/blog migration.
