---
slug: robochart-chemical-detector
title: Animation of an autonomous chemical detector
subtitle: Explore a RoboChart model through sound animation.
summary: A recorded demonstration of autonomous chemical-detector animation,
  generated from the Isabelle/HOL interaction-tree semantics of a RoboChart
  model.
researchArea: Concurrency & Process Algebra
status: recorded-demonstration
problem: Reactive robotic models interact with their environment. Exploring
  executions helps make their specified behaviour easier to inspect.
method: The demonstration uses an interaction-tree implementation of
  RoboChart semantics in Isabelle/HOL and generated Haskell code to animate an
  autonomous chemical detector.
whatVisitorsSee:
  - title: Identify the RoboChart case study
    description: Explore the autonomous chemical-detector model and
      its supporting case-study description.
  - title: Explore generated animation
    description: The recording demonstrates animation based on the
      interaction-tree development in Isabelle/HOL.
  - title: Connect the execution to the semantics
    description: The ICFEM2022 paper and presentation explain the formal background.

resultsOrLimitations: Animation explores behaviour of the specified model. It
  does not establish arbitrary safety or security properties of a physical
  detector. Reproduction requires the corresponding Isabelle/UTP theory versions
  and generated-code environment.
thumbnail: /old_entry/showcase/animation_of_autonomous_chemical_detector/Featured_hud9be3fd51e9ded56112bb3323c9633e2_1004789_720x2500_fit_q75_h2_lanczos_3.webp
thumbnailAlt: Original screenshot from the autonomous chemical-detector animation showcase.
mediaNote: Captions and transcript are unavailable. The topics are summarised below.
media:
  - kind: video
    src: /old_entry/showcase/animation_of_autonomous_chemical_detector/Animation_of_Chemical_Detector.mp4
    title: Animation of an autonomous chemical detector
    caption: Demonstration published on 26 January 2023.
    poster: /old_entry/showcase/animation_of_autonomous_chemical_detector/Featured_hud9be3fd51e9ded56112bb3323c9633e2_1004789_720x2500_fit_q75_h2_lanczos_3.webp
    mimeType: video/mp4
    sourcePath: showcase/animation_of_autonomous_chemical_detector/Animation_of_Chemical_Detector.mp4
    sha256: 2bdab13c0778c25c090315d7208536bcf1fb4f5080bbd39f8b8332ecf14d2a4d
    verificationStatus: preserved
provenance:
  sourcePage: showcase/animation_of_autonomous_chemical_detector/index.html
  originalDate: '2023-01-26'
relatedPublications:
  - robochart-animation-icfem
  - robochart-animation-jlamp
paperLinks:
  - label: Read the related paper
    url: https://doi.org/10.1007/978-3-031-17244-1_24
sourceLinks:
  - label: Original interaction-tree theory directory
    url: https://github.com/isabelle-utp/interaction-trees/tree/robochart_nondeterminism_resolving/RoboChart/examples/RoboChart_ChemicalDetector_autonomous
exampleLinks:
  - label: Autonomous chemical-detector case study
    description: Model and supporting documentation for the autonomous chemical detector.
    url: https://robostar.cs.york.ac.uk/case_studies/autonomous-chemical-detector/autonomous-chemical-detector.html
examplesHeading: Model and case-study resources
slidesLinks:
  - label: Original conference presentation (PDF)
    url: /old_entry/talk/20221026_icfem_2022/20221026_ICFEM_2022.pdf
  - label: Research poster (January 2023, PDF)
    url: /old_entry/showcase/poster_animation_robochart_interaction_trees/Poster_Animation_RoboChart_Interaction_Trees.pdf
featured: false
order: 4
---
## Formal background

The work is described in *Formally Verified Animation for RoboChart Using Interaction Trees* at ICFEM2022, co-authored by **K. Ye, S. Foster and J. Woodcock**. The later 2024 journal article is a distinct publication, linked below alongside the conference contribution.

The recording belongs to the earlier demonstration. Later journal results should be read in their own context rather than attributed to this recording.

## Theory versions and execution

The original source link targets the `robochart_nondeterminism_resolving` branch. The implementation generates Haskell animation code from the Isabelle/HOL semantic implementation. Consult the source repository for its environment and version requirements; this website plays the recording without running Isabelle or Haskell.
