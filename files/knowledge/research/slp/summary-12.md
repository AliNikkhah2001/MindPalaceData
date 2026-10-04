---
title: "Summary"
summary: "§I Large Language Models › RNNs and LSTMs › Summary: 13.9 • SUMMARY With this, we finally have a fixed-length context vector that takes into account information from the entire encoder state that is dynamically updated to reflect the needs of the decoder at each step of decoding."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "315-315"
---

# Summary

§I Large Language Models › RNNs and LSTMs › Summary · pp. 315–315 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
13.9 • SUMMARY With this, we finally have a fixed-length context vector that takes into account information from the entire encoder state that is dynamically updated to reflect the needs of the decoder at each step of decoding. Fig. 13.22 illustrates an encoderdecoder network with attention, focusing on the computation of one context vector ci. Encoder Decoder hd i-1 he he he hd i hidden layer(s) x1 x2 yi-1 x3 xn yi-2 yi-1 yi he n ci weights ci-1 ci X j ↵ijhe j ↵ij hd i−1 · he j … … … Figure 13.22 A sketch of the encoder-decoder network with attention, focusing on the computation of ci. The context value ci is one of the inputs to the computation of hd i . It is computed by taking the weighted sum of all the encoder hidden states, each weighted by their dot product with the prior decoder hidden state hd i−1. It’s also possible to create more sophisticated scoring functions for attention models. Instead of simple dot product attention, we can get a more powerful function that computes the relevance of each encoder hidden state to the decoder hidden state by parameterizing the score with its own set of weights, Ws. score(hd i−1,he j) = hd i−1Wshe j (13.38) The weights Ws, which are then trained during normal end-to-end training, give the network the ability to learn which aspects of similarity between the decoder and encoder states are important to the current application.

## Key terms
- **encoder** — 7 mentions
- **state** — 7 mentions
- **decoder** — 7 mentions
- **attention** — 7 mentions
- **hidden** — 7 mentions
- **network** — 5 mentions
- **context** — 3 mentions
- **vector** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=315|Speech and Language Processing.pdf p. 315]]

## Liens
- Up: [[research/slp/rnns-and-lstms]]
- ← Prev: [[research/slp/attention-2]]
- Next: [[research/slp/historical-notes-12]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
