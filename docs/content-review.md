# Content review before release

## User confirmation

- Preferred current employer wording: IOHK or IOG? The draft retains IOHK, matching the original site, without implying ongoing York affiliation.
- Publication years remain faithful to the bibliography: physical-layer security is listed as 2026 although the news announces online publication in November 2025; DataMod proceedings are listed as 2024. Confirm preferred treatment rather than guessing.
- CV is the original file; confirm it is suitable for public use and up to date.

## Resource verification outstanding

- Security recording `https://www.youtube.com/watch?v=8FO6KT6EMqM`: exact original destination recovered; video page and oEmbed could not be fetched. The site labels playback verification pending and offers click-to-load and external-link fallback. Confirm video is public, embeddable, and accurately described. No still, duration, transcript or timestamp claims added.
- Original NSPK/DH links point to absent or moved directories. Updated example links use the README's early-framework theory locations inspected through GitHub. Check again before publication.
- DOI linked by both homepage and README; the audit tool could not fetch the DOI destination. Verify access before release.
- Original talk recording, scholarly profiles, and other outbound destinations still need HTTP/manual checks. A failure to fetch during this audit does not establish that a link is broken.
- The original SEFM talk points to `Posts/SEFM_DataMod/cheddar_updates.html`; the latest-site report is `posts/SEFM_DataMod/SEFM_DataMod_2024.html`. The complete report is now a structured post at `/posts/sefm-datamod-report/`; the legacy mixed-case `.html` URL redirects there, while the original source and report file remain preserved.

## Scientific scope

- Animation soundness is separate from universal proofs of security properties. No new theorem, search result, attack trace or browser simulation has been invented.
- Early SEFM models are distinguished from newer generic framework additions.
- The documented workflow is a source-based explanation, not a transcript or claim about specific moments in an unreviewed recording.
- All 20 publications retain co-authors. Original research, news, projects, academic activities and contribution caveats remain accessible in the full archive; detailed structured migration is Phase 3.

The original exported homepage refers to a local file:// KaTeX stylesheet. The archived rendering strips that unusable link; verify archived maths before release. No source HTML was overwritten.

## Historical probabilistic-relations showcase

- Original date is 4 February 2023; the linked current publication is the 2024 co-authored journal paper. They are presented separately as a historical walkthrough and a related published result.
- The current theory repository was inspectable through the web tool; the old `probabilistic_designs/tree/TCS` destination was not. The older link is retained in provenance rather than presented as a verified reproduction endpoint.
- The preprint page `https://arxiv.org/abs/2303.09692` was inspected: it identifies the same authors and journal DOI as the current bibliography. It is attached as a version link, not another publication.
- Original screenshot visually inspected. The MP4 and slides match audited hashes; header inspection is recorded separately. Playback, subtitles/captions and exact correspondence between each recorded proof and later paper results have not been asserted.
- The original 2018 report BibTeX contains an invalid institution export field. Its raw download is preserved as historical data; it is not rendered as authoritative current metadata or counted as a new peer-reviewed paper.

## RoboChart demos recovered from old_entry

All three recordings have original showcase dates of 26 January 2023. Latest-site publication metadata remains authoritative: RoboChart/PRISM (2022), ICFEM animation (2022), and the later JLAMP animation paper (2024). The later journal paper is related research, not evidence that the earlier videos show every later result. Original deep links to the `robochart_nondeterminism_resolving` branch and RoboStar case-study pages are retained; their current external availability and actual video playback remain to be checked. No numerical PRISM results, universal correctness guarantees or physical-robot claims were added.

## Selected steady-state article

The migrated post retains the original working notes rather than silently rewriting quoted definitions or numerical examples. A visible banner flags the non-negative time-index condition, first-return-event definition, expected-visits interpretation, exact finite-step versus limiting equality, and unresolved time-average/pointwise-limit distinctions. The original unfinished example and summary image remain historical content. Successful equation typesetting is not scientific validation. Only this post and Temporal Logic are now in migration scope.
