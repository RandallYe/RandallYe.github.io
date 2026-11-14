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

## Project, news and teaching migration — 5 November 2026

Added six validated canonical project histories from all seven substantive archive project pages. RoboCalc/RoboTest share the latest homepage’s combined participation period; both old routes resolve to that history. Latest-source participation dates override obsolete archive dates, with discrepancies retained in `content-review.md`. Research lists the projects and links their detail pages to the recovered demonstrations. The VeTSS page retains its historical technical account and report reference. Every migrated record carries source paths and SHA-256 provenance.

Added `/news/` with 46 dated updates from both sources, accounting for all 21 archive announcements. The JLAMP final-version announcement is merged into the latest-source acceptance record; separate submission, acceptance, publication and presentation milestones are retained. Event-date ranges are separate from archive announcement dates. Recorded the contradictory July/November SEFM source dates without inventing a resolution. Home now shows the three newest merged updates, and Home/Footer link the news archive. All old project/news/teaching routes on the new host have base-aware redirects.

About now includes the historical CSAV teaching role/module resource and Chinese-language Isabelle/UTP tutorial, retaining Simon Foster’s attribution. A reproducible migration script reads both source trees without changing them. Tests cover all 29 project/news/teaching archive pages, provenance hashes, current project dates, canonical merging and announcement/event distinctions; a new built-output check verifies discoverability and redirects.

Also retained the pre-existing uncommitted Posts/Talks thumbnail work and its derivative manifest. Its existing tests and built-output checks are included in regression validation; no browser acceptance is inferred.

Validation: Node 24 Astro check reports zero diagnostics; all six test files pass. Root and `/research-preview/` builds, internal links, history, demos, posts, talks and bibliography output checks pass. Link checks cover 76 HTML pages and 720 internal references with zero errors/warnings at each base. The Talks output checker now also honours `ASTRO_BASE` while retaining `CHECK_BASE` compatibility. Re-running the migration produces byte-identical data/aliases. Original latest-site HTML/Markdown/assets have no diff against `4544eec`; root build output is restored. Browser layouts, keyboard use, media playback and external destinations remain unverified. No push, deployment or Pages setting change.

## News navigation — 5 November 2026

Added News to the shared main header navigation between Talks and About, including the mobile menu and current-page indicator. Astro check and root/preview builds and internal-link checks pass with zero diagnostics or link errors; root output restored. Browser visual review remains pending.

## Visitor-facing copy — 5 November 2026

Following the user's clarification, removed migration/source-comparison language from Research/projects, News, Publications, Posts, Talks and demonstrations, including homepage panels, captions and BibTeX labels. Pages now describe the work, dates and resources directly. Source paths, hashes, reconciliation details, missing-resource records and pending verification remain in documentation/metadata; scientific qualifications and attribution remain visible where relevant. Updated migration generators so regenerated copy follows the same convention.

Validation: Astro check has zero diagnostics; all six test files, root build, internal links and history/demo/post/talk/publication output checks pass. A text-only audit of generated redesigned pages found no remaining migration, preservation or homepage-comparison phrases. Original source pages, asset URLs and provenance hashes are unchanged. Browser acceptance remains pending; no deployment.

## Combined-site route QA and preview preparation — 5 November 2026

Completed the exact-path archive route audit. All 84 inventoried pages now have explicit dispositions in `docs/route-coverage.json`: 70 canonical destinations, nine excluded theme examples and five posts excluded by the user. Added the 17 publication and three poster aliases that were missing from the rendered site. Publication versions and the 2018 companion report resolve to their canonical work without duplicate entries. Poster aliases target a stable resources anchor on the corresponding demonstration. Reconciled the Markdown merge map with implemented routes and the selected-post scope.

The audit also found two preserved PDFs without visitor links: the October 2022 industry-exhibition poster and SoSyM award document. Both are now reachable; the exhibition talk also links its poster. Poster editions remain separately labelled by date. All 43 intended preserved video/PDF/BibTeX/CSP/ZIP downloads are linked. The superseded CV remains preservation-only while About promotes the current CV. No migration notes were added to visitor copy.

Added `npm run audit:routes`, `npm run check:routes` and `npm run verify`. The complete verifier runs diagnostics, tests, both base-path builds, link/route/history/demo/post/talk/publication checks, and restores root output even after a preview-stage failure. The route checker rejects unaccounted pages, stale reports, missing or wrong-case aliases, incorrect refresh/fallback targets, missing canonical fragments, accidentally generated excluded pages, and unlinked intended downloads.

Prepared a manual-only preview artifact workflow at `.github/workflows/preview.yml`, using the current official Astro/GitHub action documentation linked in `docs/preview-review.md`. It installs from the lockfile on Node 24, verifies both bases and packages root output with seven-day retention. It has read-only repository permission and no deployment step or automatic trigger. Its YAML and trigger/permission/step structure were checked locally; the workflow has not run on GitHub and provides no hosted preview URL yet.

Validation: `npm run verify` passes on Node 24. Astro has zero diagnostics; all six test files pass. Each base passes checks over 96 HTML files and 766 internal references with zero errors or archive warnings, including every canonical alias and intended preserved download. Original source HTML/Markdown/assets have no diff from `4544eec`; `git diff --check` passes; root build restored. Browser execution remains blocked by denied local socket binding (`Operation not permitted`), so responsive/keyboard/MathML/media/network acceptance remains open, separately from these static checks. No push, hosted deployment, Pages settings change or production cutover.

Next: perform the browser/media/external-resource checklist in `docs/preview-review.md` in a serving-capable environment; review the remaining content questions before requesting a hosted preview or production release.

## Research as a substantive portfolio section — 5 November 2026

Expanded Research from four short prose blocks into a structured overview and four detailed area pages: `/research/semantics/`, `/research/probability/`, `/research/concurrency/` and `/research/security/`. The overview introduces the research questions and relationship between specification, semantics and analysis; highlights ProbURel, RoboChart/PRISM and security-protocol animation; provides a navigable contribution index; and shows the original UVC human-state model and hospital intralogistics diagram with full-size links. Existing theme/project fragments remain valid, and homepage research cards now link directly to area pages.

The validated `researchAreas` collection covers 13 contributions: ProbURel, probabilistic designs, control-law diagrams, Abel’s limit theorem, RoboChart/PRISM, activity-diagram analysis, O-RAN, Circus model checking, the parser/typechecker, RoboChart interaction-tree animation, reactive relations, sound security animation and physical-layer security protocols. Each page explains the problem, approach and examples, with applicable software, recorded demos, projects and publications. All 20 canonical works appear through their original co-author/year metadata. The partial parser implementation and focused reactive-relations contribution remain explicit; no new proof, benchmark or public execution service is claimed. Sources and editorial choices are recorded only in `research-content-map.md` and metadata.

Added reusable ResearchMethod and ResearchContribution components and research-specific CSS using existing theme tokens. No dependency, client framework, external asset or new animation. Added `check:research` to the complete verifier.

Validation: `npm run verify` passes: Astro zero diagnostics, all six existing test files, root and `/research-preview/` builds and all output checks including the new research coverage check. Each base has 100 HTML files and 920 internal references with zero errors or archive warnings. All four existing theme anchors, the 70 archive aliases and 43 preserved downloads still pass. Root output restored; original source files/assets unchanged; `git diff --check` passes. Browser screenshots, actual visual/keyboard acceptance and media playback remain unverified in this restricted executor. No commit, push or deployment in this increment.

## UTP and Circus as the central research identity — 5 November 2026

Applied the user's clarification that UTP and Circus, modelling state-rich concurrent systems and verification through refinement checking are the most important part of the research. The homepage introduction/primary research link, mathematical illustration, selected bibliography and research-theme ordering now lead with this foundation. Research opens with the same framing and a Circus modelling → UTP semantics → refinement-checking panel; its first selected contribution is UTP/Circus, followed by ProbURel and RoboChart/PRISM. The detailed concurrency area is titled “UTP & Circus: State-Rich Concurrent Systems” and appears first. Its Circus contribution explains the modelling/refinement connection and links to the thesis, journal work, translator and case studies. The probabilistic-semantics area explicitly builds on UTP; the other research content, contribution boundaries and existing URLs remain intact.

Validation: `npm run verify` passes at root and preview bases, including checks for the leading UTP/Circus contribution and refinement-checking copy. Astro zero diagnostics, existing unit tests and all route/content/preservation/output checks pass; 100 HTML files and 920 internal references per base, zero errors/warnings. Root output restored. Browser visual acceptance remains pending. No commit, push or deployment.

## One research theme and application diagrams — 5 November 2026

Replaced the Research opening with the user's unified focus: modelling, verification and quantification of state-rich reactive, concurrent and distributed systems using Unifying Theories of Programming (UTP), Circus, CSP and Z. Added a prominent ResearchFocus section describing the three complementary activities, followed by application cards and native SVG conceptual diagrams for blockchains, security protocols and robotic systems. Existing research contributions are framed as strands within this theme; their detail pages and links are retained. Blockchain is included as the user-specified application domain, without inventing a publication, implementation or verification result. No image-generation dependency or client JavaScript was added; layouts use the existing theme tokens and collapse to one column on narrow screens.

Validation: complete root/preview verification passes; source preservation and links remain intact. Browser visual review remains pending. Changes are uncommitted; no push or deployment.

## Formal notation and development in the research introduction — 5 November 2026

Added development immediately after verification in the unified theme and its activity cards. The opening now reads “Modelling, verification, development & quantification.” Each activity includes native MathML notation: parallel composition, specification refinement, a successive-refinement chain and event probability. Accessible labels explain the symbols. These are schematic expressions introducing the methods, not claimed verification results. Development connects specifications and successive refinement to executable software. The four-column layout becomes two columns at intermediate widths and one on mobile.

Validation: Astro check, root build, internal links and research output checks pass; `git diff --check` passes. No new dependencies or remote maths assets. Browser visual/assistive-technology review remains pending. Changes remain uncommitted.

## Research title refinement — 5 November 2026

Replaced the oversized activity-list heading with “The mathematics of interacting systems.” The title uses a smaller responsive size (maximum 3rem instead of 4.5rem), balanced wrapping and a serif accent. Modelling, verification, development and quantification remain together as a compact supporting line; the precise system scope and formal notation remain below it. Astro check, root build, internal links and diff whitespace checks pass. Browser visual review remains pending; changes are uncommitted.

## Research title wording restored — 5 November 2026

Restored the user's exact preferred heading, “Modelling · Verification · Development · Quantification,” and removed the duplicate supporting line. The title now uses the full content width and a compact responsive size capped at 2rem, fitting a single desktop line while permitting wrapping on smaller screens. Root build, internal links and whitespace checks pass; browser visual review remains pending. Changes remain uncommitted.

## Temporal logic notation — 5 November 2026

Added the temporal-logic expression `□(p ⇒ ◇q)` alongside refinement in the Verification activity, with a spoken MathML label explaining “always, if p holds, q eventually holds.” Updated the description to name temporal logic. The expression illustrates a property form, not a verified result for a particular system. Astro check, root build and internal links pass; changes remain uncommitted.

## Academic CV development-server 404 — 5 November 2026

Reproduced the reported `/CV/Academic_CV-Kangfeng_Ye.pdf` 404 by invoking the installed Astro 7.4.5 browser-navigation route guard. Its filesystem lookup resolves that URL against the repository root and blocks the preserved root PDF, despite an identical copy under public/. The PDF itself is valid (four pages) and matches its preserved checksum.

Added a byte-identical public download at `/downloads/academic-cv.pdf`, which has no repository-root collision, and updated About and the rendered legacy CV link. Original PDFs and source HTML remain unchanged. A regression test checks exact PDF bytes and passes a browser-style request through the installed Astro guard. `npm run verify` passes, including the new test, root/preview builds and output/link checks. The original URL's guard response was reproduced as 404; the new URL passes the guard. Live HTTP/browser validation is still restricted by the environment. Root output restored; changes uncommitted.

## News timeline — 5 November 2026

Added a reusable NewsTimeline component for the News archive and the three homepage updates. Entries use semantic ordered lists with a vertical line and circular markers, dates on the left and content on the right; mobile stacks dates above the content beside the line. The archive retains its year navigation, all 46 announcement anchors, event ranges, expandable details and resource links. The compact homepage timeline links to the corresponding full entries. Styling follows existing theme tokens and adds no JavaScript.

Validation: Astro check reports zero diagnostics; root build, history-output checks and all internal links pass (100 HTML pages, 922 references, zero errors/warnings); whitespace checks pass. Browser visual review remains pending. Changes remain uncommitted.

## Linkable research interests summary — 5 November 2026

The old homepage's "Research interests and summary" section now has a rebuilt page at `/research/interests/`. It summarises all four research strands and their 13 contributions from `src/data/research-areas.json` (no duplicated copy) and links every entry to its detailed page anchor. The page keeps the original fragment id `insresearch-interests-and-summaryins`, and the homepage's legacy fragment target for that id now points at the rebuilt page instead of the raw archive, so existing deep links resolve to readable content. The research overview links to it twice: beside “Explore the contributions to this theme” in the hero, and from the contributions section heading.

## Light-theme dark panels — 5 November 2026

Two surfaces ignored the theme: the homepage "Security verification you can explore" featured band (`--feature` was a fixed dark navy) and the hero "Mathematical foundations" panel (fully hardcoded palette). Both now use the shared theme tokens, so the light theme renders them as light tinted panels and the dark theme keeps its existing contrast.

- `.feature` in `src/styles/global.css`: light `--feature` is `#e7efeb`; text, paragraphs, links, buttons and borders come from `--ink`, `--muted`, `--accent` and `--line`; the fixed mint overrides and the dark decorative pattern were replaced with `color-mix()` on the accent. The obsolete "keep the panel dark in both themes" comment is gone.
- `src/components/ResearchVisual.astro`: panel, header, caption and SVG take `--white`, `--ink`, `--muted`, `--accent`, `--line` and `--focus`; nothing is a fixed hex anymore.
- Removed the three decorative dots in the panel header. They looked like carousel pagination; there is no carousel.

Deliberately still dark in both themes: the selected-contribution preview matte and the case-study image frames (`research.css`), and video frames, which act as mattes for media.

Validation: Astro check, root build, 16 tests and internal links pass (101 pages, 962 references, 0 errors). No browser is available in this environment, so the light-theme result was reviewed statically only; screenshot review remains pending.

## Mathematical-foundations panel sharpened — 5 November 2026

The panel looked blurred because it carried a `transform: rotate(1deg)`, which forces the browser to resample the whole card, including its small text and 1px diagram strokes. The rotation and its rotated shadow are gone.

Type and diagram were raised too: header 0.64rem, context label 0.68rem, support line 0.76rem (was 0.55/0.58/0.65), diagram labels 8px → 10px in the 360-unit viewBox, figures 22px → 23px, equation 2.8rem → 3rem. Straight grid, axis and separator lines use `shape-rendering: crispEdges`; dashed transition arrow and node radii were adjusted so the markers no longer overlap the nodes.

Astro check, root build, internal links and 16 tests pass. No browser here, so sharpness was not visually confirmed.

## News authored as Markdown — 5 November 2026

Adding an announcement no longer means editing JSON. Each item is now one note in `src/content/news/<slug>.md`: frontmatter for `title`, `date`, `summary`, optional `eventDate`/`eventEndDate`, `resources` and `provenance`, plus an optional prose body shown behind “More details”. The filename is the id and the page anchor.

`scripts/build-news.mjs` compiles those notes into the existing `src/data/news.json`, which the validated `news` collection still reads, so page components, the history checks and the archive tests are unchanged. Frontmatter is a small YAML subset: `key: value` lines plus `key:` with indented `- field: value` items for `resources` and `provenance`; plain values need no quotes, and the parser rejects a list item outside a list or a missing required field instead of guessing. The generator sorts by filename, keeps `detail` optional and fails loudly on missing frontmatter or required fields. `npm run build:news` regenerates the file; `prebuild` and `pretest` run it automatically, and `scripts/build-news.test.mjs` fails when the committed JSON differs from the notes. Existing note filenames and frontmatter keep every current id, date, event range, resource and checksum.

News `provenance` is now optional (`.default([])`) so a hand-written announcement needs no invented source hash; migrated items keep their GitHub/archive entries, and the existing hash assertions still cover them. `scripts/migrate-supporting-history.py` now writes the same Markdown notes instead of JSON.

Validation: Astro check, build, 17 tests, links (101 pages, 962 references, 0 errors) and history output pass at the root base.

## News notes reload while developing — 5 November 2026

A newly added note did not appear because `src/data/news.json` is compiled, and a running `astro dev` only compiled it at startup. `astro.config.mjs` now registers a small Vite plugin: when a note under `src/content/news/` changes, it recompiles the JSON, which the content layer then reloads. Compilation errors are logged as `[news-notes] <file>: <problem>` and keep the previous data, so the dev server survives a malformed note. `predev`, `prebuild` and `pretest` still cover command-line runs.

Note for the current session: the running dev server had to be restarted once to load the new config (Astro 7 runs it as a background daemon; `npx astro dev stop` then `npm run dev`).
