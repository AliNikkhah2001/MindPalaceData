---
title: "Contextual Embeddings and Word Sense"
summary: "§I Large Language Models › Masked Language Models › Contextua: 9.3 • CONTEXTUAL EMBEDDINGS Given a pretrained language model and a novel input sentence, we can think of the sequence of model outputs as constituting contextual embeddings for each token in contextual embeddings the"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "215-216"
---

# Contextual Embeddings and Word Sense

§I Large Language Models › Masked Language Models › Contextual Embeddings › Contextual Embeddings and Word Sense · pp. 215–216 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
9.3 • CONTEXTUAL EMBEDDINGS Given a pretrained language model and a novel input sentence, we can think of the sequence of model outputs as constituting contextual embeddings for each token in contextual embeddings the input. These contextual embeddings are vectors representing some aspect of the meaning of a token in context, and can be used for any task requiring the meaning of tokens or words. More formally, given a sequence of input tokens x1,...,xn, we can use the output vector hLi from the final layer L of the model as a representation of the meaning of token xi in the context of sentence x1,...,xn. Or instead of just using the vector hLi from the final layer of the model, it’s common to compute a representation for xi by averaging the output tokens hi from each of the last four layers of the model, i.e., hLi, hL−1i, hL−2i, and hL−3i. [CLS] So long and thanks for all hL hL CLS hL hL hL hL hL E i + E i + E i + E i + E i + E i + E i + Figure 9.5 The output of a BERT-style model is a contextual embedding vector hL i for each input token xi. Just as we used static embeddings like word2vec in Chapter 5 to represent the meaning of words, we can use contextual embeddings as representations of word meanings in context for any task that might require a model of word meaning.

## Key terms
- **word** — 32 mentions
- **sense** — 23 mentions
- **embedding** — 15 mentions
- **meaning** — 13 mentions
- **contextual** — 12 mentions
- **model** — 10 mentions
- **context** — 10 mentions
- **token** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=215|Speech and Language Processing.pdf p. 215]]

## Liens
- Up: [[research/slp/contextual-embeddings]]
- Next: [[research/slp/contextual-embeddings-and-word-similarity]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
