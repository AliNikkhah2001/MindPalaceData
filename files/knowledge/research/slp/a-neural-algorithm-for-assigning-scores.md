---
title: "A neural algorithm for assigning scores"
summary: "§II Annotating Linguistic Structure › Dependency Parsing › Gr: 19.3 • GRAPH-BASED DEPENDENCY PARSING root Book tf root Book that flight -3 -4 -7 -1 -6 -2 root Book that flight -4 -3 -2 -6 -1 -7 root Book tf -1 -3 -4 -7 -1 -6 -2 root Book that flight Deleted from cycle Figure 19.1"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "457-458"
---

# A neural algorithm for assigning scores

§II Annotating Linguistic Structure › Dependency Parsing › Graph-Based Dependency Parsing › A neural algorithm for assigning scores · pp. 457–458 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
19.3 • GRAPH-BASED DEPENDENCY PARSING root Book tf root Book that flight -3 -4 -7 -1 -6 -2 root Book that flight -4 -3 -2 -6 -1 -7 root Book tf -1 -3 -4 -7 -1 -6 -2 root Book that flight Deleted from cycle Figure 19.13 Chu-Liu-Edmonds graph-based example for Book that flight • Wordforms, lemmas, and parts of speech of the headword and its dependent. • Corresponding features from the contexts before, after and between the words. • Word embeddings. • The dependency relation itself. • The direction of the relation (to the right or left). • The distance from the head to the dependent. Given a set of features, our next problem is to learn a set of weights corresponding to each. Unlike many of the learning problems discussed in earlier chapters, here we are not training a model to associate training items with class labels, or parser actions. Instead, we seek to train a model that assigns higher scores to correct trees than to incorrect ones. An effective framework for problems like this is to use inference-based learning combined with the perceptron learning rule. In this inference-based framework, we parse a sentence (i.e, perform inference) from the training set using some initially random set of initial weights.

## Key terms
- **head** — 14 mentions
- **book** — 8 mentions
- **dependent** — 8 mentions
- **representation** — 7 mentions
- **score** — 7 mentions
- **flight** — 6 mentions
- **word** — 6 mentions
- **root** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=457|Speech and Language Processing.pdf p. 457]]

## Liens
- Up: [[research/slp/graph-based-dependency-parsing]]
- ← Prev: [[research/slp/a-feature-based-algorithm-for-assigning-scores]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
