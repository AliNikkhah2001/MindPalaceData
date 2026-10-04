---
title: "RNNs as Language Models"
summary: "§I Large Language Models › RNNs and LSTMs › RNNs as Language : 13.1 • RECURRENT NEURAL NETWORKS U V W U V W U V W x1 x2 x3 y1 y2 y3 h1 h3 h2 h0 Figure 13.4 A simple recurrent neural network shown unrolled in time."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "295-298"
---

# RNNs as Language Models

§I Large Language Models › RNNs and LSTMs › RNNs as Language Models · pp. 295–298 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
13.1 • RECURRENT NEURAL NETWORKS U V W U V W U V W x1 x2 x3 y1 y2 y3 h1 h3 h2 h0 Figure 13.4 A simple recurrent neural network shown unrolled in time. Network layers are recalculated for each time step, while the weights U, V and W are shared across all time steps. Tailoring the backpropagation algorithm to this situation leads to a two-pass algorithm for training the weights in RNNs. In the first pass, we perform forward inference, computing ht, yt, accumulating the loss at each step in time, saving the value of the hidden layer at each step for use at the next time step. In the second pass, we process the sequence in reverse, computing the required gradients as we go, computing and saving the error term for use in the hidden layer for each step backward in time. This general approach is commonly referred to as backpropagation through time (Werbos 1974, Rumelhart et al. 1986, Werbos 1990). backpropaga- tion through time Fortunately, with modern computational frameworks and adequate computing resources, there is no need for a specialized approach to training RNNs. As illustrated in Fig. 13.4, explicitly unrolling a recurrent network into a feedforward computational graph eliminates any explicit recurrences, allowing the network weights to be trained directly.

## Key terms
- **word** — 34 mentions
- **model** — 29 mentions
- **language** — 20 mentions
- **next** — 18 mentions
- **sequence** — 16 mentions
- **time** — 15 mentions
- **input** — 14 mentions
- **hidden** — 13 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=295|Speech and Language Processing.pdf p. 295]]

## Liens
- Up: [[research/slp/rnns-and-lstms]]
- ← Prev: [[research/slp/recurrent-neural-networks]]
- Next: [[research/slp/rnns-for-other-nlp-tasks]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
