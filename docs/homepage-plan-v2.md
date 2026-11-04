# Homepage plan v2 — one portfolio from two sources

Revised 4 November 2026 following the audit of `old_entry` and the user's clarification. This replaces the **remaining migration roadmap** in `../../CODEX_HOMEPAGE_PLAN.md` (the original brief is in the parent workspace). It retains Astro, the existing branch/design, first-class demonstrations, static hosting and the production approval gate.

## 1. Objective and source rules

Present a consistent view of Kangfeng (Randall) Ye by combining the latest GitHub homepage with valuable historical resources. Move all seven authored blogs into the website. Recover missing work, rather than duplicate contributions or restore an obsolete identity.

1. **GitHub wins for current facts:** biography, IOHK role, primary CV, project dates, final publication metadata and contact links.
2. **The archive adds evidence:** videos, slides, posters, code downloads, detailed explanations, teaching and blogs. Older affiliations/statuses remain historical.
3. **One canonical record per work:** published paper and its preprints are linked versions; a poster, talk and demo are related resources, not additional publications. Distinct conference and journal contributions remain distinct records.
4. **Keep provenance:** source page, original path, source date, content type and relationship to the canonical work. Preserve conflicting raw evidence in review metadata, not contradictory visitor-facing text.
5. **Do not resolve uncertainty by guessing:** record missing resources and disputed scientific statements explicitly. Never fabricate media, execution results or verification claims.

Evidence: `old-entry-analysis.md`, `old-entry-inventory.json`, `old-entry-merge-map.md`. The source export remains outside this repository until selected resources are preserved during migration.

## 2. Unified information architecture

Give **Posts** a first-class navigation link now that seven authored articles have been recovered. Keep six links—Research, Tools & Demos, Publications, Posts, Talks, About—with Home accessible through the existing logo/name link. Keep the News archive in the home news section and footer.

| Route | Unified role |
| --- | --- |
| `/` | Current identity; security feature; 3–5 selected research demonstrations/contributions; a compact recent-posts section; latest dated news |
| `/research/` | Four established themes, with related publications, demos, projects and notes |
| `/research/projects/[slug]/` | Consolidated project descriptions and latest-source dates; no duplicate old/new project pages |
| `/tools/`, `/tools/[slug]/` | Real recorded demonstrations, source walkthroughs and clearly labelled engineering case studies |
| `/publications/` | Current bibliography enriched with abstracts, BibTeX, preprints and related resources; stable canonical identifiers |
| `/talks/` | Unified current and historical presentations; separate event dates; rehearsals nested beneath their associated presentation |
| `/posts/`, `/posts/[slug]/` | All seven authored blogs with original dates, figures, references and source context |
| `/news/` | Merged chronology of current and archived announcements, deduplicated by event/work |
| `/about/` | Current identity and career timeline, plus dated teaching/outreach; current CV remains primary |

Home remains concise. Archive and sample material must not crowd out current research.

## 3. Content and media architecture

Keep the existing Astro components and demo collection. Move the currently small JSON/TypeScript records into validated collections when migration needs them, without introducing a client framework or CMS.

- Shared identifiers connect `publications`, `demos`, `talks`, `projects`, `posts` and `news`. Use aliases to merge older titles/slugs; use normalised DOI/arXiv identifiers before fuzzy title matches.
- Add media/resource arrays to demos/talks for multiple recordings, figures, posters and slides. Store a caption, source path, format, original checksum and verification state. Keep an accessible summary and transcript/captions where actually available; do not invent them.
- Posts store original publication date separately from editorial updates, author/attribution, full Markdown body, figures, references and any outstanding technical review notes.
- Add a local **HTML5 video** component with controls, `preload="none"`, a genuine poster where available and a direct download fallback. Keep click-to-load YouTube for security. No autoplay, remote tracking assets or theorem-prover backend.
- Preserve selected original binary paths under `public/old_entry/…`; new pages use base-aware links. Optimised preview images may be derived separately. Record old-to-new page aliases; do not pretend to redirect an external York hostname.
- Nine videos total 182.9 MB. Include only each page's selected media in its markup and avoid eager downloads. Confirm playback/encoding before release; retain original masters rather than overwriting them.
- Add build-time mathematical typesetting for authored posts. Check compatibility with the installed Astro version before choosing the integration; load maths styles only where needed. Test display equations, matrices, align environments, inline notation and narrow screens.

## 4. Revised implementation order

### Phase 0B — historical audit and reconciliation

**Completed in this planning step:** inventory 613 files; classify 84 content leaves; identify 75 substantive entries and nine sample pages; map proposed destinations; record resource gaps and duplicate/version relationships.

**Still required before migration:** assign canonical identifiers and reconcile conflicting metadata against latest GitHub records. Keep source inspection separate from claims of playable media or verified external links.

Acceptance: every substantive page and standalone download has a migration decision; examples and unknowns are explicit. Use the supplied merge map as the checklist.

### Phase 3A — preservation and canonical merge foundation

- Preserve selected original videos, PDFs, diagrams, BibTeX and code downloads with checksums and an asset-to-page dependency manifest.
- Create collection schemas, canonical identifiers, version/resource relationships and URL mappings.
- Use GitHub for current facts. Keep the historic CV dated and secondary; retain the newer CV as primary.
- Exclude stock publications/projects/posts, CMS/admin files and theme infrastructure from production output.
- Repair known malformed DOI destinations and the already-recorded relative DOI link, with raw source retained for comparison.

Acceptance: copied resources match their original hashes; no contradictory current identity or accidental duplicate canonical record; source archive and latest-site originals remain unchanged.

### Phase 3B — recover real research demonstrations first

Keep Security Protocol Animation as the homepage feature. Add these four source-backed showcase pages next:

1. Probabilistic relations / theorem-proving walkthrough.
2. RoboChart probabilistic verification using PRISM, with the mail-delivery robot.
3. RoboChart autonomous chemical detector animation.
4. RoboChart patrol robot animation.

Link their actual recordings, diagrams, source and corresponding papers. Attach the three poster editions to appropriate research/talk pages. Preserve differences between the older probabilistic-relations framework and the current ProbURel publication.

Acceptance: recordings play locally, controls are keyboard accessible, media is not downloaded before requested, source resources are reachable, and the scientific scope matches the original work. No unsupported Try button.

### Phase 3C — migrate all authored blogs

Create Posts index/detail routes and migrate all seven posts listed in the analysis. Preserve original dates, full explanations, references and diagrams, including the temporal-logic timeline. Keep notes on other speakers' work attributed.

Review the identified Markov-chain, index-condition and qubit wording issues before publication. Document substantive corrections with an editorial note while retaining the original evidence. Do not treat successful equation rendering as scientific validation.

Acceptance: seven authored posts accounted for, zero stock-example posts; figures and references preserved; no raw TeX leakage, clipped matrices or unreviewed doubtful claims silently republished. Blogs are reachable from the site rather than hidden in the legacy archive.

### Phase 3D — talks, bibliography, projects and supporting history

- Enrich current bibliography with the archived abstracts, BibTeX and preprint versions. Recover the 2018 working report as a labelled companion resource; avoid double-counting it as the later chapter.
- Add all 14 genuine talk entries, grouping rehearsals with main presentations; restore MODELS2022 recording and slide variants, ICFEM2022 and other available slides.
- Merge seven project histories and 21 news entries with current records. Distinguish dates of publication, announcement and event.
- Add CSAV teaching and the Chinese Isabelle/UTP tutorial to About/Talks.
- Add the line-following robot as a dated engineering case study, explicitly retaining that formal verification was not completed. Record its missing physical-model image.
- Restore the five CSP frog-puzzle downloads from the outreach talk. An executable browser recreation is optional future work and needs separate validation.

Acceptance: every substantive archive entry is migrated, merged into a canonical record, or explicitly deferred with a visible access path. No duplicate publication/event listings or stale “Present” statuses.

### Phase 4 — combined-site quality assurance and preview

Run build, type/content checks, asset-hash checks, internal route/fragment checks and external-resource review. Validate root and preview base paths. Check all seven articles' maths, local videos, keyboard navigation, 320px/mobile/desktop layouts, both themes and media loading/performance. Generate an old-to-new route report and validate aliases, including preserved filenames and case.

Prepare a preview-only hosting workflow using current official guidance. Do not create a production-triggering workflow, change Pages settings or deploy while this approval gate is closed. Browser checks remain outstanding in the current restricted execution environment; passing build checks does not replace them.

Acceptance: shareable preview, no unexplained broken resources, content checklist complete, reproducible dependency lockfile committed, and any remaining scientific/date questions documented for review.

### Phase 5 — review and controlled release

Present the coherent merged portfolio and review unresolved biography/company wording, publication dates, article corrections and historical-resource handling. **Production deployment requires explicit user approval.** Preserve original sources/history and run post-release checks only after that approval.

## 5. Working practice and next concrete increment

Continue on `redesign/astro`; make small commits per content group and update `docs/progress.md`. Do not restart the existing design or replace the current website with the old export.

The next implementation increment is **Phase 3A plus the probabilistic-relations showcase**, followed by the other three recovered research demonstrations and all seven blogs. This produces a reviewable, evidence-backed addition before undertaking the longer historical migration. The current turn delivers analysis and this revised plan; it does not yet migrate the website or deploy it.
