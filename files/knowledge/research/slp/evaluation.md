---
title: "Evaluation"
summary: "§II Annotating Linguistic Structure › Dependency Parsing › Ev: 19.4 • EVALUATION where U, W, and b are weights learned by the model. The idea of using a biaffine function is to allow the system to learn multiplicative interactions between the vectors x and y."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "459-459"
---

# Evaluation

§II Annotating Linguistic Structure › Dependency Parsing › Evaluation · pp. 459–459 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
19.4 • EVALUATION where U, W, and b are weights learned by the model. The idea of using a biaffine function is to allow the system to learn multiplicative interactions between the vectors x and y. If we pass Score(i →j) through a softmax, we end up with a probability distribution, for each token j, over potential heads i (all other tokens in the sentence): p(i →j) = softmax([Score(k →j);∀k̸ = j,1 ≤k ≤n]) (19.17) This probability can then be passed to the maximum spanning tree algorithm of Section 19.3.1 to find the best tree. This p(i →j) classifier is trained by optimizing the cross-entropy loss. Note that the algorithm as we’ve described it is unlabeled. To make this into a labeled algorithm, the Dozat and Manning (2017) algorithm actually trains two classifiers. The first classifier, the edge-scorer, the one we described above, assigns a probability p(i →j) to each word wi and w j. Then the Maximum Spanning Tree algorithm is run to get a single best dependency parse tree for the second. We then apply a second classifier, the label-scorer, whose job is to find the maximum probability label for each edge in this parse. This second classifier has the same form as (19.15-19.17), but instead of being trained to predict with binary softmax the probability of an edge existing between two words, it is trained with a softmax over dependency labels to predict the dependency label between the words.

## Key terms
- **dependency** — 9 mentions
- **relation** — 8 mentions
- **system** — 7 mentions
- **parse** — 7 mentions
- **score** — 6 mentions
- **attachment** — 6 mentions
- **probability** — 5 mentions
- **algorithm** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=459|Speech and Language Processing.pdf p. 459]]

## Liens
- Up: [[research/slp/dependency-parsing]]
- ← Prev: [[research/slp/graph-based-dependency-parsing]]
- Next: [[research/slp/summary-18]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
