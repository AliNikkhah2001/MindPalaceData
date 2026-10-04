---
title: "Simple count-based embeddings"
summary: "§I Large Language Models › Embeddings › Simple count-based em: 5.3 • SIMPLE COUNT-BASED EMBEDDINGS 200-dimensional space into a 2-dimensional space. Note that the nearest neighbors of sweet are semantically related words like honey, candy, juice, chocolate."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "109-110"
---

# Simple count-based embeddings

§I Large Language Models › Embeddings › Simple count-based embeddings · pp. 109–110 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
5.3 • SIMPLE COUNT-BASED EMBEDDINGS 200-dimensional space into a 2-dimensional space. Note that the nearest neighbors of sweet are semantically related words like honey, candy, juice, chocolate. This idea that similar words are neighbors in high-dimensional space offers enormous power to language models and other NLP applications. For example the sentiment classifiers of Chapter 4 depend on the same words appearing in the training and test sets. But by representing words as embeddings, a classifier can assign sentiment as long as it sees some words with similar meanings. And as we’ll see, vector semantic models like the ones showed in Fig. 5.1 can be learned automatically from text without supervision. In this chapter we’ll begin with a simple pedagogical model of embeddings in which the meaning of a word is defined by a vector with the counts of nearby words. We introduce this model as a helpful way to understand the concept of vectors and what it means for a vector to be a representation of word meaning, but more sophisticated variants like the tf-idf model we will introduce in Chapter 11 are important methods you should understand. We will see that this method results in very long vectors that are sparse, i.e.

## Key terms
- **word** — 44 mentions
- **vector** — 32 mentions
- **space** — 12 mentions
- **context** — 12 mentions
- **dimension** — 12 mentions
- **matrix** — 9 mentions
- **count** — 9 mentions
- **dimensional** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=109|Speech and Language Processing.pdf p. 109]]

## Liens
- Up: [[research/slp/embeddings]]
- ← Prev: [[research/slp/vector-semantics-the-intuition]]
- Next: [[research/slp/cosine-for-measuring-similarity]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
