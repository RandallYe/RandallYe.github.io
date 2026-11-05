---
slug: line-following-robot
category: engineering-case-study
title: Engineering a line-following robot
subtitle: From mathematical modelling to simulation and physical experiments.
summary: A 2018 engineering case study combining an m3pi line-following robot,
  mathematical modelling, simulation, design-space exploration and a C++
  controller.
researchArea: Model-Based Engineering
status: recorded-demonstration
problem: A line-following robot must respond to changes in the route, including
  sharp corners. Models, simulation and physical trials provide different ways
  to investigate the controller.
method: The work draws on INTO-CPS model-based engineering experience,
  including co-simulation with Functional Mock-up Units. It documents a
  mathematical model, OpenModelica modelling, a C++ controller and
  simulation-based design-space exploration.
whatVisitorsSee:
  - title: Compare models and hardware
    description: The m3pi robot photograph and mathematical model connect the hardware to its specification.
  - title: Watch physical and simulated runs
    description: Three separate original recordings show a sharp-corner route, a
      robot run on a map used for simulation, and a simulation on that map.
  - title: Inspect the implementation and exploration
    description: The C++ implementation and design-space-exploration figure provide supporting engineering material.
resultsOrLimitations: The original author explicitly states that the proposed
  formal verification was not completed after the research focus moved to
  probabilistic RoboChart. These physical and simulation recordings are
  engineering demonstrations, not proofs of controller correctness or new
  performance measurements.
thumbnail: /old_entry/showcase/engineer_lfr/featured_hue7d176f41346907722bcc5ab0fc7f63b_167208_720x2500_fit_q75_h2_lanczos_3.webp
thumbnailAlt: Original preview image from the line-following robot engineering case study.
mediaNote: Captions and transcript are unavailable. The engineering workflow is described below.
media:
  - kind: video
    src: /old_entry/showcase/engineer_lfr/lfr_demo_sharp_corner.mp4
    title: Line following with sharp corners
    caption: Original physical line-following robot demonstration on a route with
      sharp corners.
    mimeType: video/mp4
    sourcePath: showcase/engineer_lfr/lfr_demo_sharp_corner.mp4
    sha256: eacde7723b7c9a26b042919455c823c015ca646177d51ec9eec77b3d959a73bb
    verificationStatus: preserved
    poster: /old_entry/showcase/engineer_lfr/featured_hue7d176f41346907722bcc5ab0fc7f63b_167208_720x2500_fit_q75_h2_lanczos_3.webp
  - kind: video
    src: /old_entry/showcase/engineer_lfr/lfr_map1.mp4
    title: Robot running on the simulation map
    caption: Physical robot running on the map used for simulation.
    mimeType: video/mp4
    sourcePath: showcase/engineer_lfr/lfr_map1.mp4
    sha256: 3f55a88c24667c7a0574b7f92a2cd949c8be03af32040cb04ae76af176ef8fd1
    verificationStatus: preserved
  - kind: video
    src: /old_entry/showcase/engineer_lfr/lfr_map1_sim.mp4
    title: Simulation on the map
    caption: Original simulation recording, kept separate from the physical robot
      demonstrations.
    mimeType: video/mp4
    sourcePath: showcase/engineer_lfr/lfr_map1_sim.mp4
    sha256: 1e89b6236ca1ce4a5e4d84fd7a75bd2480dcb37286306139aa6b16057b4876dc
    verificationStatus: preserved
  - kind: image
    src: /old_entry/showcase/engineer_lfr/m3pi_hu04d1b6a4e115dfc35ed5904b40c996fa_183585_1200x1200_fit_q75_h2_lanczos_3.webp
    title: The m3pi robot
    caption: Original photograph of the robot used in the engineering case study.
    alt: The m3pi robot from the original line-following robot case study
    sourcePath: showcase/engineer_lfr/m3pi_hu04d1b6a4e115dfc35ed5904b40c996fa_183585_1200x1200_fit_q75_h2_lanczos_3.webp
    sha256: 9dd5a67485b7612c51460b83a5dcf20e0be64e077b69c0fd81eb4fe41a48b910
    verificationStatus: preserved
  - kind: image
    src: /old_entry/showcase/engineer_lfr/lfr_math_model_hu11154b5c7d56c293c951a3ab585eac38_2121722_1200x1200_fit_q75_h2_lanczos.webp
    title: Mathematical model
    caption: Mathematical model of the line-following robot.
    alt: Mathematical model from the original line-following robot case study
    sourcePath: showcase/engineer_lfr/lfr_math_model_hu11154b5c7d56c293c951a3ab585eac38_2121722_1200x1200_fit_q75_h2_lanczos.webp
    sha256: ce3793308b8acf2f825cd2654d524f800a698cdce21c93184995b9e1326bc24b
    verificationStatus: preserved
  - kind: image
    src: /old_entry/showcase/engineer_lfr/lfr_dse_result_hu1b4adb50a28e97bc749041e0355b4f07_2481568_1200x1200_fit_q75_h2_lanczos_3.webp
    title: Design-space exploration
    caption: Design-space exploration results obtained using simulation.
    alt: Design-space exploration from the original line-following robot case study
    sourcePath: showcase/engineer_lfr/lfr_dse_result_hu1b4adb50a28e97bc749041e0355b4f07_2481568_1200x1200_fit_q75_h2_lanczos_3.webp
    sha256: f0ea2b9c85552031c919d5bc8ace76b95be9d311c99258388393be4e5943da1b
    verificationStatus: preserved
provenance:
  sourcePage: showcase/engineer_lfr/index.html
  originalDate: '2018-07-03'
relatedPublications: []
paperLinks: []
sourceLinks:
  - label: Original C++ controller source (ZIP)
    url: /old_entry/files/lfr/my_lfr_gcc_20180807.zip
  - label: INTO-CPS Examples Compendium
    url: https://github.com/INTO-CPS-Association/Documentation/blob/master/examples_compendium/INTO-CPS_Examples_Compendium.pdf
  - label: Controller reference cited in the original case study
    url: https://doi.org/10.1016/j.procs.2015.12.329
exampleLinks: []
slidesLinks: []
featured: false
order: 6
---
## Engineering context

This work followed experience in the INTO-CPS project and the start of work on RoboCalc. The original account credits Prof. Jim Woodcock and Prof. Ana Cavalcanti with proposing the physical robot as a way to demonstrate the technologies and explore a potential formal-verification case study.

The original controller discussion cites *Optimization of PID Control for High Speed Line Tracking Robots* as a source of ideas. That reference is supporting literature, not a publication claimed as the author's own work. The INTO-CPS Examples Compendium is also linked as a document to which the author contributed.

## What was completed

The case study includes a controller implementation, physical robot runs, simulation and design-space exploration. The planned formal verification was not completed.

## Implementation

The C++ controller is available as a ZIP download. Consult the hardware, toolchain and simulation requirements before reproducing the experiments.
