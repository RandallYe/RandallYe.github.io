import researchAreas from './research-areas.json';

export const research = researchAreas;
export const tools = [
  { title: 'ProbURel', demoId: 'probabilistic-relations', kind: 'Mechanised theory', summary: 'Probabilistic relations and algebraic laws in Isabelle/HOL, with worked examples in the source repository.', url: 'https://github.com/RandallYe/probabilistic_programming_utp/tree/main/probability/probabilistic_relations' },
  { title: 'Circus2ZCSP', kind: 'Translation tool', summary: 'Linking state-rich Circus models to a combination of state-based specification and process algebra for model checking.', url: 'https://github.com/RandallYe/Circus2ZCSP' },
  { title: 'Interaction trees', demoId: 'robochart-chemical-detector', kind: 'Formal foundations', summary: 'Isabelle/HOL interaction trees and a CSP model underpinning co-authored work on RoboChart animation.', url: 'https://github.com/isabelle-utp/interaction-trees' },
];
