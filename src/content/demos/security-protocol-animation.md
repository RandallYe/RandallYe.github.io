---
slug: security-protocol-animation
title: User-Guided Verification of Security Protocols via Sound Animation
subtitle: Explore protocol behaviour, grounded in a formal model.
summary: A research tool for exploring executions of security-protocol specifications, connecting interactive animation with Isabelle/HOL foundations.
researchArea: Security Protocol Verification
status: recorded-demonstration
problem: Protocol specifications can be difficult to inspect. An accessible animator helps designers explore how participants and an intruder may interact within a specified model.
method: This co-authored work uses interaction-tree-based CSP models in Isabelle/HOL and generates Haskell animators. The repository documents manual exploration and user-guided reachability searches.
whatVisitorsSee:
  - title: Start from a protocol specification
    description: The source repository provides Isabelle/HOL models and generated Haskell animator code for the early framework presented at SEFM 2024.
  - title: Explore possible executions
    description: The documented terminal interface offers enabled events for the user to select, revealing the next state of an execution.
  - title: Inspect behaviour within the model
    description: Repository examples combine manual choices with automatic reachability exploration and display resulting traces. These instructions describe the documented workflow, rather than a timestamped video transcript.
resultsOrLimitations: Animation soundness relates generated behaviour to the formal semantics. It is distinct from a proof that every execution satisfies a particular security property. Conclusions depend on the chosen model, intruder assumptions, parameters and exploration bounds.
thumbnailAlt: No verified video still is available.
mediaNote: Security-protocol animation demonstration presented at MWC2025.
videoUrl: https://www.youtube.com/watch?v=8FO6KT6EMqM
paperLinks:
  - label: Read the SEFM 2024 paper
    url: https://doi.org/10.1007/978-3-031-77382-2_3
sourceLinks:
  - label: View Isabelle/HOL and animator source
    url: https://github.com/RandallYe/Animation_of_Security_Protocols
relatedPublications:
  - security-protocol-animation
examplesHeading: Two protocol examples
exampleLinks:
  - label: Needham–Schroeder public-key specification
    description: Explore the public-key protocol specification in the early-framework model collection. Related variants are documented in the repository.
    url: https://github.com/RandallYe/Animation_of_Security_Protocols/blob/master/User_Guided_Verification_Security/NSPKP/NSPK3/NSPK3.thy
  - label: Diffie–Hellman specification
    description: Inspect the key-agreement specification and its explicit intruder model. The repository also documents a digital-signature variant.
    url: https://github.com/RandallYe/Animation_of_Security_Protocols/blob/master/User_Guided_Verification_Security/Diffie_Hellman/DH_v1/DH.thy
slidesLinks:
  - label: SEFM presentation slides (PDF)
    url: https://randallye.github.io/SEFM2024/SEFM2024_presentation.pdf
featured: true
order: 1
---
## Formal foundations and scope

The SEFM 2024 paper is by **K. Ye, R. Metere and P. Yadav**, published in *Software Engineering and Formal Methods*, pages 33–51. The animator is grounded in an interaction-tree model of CSP mechanised in Isabelle/HOL.

The repository includes an early framework associated with this paper and a later generic framework. Later additions and their security claims should be read in their own context rather than attributed to the 2024 publication.

## Running the research software

The repository documents local execution of generated Haskell animators with GHC. Regenerating an animator from a theory requires the patched Isabelle/UTP environment described in the README. The web interface uses the Haskell Yesod framework and requires its own runtime.

Run the animators locally using the repository’s installation instructions.
