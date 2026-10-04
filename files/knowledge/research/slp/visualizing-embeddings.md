---
title: "Visualizing Embeddings"
summary: "§I Large Language Models › Embeddings › Visualizing Embedding: 5.6 • VISUALIZING EMBEDDINGS There are many kinds of static embeddings. An extension of word2vec, fasttext fasttext (Bojanowski et al., 2017), addresses a problem with word2vec as we have presented it so far: it has n"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "119-119"
---

# Visualizing Embeddings

§I Large Language Models › Embeddings › Visualizing Embeddings · pp. 119–119 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
5.6 • VISUALIZING EMBEDDINGS There are many kinds of static embeddings. An extension of word2vec, fasttext fasttext (Bojanowski et al., 2017), addresses a problem with word2vec as we have presented it so far: it has no good way to deal with unknown words-words that appear in a test corpus but were unseen in the training corpus. A related problem is word sparsity, such as in languages with rich morphology, where some of the many forms for each noun and verb may only occur rarely. Fasttext deals with these problems by using subword models, representing each word as itself plus a bag of constituent n-grams, with special boundary symbols < and > added to each word. For example, with n = 3 the word where would be represented by the sequence <where> plus the character n-grams: <wh, whe, her, ere, re> Then a skipgram embedding is learned for each constituent n-gram, and the word where is represented by the sum of all of the embeddings of its constituent n-grams. Unknown words can then be presented only by the sum of the constituent n-grams. A fasttext open-source library, including pretrained embeddings for 157 languages, is available at https://fasttext.cc. Another very widely used static embedding model is GloVe (Pennington et al., 2014), short for Global Vectors, because the model is based on capturing global corpus statistics.

## Key terms
- **word** — 12 mentions
- **embedding** — 12 mentions
- **fasttext** — 5 mentions
- **n-gram** — 5 mentions
- **vector** — 5 mentions
- **word2vec** — 4 mentions
- **constituent** — 4 mentions
- **model** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=119|Speech and Language Processing.pdf p. 119]]

## Liens
- Up: [[research/slp/embeddings]]
- ← Prev: [[research/slp/word2vec]]
- Next: [[research/slp/semantic-properties-of-embeddings]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
