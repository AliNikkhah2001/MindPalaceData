---
title: "More details on feedforward networks"
summary: "§I Large Language Models › Neural Networks › Feedforward Neur: 6.3 • FEEDFORWARD NEURAL NETWORKS Let’s now set up some notation to make it easier to talk about deeper networks of depth more than 2."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "137-137"
---

# More details on feedforward networks

§I Large Language Models › Neural Networks › Feedforward Neural Networks › More details on feedforward networks · pp. 137–137 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
6.3 • FEEDFORWARD NEURAL NETWORKS Let’s now set up some notation to make it easier to talk about deeper networks of depth more than 2. We’ll use superscripts in square brackets to mean layer numbers, starting at 0 for the input layer. So W[1] will mean the weight matrix for the (first) hidden layer, and b[1] will mean the bias vector for the (first) hidden layer. n j will mean the number of units at layer j. We’ll use g(·) to stand for the activation function, which will tend to be ReLU or tanh for intermediate layers and softmax for output layers. We’ll use a[i] to mean the output from layer i, and z[i] to mean the combination of previous layer output, weights and biases W[i]a[i−1] + b[i]. The 0th layer is for inputs, so we’ll refer to the inputs x more generally as a[0]. Thus we can re-represent our 2-layer net from Eq. 6.12 as follows: z[1] = W[1]a[0] +b[1] a[1] = g[1](z[1]) z[2] = W[2]a[1] +b[2] a[2] = g[2](z[2]) ˆy = a[2] (6.13) Note that with this notation, the equations for the computation done at each layer are the same. The algorithm for computing the forward step in an n-layer feedforward network, given the input vector a[0] is thus simply: for i in 1,...,n z[i] = W[i] a[i−1] + b[i] a[i] = g[i](z[i]) ˆy = a[n] It’s often useful to have a name for the final set of activations right before the final softmax.

## Key terms
- **layer** — 18 mentions
- **network** — 11 mentions
- **mean** — 6 mentions
- **activation** — 5 mentions
- **function** — 5 mentions
- **input** — 4 mentions
- **vector** — 4 mentions
- **final** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=137|Speech and Language Processing.pdf p. 137]]

## Liens
- Up: [[research/slp/feedforward-neural-networks]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
