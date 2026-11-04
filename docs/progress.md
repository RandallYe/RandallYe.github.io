# Redesign progress

## Phase 0 — audit and preserve

- [x] Read brief and contributor guide; inspect upstream and live site.
- [x] Work on `redesign/astro` in `astro-redesign/`, descended from upstream `4544eec` (clean local clone supplied by user).
- [x] Retain original HTML, Markdown and Git history; copy all 17 static assets byte-for-byte to original public paths.
- [x] Record asset digests, 37 fragment IDs, 175 href/src references, migration mapping and uncertain destinations.
- [x] Extract all 20 publication records from original Markdown, retaining authors, venues and years.
- [ ] Complete outbound HTTP/playback checks; network failures are recorded rather than treated as broken resources.

## Phase 1 — Astro foundation (implemented; acceptance pending)

- [x] Static Astro configuration, strict TypeScript, reusable layout/navigation/footer/hero/cards/publication/news components.
- [x] Home, research, tools, publications, talks, About and complete original-page archive.
- [x] Mobile CSS, keyboard menu with Escape, no-JavaScript navigation, skip link, visible focus, reduced-motion support, base-aware links and page metadata.
- [x] Existing portrait, CV, slides and archived post reused. Original root fragment links expose links to the corresponding archived sections.
- [ ] Build/type checks and actual 320px/desktop browser QA.

## Phase 2 — Security animation showcase (implemented; acceptance pending)

- [x] Schema-validated Markdown demo collection using current Astro loaders and Zod schema.
- [x] Featured demonstration directly after the homepage hero, and on Tools & Demos.
- [x] `/tools/security-protocol-animation/` with source-based explanation, formal scope, documented workflow, protocol examples and paper/source/slides links.
- [x] Generic FeaturedDemo, VideoEmbed and ResourceLinks components. Player contacts YouTube only after a button click, with no autoplay and an always-visible external watch link; link remains usable without JavaScript.
- [x] Missing video still/transcript and uncertain playback recorded in metadata; no invented imagery, results or public interactive service.
- [ ] Verify playback, embedding, page rendering and complete browser acceptance.


## Checks and environment

- `npm install --fetch-retries=0`: FAIL — EAI_AGAIN resolving registry.npmjs.org; no dependencies or lockfile produced.
- Phase 1 and Phase 2 `npm run build`: BLOCKED — astro executable not installed (exit 127).
- Phase 1 and Phase 2 `npm run check`: BLOCKED — astro executable not installed (exit 127).
- `npm test`: PASS — base-prefix behaviour and exact preservation of 17 assets, original Markdown and 20 publication records.
- `git diff --check`: PASS.
- Original source comparison against `4544eec`: PASS — no changes to index.html, index.md or original asset directories.
- `npm run check:links`: BLOCKED — correctly refuses to pass without built dist output. The checker validates generated routes, assets and fragments at the configured base; reports inherited archive issues separately.
- Registry metadata reports Astro 7.4.5 requires Node >=22.23.4; installed Node is 22.23.2. Upgrade Node before installing.

## Remaining acceptance checklist

On a supported, network-enabled environment: install and commit lockfile; run type checks, tests, root build/link checks and project-base build/link checks. Check 320px, 768px and desktop widths, menu keyboard behaviour, focus order, screen-reader labels, video load and fallback, no third-party requests before consent, portrait sizing, archived equations and all external resources. No browser checks have run yet.

## Next phases and release gate

Migrate the rest of the research detail/news/projects/activities into structured pages (currently preserved in full in the archive). Confirm preferred IOHK/IOG wording, bibliography date discrepancies and video availability in `content-review.md`. Production cutover, Pages settings, deployment workflows and pushes remain untouched; explicit approval is required before deployment.

## Known archive limitations

Original exported HTML includes a local `file://` KaTeX stylesheet path. The archive strips this unusable link but mathematical display still needs browser review/local styling. The original files and all content remain unchanged. Newly designed pages use plain text notation and do not depend on remote maths assets. Old archive files may contain inherited outbound/internal issues; link checks report these as explicit legacy warnings rather than silently treating them as validated.

## Local runtime fix — 4 November 2026

Fixed Vite resolving extensionless `lib/paths` imports to `paths.mjs` instead of `paths.ts`, causing `local is not a function`. Renamed the Astro wrapper to `site-paths.ts` and updated every component/page import. The pure base-path helper and preservation tests are unchanged. Replaced the archive's Node filesystem import with a build-time raw HTML import, resolving missing Node type declarations.

Using the user-installed Node 24.22.2 and dependencies: `npm run check` passes with zero errors/warnings; `npm test` passes; root and `/research-preview/` builds succeed; both built link checks report zero errors and one inherited legacy warning (`10.1109/CASE56687.2023.10260395` was a relative URL in the original homepage). Root build output is restored. These results supersede the earlier environment-blocked build/type/link status above. Browser and video verification remain outstanding.

## Theme toggle — 4 November 2026

Added a keyboard-accessible Dark toggle to the header on every redesigned page, including mobile. It sets dark/light CSS tokens, exposes pressed state and an action label, remembers the preference in localStorage, defaults to the system setting, and initialises before page paint. Storage failures do not prevent switching. Without JavaScript, CSS follows the system theme. The preserved original archive retains its original appearance.

Validation: build, Astro check (zero diagnostics), existing tests and built link check pass, with the previously documented legacy warning unchanged. Five scripted DOM scenarios cover system preference, saved overrides, invalid storage values, unavailable storage, toggling, persistence and accessible state. Actual browser visual/keyboard review remains pending.
