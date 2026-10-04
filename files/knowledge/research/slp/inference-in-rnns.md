---
title: "Inference in RNNs"
summary: "§I Large Language Models › RNNs and LSTMs › Recurrent Neural : 13.1 • RECURRENT NEURAL NETWORKS xt ht yt Figure 13.1 Simple recurrent neural network after Elman (1990). The hidden layer includes a recurrent connection as part of its input."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "293-293"
---

# Inference in RNNs

§I Large Language Models › RNNs and LSTMs › Recurrent Neural Networks › Inference in RNNs · pp. 293–293 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
13.1 • RECURRENT NEURAL NETWORKS xt ht yt Figure 13.1 Simple recurrent neural network after Elman (1990). The hidden layer includes a recurrent connection as part of its input. That is, the activation value of the hidden layer depends on the current input as well as the activation value of the hidden layer from the previous time step. subscripts to represent time, thus xt will mean the input vector x at time t. The key difference from a feedforward network lies in the recurrent link shown in the figure with the dashed line. This link augments the input to the computation at the hidden layer with the value of the hidden layer from the preceding point in time. The hidden layer from the previous time step provides a form of memory, or context, that encodes earlier processing and informs the decisions to be made at later points in time. Critically, this approach does not impose a fixed-length limit on this prior context; the context embodied in the previous hidden layer can include information extending back to the beginning of the sequence. Adding this temporal dimension makes RNNs appear to be more complex than non-recurrent architectures. But in reality, they’re not all that different.

## Key terms
- **hidden** — 13 mentions
- **layer** — 13 mentions
- **time** — 10 mentions
- **input** — 9 mentions
- **network** — 8 mentions
- **step** — 6 mentions
- **recurrent** — 5 mentions
- **value** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=293|Speech and Language Processing.pdf p. 293]]

## Liens
- Up: [[research/slp/recurrent-neural-networks]]
- Next: [[research/slp/training-2]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
