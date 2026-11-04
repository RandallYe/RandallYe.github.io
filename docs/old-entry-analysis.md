# Analysis of the historical homepage

Analysed 4 November 2026. Source: `/home/rye/workspace/web/old_entry`, read-only. Comparison: the latest GitHub homepage retained in this repository and its Astro migration. The user has explicitly established that **GitHub is the latest source; old_entry supplies missing material**.

## Evidence and scope

The archive is a generated Hugo/Wowchemy website, rather than a directory of editable Markdown sources. Its HTML pages, search index, BibTeX and downloadable resources must be reconciled; copying its navigation or importing its entire rendered layout would also import example content and obsolete site machinery.

A reproducible audit is in `scripts/audit-old-entry.py`. `old-entry-inventory.json` records every file's path, size and SHA-256 digest, leaf-page metadata, resource references, exact duplicates and missing local references. `old-entry-merge-map.md` assigns every substantive leaf page a proposed destination or exclusion.

| Evidence | Finding |
| --- | --- |
| Whole export | 613 files; 291,305,132 bytes (291.3 MB / 277.8 MiB) |
| HTML | 255 pages, including indexes, pagination and taxonomies |
| Main content sections | 84 leaf pages: 75 substantive indexed entries and 9 stock examples |
| Search index | 76 records: those 75 entries plus the author profile |
| Research showcases | 8: five demonstrations/case studies plus three poster pages |
| Other authored content | 14 talks, 7 posts, 21 news entries, 7 projects, 1 teaching entry |
| Bibliography | 17 genuine publication pages, often earlier versions of current works; 19 BibTeX files, including sample records |
| Media/downloads | 9 MP4s, 13 PDFs (one is a theme sample), 5 CSP files and a C++ source ZIP |
| Video volume | 182,947,987 bytes (182.9 MB), largest recording 45.24 MB |
| Existing exact asset match | Original portrait matches `public/pics/me.jpg`; filename similarity alone was not treated as duplication |

Local presence and byte identity are verified. Video decoding/playback, external destinations and executable models have not been validated. The link inventory checks href/src/srcset/poster/data references; it does not prove that every JavaScript-generated resource request works. The only missing file among these checked leaf-page references is the line-following robot's `lfr/lfr_phy_model.png`.

## Most valuable additions

| Material | Evidence available locally | Recommended use |
| --- | --- | --- |
| Probabilistic relations theorem-proving walkthrough | 36.16 MB MP4; explanatory text; theory link; 2023 seminar slides | A full Tools & Demos page, linked to the current ProbURel publication with historical framework/version identified |
| RoboChart → PRISM verification | 26.40 MB mail-delivery-robot MP4; model diagram; paper/source references | A full showcase linked to the current RoboChart/PRISM publication |
| Autonomous chemical detector animation | 9.55 MB MP4; screenshot; theory and ICFEM paper links | A demonstration detail page under the RoboChart animation research family |
| Patrol robot animation | 15.46 MB MP4; model/corridor diagrams; theory link | A companion demonstration with its own examples and resource links |
| Line-following robot engineering | Three MP4s; mathematical model, simulation and design-space-exploration figures; C++ ZIP | A clearly dated engineering case study. The source explicitly says planned formal verification was not completed |
| Conference/seminar resources | MODELS2022 recording and two slide decks; ICFEM2022 slides and movement clip; RAMiCS2021, 2023 seminar and control-law slides | Enrich Talks and the related research/demo pages; merge rehearsals under their corresponding main presentation |
| Three posters | Original PDFs and images | Related resources on research/demo/talk pages; retain 2022 and improved 2023 editions without treating repeated explanatory text as new research |
| Five frog-jumper CSP models | Original files and explanation in the Pint of Science talk | Restore downloadable educational examples; optional future guided showcase |
| Teaching | CSAV practical-course description and Chinese Isabelle/UTP tutorial entry | Add a dated teaching/outreach section and talk links; do not claim missing tutorial slides exist |

The local research recordings offer a stronger next step than additional decorative mockups. Security protocol animation remains the primary feature; the newly recovered recordings broaden the portfolio without changing its scientific claims.

## Blogs to migrate

All seven authored posts belong on the new website, with full text, dates, diagrams and references:

1. **Steady state probabilities of Markov Chains** — substantial probability notes with equations and examples.
2. **[Quantum] What is superposition?** — mathematical/probabilistic explanation.
3. **Temporal Logic — history and semantics** — includes the original timeline image.
4. **Probabilistic vs. Stochastic** — connects mathematical definitions to the RoboChart/PRISM paper.
5. **Belief-Desire-Intention (BDI)** — research reading notes.
6. **Testing Robotic Systems** — notes on Arnaud Gotlieb's talk; preserve speaker attribution.
7. **Evolving Robot Software and Hardware** — notes on Gusz Eiben's talk; preserve attribution.

The other three post pages (`getting-started`, `jupyter`, `writing-technical-content`) are stock theme demonstrations, not the user's articles. Exclude them from the new Posts index.

## Consistency and review findings

- **Current identity:** the old York research-associate biography must not replace the newer IOHK role or current CV. Historical affiliations remain on dated events.
- **Project dates:** old RoboTest says “Present”; GitHub ends the combined RoboCalc/RoboTest period in June 2023. INTO-CPS starts in December 2016 in the old export but November 2016 on GitHub; CyPhyAssure ends in August versus September 2021. Use latest GitHub dates in the unified view, retaining source discrepancies for review.
- **Dates have different meanings:** news publish dates, event dates, project durations and bibliography years must remain separate. The ICFEM rehearsal slug contains `20221119` while indexed date is 19 October 2022. The 2022 award news is indexed on 1 January 2023. Do not infer dates from slugs or filesystem timestamps.
- **Bibliography:** 17 genuine archived pages map to 13 works already represented in the current bibliography plus one related 2018 working report. Earlier arXiv versions should become links on their canonical works, not duplicate contributions. The thesis BibTeX enriches the existing thesis entry. The report has an invalid `ARRAY(...)` institution field; preserve raw evidence but do not display that export artefact.
- **Links:** some old DOI URLs contain `https://doi.org/https://doi.org/`; a chapter URL uses `/chapter/` after doi.org. Normalise using the current verified identifier while retaining the raw source in provenance. GitHub branches and remote PDFs remain to be checked.
- **Scientific review:** the steady-state article asserts exact equality to a limiting matrix for all n ≥ 11. Exact rational multiplication of the displayed transition matrix gives a different first element at n = 11 (`382205275/1019215872`, versus `3/8`). The stochastic article displays n ≤ 0 in its Markov-property condition; the quantum introduction calls a qubit “two binary bits”. Flag these for correction/review; do not silently reissue doubtful statements as new authoritative explanations.
- **Missing resource:** the robot physical-model picture is absent. Keep an explicit missing-asset record; do not invent a replacement or imply it was recovered.
- **Old URL hosts:** the export uses York's `/~ky582/old_entry/` prefix (and sample pages use `/ky582/old_entry/`). New local paths need an explicit mapping. A redirect on the old York hostname requires control of that host and is outside this repository.

## Disposition

Recover the substantive authored content and original assets. Merge related editions and resources into one coherent research view. Keep stock samples, generated taxonomy/pagination, old CMS/admin files, vendored theme JavaScript, fonts and obsolete biography out of the new production site. Do not copy all 291 MB into the public output as the migration strategy.

This analysis has not changed either website or copied the archive into production assets. The source remains untouched; preservation manifests alone are not a portable backup of its binary files.
