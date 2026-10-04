---
title: "Smoothing, Interpolation, and Backoff"
summary: "§I Large Language Models › N-gram Language Models › Smoothing: 3.6 • SMOOTHING, INTERPOLATION, AND BACKOFF (3.22) Bored af den my phone finna die!!! while tweets from English-based languages like Nigerian Pidgin have markedly different vocabulary and n-gram patterns from American"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "59-62"
---

# Smoothing, Interpolation, and Backoff

§I Large Language Models › N-gram Language Models › Smoothing, Interpolation, and Backoff · pp. 59–62 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
3.6 • SMOOTHING, INTERPOLATION, AND BACKOFF (3.22) Bored af den my phone finna die!!! while tweets from English-based languages like Nigerian Pidgin have markedly different vocabulary and n-gram patterns from American English (Jurgens et al., 2017): (3.23) @username R u a wizard or wat gan sef: in d mornin - u tweet, afternoon - u tweet, nyt gan u dey tweet. beta get ur IT placement wiv twitter Is it possible for the testset nonetheless to have a word we have never seen before? What happens if the word Jurafsky never occurs in our training set, but pops up in the test set? The answer is that although words might be unseen, we normally run our NLP algorithms not on words but on subword tokens. With subword tokenization (like the BPE algorithm of Chapter 2) any word can be modeled as a sequence of known smaller subwords, if necessary by a sequence of tokens corresponding to individual letters. So although for convenience we’ve been referring to words in this chapter, the language model vocabulary is normally the set of tokens rather than words, and in this way the test set can never contain unseen tokens. There is a problem with using maximum likelihood estimates for probabilities: any finite training corpus will be missing some perfectly acceptable English word sequences.

## Key terms
- **count** — 36 mentions
- **word** — 22 mentions
- **smoothing** — 21 mentions
- **probability** — 19 mentions
- **bigram** — 15 mentions
- **n-gram** — 13 mentions
- **interpolation** — 12 mentions
- **algorithm** — 11 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=59|Speech and Language Processing.pdf p. 59]]

## Liens
- Up: [[research/slp/n-gram-language-models]]
- ← Prev: [[research/slp/generalizing-vs-overfitting-the-training-set]]
- Next: [[research/slp/advanced-perplexity-s-relation-to-entropy]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
