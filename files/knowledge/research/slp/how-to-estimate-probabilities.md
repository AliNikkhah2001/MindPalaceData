---
title: "How to estimate probabilities"
summary: "§I Large Language Models › N-gram Language Models › N-Grams ›: 3.1 • N-GRAMS size, so N = 2 means bigrams and N = 3 means trigrams. Then we approximate the probability of a word given its entire context as follows: P(wn|w1:n−1) ≈P(wn|wn−N+1:n−1) (3.8) Given the bigram assumption "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "49-50"
---

# How to estimate probabilities

§I Large Language Models › N-gram Language Models › N-Grams › How to estimate probabilities · pp. 49–50 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
3.1 • N-GRAMS size, so N = 2 means bigrams and N = 3 means trigrams. Then we approximate the probability of a word given its entire context as follows: P(wn|w1:n−1) ≈P(wn|wn−N+1:n−1) (3.8) Given the bigram assumption for the probability of an individual word, we can compute the probability of a complete word sequence by substituting Eq. 3.7 into Eq. 3.4: P(w1:n) ≈ n Y k=1 P(wk|wk−1) (3.9) How do we estimate these bigram or n-gram probabilities? An intuitive way to estimate probabilities is called maximum likelihood estimation or MLE. We get maximum likelihood estimation the MLE estimate for the parameters of an n-gram model by getting counts from a corpus, and normalizing the counts so that they lie between 0 and 1. For probanormalize bilistic models, normalizing means dividing by some total count so that the resulting probabilities fall between 0 and 1 and sum to 1. For example, to compute a particular bigram probability of a word wn given a previous word wn−1, we’ll compute the count of the bigram C(wn−1wn) and normalize by the sum of all the bigrams that share the same first word wn−1: P(wn|wn−1) = C(wn−1wn) P wC(wn−1w) (3.10) We can simplify this equation, since the sum of all …

## Key terms
- **word** — 20 mentions
- **bigram** — 14 mentions
- **probability** — 12 mentions
- **count** — 11 mentions
- **sentence** — 11 mentions
- **estimate** — 8 mentions
- **probabilities** — 8 mentions
- **corpus** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=49|Speech and Language Processing.pdf p. 49]]

## Liens
- Up: [[research/slp/n-grams]]
- ← Prev: [[research/slp/the-markov-assumption]]
- Next: [[research/slp/dealing-with-scale-in-large-n-gram-models]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
