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

## About career timeline — 4 November 2026

Replaced the Background prose with a reusable CareerTimeline component covering the four source-documented periods: IOHK from November 2025, York research (2016–2025), York PhD (2012–2016), and embedded engineering/team leadership (2004–2012). The newest-first timeline uses semantic list/time elements, an explicit current-role marker and existing IOHK/thesis links. Mobile stacks dates above descriptions; colours follow the light/dark tokens. CV and contact links remain intact. No additional JavaScript or dependencies.

Validation: Astro check reports zero diagnostics; static build and internal link checks pass, with the existing archive warning unchanged. Browser visual review remains outstanding.

## Mathematical visual identity — 4 November 2026

Added a code-native SVG/CSS ResearchVisual component featuring Hoare-style notation, an illustrative labelled transition system and a symmetric probability-mass diagram (binomial weights 1:4:6:4:1). The graphic is decorative and carries no verification results or executable-demo claims. The original portrait remains in the hero as an author signature. Added a subtle notebook dot grid, mathematical serif accents, formal notation on research cards, diagram-style borders and a stronger security feature panel. Existing light/dark themes, readable content, mobile stacking and reduced-motion behaviour are retained; no new dependencies or third-party assets/requests.

Validation: Astro check reports zero errors/warnings; build and built link checks pass with the existing archive warning. `git diff --check` passes. Browser visual verification could not run: this execution environment denies creation of a local HTTP server socket (PermissionError). Review at 320px and desktop in both themes remains pending.

## Expanded historical-source analysis and plan — 4 November 2026

The user requested analysis and a revised plan for old_entry, clarified that the GitHub homepage is the latest authority, and explicitly included all authored blogs in the migration scope.

Completed a read-only inventory of `/home/rye/workspace/web/old_entry`: 613 files (291.3 MB), 84 main-section leaf pages (75 substantive entries plus nine theme examples), nine local MP4s, 13 PDFs including a sample, 19 BibTeX files, five CSP examples and a source ZIP. Found four research demonstration recordings plus a line-following engineering case study, three poster pages, 14 talks, seven blogs, 21 news entries, seven projects and teaching material. Identified duplicate publication versions, date/status conflicts, malformed DOI destinations, a missing physical-model image and scientific-review questions in posts.

Added a reproducible audit script, file hashes/resource inventory, per-page merge map, analysis and `docs/homepage-plan-v2.md`. Latest GitHub facts take precedence; old content supplies missing resources and dated history. Plan includes all seven authored blogs and excludes three stock blog examples. All website changes are deferred to the revised implementation phases: no source, assets, UI or deployment was changed in this analysis step.

Validation: audit counts and classifications checked against the search index and actual leaf HTML files; every archive file has a SHA-256 record; all 84 leaf pages have a migration disposition. `git diff --check` passes. No application rebuild is needed for this documentation/audit-only change. Media playback, external links and scientific article corrections remain outstanding.

## Phase 3A and first recovered showcase — 4 November 2026

Completed the next increment on `redesign/astro`:

- Preserved **81 original authored resources plus one genuine lightweight preview** under `public/old_entry/` (274,825,826 bytes): all nine local videos, 12 non-template PDFs, 17 BibTeX records, five CSP examples, the C++ ZIP and selected original figures. `old-entry-assets.json` ties each file to its original audit hash and source-page consumers. Historical CV remains separate; examples, theme infrastructure and unselected generated image derivatives are excluded. Preservation is idempotent and refuses changed sources or conflicting destinations.
- Added stable identifiers to all 20 current publications and a validated publications collection. `canonical-content-map.json` merges old publication aliases into current records, retaining distinct conference/journal works. Earlier preprints and archived BibTeX are related resources, not duplicate publications. The 2018 working report is labelled as a companion to the later control-law chapter. Refreshing source metadata retains these IDs/resources.
- Added local-media/provenance/publication relationships to the demo schema and a reusable native LocalVideo component. It has controls, `preload="none"`, a genuine poster and a permanent download fallback; no autoplay, backend or new client framework.
- Implemented `/tools/probabilistic-relations/` with the original February 2023 recording, screenshot, source-based three-example summary, current theory link, related 2024 paper/preprint and June 2023 seminar slides. Distinguishes the historical walkthrough from later ProbURel results and versions. No captions/transcript were supplied by the archive; that limitation remains explicit.
- Replaced the source-only ProbURel card with the recovered showcase on Home and Tools, avoiding duplicate cards. Added links from Research and Publications, and a base-aware static redirect from `/old_entry/showcase/demonstration_of_probabilistic_relation/` on the new host.
- Removed hardcoded security-protocol assumptions from the generic demo page; its two original protocol examples still render correctly. Corrected the inherited relative DOI link in archived rendering without changing original HTML. Built link checks now have zero archive warnings.
- Committed the existing matching dependency lockfile. README records working commands and current verification limits.

Validation: Astro check has zero diagnostics. Tests verify preservation, canonical merging and distinct publication versions. Root and `/research-preview/` builds, internal links/fragments/posters/duplicate-ID checks, and built-demo markup checks all pass. Checks cover deferred local media, direct download, publication backlinks, exactly one showcase card and retention of the security YouTube fallback. Root build output is restored. Original latest-site files/assets have no diff against upstream `4544eec`.

Media headers identify an MP4 container, 227.478-second duration and `avc1`/`mp4a` sample entries (`probabilistic-relations-media-check.json`). **Actual decoding, browser playback, responsive layout and keyboard review remain unverified**; header inspection does not close these acceptance criteria. The older TCS-branch URL could not be fetched; it stays in provenance, while the primary link uses the current homepage's repository. The arXiv page was inspected and explicitly connects its version history to the existing journal DOI.

Next: add the RoboChart/PRISM, chemical-detector and patrol-robot showcases using their now-preserved recordings, then migrate all seven authored blogs. Talks/news/projects/teaching still require structured migration; their preserved files and inventory entries do not imply their pages are complete. No push, Pages setting change or deployment occurred.

## Portrait placement — 4 November 2026

Moved the original portrait from beneath the mathematical illustration into the first identity block at the upper-left of the homepage hero, beside the name. It is now larger, eagerly loaded with high fetch priority, and remains before the biography and illustration in mobile/source order. Added compact sizing for narrow screens; removed the old signature styles and duplicate placement. Build, Astro check and built internal-link checks pass. Actual browser visual review remains pending.

## Portrait clarification — 4 November 2026

Moved the portrait into the far-left brand/home link on the first navigation row, replacing the RY monogram on every redesigned page. Removed the hero portrait and its placement-specific CSS. The sticky header keeps it visible; compact sizing retains space for mobile menu/theme controls. Build, Astro check and internal-link checks pass; browser visual review remains pending.

## Preferred display name — 4 November 2026

Updated the navigation identity/home label, document/social titles, archive redirect title and About introduction to the user-preferred “Kangfeng (Randall) Ye”. Footer and hero already use that name. Added mobile wrapping space for the longer navigation name beside the portrait and controls. Original publications, URLs and historical source files are unchanged. Build and internal-link checks pass; browser visual review remains pending.

## Remaining three recovered research demos — 4 November 2026

Implemented `/tools/robochart-prism/`, `/tools/robochart-chemical-detector/` and `/tools/robochart-patrol-robot/` using the original January 2023 descriptions and distinct preserved MP4s. Each page includes the source screenshot, documented workflow, scope/limitations, original model/case-study links, related publication anchors and available slides/posters. The patrol page renders its two original model/corridor diagrams; PRISM includes the mail-delivery model diagram. No invented quantitative results, traces or live execution controls.

Added five audited lightweight preview/diagram derivatives (87 preserved resources total: 81 originals plus six selected derivatives). The generic demo template now renders image media with alt text and captions. Added three new-host legacy-route redirects and publication backlinks while keeping the existing bibliography at 20 canonical records. Conference and journal animation papers remain distinct. The Interaction Trees source-only card is represented by the recovered animation demos, keeping Home/Tools to four recorded walkthroughs plus the Circus source card; security remains the sole featured demo.

Validation: Astro check has zero diagnostics; preservation and canonical-merge tests pass. Root and `/research-preview/` builds, link/fragment/poster/duplicate-ID checks and expanded four-demo output checks all pass. Output checks confirm distinct local videos, native controls, preload none, no autoplay, genuine posters and model images, correct publication links, exactly one card per recovered demo, and retention of the security fallback. Root output restored. Browser playback, visual/keyboard review and external historical branch availability remain pending; captions/transcripts were not supplied and are not invented.

Phase 3B page implementation is complete; its browser acceptance remains open. The selected blog migration is now complete; five other authored blogs remain excluded by the user's narrowed scope.

## Line-following robot case study — 4 November 2026

Recovered `engineer_lfr` at `/tools/line-following-robot/`, with a static redirect from its original new-host old_entry path. Includes all three original recordings (sharp corners, physical map run, simulation), the robot photograph, mathematical-model and design-space-exploration figures, original C++ ZIP, INTO-CPS compendium and the cited controller reference. The borrowed controller paper is supporting literature, not a new publication by the site owner. The original missing physical-model image is explicitly recorded; the mathematical-model image is not substituted for it.

Added an engineering-case-study category to distinguish this work from theorem-proving demonstrations. Retained the explicit source statement that planned formal verification was not completed. Videos now have visible titles and spacing for multi-recording pages. The page is discoverable on Home and Tools; Home selects five showcase cards while Tools retains the complete source/tool list. Added four audited lightweight image derivatives (91 preserved resources in total).

Validation: zero Astro diagnostics; preservation/canonical tests pass; root and preview builds, internal-link checks and seven-video output checks pass. Output checks verify all three LFR videos, captions, figures, source download, absence of autoplay and explicit unfinished-verification scope. Root output restored. Browser playback, responsive visual/keyboard review and reproducing the hardware/controller remain unverified. No production deployment.

## Two selected historical posts — 4 November 2026

The user narrowed blog migration to **Temporal Logic** and **Steady State Probabilities**. This supersedes earlier seven-blog tasks; the other five authored posts are excluded unless requested later. Updated the parent AGENTS.md and remaining plan accordingly.

Added a validated posts collection, `/posts/` index and two detail pages: `/posts/temporal-logic/` and `/posts/steady-state-probabilities/`. Recovered complete article bodies from their article-content sections, with original dates (18 and 23 November 2022), source-page hashes, heading anchors, references, temporal-logic timeline and both probability diagrams. Removed theme wrappers, social-sharing widgets, generated-image dependencies and old navigation. Added Posts to the main navigation, using the existing logo as Home, and new-host legacy-path redirects for both articles. No other blog routes were generated.

Added pinned KaTeX 0.16.22 for build-time **native MathML only**. No client maths library, remote fonts or stylesheet is required. The original LaTeX `mbox` notation and encoded ellipsis are adapted only for rendering. Strict equation parsing, matrices and aligned derivations pass; original archived mathematical content is retained. A visible historical-working-notes review banner identifies known doubtful/unfinished statements rather than silently rewriting them or claiming scientific validation.

Initial executor npm access failed DNS; installation subsequently became available in the shared workspace, and the matching dependency lockfile is included. Build/type checks now pass. Tests cover the two requested old-entry articles plus the separately selected latest-site SEFM/DataMod report, source hashes/figures, retained references, MathML rendering and anchors. Root and preview-subpath builds, internal links and posts-output checks pass; demo-output regressions pass. Root output restored. Browser visual/screen-reader checks and external reference availability remain unverified. No deployment.

Talks and the canonical bibliography are now enriched; remaining archive work is projects/news/teaching, with no additional old-entry blogs in the current scope.

## Historical talks — 4 November 2026

Merged the current site's three talks with the old-entry archive. The rebuilt Talks page now lists 14 distinct presentations across both sources: 11 substantive archived presentations and three current-site entries. The three archive rehearsals are grouped under their matching RAMiCS, MODELS, and ICFEM presentations. Original archived dates, event labels, slides, the MODELS recording, ICFEM animation clip, and Pint of Science CSP files are linked. The two local videos use native controls with `preload="none"`, no autoplay, and a download fallback. Historical talk URLs on the new site resolve to canonical talk anchors. Talk metadata is schema-validated in `src/data/talks.json`; provenance and binary hashes remain in the archive inventory/manifests.

Validation: `npm run check`, `npm test`, root and `/research-preview/` builds, `check:links`, `check:demo`, `check:posts`, and `check:talks` pass. The built Talks route contains 14 source aliases, 11 archive records, three grouped rehearsals, and two deferred local recordings. External talk links and actual video playback remain unverified; browser/device acceptance is still outstanding.

## Remaining archive work

Next: reconcile and merge the seven project histories and 21 news entries against current site records, then add the documented teaching and tutorial history. Only the two user-selected blog posts remain in scope.

## SEFM and DataMod report migration — 4 November 2026

After the user reported the report link broken, traced the original homepage URL to a mixed-case `.html` path that was not emitted by the existing Astro directory route. Migrated the full latest-site report to `/posts/sefm-datamod-report/`, retaining both SEFM and DataMod sections, six original figures, attribution, paper and project links, and a SHA-256 reference to the untouched source file. The Talks resource and rendered legacy homepage now point to the new post. The exact historic `Posts/SEFM_DataMod/cheddar_updates.html` URL now has a matching `.html` redirect route. The two selected old-entry blogs remain the only old-entry blog migrations.

Validation: post tests verify source hash, all six figure files and paper links. Build and post/link checks verify the new route and exact legacy `.html` redirect at root and preview base paths. Browser validation remains pending.

## Canonical bibliography enrichment — 4 November 2026

Added archived abstracts to the nine matching canonical records where the old-entry publication page explicitly supplied one. Each abstract stores its source page and SHA-256; the duplicated CSP‖B text artifact in the old HTML export is normalized. No abstract was invented for records without a captured source abstract. Kept the 2018 working report as a labelled resource on the 2020 chapter rather than a second publication. Verified that all 17 archived BibTeX files are reachable from their canonical work/companion record. Added the security-paper and O-RAN arXiv versions referenced in the SEFM/DataMod report, without duplicating works. Abstracts are available in expandable details on Publications.

Validation: Astro check, all unit tests, root and `/research-preview/` builds, and internal links pass. Tests and `check:publications` verify nine rendered abstracts, 17 BibTeX links, the 2018 companion links, preprint versions, and unique canonical records. External abstract links and browser review are still pending.
