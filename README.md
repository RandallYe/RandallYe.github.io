# Randall Ye — Astro research homepage

Local redesign based on `../CODEX_HOMEPAGE_PLAN.md`. Read `docs/progress.md` and `docs/content-inventory.md` before integrating. The checkout is a local clone of the user-supplied repository, on `redesign/astro` based on upstream commit `4544eec`. Original source files are retained and 17 legacy assets are preserved under `public/` with checksums.

Use Node >=22.23.4. Astro 7.4.5 was the registry's stable version at the audit. No client framework, backend, remote fonts or analytics.

```sh
cd astro-redesign
npm install
npm run check
npm test
npm run build
npm run check:links
npm run dev
```

Commit the generated package-lock.json once installation succeeds. For subsequent installations use `npm ci`. This environment has no npm/GitHub shell DNS, so no lockfile or successful build is claimed.

`src/components/` contains shared UI, `src/data/` contains source-based publication/research records, and `src/content/demos/` stores schema-validated demonstrations. `public/` is reserved for preserved legacy paths. Use two spaces, descriptive component names and strict TypeScript. There is no formatter or linter configured yet; avoid claiming otherwise.

Root deployment configuration is static and targets https://randallye.github.io. Test project-path previews separately:

```sh
ASTRO_BASE=/research-preview/ npm run build
ASTRO_BASE=/research-preview/ npm run check:links
npm run preview
```

`local()` prefixes internal links with Astro's base; canonical URLs include the generated path. After preview checks, rebuild without ASTRO_BASE for production. Do not copy preview output to production.

Before release, perform the browser checklist in `docs/progress.md`, verify the real video, review legacy URL aliases, and obtain explicit user approval. There is deliberately no deployment workflow. Do not push, change Pages settings or deploy as part of local development.
