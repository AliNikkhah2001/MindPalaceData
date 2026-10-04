---
title: "Word2vec"
summary: "§I Large Language Models › Embeddings › Word2vec: 5.5 • WORD2VEC digital cherry information Dimension 1: ‘pie’ Dimension 2: ‘computer’ Figure 5.5 A (rough) graphical demonstration of cosine similarity, showing vectors for three words (cherry, digital, and information) in the two "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "113-118"
---

# Word2vec

§I Large Language Models › Embeddings › Word2vec · pp. 113–118 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
5.5 • WORD2VEC digital cherry information Dimension 1: ‘pie’ Dimension 2: ‘computer’ Figure 5.5 A (rough) graphical demonstration of cosine similarity, showing vectors for three words (cherry, digital, and information) in the two dimensional space defined by counts of the words computer and pie nearby. The figure doesn’t show the cosine, but it highlights the angles; note that the angle between digital and information is smaller than the angle between cherry and information. When two vectors are more similar, the cosine is larger but the angle is smaller; the cosine has its maximum (1) when the angle between two vectors is smallest (0◦); the cosine of all other angles is less than 1. Cosine similarity can be used to estimate word similarity, for tasks like finding word paraphrases, tracking changes in word meaning, or automatically discovering meanings of words in different corpora. For example, we can fine the 10 most similar words to any target word w by computing the cosines between w and each of the |V|−1 other words, sorting, and looking at the top 10. In the previous sections we saw how to represent a word as a sparse, long vector with dimensions corresponding to words in the vocabulary.

## Key terms
- **word** — 77 mentions
- **embedding** — 36 mentions
- **apricot** — 24 mentions
- **context** — 23 mentions
- **target** — 20 mentions
- **vector** — 20 mentions
- **probability** — 18 mentions
- **word2vec** — 12 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=113|Speech and Language Processing.pdf p. 113]]

## Liens
- Up: [[research/slp/embeddings]]
- ← Prev: [[research/slp/cosine-for-measuring-similarity]]
- Next: [[research/slp/visualizing-embeddings]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
