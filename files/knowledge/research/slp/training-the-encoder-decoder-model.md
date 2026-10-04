---
title: "Training the Encoder-Decoder Model"
summary: "§I Large Language Models › RNNs and LSTMs › The Encoder-Decod: CHAPTER 13 • RNNS AND LSTMS use c as its prior hidden state hd 0. The decoder would then autoregressively generate a sequence of outputs, an element at a time, until an end-of-sequence marker is generated."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "312-312"
---

# Training the Encoder-Decoder Model

§I Large Language Models › RNNs and LSTMs › The Encoder-Decoder Model with RNNs › Training the Encoder-Decoder Model · pp. 312–312 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 13 • RNNS AND LSTMS use c as its prior hidden state hd 0. The decoder would then autoregressively generate a sequence of outputs, an element at a time, until an end-of-sequence marker is generated. Each hidden state is conditioned on the previous hidden state and the output generated in the previous state. As Fig. 13.18 shows, we do something more complex: we make the context vector c available to more than just the first decoder hidden state, to ensure that the influence of the context vector, c, doesn’t wane as the output sequence is generated. We do this by adding c as a parameter to the computation of the current hidden state. using the following equation: hd t = g(ˆyt−1,hd t−1,c) (13.32) Now we’re ready to see the full equations for this version of the decoder in the basic encoder-decoder model, with context available at each decoding timestep. Recall that g is a stand-in for some flavor of RNN and ˆyt−1 is the embedding for the output sampled from the softmax at the previous step: c = he n hd 0 = c hd t = g(ˆyt−1,hd t−1,c) ˆyt = softmax(hd t ) (13.33) Thus ˆyt is a vector of probabilities over the vocabulary, representing the probability of each word occurring at time t.

## Key terms
- **training** — 9 mentions
- **decoder** — 7 mentions
- **output** — 7 mentions
- **state** — 6 mentions
- **hidden** — 5 mentions
- **time** — 4 mentions
- **token** — 4 mentions
- **generate** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=312|Speech and Language Processing.pdf p. 312]]

## Liens
- Up: [[research/slp/the-encoder-decoder-model-with-rnns]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
