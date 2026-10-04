---
title: "Summary: Common RNN NLP Architectures"
summary: "§I Large Language Models › RNNs and LSTMs › Summary: Common R: CHAPTER 13 • RNNS AND LSTMS networks making use of gated units can be unrolled into deep feedforward networks and trained in the usual fashion with backpropagation."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "308-308"
---

# Summary: Common RNN NLP Architectures

§I Large Language Models › RNNs and LSTMs › Summary: Common RNN NLP Architectures · pp. 308–308 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 13 • RNNS AND LSTMS networks making use of gated units can be unrolled into deep feedforward networks and trained in the usual fashion with backpropagation. In practice, therefore, LSTMs rather than RNNs have become the standard unit for any modern system that makes use of recurrent networks. We’ve now introduced the RNN, seen advanced components like stacking multiple layers and using the LSTM version, and seen how the RNN can be applied to various tasks. Let’s take a moment to summarize the architectures for these applications. Fig. 13.15 shows the three architectures we’ve discussed so far: sequence labeling, sequence classification, and language modeling. In sequence labeling (for example for part of speech tagging), we train a model to produce a label for each input word or token. In sequence classification, for example for sentiment analysis, we ignore the output for each token, and only take the value from the end of the sequence (and similarly the model’s training signal comes from backpropagation from that last token). In language modeling, we train the model to predict the next word at each token step. In the next section we’ll introduce a fourth architecture, the encoder-decoder.

## Key terms
- **sequence** — 12 mentions
- **token** — 8 mentions
- **model** — 5 mentions
- **labeling** — 4 mentions
- **classification** — 4 mentions
- **language** — 4 mentions
- **modeling** — 4 mentions
- **input** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=308|Speech and Language Processing.pdf p. 308]]

## Liens
- Up: [[research/slp/rnns-and-lstms]]
- ← Prev: [[research/slp/the-lstm]]
- Next: [[research/slp/the-encoder-decoder-model-with-rnns]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
