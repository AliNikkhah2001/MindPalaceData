---
title: "Neural net classifiers with hand-built features"
summary: "§I Large Language Models › Neural Networks › Feedforward netw: 6.4 • FEEDFORWARD NETWORKS FOR NLP: CLASSIFICATION of Chapter 9. Nonetheless seeing a feedforward network text classifier will let us introduce key ideas that will play a role throughout the rest of the book, includin"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "139-139"
---

# Neural net classifiers with hand-built features

§I Large Language Models › Neural Networks › Feedforward networks for NLP: Classification › Neural net classifiers with hand-built features · pp. 139–139 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
6.4 • FEEDFORWARD NETWORKS FOR NLP: CLASSIFICATION of Chapter 9. Nonetheless seeing a feedforward network text classifier will let us introduce key ideas that will play a role throughout the rest of the book, including the ideas of the embedding matrix, representation pooling, and representation learning. But before introducing any of these ideas, let’s start with a classifier by making only minimal change from the sentiment classifiers we saw in Chapter 4. Like them, we’ll take hand-built features, pass them through a classifier, and produce a class probability. The only difference is that we’ll use a neural network instead of logistic regression as the classifier. Let’s begin with a simple 2-layer sentiment classifier by taking our logistic regression classifier from Chapter 4, which corresponds to a 1-layer network, and just adding a hidden layer. The input element xi can be scalar features like those in Fig. 4.2, e.g., x1 = count(words ∈doc), x2 = count(positive lexicon words ∈doc), x3 = 1 if “no” ∈doc, and so on, for a total of d features. And the output layer ˆy could have two nodes (one each for positive and negative), or 3 nodes (positive, negative, neutral), in which case ˆy1 would be the estimated probability of positive sentiment, ˆy2 the probability of negative and ˆy3 the probability of neutral.

## Key terms
- **classifier** — 9 mentions
- **layer** — 9 mentions
- **network** — 7 mentions
- **feature** — 7 mentions
- **sentiment** — 5 mentions
- **positive** — 5 mentions
- **probability** — 4 mentions
- **input** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=139|Speech and Language Processing.pdf p. 139]]

## Liens
- Up: [[research/slp/feedforward-networks-for-nlp-classification]]
- Next: [[research/slp/vectorizing-for-parallelizing-inference]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
