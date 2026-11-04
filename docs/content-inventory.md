# Content inventory and migration map

Audit: 4 November 2026. Sources: https://randallye.github.io/ and https://github.com/RandallYe/RandallYe.github.io (master). See `live-site-audit.txt` for the rendered source inspected before implementation. This is an audit snapshot, not a byte-for-byte backup.

## Repository and preservation status

The supplied workspace initially contained only the guide and brief. The user subsequently supplied a clean clone at `/home/rye/workspace/RandallYe.github.io`. A local clone now lives in `astro-redesign/`, on `redesign/astro`, descended from upstream `master` at `4544eec`. The initial audit commit was brought across; original history and all 19 tracked legacy files remain unchanged. No upstream pushes or production changes occurred.

`docs/legacy-assets.json` records the paths, sizes and SHA-256 digests of all 17 original binary/static assets. They are copied byte-for-byte to `public/` at their original paths. `index.html` and `index.md` remain unchanged at the repository root. The original homepage is served at `/legacy/` with relative file URLs adjusted for Astro's base path; the original Markdown is downloadable at `/legacy/index.md`. `docs/legacy-links.json` records 37 original IDs and 175 href/src occurrences.

Upstream root observed: `index.html`, `index.md`, `CV/`, `pics/`, `SEFM2024/`, `Cheddar/Cheddar_20250715/`, `posts/SEFM_DataMod/`.

| Existing content | Destination / preservation policy |
| --- | --- |
| Name, biography, career, education, contacts | `/about/` and home; retain IOHK wording pending preference review |
| Probabilistic programming, Z/Circus, CSP, graphical notation, security research | `/research/`; source remains linked for detailed descriptions |
| Journal articles (5), conference papers (8), formal proofs (1), chapters (3), thesis (1), preprints (2) | `/publications/`, 20 records with source authors, venue, year and URL |
| News: general, papers, events | Selected dated home items; full archive migration pending Phase 3 |
| Talks, award, projects, academic activities, footnotes | Talks and About summaries; full detail and archive migration pending Phase 3 |
| Empty Showcases section | `/tools/` and security animation detail |
| `index.html` and legacy fragment identifiers | Original page retained at `/legacy/`; all 37 exact IDs inventoried |
| `/pics/me.jpg` | Existing portrait URL identified; preserved locally and reused in the hero |
| `/SEFM2024/SEFM2024_presentation.pdf` | Preserve exact path; preserved locally and linked through the configured base |
| `/Cheddar/Cheddar_20250715/CHEDDAR_York_P3.2_20250715.pdf` | Same policy |
| `/CV/`, other pictures and downloads | All 17 assets inventoried with checksums; CV is `CV/Academic_CV-Kangfeng_Ye.pdf` |
| `/Posts/SEFM_DataMod/cheddar_updates.html` | Site links uppercase Posts while repo lists lowercase posts; actual post is `posts/SEFM_DataMod/SEFM_DataMod_2024.html`; archive rendering corrects this broken destination |

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

File-level inventory and asset preservation are complete. Still verify all outbound links, check archived equations in a browser, and verify video manually. No production cutover until these gaps and the user review are resolved.
