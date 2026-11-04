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

## Phase 2 — Security animation showcase

Source resource audit complete; implementation in progress. Video URL is confirmed in the original source; playback and embedding remain unverified. No public interactive service established.

## Checks and environment

- `npm install --fetch-retries=0`: FAIL — EAI_AGAIN resolving registry.npmjs.org; no dependencies or lockfile produced.
- Phase 1 `npm run build`: BLOCKED — astro executable not installed (exit 127).
- Phase 1 `npm run check`: BLOCKED — astro executable not installed (exit 127).
- Registry metadata reports Astro 7.4.5 requires Node >=22.23.4; installed Node is 22.23.2. Upgrade Node before installing.

## Remaining acceptance checklist

On a supported, network-enabled environment: install and commit lockfile; run type checks, tests, root build/link checks and project-base build/link checks. Check 320px, 768px and desktop widths, menu keyboard behaviour, focus order, screen-reader labels, video load and fallback, no third-party requests before consent, portrait sizing, archived equations and all external resources. No browser checks have run yet.

## Next phases and release gate

Migrate the rest of the research detail/news/projects/activities into structured pages (currently preserved in full in the archive). Confirm preferred IOHK/IOG wording, bibliography date discrepancies and video availability in `content-review.md`. Production cutover, Pages settings, deployment workflows and pushes remain untouched; explicit approval is required before deployment.
