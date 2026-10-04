---
title: "Semantic properties of embeddings"
summary: "§I Large Language Models › Embeddings › Semantic properties o: CHAPTER 5 • EMBEDDINGS Probably the most common visualization method, however, is to project the 100 dimensions of a word down into 2 dimensions."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "120-121"
---

# Semantic properties of embeddings

§I Large Language Models › Embeddings › Semantic properties of embeddings · pp. 120–121 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 5 • EMBEDDINGS Probably the most common visualization method, however, is to project the 100 dimensions of a word down into 2 dimensions. Fig. 5.1 showed one such visualization, as does Fig. 5.9, using a projection method called t-SNE (van der Maaten and Hinton, 2008). In this section we briefly summarize some of the semantic properties of embeddings that have been studied. Different types of similarity or association: One parameter of vector semantic models that is relevant to both sparse PPMI vectors and dense word2vec vectors is the size of the context window used to collect counts. This is generally between 1 and 10 words on each side of the target word (for a total context of 2-20 words). The choice depends on the goals of the representation. Shorter context windows tend to lead to representations that are a bit more syntactic, since the information is coming from immediately nearby words. When the vectors are computed from short context windows, the most similar words to a target word w tend to be semantically similar words with the same parts of speech. When vectors are computed from long context windows, the highest cosine words to a target word w tend to be words that are topically related but not similar.

## Key terms
- **word** — 25 mentions
- **vector** — 15 mentions
- **model** — 9 mentions
- **parallelogram** — 9 mentions
- **embedding** — 9 mentions
- **method** — 6 mentions
- **window** — 6 mentions
- **similar** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=120|Speech and Language Processing.pdf p. 120]]

## Liens
- Up: [[research/slp/embeddings]]
- ← Prev: [[research/slp/visualizing-embeddings]]
- Next: [[research/slp/bias-and-embeddings]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
