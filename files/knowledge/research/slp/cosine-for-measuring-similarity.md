---
title: "Cosine for measuring similarity"
summary: "§I Large Language Models › Embeddings › Cosine for measuring : 5.4 • COSINE FOR MEASURING SIMILARITY aardvark ... The vector for digital is outlined in red. Note that a real vector would have vastly more dimensions and thus be much sparser, i.e."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "111-112"
---

# Cosine for measuring similarity

§I Large Language Models › Embeddings › Cosine for measuring similarity · pp. 111–112 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
5.4 • COSINE FOR MEASURING SIMILARITY aardvark ... computer data result pie sugar ... cherry ... ... strawberry ... ... digital ... ... information ... ... Figure 5.3 Co-occurrence vectors for four words in the Wikipedia corpus, showing six of the dimensions (hand-picked for pedagogical purposes). The vector for digital is outlined in red. Note that a real vector would have vastly more dimensions and thus be much sparser, i.e. would have zero values in most dimensions. 1000 2000 3000 4000 digital [1683,1670] computer data information [3982,3325] Figure 5.4 A spatial visualization of word vectors for digital and information, showing just two of the dimensions, corresponding to the words data and computer. Note that |V|, the dimensionality of the vector, is generally the size of the vocabulary, often between 10,000 and 50,000 words (using the most frequent words in the training corpus; keeping words after about the most frequent 50,000 or so is generally not helpful). Since most of these numbers are zero these are sparse vector representations; there are efficient algorithms for storing and computing with sparse matrices. It’s also possible to apply various kinds of weighting functions to the counts in these cells.

## Key terms
- **vector** — 30 mentions
- **product** — 15 mentions
- **word** — 14 mentions
- **cosine** — 10 mentions
- **similarity** — 10 mentions
- **digital** — 8 mentions
- **information** — 8 mentions
- **length** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=111|Speech and Language Processing.pdf p. 111]]

## Liens
- Up: [[research/slp/embeddings]]
- ← Prev: [[research/slp/simple-count-based-embeddings]]
- Next: [[research/slp/word2vec]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
