---
title: "RST parsing"
summary: "§II Annotating Linguistic Structure › Discourse Coherence › D: 24.2 • DISCOURSE STRUCTURE PARSING tree as we do for RST). RST parsing is generally done in two stages. The first stage, EDU segmentation, extracts the start and end of each EDU."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "565-566"
---

# RST parsing

§II Annotating Linguistic Structure › Discourse Coherence › Discourse Structure Parsing › RST parsing · pp. 565–566 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
24.2 • DISCOURSE STRUCTURE PARSING tree as we do for RST). RST parsing is generally done in two stages. The first stage, EDU segmentation, extracts the start and end of each EDU. The output of this stage would be a labeling like the following: (24.16) [Mr. Rambo says]e1 [that a 3.2-acre property]e2 [overlooking the San Fernando Valley]e3 [is priced at $4 million]e4 [because the late actor Erroll Flynn once lived there.]e5 Since EDUs roughly correspond to clauses, early models of EDU segmentation first ran a syntactic parser, and then post-processed the output. Modern systems generally use neural sequence models supervised by the gold EDU segmentation in datasets like the RST Discourse Treebank. Fig. 24.4 shows an example architecture simplified from the algorithm of Lukasik et al. (2020) that predicts for each token whether or not it is a break. Here the input sentence is passed through an encoder and then passed through a linear layer and a softmax to produce a sequence of 0s and 1, where 1 indicates the start of an EDU. Mr. Rambo says that ENCODER … linear layer EDU break Figure 24.4 Predicting EDU segment beginnings from encoded text. Tools for building RST coherence structure for a discourse have long been based on syntactic parsing algorithms like shift-reduce parsing (Marcu, 1999).

## Key terms
- **parser** — 8 mentions
- **representation** — 7 mentions
- **sequence** — 6 mentions
- **stack** — 6 mentions
- **action** — 6 mentions
- **bilstm** — 6 mentions
- **discourse** — 5 mentions
- **parsing** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=565|Speech and Language Processing.pdf p. 565]]

## Liens
- Up: [[research/slp/discourse-structure-parsing]]
- ← Prev: [[research/slp/edu-segmentation-for-rst-parsing]]
- Next: [[research/slp/pdtb-discourse-parsing]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
