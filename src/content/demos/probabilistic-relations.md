---
slug: probabilistic-relations
title: Reasoning about probabilistic programs in Isabelle/HOL
subtitle: From probabilistic notation to mechanised reasoning.
summary: A research walkthrough introducing probabilistic relations, their Isabelle/UTP implementation, and examples involving a coin flip, Monty Hall and robot localisation.
researchArea: Formal Semantics & Theorem Proving
status: recorded-demonstration
problem: Probabilistic programs combine state changes with uncertainty. Precise semantics and mechanised reasoning help make their assumptions and intended behaviour explicit.
method: The walkthrough introduces the probabilistic programming language and Isabelle/UTP implementation covered in the demonstration, including Iverson brackets, distribution notation, algebraic laws and fixed-point theorems.
whatVisitorsSee:
  - title: A language for probabilistic behaviour
    description: The walkthrough introduces probabilistic programming notation and its semantic implementation in Isabelle/UTP, built on Isabelle/HOL.
  - title: Definitions and algebraic foundations
    description: The walkthrough covers Iverson brackets, distribution notation, algebraic laws and fixed-point theorems. The screenshot shows the theory inside the Isabelle editor.
  - title: Three worked examples
    description: The examples cover a coin flip, the Monty Hall problem with learning facts, and robot localisation.
resultsOrLimitations: This is a historical walkthrough, originally published in February 2023. It does not demonstrate every result in the later 2024 ProbURel paper, and it does not run Isabelle in this website. Reproducing the proofs requires the corresponding theory versions and Isabelle/UTP environment.
thumbnail: /old_entry/showcase/demonstration_of_probabilistic_relation/featured_hu7888d7cc804f4e8e895bb066cdd171ef_1109337_720x2500_fit_q75_h2_lanczos_3.webp
thumbnailAlt: The original Isabelle editor screenshot showing probabilistic relation definitions and the theory outline.
mediaNote: Captions and transcript are unavailable. The topics are summarised below.
media:
  - kind: video
    src: /old_entry/showcase/demonstration_of_probabilistic_relation/Demonstration_of_probabilistic_relations.mp4
    title: Demonstration of proving probabilistic programs using theorem proving
    caption: Original recording from the probabilistic-relations showcase, first published on 4 February 2023.
    poster: /old_entry/showcase/demonstration_of_probabilistic_relation/featured_hu7888d7cc804f4e8e895bb066cdd171ef_1109337_720x2500_fit_q75_h2_lanczos_3.webp
    mimeType: video/mp4
    sourcePath: showcase/demonstration_of_probabilistic_relation/Demonstration_of_probabilistic_relations.mp4
    sha256: 0458a81e843412d012a548175bacf1c160c0208a878ab8cee38013cc4cc17bef
    verificationStatus: headers-checked
provenance:
  sourcePage: showcase/demonstration_of_probabilistic_relation/index.html
  originalDate: '2023-02-04'
relatedPublications:
  - proburel
paperLinks:
  - label: Read the related ProbURel journal paper (2024)
    url: https://doi.org/10.1016/j.tcs.2024.114876
  - label: Preprint and version history
    url: https://arxiv.org/abs/2303.09692
sourceLinks:
  - label: Probabilistic-relations theory
    url: https://github.com/RandallYe/probabilistic_programming_utp/tree/main/probability/probabilistic_relations
examplesHeading: Worked examples
exampleLinks:
  - label: Coin flip
    description: A basic probabilistic example introducing the language and its treatment of uncertain outcomes.
    url: https://github.com/RandallYe/probabilistic_programming_utp/tree/main/probability/probabilistic_relations/Examples
  - label: Monty Hall with learning facts
    description: A worked example about probabilistic reasoning as information becomes available.
    url: https://github.com/RandallYe/probabilistic_programming_utp/tree/main/probability/probabilistic_relations/Examples
  - label: Robot localisation
    description: A robotics example connecting probabilistic relations to uncertainty about position.
    url: https://github.com/RandallYe/probabilistic_programming_utp/tree/main/probability/probabilistic_relations/Examples
slidesLinks:
  - label: Related RoboStar seminar slides (28 June 2023, PDF)
    url: /old_entry/talk/robostar_seminar_20230628_probabilistic_relations/robostar_seminar_20230628_probabilistic_relations.pdf
featured: false
order: 2
---
## How this relates to ProbURel

The later journal paper, *Probabilistic unifying relations for modelling epistemic and aleatoric uncertainty: Semantics and automated reasoning with theorem proving*, is co-authored by **K. Ye, J. Woodcock and S. Foster** and published in *Theoretical Computer Science* in 2024.

The February 2023 walkthrough covers three worked examples. The later journal paper develops a broader set of examples and results.

## Theory and examples

The probabilistic-relations repository contains installation instructions and worked examples. Reproducing the proofs requires the corresponding Isabelle/UTP environment and theory versions.
