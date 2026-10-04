---
title: "Bidirectional RNNs"
summary: "§I Large Language Models › RNNs and LSTMs › Stacked and Bidir: 13.4 • STACKED AND BIDIRECTIONAL RNN ARCHITECTURES y1 y2 y3 yn x1 x2 x3 xn RNN 1 RNN 2 RNN 3 Figure 13.10 Stacked recurrent networks."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "303-303"
---

# Bidirectional RNNs

§I Large Language Models › RNNs and LSTMs › Stacked and Bidirectional RNN architectures › Bidirectional RNNs · pp. 303–303 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
13.4 • STACKED AND BIDIRECTIONAL RNN ARCHITECTURES y1 y2 y3 yn x1 x2 x3 xn RNN 1 RNN 2 RNN 3 Figure 13.10 Stacked recurrent networks. The output of a lower level serves as the input to higher levels with the output of the last network serving as the final output. quickly. The RNN uses information from the left (prior) context to make its predictions at time t. But in many applications we have access to the entire input sequence; in those cases we would like to use words from the context to the right of t. One way to do this is to run two separate RNNs, one left-to-right, and one right-to-left, and concatenate their representations. In the left-to-right RNNs we’ve discussed so far, the hidden state at a given time t represents everything the network knows about the sequence up to that point. The state is a function of the inputs x1,...,xt and represents the context of the network to the left of the current time. h f t = RNNforward(x1,...,xt) (13.16) This new notation h f t simply corresponds to the normal hidden state at time t, representing everything the network has gleaned from the sequence so far. To take advantage of context to the right of the current input, we can train an RNN on a reversed input sequence.

## Key terms
- **input** — 8 mentions
- **sequence** — 7 mentions
- **network** — 6 mentions
- **time** — 6 mentions
- **context** — 5 mentions
- **state** — 5 mentions
- **right** — 4 mentions
- **hidden** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=303|Speech and Language Processing.pdf p. 303]]

## Liens
- Up: [[research/slp/stacked-and-bidirectional-rnn-architectures]]
- ← Prev: [[research/slp/stacked-rnns]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
