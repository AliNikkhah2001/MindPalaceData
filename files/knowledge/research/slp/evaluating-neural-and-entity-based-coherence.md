---
title: "Evaluating Neural and Entity-based coherence"
summary: "§II Annotating Linguistic Structure › Discourse Coherence › C: CHAPTER 24 • DISCOURSE COHERENCE a modified order (such as a randomized order). We turn to these evaluations in the next section."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "572-572"
---

# Evaluating Neural and Entity-based coherence

§II Annotating Linguistic Structure › Discourse Coherence › Centering and Entity-Based Coherence › Evaluating Neural and Entity-based coherence · pp. 572–572 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 24 • DISCOURSE COHERENCE a modified order (such as a randomized order). We turn to these evaluations in the next section. Entity-based coherence models, as well as the neural models we introduce in the next section, are generally evaluated in one of two ways. First, we can have humans rate the coherence of a document and train a classifier to predict these human ratings, which can be categorial (high/low, or high/mid/low) or continuous. This is the best evaluation to use if we have some end task in mind, like essay grading, where human raters are the correct definition of the final label. Alternatively, since it’s very expensive to get human labels, and we might not yet have an end-task in mind, we can use natural texts to do self-supervision. In self-supervision we pair up a natural discourse with a pseudo-document created by changing the ordering. Since naturally-ordered discourses are more coherent than random permutation (Lin et al., 2011), a successful coherence algorithm should prefer the original ordering. Self-supervision has been implemented in 3 ways. In the sentence order discrimination task (Barzilay and Lapata, 2005), we compare a document to a random permutation of its sentences.

## Key terms
- **document** — 12 mentions
- **sentence** — 9 mentions
- **coherence** — 7 mentions
- **original** — 7 mentions
- **task** — 6 mentions
- **permutation** — 6 mentions
- **discourse** — 5 mentions
- **order** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=572|Speech and Language Processing.pdf p. 572]]

## Liens
- Up: [[research/slp/centering-and-entity-based-coherence]]
- ← Prev: [[research/slp/entity-grid-model]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
