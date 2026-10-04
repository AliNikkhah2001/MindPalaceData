---
title: "Representation learning models for local coherence"
summary: "§II Annotating Linguistic Structure › Discourse Coherence › R: CHAPTER 24 • DISCOURSE COHERENCE a modified order (such as a randomized order). We turn to these evaluations in the next section."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "572-573"
---

# Representation learning models for local coherence

§II Annotating Linguistic Structure › Discourse Coherence › Representation learning models for local coherence · pp. 572–573 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 24 • DISCOURSE COHERENCE a modified order (such as a randomized order). We turn to these evaluations in the next section. Entity-based coherence models, as well as the neural models we introduce in the next section, are generally evaluated in one of two ways. First, we can have humans rate the coherence of a document and train a classifier to predict these human ratings, which can be categorial (high/low, or high/mid/low) or continuous. This is the best evaluation to use if we have some end task in mind, like essay grading, where human raters are the correct definition of the final label. Alternatively, since it’s very expensive to get human labels, and we might not yet have an end-task in mind, we can use natural texts to do self-supervision. In self-supervision we pair up a natural discourse with a pseudo-document created by changing the ordering. Since naturally-ordered discourses are more coherent than random permutation (Lin et al., 2011), a successful coherence algorithm should prefer the original ordering. Self-supervision has been implemented in 3 ways. In the sentence order discrimination task (Barzilay and Lapata, 2005), we compare a document to a random permutation of its sentences.

## Key terms
- **sentence** — 28 mentions
- **coherence** — 20 mentions
- **model** — 19 mentions
- **document** — 15 mentions
- **pair** — 15 mentions
- **embedding** — 8 mentions
- **discourse** — 7 mentions
- **original** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=572|Speech and Language Processing.pdf p. 572]]

## Liens
- Up: [[research/slp/discourse-coherence]]
- ← Prev: [[research/slp/centering-and-entity-based-coherence]]
- Next: [[research/slp/global-coherence]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
