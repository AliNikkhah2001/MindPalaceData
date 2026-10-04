---
title: "Stacked and Bidirectional RNN architectures"
summary: "§I Large Language Models › RNNs and LSTMs › Stacked and Bidir: CHAPTER 13 • RNNS AND LSTMS This simple architecture underlies state-of-the-art approaches to applications such as machine translation, summarization, and question answering."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "302-303"
---

# Stacked and Bidirectional RNN architectures

§I Large Language Models › RNNs and LSTMs › Stacked and Bidirectional RNN architectures · pp. 302–303 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 13 • RNNS AND LSTMS This simple architecture underlies state-of-the-art approaches to applications such as machine translation, summarization, and question answering. The key to these approaches is to prime the generation component with an appropriate context. That is, instead of simply using <s> to get things started we can provide a richer task-appropriate context; for translation the context is the sentence in the source language; for summarization it’s the long text we want to summarize. So long <s> and So long and ? Sampled Word Embedding Input Word RNN Figure 13.9 Autoregressive generation with an RNN-based neural language model. Recurrent networks are quite flexible. By combining the feedforward nature of unrolled computational graphs with vectors as common inputs and outputs, complex networks can be treated as modules that can be combined in creative ways. This section introduces two of the more common network architectures used in language processing with RNNs. In our examples thus far, the inputs to our RNNs have consisted of sequences of word or character embeddings (vectors) and the outputs have been vectors useful for predicting words, tags or sequence labels. However, nothing prevents us from using the entire sequence of outputs from one RNN as an input sequence to another one.

## Key terms
- **input** — 13 mentions
- **network** — 13 mentions
- **sequence** — 11 mentions
- **rnns** — 10 mentions
- **context** — 8 mentions
- **stacked** — 7 mentions
- **output** — 7 mentions
- **time** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=302|Speech and Language Processing.pdf p. 302]]

## Liens
- Up: [[research/slp/rnns-and-lstms]]
- ← Prev: [[research/slp/rnns-for-other-nlp-tasks]]
- Next: [[research/slp/the-lstm]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
