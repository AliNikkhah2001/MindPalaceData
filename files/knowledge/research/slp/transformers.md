---
title: "Transformers"
summary: "§I Large Language Models › Transformers: CHAPTER Transformers “The true art of memory is the art of attention ” Samuel Johnson, Idler #74, September 1759 In this chapter we introduce the transformer, the standard architecture for building large language models."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "181-206"
---

# Transformers

§I Large Language Models › Transformers · pp. 181–206 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER Transformers “The true art of memory is the art of attention ” Samuel Johnson, Idler #74, September 1759 In this chapter we introduce the transformer, the standard architecture for building large language models. As we discussed in the prior chapter, transformer-based large language models have completely changed the field of speech and language processing. Indeed, every subsequent chapter in this textbook will make use of them. As with the previous chapter, we’ll focus for this chapter on the use of transformers to model left-to-right (sometimes called causal or autoregressive) language modeling, in which we are given a sequence of input tokens and predict output tokens one by one by conditioning on the prior context. Layer Norm + Layer Norm MultiHead Feedforward Positional Unembedding Embedding + residual stream N times output probabilities (over tokens) + input token Layer Norm + Layer Norm MultiHead Feedforward residual stream N times + Figure 8.1 A transformer decoder for language modeling, showing the residual stream for processing an input token. A single token is embedded and passed forward in the network, with the feedforward and attention components adding information.

## Key terms
- **token** — 44 mentions
- **transformer** — 30 mentions
- **layer** — 28 mentions
- **representation** — 22 mentions
- **word** — 19 mentions
- **language** — 17 mentions
- **chicken** — 16 mentions
- **attention** — 15 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=181|Speech and Language Processing.pdf p. 181]]

## Liens
- Up: [[research/slp/i-large-language-models]]
- ← Prev: [[research/slp/large-language-models]]
- Next: [[research/slp/masked-language-models]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
