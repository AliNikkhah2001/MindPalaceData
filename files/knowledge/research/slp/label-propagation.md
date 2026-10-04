---
title: "Label Propagation"
summary: "§II Annotating Linguistic Structure › Lexicons for Sentiment,: CHAPTER 22 • LEXICONS FOR SENTIMENT, AFFECT, AND CONNOTATION on a specific corpus (for example using a financial corpus if a finance lexicon is the goal), or we can finetune off-the-shelf embeddings to a corpus."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "516-516"
---

# Label Propagation

§II Annotating Linguistic Structure › Lexicons for Sentiment, Affect, and Connotation › Semi-supervised Induction of Affect Lexicons › Label Propagation · pp. 516–516 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 22 • LEXICONS FOR SENTIMENT, AFFECT, AND CONNOTATION on a specific corpus (for example using a financial corpus if a finance lexicon is the goal), or we can finetune off-the-shelf embeddings to a corpus. Fine-tuning is especially important if we have a very specific genre of text but don’t have enough data to train good embeddings. In finetuning, we begin with off-the-shelf embeddings like word2vec, and continue training them on the small target corpus. Once we have embeddings for each pole word, we create an embedding that represents each pole by taking the centroid of the embeddings of each of the seed words; recall that the centroid is the multidimensional version of the mean. Given a set of embeddings for the positive seed words S+ = {E(w+ 1 ),E(w+ 2 ),...,E(w+ n )}, and embeddings for the negative seed words S−= {E(w− 1 ),E(w− 2 ),...,E(w− m)}, the pole centroids are: V+ = 1 n n X E(w+ i ) V−= 1 m m X E(w− i ) (22.1) The semantic axis defined by the poles is computed just by subtracting the two vectors: Vaxis = V+ −V− (22.2) Vaxis, the semantic axis, is a vector in the direction of positive sentiment. Finally, we compute (via cosine similarity) the angle between the vector in the direction of positive sentiment and the direction of w’s embedding.

## Key terms
- **word** — 10 mentions
- **embedding** — 10 mentions
- **seed** — 7 mentions
- **sentiment** — 6 mentions
- **lexicon** — 5 mentions
- **positive** — 5 mentions
- **vaxis** — 5 mentions
- **corpus** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=516|Speech and Language Processing.pdf p. 516]]

## Liens
- Up: [[research/slp/semi-supervised-induction-of-affect-lexicons]]
- ← Prev: [[research/slp/semantic-axis-methods]]
- Next: [[research/slp/other-methods]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
