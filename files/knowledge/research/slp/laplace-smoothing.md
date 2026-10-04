---
title: "Laplace Smoothing"
summary: "§I Large Language Models › N-gram Language Models › Smoothing: 3.6 • SMOOTHING, INTERPOLATION, AND BACKOFF (3.22) Bored af den my phone finna die!!! while tweets from English-based languages like Nigerian Pidgin have markedly different vocabulary and n-gram patterns from American"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "59-60"
---

# Laplace Smoothing

§I Large Language Models › N-gram Language Models › Smoothing, Interpolation, and Backoff › Laplace Smoothing · pp. 59–60 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
3.6 • SMOOTHING, INTERPOLATION, AND BACKOFF (3.22) Bored af den my phone finna die!!! while tweets from English-based languages like Nigerian Pidgin have markedly different vocabulary and n-gram patterns from American English (Jurgens et al., 2017): (3.23) @username R u a wizard or wat gan sef: in d mornin - u tweet, afternoon - u tweet, nyt gan u dey tweet. beta get ur IT placement wiv twitter Is it possible for the testset nonetheless to have a word we have never seen before? What happens if the word Jurafsky never occurs in our training set, but pops up in the test set? The answer is that although words might be unseen, we normally run our NLP algorithms not on words but on subword tokens. With subword tokenization (like the BPE algorithm of Chapter 2) any word can be modeled as a sequence of known smaller subwords, if necessary by a sequence of tokens corresponding to individual letters. So although for convenience we’ve been referring to words in this chapter, the language model vocabulary is normally the set of tokens rather than words, and in this way the test set can never contain unseen tokens. There is a problem with using maximum likelihood estimates for probabilities: any finite training corpus will be missing some perfectly acceptable English word sequences.

## Key terms
- **count** — 22 mentions
- **word** — 17 mentions
- **smoothing** — 16 mentions
- **probability** — 11 mentions
- **algorithm** — 8 mentions
- **bigram** — 8 mentions
- **n-gram** — 7 mentions
- **test** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=59|Speech and Language Processing.pdf p. 59]]

## Liens
- Up: [[research/slp/smoothing-interpolation-and-backoff]]
- Next: [[research/slp/add-k-smoothing]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
