---
title: "Gated Units, Layers and Networks"
summary: "§I Large Language Models › RNNs and LSTMs › The LSTM › Gated : 13.5 • THE LSTM + xt ht-1 ct ht ct ht ct-1 ht-1 xt tanh + σ tanh σ σ + + + i g f o ⦿ ⦿ ⦿ LSTM ct-1 Figure 13.13 A single LSTM unit displayed as a computation graph."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "307-307"
---

# Gated Units, Layers and Networks

§I Large Language Models › RNNs and LSTMs › The LSTM › Gated Units, Layers and Networks · pp. 307–307 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
13.5 • THE LSTM + xt ht-1 ct ht ct ht ct-1 ht-1 xt tanh + σ tanh σ σ + + + i g f o ⦿ ⦿ ⦿ LSTM ct-1 Figure 13.13 A single LSTM unit displayed as a computation graph. The inputs to each unit consists of the current input, x, the previous hidden state, ht−1, and the previous context, ct−1. The outputs are a new hidden state, ht and an updated context, ct. h x xt xt ht-1 ht ht ct-1 ct ht-1 (b) (a) (c) ⌃ g z a ⌃ g z LSTM Unit a Figure 13.14 Basic neural units used in feedforward, simple recurrent networks (SRN), and long short-term memory (LSTM). The neural units used in LSTMs are obviously much more complex than those used in basic feedforward networks. Fortunately, this complexity is encapsulated within the basic processing units, allowing us to maintain modularity and to easily experiment with different architectures. To see this, consider Fig. 13.14 which illustrates the inputs and outputs associated with each kind of unit. At the far left, (a) is the basic feedforward unit where a single set of weights and a single activation function determine its output, and when arranged in a layer there are no connections among the units in the layer. Next, (b) represents the unit in a simple recurrent network.

## Key terms
- **unit** — 15 mentions
- **lstm** — 10 mentions
- **input** — 5 mentions
- **basic** — 5 mentions
- **output** — 5 mentions
- **ht-1** — 4 mentions
- **single** — 4 mentions
- **network** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=307|Speech and Language Processing.pdf p. 307]]

## Liens
- Up: [[research/slp/the-lstm]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
