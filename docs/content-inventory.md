# Content inventory and migration map

Audit: 4 November 2026. Sources: https://randallye.github.io/ and https://github.com/RandallYe/RandallYe.github.io (master). See `live-site-audit.txt` for the rendered source inspected before implementation. This is an audit snapshot, not a byte-for-byte backup.

## Repository and preservation status

The supplied workspace contains only AGENTS.md and CODEX_HOMEPAGE_PLAN.md; its read-only .git mount is empty. Shell GitHub access fails DNS. Implementation is isolated in `astro-redesign/`, a new local Git repository on `redesign/astro`, **not a branch descended from upstream**. No upstream files or production settings were changed. Before integration, clone upstream, branch from master, and cherry-pick these commits. Copy all original assets unchanged into public at their original case-sensitive paths; verify checksums. Asset preservation remains incomplete until this is done.

Upstream root observed: `index.html`, `index.md`, `CV/`, `pics/`, `SEFM2024/`, `Cheddar/Cheddar_20250715/`, `posts/SEFM_DataMod/`.

| Existing content | Destination / preservation policy |
| --- | --- |
| Name, biography, career, education, contacts | `/about/` and home; retain IOHK wording pending preference review |
| Probabilistic programming, Z/Circus, CSP, graphical notation, security research | `/research/`; source remains linked for detailed descriptions |
| Journal articles (5), conference papers (8), formal proofs (1), chapters (3), thesis (1), preprints (2) | `/publications/`, 20 records with source authors, venue, year and URL |
| News: general, papers, events | Selected dated home items; full archive migration pending Phase 3 |
| Talks, award, projects, academic activities, footnotes | Talks and About summaries; full detail and archive migration pending Phase 3 |
| Empty Showcases section | `/tools/` and security animation detail |
| `index.html` and legacy fragment identifiers | Retain original page under `/legacy/` after upstream clone; capture exact IDs and add aliases before cutover |
| `/pics/me.jpg` | Existing portrait URL identified; binary unavailable locally, do not substitute fabricated portrait |
| `/SEFM2024/SEFM2024_presentation.pdf` | Preserve exact path; currently link to original absolute URL |
| `/Cheddar/Cheddar_20250715/CHEDDAR_York_P3.2_20250715.pdf` | Same policy |
| `/CV/`, other pictures and downloads | Exact filenames and checksums pending clone; never infer a CV filename |
| `/Posts/SEFM_DataMod/cheddar_updates.html` | Site links uppercase Posts while repo lists lowercase posts; verify case before redirecting; keep original destination recorded |

## Security demonstration resources

- Paper: https://doi.org/10.1007/978-3-031-77382-2_3 — linked on homepage and repository; DOI fetch unavailable through audit tool.
- Co-authors: K. Ye, R. Metere, P. Yadav; SEFM 2024, pp. 33–51.
- Video: https://www.youtube.com/watch?v=8FO6KT6EMqM — actual MWC2025 news destination found; playback/oEmbed could not be fetched. Clearly mark playback unverified, retain external watch fallback; no fabricated poster or transcript.
- Source: https://github.com/RandallYe/Animation_of_Security_Protocols — README inspected.
- Old model links `/tree/master/NSPK` and `/tree/master/Diffie_Hellman` could not be fetched. README gives current early-framework models under `User_Guided_Verification_Security/NSPKP/NSPK3/NSPK3.thy` and `User_Guided_Verification_Security/Diffie_Hellman/DH_v1/DH.thy`; both file pages inspected.
- README distinguishes early SEFM framework from newer generic framework. Do not attribute newer results to the 2024 paper.
- Running generated animators needs GHC; regenerating code needs patched Isabelle/UTP. Web UI uses Haskell/Yesod. No hosted interactive endpoint verified.

## Other reviewed sources

ProbURel: https://github.com/RandallYe/probabilistic_programming_utp/tree/main/probability/probabilistic_relations

Circus translator: https://github.com/RandallYe/Circus2ZCSP

Interaction trees: https://github.com/isabelle-utp/interaction-trees

QANAD: https://github.com/RandallYe/QANAD

Profile destinations from live site: https://github.com/RandallYe ; https://www.linkedin.com/in/randallye ; https://scholar.google.com/citations?hl=en&user=PbLkCR8AAAAJ ; https://dblp.org/pid/193/5774.html . Scholar returned 403; others remain recorded rather than asserted healthy.

## Release prerequisites

Complete file-level inventory from upstream; preserve original HTML/Markdown and every binary; verify all outbound links; resolve case mismatch and old fragment aliases; verify video manually. No production cutover until these gaps and the user review are resolved.
