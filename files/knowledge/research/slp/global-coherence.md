---
title: "Global Coherence"
summary: "§II Annotating Linguistic Structure › Discourse Coherence › G: CHAPTER 24 • DISCOURSE COHERENCE Figure 24.11 The architecture of the LCD model of document coherence, showing the computation of the score for a pair of sentences s and t."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "574-576"
---

# Global Coherence

§II Annotating Linguistic Structure › Discourse Coherence › Global Coherence · pp. 574–576 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 24 • DISCOURSE COHERENCE Figure 24.11 The architecture of the LCD model of document coherence, showing the computation of the score for a pair of sentences s and t. Figure from Xu et al. (2019). uniformly over the other sentences in the same document. L is a loss function that takes two scores, one for a positive pair and one for a negative pair, with the goal of encouraging f + = fθ(si,si+1) to be high and f −= fθ(si,s′)) to be low. Fig. 24.11 use the margin loss l(f +, f −) = max(0,η −f + + f −) where η is the margin hyperparameter. Xu et al. (2019) also give a useful baseline algorithm that itself has quite high performance in measuring perplexity: train an RNN language model on the data, and compute the log likelihood of sentence si in two ways, once given the preceding context (conditional log likelihood) and once with no context (marginal log likelihood). The difference between these values tells us how much the preceding context improved the predictability of si, a predictability measure of coherence. Training models to predict longer contexts than just consecutive pairs of sentences can result in even stronger discourse representations. For example a Transformer language model trained with a contrastive sentence objective to predict text up to a distance of ±2 sentences improves performance on various discourse coherence tasks (Iter et al., 2020).

## Key terms
- **structure** — 18 mentions
- **argument** — 17 mentions
- **discourse** — 11 mentions
- **coherence** — 11 mentions
- **model** — 11 mentions
- **argumentation** — 11 mentions
- **premise** — 10 mentions
- **relation** — 9 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=574|Speech and Language Processing.pdf p. 574]]

## Liens
- Up: [[research/slp/discourse-coherence]]
- ← Prev: [[research/slp/representation-learning-models-for-local-coherence]]
- Next: [[research/slp/summary-23]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
