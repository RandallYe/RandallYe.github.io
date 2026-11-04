---
slug: probabilistic-relations
title: Reasoning about probabilistic programs in Isabelle/HOL
subtitle: From probabilistic notation to mechanised reasoning.
summary: An archived research walkthrough introducing probabilistic relations, their Isabelle/UTP implementation, and examples involving a coin flip, Monty Hall and robot localisation.
researchArea: Formal Semantics & Theorem Proving
status: recorded-demonstration
problem: Probabilistic programs combine state changes with uncertainty. Precise semantics and mechanised reasoning help make their assumptions and intended behaviour explicit.
method: The walkthrough introduces the probabilistic programming language and Isabelle/UTP implementation documented in the original showcase, including Iverson brackets, distribution notation, algebraic laws and fixed-point theorems.
whatVisitorsSee:
  - title: A language for probabilistic behaviour
    description: The original showcase introduces probabilistic programming notation and its semantic implementation in Isabelle/UTP, built on Isabelle/HOL.
  - title: Definitions and algebraic foundations
    description: The archived description covers Iverson brackets, distribution notation, algebraic laws and fixed-point theorems. Its genuine screenshot shows the theory inside the Isabelle editor.
  - title: Three worked examples
    description: The original showcase lists a coin flip, the Monty Hall problem with learning facts, and robot localisation. This is a source-based summary, not a timestamped transcript.
resultsOrLimitations: This is a historical walkthrough, originally published in February 2023. It does not demonstrate every result in the later 2024 ProbURel paper, and it does not run Isabelle in this website. Reproducing the proofs requires the corresponding theory versions and Isabelle/UTP environment.
thumbnail: /old_entry/showcase/demonstration_of_probabilistic_relation/featured_hu7888d7cc804f4e8e895bb066cdd171ef_1109337_720x2500_fit_q75_h2_lanczos_3.webp
thumbnailAlt: The original Isabelle editor screenshot showing probabilistic relation definitions and the theory outline.
mediaNote: Original recording preserved from the earlier homepage. A summary of its documented topics appears below; the source archive does not provide a transcript or captions.
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
  - label: Current probabilistic-relations theory
    url: https://github.com/RandallYe/probabilistic_programming_utp/tree/main/probability/probabilistic_relations
examplesHeading: Worked examples in the original showcase
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

This recording was introduced on the earlier homepage in February 2023. It provides historical context for the research, rather than a demonstration of every result in the final paper. The original description lists three worked examples; the later paper describes a broader set of examples.

## Theory versions and reproduction

The original showcase linked to the `TCS` branch of the earlier `probabilistic_designs` repository. The current homepage instead links to `probabilistic_programming_utp`. Use the current repository for its documented installation instructions and example collection; reproducing a particular historical development may require the earlier environment.

The original branch URL is preserved as a historical reference in the migration records. Its availability has not been confirmed, so the primary source link above uses the current homepage's repository.

## About the recording

The video and Isabelle editor screenshot are recovered assets from the original showcase. They are not a simulated proof interface. This static website plays the recording and links to the theories; it does not execute proof commands.
