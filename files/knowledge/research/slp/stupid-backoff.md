---
title: "Stupid Backoff"
summary: "§I Large Language Models › N-gram Language Models › Smoothing: CHAPTER 3 • N-GRAM LANGUAGE MODELS language modeling, generating counts with poor variances and often inappropriate discounts (Gale and Church, 1994)."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "62-62"
---

# Stupid Backoff

§I Large Language Models › N-gram Language Models › Smoothing, Interpolation, and Backoff › Stupid Backoff · pp. 62–62 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 3 • N-GRAM LANGUAGE MODELS language modeling, generating counts with poor variances and often inappropriate discounts (Gale and Church, 1994). There is an alternative source of knowledge we can draw on to solve the problem of zero frequency n-grams. If we are trying to compute P(wn|wn−2wn−1) but we have no examples of a particular trigram wn−2wn−1wn, we can instead estimate its probability by using the bigram probability P(wn|wn−1). Similarly, if we don’t have counts to compute P(wn|wn−1), we can look to the unigram P(wn). In other words, sometimes using less context can help us generalize more for contexts that the model hasn’t learned much about. The most common way to use this n-gram hierarchy is called interpolation: interpolation computing a new probability by interpolating (weighting and combining) the trigram, bigram, and unigram probabilities. In simple linear interpolation, we combine different order n-grams by linearly interpolating them. Thus, we estimate the trigram probability P(wn|wn−2wn−1) by mixing together the unigram, bigram, and trigram probabilities, each weighted by a λ: ˆP(wn|wn−2wn−1) = λ1P(wn) +λ2P(wn|wn−1) +λ3P(wn|wn−2wn−1) (3.29) The λs must sum to 1, making Eq.

## Key terms
- **interpolation** — 9 mentions
- **trigram** — 7 mentions
- **n-gram** — 6 mentions
- **held-out** — 6 mentions
- **counts** — 5 mentions
- **probability** — 5 mentions
- **bigram** — 5 mentions
- **context** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=62|Speech and Language Processing.pdf p. 62]]

## Liens
- Up: [[research/slp/smoothing-interpolation-and-backoff]]
- ← Prev: [[research/slp/language-model-interpolation]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
