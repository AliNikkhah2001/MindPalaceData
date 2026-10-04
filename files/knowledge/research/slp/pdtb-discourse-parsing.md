---
title: "PDTB discourse parsing"
summary: "§II Annotating Linguistic Structure › Discourse Coherence › D: 24.2 • DISCOURSE STRUCTURE PARSING Training first maps each RST gold parse tree into a sequence of oracle actions, and then uses the standard cross-entropy loss (with l2 regularization) to train the system to take suc"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "567-567"
---

# PDTB discourse parsing

§II Annotating Linguistic Structure › Discourse Coherence › Discourse Structure Parsing › PDTB discourse parsing · pp. 567–567 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
24.2 • DISCOURSE STRUCTURE PARSING Training first maps each RST gold parse tree into a sequence of oracle actions, and then uses the standard cross-entropy loss (with l2 regularization) to train the system to take such actions. Give a state S and oracle action a, we first compute the decoder output using Eq. 24.20, apply a softmax to get probabilities: pa = exp(oa) P a′∈A exp(oa′) (24.22) and then computing the cross-entropy loss: LCE() = −log(pa)+ λ 2 ||Θ||2 (24.23) RST discourse parsers are evaluated on the test section of the RST Discourse Treebank, either with gold EDUs or end-to-end, using the RST-Pareval metrics (Marcu, 2000b). It is standard to first transform the gold RST trees into right-branching binary trees, and to report four metrics: trees with no labels (S for Span), labeled with nuclei (N), with relations (R), or both (F for Full), for each metric computing micro-averaged F1 over all spans from all documents (Marcu 2000b, Morey et al. 2017). PDTB discourse parsing, the task of detecting PDTB coherence relations between spans, is sometimes called shallow discourse parsing because the task just involves shallow discourse parsing flat relationships between text spans, rather than the full trees of RST parsing.

## Key terms
- **discourse** — 10 mentions
- **span** — 9 mentions
- **task** — 9 mentions
- **parsing** — 6 mentions
- **tree** — 5 mentions
- **connective** — 5 mentions
- **relation** — 5 mentions
- **first** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=567|Speech and Language Processing.pdf p. 567]]

## Liens
- Up: [[research/slp/discourse-structure-parsing]]
- ← Prev: [[research/slp/rst-parsing]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
