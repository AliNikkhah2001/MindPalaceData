---
title: "Learning skip-gram embeddings"
summary: "§I Large Language Models › Embeddings › Word2vec › Learning s: CHAPTER 5 • EMBEDDINGS W C aardvark zebra zebra aardvark apricot apricot |V| |V|+1 2|V| 𝜽 = target words context & noise … … 1..d … … Figure 5.6 The embeddings learned by the skipgram model."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "116-118"
---

# Learning skip-gram embeddings

§I Large Language Models › Embeddings › Word2vec › Learning skip-gram embeddings · pp. 116–118 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 5 • EMBEDDINGS W C aardvark zebra zebra aardvark apricot apricot |V| |V|+1 2|V| 𝜽 = target words context & noise … … 1..d … … Figure 5.6 The embeddings learned by the skipgram model. The algorithm stores two embeddings for each word, the target embedding (sometimes called the input embedding) and the context embedding (sometimes called the output embedding). The parameter θ that the algorithm learns is thus a matrix of 2|V| vectors, each of dimension d, formed by concatenating two matrices, the target embeddings W and the context+noise embeddings C. The learning algorithm for skip-gram embeddings takes as input a corpus of text, and a chosen vocabulary size N. It begins by assigning a random embedding vector for each of the N vocabulary words, and then proceeds to iteratively shift the embedding of each word w to be more like the embeddings of words that occur nearby in texts, and less like the embeddings of words that don’t occur nearby. Let’s start by considering a single piece of training data: ... lemon, a [tablespoon of apricot jam, a] pinch ... c1 c2 w c3 c4 This example has a target word w (apricot), and 4 context words in the L = ±2 window, resulting in 4 positive t…

## Key terms
- **word** — 32 mentions
- **embedding** — 28 mentions
- **apricot** — 22 mentions
- **cpos** — 17 mentions
- **context** — 15 mentions
- **target** — 11 mentions
- **noise** — 10 mentions
- **negative** — 10 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=116|Speech and Language Processing.pdf p. 116]]

## Liens
- Up: [[research/slp/word2vec]]
- ← Prev: [[research/slp/the-classifier]]
- Next: [[research/slp/other-kinds-of-static-embeddings]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
