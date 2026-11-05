---
slug: robochart-patrol-robot
title: Animation of a patrol robot model
subtitle: Inspect shared state and choices in a robotic model.
summary: An original interaction-tree animation recording of a RoboChart patrol
  robot, with the model and its three-section corridor diagrams.
researchArea: Concurrency & Process Algebra
status: recorded-demonstration
problem: Shared variables and nondeterministic choices make reactive behaviour
  harder to understand from a diagram alone.
method: The patrol-robot demonstration uses interaction trees in
  Isabelle/HOL to animate a RoboChart model with nondeterministic choice and
  shared variables. The corridor is divided into three sections with soft and
  hard boundaries.
whatVisitorsSee:
  - title: Inspect the model
    description: The RoboChart diagram provides the specification context,
      including the model described as using shared variables and
      nondeterministic choice.
  - title: Understand the corridor
    description: A separate three-section corridor illustration shows the environment
      with soft and hard boundaries.
  - title: Watch the model animation
    description: The original recording makes the model behaviour available for
      inspection. No new trace, safety result or exhaustive analysis is claimed
      here.
resultsOrLimitations: The recording illustrates a particular model and semantic
  development. It is not an exhaustive proof of every possible execution or a
  demonstration of a physical robot. The associated theory branch and tool
  environment are needed to reproduce it.
thumbnail: /old_entry/showcase/animation_of_patrol_robot/Featured_hu022584ec861fb5fb603cb43189fc6f04_1083944_720x2500_fit_q75_h2_lanczos_3.webp
thumbnailAlt: Original screenshot from the patrol-robot animation showcase.
mediaNote: Captions and transcript are unavailable. The topics are summarised below.
media:
  - kind: video
    src: /old_entry/showcase/animation_of_patrol_robot/Animation_of_Patrol_Robot.mp4
    title: Animation of a patrol robot model
    caption: Demonstration published on 26 January 2023.
    poster: /old_entry/showcase/animation_of_patrol_robot/Featured_hu022584ec861fb5fb603cb43189fc6f04_1083944_720x2500_fit_q75_h2_lanczos_3.webp
    mimeType: video/mp4
    sourcePath: showcase/animation_of_patrol_robot/Animation_of_Patrol_Robot.mp4
    sha256: 4f0adadc1f60b6d5ccaa967720967ac41f7e53fb2535ac3cb5c88c39dc9129eb
    verificationStatus: preserved
  - kind: image
    src: /old_entry/showcase/animation_of_patrol_robot/PatrolMod_hu38db1eb6168b86b42bf1b461bf10a67e_2104495_1200x1200_fit_q75_h2_lanczos_3.webp
    title: RoboChart patrol-robot model
    caption: Original RoboChart model described as using nondeterministic choice and
      shared variables.
    alt: RoboChart patrol-robot model
    sourcePath: showcase/animation_of_patrol_robot/PatrolMod_hu38db1eb6168b86b42bf1b461bf10a67e_2104495_1200x1200_fit_q75_h2_lanczos_3.webp
    sha256: 8b34f290fa2f9c58b587f461cde0b1221b3aa58eb8d12b4df5fca68f93663a5e
    verificationStatus: preserved
  - kind: image
    src: /old_entry/showcase/animation_of_patrol_robot/Corridor_sections_hu9c767e2eb6e7fe0b4aefa2a101f579ca_248902_1200x1200_fit_q75_h2_lanczos_3.webp
    title: Three-section patrol corridor
    caption: Original corridor diagram with soft and hard boundaries.
    alt: Three-section patrol corridor
    sourcePath: showcase/animation_of_patrol_robot/Corridor_sections_hu9c767e2eb6e7fe0b4aefa2a101f579ca_248902_1200x1200_fit_q75_h2_lanczos_3.webp
    sha256: 2589bd9854d1c57e72d9b8d3f5c82e4f7a72c95389b9102d10c23145accba1cc
    verificationStatus: preserved
provenance:
  sourcePage: showcase/animation_of_patrol_robot/index.html
  originalDate: '2023-01-26'
relatedPublications:
  - robochart-animation-jlamp
paperLinks:
  - label: Read the related paper
    url: https://doi.org/10.1016/j.jlamp.2023.100940
sourceLinks:
  - label: Original patrol-robot Isabelle/HOL theory
    url: https://github.com/isabelle-utp/interaction-trees/blob/robochart_nondeterminism_resolving/RoboChart/examples/RoboChart_basic_v1/RoboChart_basic_v1_1.thy
exampleLinks:
  - label: Patrol-robot specification
    description: Isabelle/HOL specification of the patrol-robot model.
    url: https://github.com/isabelle-utp/interaction-trees/blob/robochart_nondeterminism_resolving/RoboChart/examples/RoboChart_basic_v1/RoboChart_basic_v1_1.thy
examplesHeading: Model and case-study resources
slidesLinks:
  - label: Related research poster (PDF)
    url: /old_entry/showcase/poster_animation_robochart_interaction_trees/Poster_Animation_RoboChart_Interaction_Trees.pdf
featured: false
order: 5
---
## Related research

The later journal paper, *Formally verified animation for RoboChart using interaction trees*, is co-authored by **K. Ye, S. Foster and J. Woodcock** and published in 2024. It discusses the chemical-detector and patrol-robot models.

The January 2023 recording illustrates the patrol model; the later journal paper develops the formal results.

## Source and model context

The implementation uses the `RoboChart_basic_v1_1.thy` theory in the `robochart_nondeterminism_resolving` branch. The model diagram and corridor illustration show the specification and environment. Consult the repository for its version and environment requirements; the static website does not execute the theory.
