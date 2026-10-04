---
title: "Evaluating Language Models: Perplexity"
summary: "§I Large Language Models › N-gram Language Models › Evaluatin: CHAPTER 3 • N-GRAM LANGUAGE MODELS to measure a statistically significant difference between two potential models. It’s important that the devset be drawn from the same kind of text as the test set, since its goal is "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "54-55"
---

# Evaluating Language Models: Perplexity

§I Large Language Models › N-gram Language Models › Evaluating Language Models: Perplexity · pp. 54–55 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 3 • N-GRAM LANGUAGE MODELS to measure a statistically significant difference between two potential models. It’s important that the devset be drawn from the same kind of text as the test set, since its goal is to measure how we would do on the test set. We said above that we evaluate language models based on which one assigns a higher probability to the test set. A better model is better at predicting upcoming words, and so it will be less surprised by (i.e., assign a higher probability to) each word when it occurs in the test set. Indeed, a perfect language model would correctly guess each next word in a corpus, assigning it a probability of 1, and all the other words a probability of zero. So given a test corpus, a better language model will assign a higher probability to it than a worse language model. But in fact, we often do not use raw probability as our metric for evaluating language models. The reason is that the probability of a test set (or any sequence) depends on the number of words or tokens in it; the probability of a test set gets smaller the longer the text. It’s useful to have a metric that is per-word, normalized by length, so we could compare across texts of different lengths.

## Key terms
- **perplexity** — 33 mentions
- **model** — 31 mentions
- **language** — 23 mentions
- **probability** — 23 mentions
- **test** — 19 mentions
- **word** — 17 mentions
- **token** — 8 mentions
- **higher** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=54|Speech and Language Processing.pdf p. 54]]

## Liens
- Up: [[research/slp/n-gram-language-models]]
- ← Prev: [[research/slp/evaluating-language-models-training-and-test-sets]]
- Next: [[research/slp/sampling-sentences-from-a-language-model]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
