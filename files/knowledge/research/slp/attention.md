---
title: "Attention"
summary: "§I Large Language Models › Transformers › Attention: CHAPTER 8 • TRANSFORMERS Transformers also have a special mechanism for encoding the position/index of the token in the input string, which is simply added to the embedding."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "182-187"
---

# Attention

§I Large Language Models › Transformers › Attention · pp. 182–187 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 8 • TRANSFORMERS Transformers also have a special mechanism for encoding the position/index of the token in the input string, which is simply added to the embedding. The resulting embedding represents both the word and its position. and is then passed through a set of N transformer blocks. It’s common to think of each of these transformer blocks as part of a stream in which the input embedding is directly passed up to the output, while simultaneously being enriched by the application of various processing modules: the multi-head attention layer, feedforward networks and the layer normalization. The value of the stream at any layer is the sum of the original embedding and all the outputs from all the previous layers and blocks. The core intuition of the transformer, and the component that distinguishes it from the feedforward layers we saw in Chapter 6, is this multi-head attention layer, also called a self-attention layer. Attention can be thought of as a way to build contextual representations of a token’s meaning by attending to and integrating information from surrounding tokens, helping the model learn how tokens relate to each other over large spans. It can also be thought of as a way to move information from one residual stream to another, augmenting the stream at one token position with information from another token position.

## Key terms
- **token** — 39 mentions
- **attention** — 27 mentions
- **transformer** — 24 mentions
- **layer** — 24 mentions
- **representation** — 24 mentions
- **word** — 23 mentions
- **input** — 17 mentions
- **chicken** — 16 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=182|Speech and Language Processing.pdf p. 182]]

## Liens
- Up: [[research/slp/transformers]]
- Next: [[research/slp/transformer-blocks]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
