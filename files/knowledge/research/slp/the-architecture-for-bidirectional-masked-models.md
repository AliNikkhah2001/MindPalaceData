---
title: "The architecture for bidirectional masked models"
summary: "§I Large Language Models › Masked Language Models › Bidirecti: CHAPTER 9 • MASKED LANGUAGE MODELS cially true for sequence labeling tasks in which we want to tag each token with a label, such as the named entity tagging task we’ll introduce in Section 9.5, or tasks like part-of-s"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "208-209"
---

# The architecture for bidirectional masked models

§I Large Language Models › Masked Language Models › Bidirectional Transformer Encoders › The architecture for bidirectional masked models · pp. 208–209 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 9 • MASKED LANGUAGE MODELS cially true for sequence labeling tasks in which we want to tag each token with a label, such as the named entity tagging task we’ll introduce in Section 9.5, or tasks like part-of-speech tagging or parsing that come up in later chapters. The bidirectional encoders that we introduce here are a different kind of beast than causal models. The causal models of Chapter 8 are generative models, designed to easily generate the next token in a sequence. But the focus of bidirectional encoders is instead on computing contextualized representations of the input tokens. Bidirectional encoders use self-attention to map sequences of input embeddings (x1,...,xn) to sequences of output embeddings of the same length (h1,...,hn), where the output vectors have been contextualized using information from the entire input sequence. These output embeddings are contextualized representations of each input token that are useful across a range of applications where we need to do a classification or a decision based on the token in context. Remember that we said the models of Chapter 8 are sometimes called decoderonly, because they correspond to the decoder part of the encoder-decoder model we will introduce in Chapter 12.

## Key terms
- **attention** — 26 mentions
- **token** — 22 mentions
- **model** — 16 mentions
- **bidirectional** — 12 mentions
- **input** — 12 mentions
- **causal** — 7 mentions
- **transformer** — 7 mentions
- **information** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=208|Speech and Language Processing.pdf p. 208]]

## Liens
- Up: [[research/slp/bidirectional-transformer-encoders]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
