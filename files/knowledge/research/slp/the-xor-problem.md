---
title: "The XOR problem"
summary: "§I Large Language Models › Neural Networks › The XOR problem: 6.2 • THE XOR PROBLEM (a) (b) Figure 6.3 The tanh and ReLU activation functions. result from it being very close to linear."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "131-132"
---

# The XOR problem

§I Large Language Models › Neural Networks › The XOR problem · pp. 131–132 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
6.2 • THE XOR PROBLEM (a) (b) Figure 6.3 The tanh and ReLU activation functions. result from it being very close to linear. In the sigmoid or tanh functions, very high values of z result in values of y that are saturated, i.e., extremely close to 1, and have saturated derivatives very close to 0. Zero derivatives cause problems for learning, because as we’ll see in Section 6.6, we’ll train networks by propagating an error signal backwards, multiplying gradients (partial derivatives) from each layer of the network; gradients that are almost 0 cause the error signal to get smaller and smaller until it is too small to be used for training, a problem called the vanishing gradient problem. vanishing gradient Rectifiers don’t have this problem, since the derivative of ReLU for high values of z is 1 rather than very close to 0. Early in the history of neural networks it was realized that the power of neural networks, as with the real neurons that inspired them, comes from combining these units into larger networks. One of the most clever demonstrations of the need for multi-layer networks was the proof by Minsky and Papert (1969) that a single neural unit cannot compute some very simple functions of its input.

## Key terms
- **input** — 15 mentions
- **function** — 14 mentions
- **weight** — 13 mentions
- **perceptron** — 11 mentions
- **network** — 10 mentions
- **unit** — 8 mentions
- **bias** — 8 mentions
- **line** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=131|Speech and Language Processing.pdf p. 131]]

## Liens
- Up: [[research/slp/neural-networks]]
- ← Prev: [[research/slp/units]]
- Next: [[research/slp/feedforward-neural-networks]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
