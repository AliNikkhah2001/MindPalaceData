---
title: "Tokenization"
summary: "§I Large Language Models › Machine Translation › Machine Tran: CHAPTER 12 • MACHINE TRANSLATION Lleg´o la bruja verde MT uses supervised machine learning: at training time the system is given a large set of parallel sentences (each sentence in a source language matched with a sen"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "272-272"
---

# Tokenization

§I Large Language Models › Machine Translation › Machine Translation using Encoder-Decoder › Tokenization · pp. 272–272 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 12 • MACHINE TRANSLATION Lleg´o la bruja verde MT uses supervised machine learning: at training time the system is given a large set of parallel sentences (each sentence in a source language matched with a sentence in the target language), and learns to map source sentences into target sentences. In practice, rather than using words (as in the example above), we split the sentences into a sequence of subword tokens (tokens can be words, or subwords, or individual characters). The systems are then trained to maximize the probability of the sequence of tokens in the target language y1,...,ym given the sequence of tokens in the source language x1,...,xn: P(y1,...,ym|x1,...,xn) (12.7) Rather than use the input tokens directly, the encoder-decoder architecture consists of two components, an encoder and a decoder. The encoder takes the input words x = [x1,...,xn] and produces an intermediate context h. At decoding time, the system takes h and, word by word, generates the output y: h = encoder(x) (12.8) yt+1 = decoder(h,y1,...,yt) ∀t ∈[1,...,m] (12.9) In the next two sections we’ll talk about subword tokenization, then how to get parallel corpora for training, and then we’ll introduce the details of the encoderdecoder architecture.

## Key terms
- **language** — 10 mentions
- **token** — 10 mentions
- **word** — 8 mentions
- **system** — 7 mentions
- **tokenization** — 7 mentions
- **algorithm** — 7 mentions
- **sentence** — 6 mentions
- **source** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=272|Speech and Language Processing.pdf p. 272]]

## Liens
- Up: [[research/slp/machine-translation-using-encoder-decoder]]
- Next: [[research/slp/creating-the-training-data]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
