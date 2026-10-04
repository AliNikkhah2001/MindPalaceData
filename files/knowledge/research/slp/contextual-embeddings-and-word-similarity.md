---
title: "Contextual Embeddings and Word Similarity"
summary: "§I Large Language Models › Masked Language Models › Contextua: 9.3 • CONTEXTUAL EMBEDDINGS an electric guitar and bass player stand off to one side electric1: using electricity electric2: tense electric3: thrilling guitar1 bass1: low range … bass4: sea fish … bass7: instrument … "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "217-218"
---

# Contextual Embeddings and Word Similarity

§I Large Language Models › Masked Language Models › Contextual Embeddings › Contextual Embeddings and Word Similarity · pp. 217–218 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
9.3 • CONTEXTUAL EMBEDDINGS an electric guitar and bass player stand off to one side electric1: using electricity electric2: tense electric3: thrilling guitar1 bass1: low range … bass4: sea fish … bass7: instrument … player1: in game player2: musician player3: actor … stand1: upright … stand5: bear … stand10: put upright … side1: relative region … side3: of body … side11: slope … x1 y1 x2 y2 x3 y3 y4 y5 y6 x4 x5 x6 Figure 9.7 The all-words WSD task, mapping from input words (x) to WordNet senses (y). Figure inspired by Chaplot and Salakhutdinov (2018). WSD can be a useful analytic tool for text analysis in the humanities and social sciences, and word senses can play a role in model interpretability for word representations. Word senses also have interesting distributional properties. For example a word often is used in roughly the same sense through a discourse, an observation called the one sense per discourse rule (Gale et al., 1992a). one sense per discourse The best performing WSD algorithm is a simple 1-nearest-neighbor algorithm using contextual word embeddings, due to Melamud et al. (2016) and Peters et al. (2018). At training time we pass each sentence in some sense-labeled dataset (like the SemCore or SenseEval datasets in various languages) through any contextual embedding (e.g., BERT) resulting in a contextual embedding for each labeled token.

## Key terms
- **word** — 21 mentions
- **sense** — 19 mentions
- **embedding** — 19 mentions
- **contextual** — 13 mentions
- **cosine** — 9 mentions
- **vector** — 8 mentions
- **model** — 7 mentions
- **token** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=217|Speech and Language Processing.pdf p. 217]]

## Liens
- Up: [[research/slp/contextual-embeddings]]
- ← Prev: [[research/slp/contextual-embeddings-and-word-sense]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
