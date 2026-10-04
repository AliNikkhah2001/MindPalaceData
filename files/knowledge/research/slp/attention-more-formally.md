---
title: "Attention more formally"
summary: "§I Large Language Models › Transformers › Attention › Attenti: CHAPTER 8 • TRANSFORMERS The point of all these examples is that these contextual words that help us compute the meaning of words in context can be quite far away in the sentence or paragraph."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "184-187"
---

# Attention more formally

§I Large Language Models › Transformers › Attention › Attention more formally · pp. 184–187 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 8 • TRANSFORMERS The point of all these examples is that these contextual words that help us compute the meaning of words in context can be quite far away in the sentence or paragraph. Transformers can build contextual representations of word meaning, contextual embeddings, by integrating the meaning of these helpful contextual words. In a contextual embeddings transformer, layer by layer, we build up richer and richer contextualized representations of the meanings of input tokens. At each layer, we compute the representation of a token i by combining information about i from the previous layer with information about the neighboring tokens to produce a contextualized representation for each word at each position. Attention is the mechanism in the transformer that weighs and combines the representations from appropriate other tokens in the context from layer k to build the representation for tokens in layer k +1. The chicken didn’t cross the road because it was too tired The chicken didn’t cross the road because it was too tired Layer k+1 Layer k self-attention distribution columns corresponding to input tokens Figure 8.3 The self-attention weight distribution α that is part of the computation of the representation for the word it at layer k +1.

## Key terms
- **attention** — 38 mentions
- **token** — 23 mentions
- **vector** — 22 mentions
- **value** — 21 mentions
- **layer** — 20 mentions
- **input** — 20 mentions
- **representation** — 20 mentions
- **transformer** — 18 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=184|Speech and Language Processing.pdf p. 184]]

## Liens
- Up: [[research/slp/attention]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
