# Research expansion: content authority and coverage

The public Research section has an overview and four area pages. The user’s clarification establishes UTP and Circus, state-rich concurrent modelling and refinement checking as the central research identity. This leads both the homepage and Research overview; probabilistic, robotic and security work is presented in relation to that foundation. Source comparisons and this editorial map remain internal, following the user's preference. Existing `/research/#semantics`, `#probability`, `#concurrency`, `#security` and `#projects` fragments remain valid. Homepage theme cards link to the corresponding detailed area pages.

## Source authority

Copy is based on the current homepage's Research interests and summary, Short background and contribution footnotes, with publication titles, co-authors and years resolved through the 20 canonical records in `src/data/publications.json`. Latest-source research links are retained. Existing demo pages provide recording dates and scope; project records supply participation dates. No new external availability, playback or proof-reproduction checks are implied.

`src/data/research-areas.json` is validated by the `researchAreas` content collection. Publications, demonstrations and projects are collection references. It supplies both the detailed research pages and the compact homepage summaries, avoiding divergent copies of the theme descriptions.

## Coverage

| Area / contribution | Source section and qualifications |
| --- | --- |
| Semantics / ProbURel | Probabilistic Unifying Relations: relational semantics, epistemic/aleatoric uncertainty, laws and examples. The 2023 walkthrough is distinguished from the 2024 journal development. No count of proved examples is inferred from the inconsistent source enumeration. |
| Semantics / probabilistic designs | Probabilistic designs: nondeterministic sequential probabilistic language, Isabelle/HOL theory and fair-coin distribution example. |
| Semantics / control-law diagrams | Graphical Notations and the preserved VeTSS account: discrete-time blocks, compositional contracts/refinement, algebraic loops and aircraft cabin-pressure subsystem. |
| Semantics / Abel's limit theorem | Current news and canonical AFP entry: power series with real coefficients, November 2025. |
| Probability / RoboChart and PRISM | Probabilistic semantics and verification for RoboChart: three RoboTool plugins, case studies, award and related property-language papers. |
| Probability / activity diagrams | Quantitative Analysis of UML Activity Diagrams: quantitative profile, PRISM/Storm tooling, DTMC/MDP/CTMC, parameter analysis, synthesis and hospital example. Both QANAD and the archive's QASCAD implementation link are retained without asserting release equivalence or acceptance status. |
| Probability / O-RAN | QoS analysis: six control-policy configurations, three radio cells, nine user equipments and exponential switching. Model-specific scope is explicit. |
| Concurrency / Circus | Z notation and Circus: CSP ∥ B semantics, Java/CZT translator, ProB and buffer/steam-boiler/ESEL case studies. Links to thesis and journal contribution. |
| Concurrency / parser | ISO Z and Circus parser/typechecker: Alex/Happy/Haskell and C++ work. The source footnote's incomplete semantics-transformation rules are explicit. No publication is invented for this software. |
| Concurrency / interaction trees | CSP / Animation of RoboChart: mechanised semantics, generated Haskell animation, chemical-detector/patrol examples. Conference and journal papers remain distinct. |
| Concurrency / reactive relations | Reactive relations and its contribution footnote: focused reactive-buffer verification and strategy input. Selected Isabelle/UTP contributions are distinguished from authorship of the entire framework. |
| Security / sound animation | Formal verification of security protocols: terminal/web code, manual event selection, reachability exploration, NSPK/DH. No hosted interactive service, new trace or universal security proof is asserted. |
| Security / physical-layer protocols | Canonical physical-layer security paper title, authors and publication year. No additional technical result or unsupported connection to the SEFM/DataMod report is inferred. |

All 20 canonical works are reachable through the related-publication lists across these 13 contributions. Their complete co-author strings and years are rendered from publication records, rather than restated as solo achievements.

## Linkable summary

The old homepage's "Research interests and summary" section is rebuilt at `/research/interests/` from the same `research-areas.json` records, so it cannot drift from the area pages. It keeps the original fragment id `insresearch-interests-and-summaryins` for existing deep links and links each contribution to its detailed anchor.

## Visuals and behaviour

- The overview uses existing probabilistic-relations and RoboChart preview assets. The leading UTP/Circus card has decorative refinement notation, not a fabricated tool screenshot or verification result.
- The three-stage Circus modelling / UTP semantics / refinement-checking panel is a conceptual explanation of the research approach; it displays no verification result or model trace.
- The two technical figures are the unchanged `pics/uvc_human.png` and `pics/PAL_use_case.png`, inspected locally before use. Captions identify the actual model and purpose. Full-size image links and meaningful alt text accompany their lazy-loaded previews.
- Layouts use existing light/dark tokens, responsive grids and native links. No new dependencies, remote assets, animation or client-side framework were added.

## Validation

`npm run check:research`, included in `npm run verify`, checks all four detailed routes, 13 contribution anchors, all 20 canonical publication relationships, homepage/detail navigation, examples/software/demo/project links, original diagrams/full-size links and important attribution/scope qualifiers at root and preview bases. Existing route, content, preservation and media-markup checks continue to run. Browser visual, keyboard and playback acceptance remains separate.

Current-source `index.md` SHA-256: `aca0f5401916db5b515d45b9a1bd595f802bc1ea78e0f3786c4b0945e764d77a`.

## Unified theme — user clarification

The overarching theme is modelling, verification and quantification of state-rich reactive/concurrent/distributed systems using Unifying Theories of Programming (UTP), Circus, CSP and Z. Blockchain, security-protocol and robotic applications are explicitly supplied by the user. The Research overview now opens with this focus, three complementary activities and three decorative SVG application diagrams. Existing contributions are organised as strands within this one theme. The blockchain illustration introduces an application domain; no blockchain publication, implemented model, verified result or executable demo is inferred.

The subsequent user clarification adds **development** immediately after verification: modelling, verification, development and quantification. Four native MathML expressions illustrate parallel composition (`P ∥ Q`), refinement (`S ⊑ P`), successive refinement (`S ⊑ D₁ ⊑ D₂`) and event probability (`Pr(A)`). They describe the research methods schematically and carry accessible labels; they do not report a proof about a particular system.
