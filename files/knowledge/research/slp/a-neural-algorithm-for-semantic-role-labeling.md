---
title: "A Neural Algorithm for Semantic Role Labeling"
summary: "§II Annotating Linguistic Structure › Semantic Role Labeling : 21.6 • SEMANTIC ROLE LABELING • The first words and the last word of the constituent. The following feature vector thus represents the first NP in our example (recall that most observations will have the value NONE ra"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "499-499"
---

# A Neural Algorithm for Semantic Role Labeling

§II Annotating Linguistic Structure › Semantic Role Labeling › Semantic Role Labeling › A Neural Algorithm for Semantic Role Labeling · pp. 499–499 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
21.6 • SEMANTIC ROLE LABELING • The first words and the last word of the constituent. The following feature vector thus represents the first NP in our example (recall that most observations will have the value NONE rather than, for example, ARG0, since most constituents in the parse tree will not bear a semantic role): ARG0: [issued, NP, Examiner, NNP, NP↑S↓VP↓VBD, active, before, VP →NP PP, ORG, The, Examiner] Other features are often used in addition, such as sets of n-grams inside the constituent, or more complex versions of the path features (the upward or downward halves, or whether particular nodes occur in the path). It’s also possible to use dependency parses instead of constituency parses as the basis of features, for example using dependency parse paths instead of constituency paths. A simple neural approach to SRL is to treat it as a sequence labeling task like namedentity recognition, using the BIO approach. Let’s assume that we are given the predicate and the task is just detecting and labeling spans. Recall that with BIO tagging, we have a begin and end tag for each possible role (B-ARG0, I-ARG0; BARG1, I-ARG1, and so on), plus an outside tag O. ENCODER [CLS] the cats love hats [SEP] love [SEP] FFN B-ARG0 I-ARG0 B-PRED concatenate with predicate B-ARG1 FFN FFN FFN FFN Figure 21.6 A simple neural approach to semantic role labeling.

## Key terms
- **word** — 5 mentions
- **predicate** — 5 mentions
- **role** — 4 mentions
- **labeling** — 4 mentions
- **feature** — 4 mentions
- **parse** — 4 mentions
- **path** — 4 mentions
- **input** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=499|Speech and Language Processing.pdf p. 499]]

## Liens
- Up: [[research/slp/semantic-role-labeling-2]]
- ← Prev: [[research/slp/a-feature-based-algorithm-for-semantic-role-labeling]]
- Next: [[research/slp/evaluation-of-semantic-role-labeling]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
