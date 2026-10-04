---
title: "Feedforward Neural Networks"
summary: "§I Large Language Models › Neural Networks › Feedforward Neur: 6.2 • THE XOR PROBLEM x1 x2 x1 x2 x1 x2 a) x1 AND x2 b) x1 OR x2 c) x1 XOR x2 ? Filled circles represent perceptron outputs of 1, and white circles perceptron outputs of 0."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "133-137"
---

# Feedforward Neural Networks

§I Large Language Models › Neural Networks › Feedforward Neural Networks · pp. 133–137 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
6.2 • THE XOR PROBLEM x1 x2 x1 x2 x1 x2 a) x1 AND x2 b) x1 OR x2 c) x1 XOR x2 ? Figure 6.5 The functions AND, OR, and XOR, represented with input x1 on the x-axis and input x2 on the y-axis. Filled circles represent perceptron outputs of 1, and white circles perceptron outputs of 0. There is no way to draw a line that correctly separates the two categories for XOR. Figure styled after Russell and Norvig (2002). x1 x2 h1 h2 y1 +1 -1 -2 +1 Figure 6.6 XOR solution after Goodfellow et al. (2016). There are three ReLU units, in two layers; we’ve called them h1, h2 (h for “hidden layer”) and y1. As before, the numbers on the arrows represent the weights w for each unit, and we represent the bias b as a weight on a unit clamped to +1, with the bias weights/units in gray. It’s also instructive to look at the intermediate results, the outputs of the two hidden nodes h1 and h2. We showed in the previous paragraph that the h vector for the inputs x = [0, 0] was [0, 0]. Fig. 6.7b shows the values of the h layer for all 4 inputs. Notice that hidden representations of the two input points x = [0, 1] and x = [1, 0] (the two cases with XOR output = 1) are merged to the single point h = [1, 0]. The merger makes it easy to linearly separate the positive and negative cases of XOR.

## Key terms
- **layer** — 58 mentions
- **network** — 32 mentions
- **output** — 30 mentions
- **input** — 28 mentions
- **hidden** — 28 mentions
- **vector** — 28 mentions
- **unit** — 26 mentions
- **weight** — 19 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=133|Speech and Language Processing.pdf p. 133]]

## Liens
- Up: [[research/slp/neural-networks]]
- ← Prev: [[research/slp/the-xor-problem]]
- Next: [[research/slp/feedforward-networks-for-nlp-classification]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
