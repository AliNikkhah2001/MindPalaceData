---
title: "N-Grams"
summary: "§I Large Language Models › N-gram Language Models › N-Grams: An n-gram is a sequence of n words: a 2-gram (which we’ll call bigram) is a two-word sequence of words like The water, or water of, and a 3gram (a trigram) is a three-word sequence of words like The water of, or water o"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "47-51"
---

# N-Grams

§I Large Language Models › N-gram Language Models › N-Grams · pp. 47–51 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
3.1 • N-GRAMS language model. An n-gram is a sequence of n words: a 2-gram (which we’ll call bigram) is a two-word sequence of words like The water, or water of, and a 3gram (a trigram) is a three-word sequence of words like The water of, or water of Walden. But we also (in a bit of terminological ambiguity) use the word ‘ngram’ to mean a probabilistic model that can estimate the probability of a word given the n-1 previous words, and thereby also to assign probabilities to entire sequences. In later chapters we will introduce the much more powerful neural large language models, based on the transformer architecture of Chapter 8. But because n-grams have a remarkably simple and clear formalization, we use them to introduce some major concepts of large language modeling, including training and test sets, perplexity, sampling, and interpolation. Let’s begin with the task of computing P(w|h), the probability of a word w given some history h. Suppose the history h is “The water of Walden Pond is so beautifully ” and we want to know the probability that the next word is blue: P(blue|The water of Walden Pond is so beautifully) (3.1) One way to estimate this probability is directly from relative frequency counts: take a very large corpus, count the number of times we see The water of Walden Pond is so beautifully, and count the number of times this is followed by blue.

## Key terms
- **word** — 54 mentions
- **probability** — 35 mentions
- **bigram** — 19 mentions
- **count** — 17 mentions
- **model** — 15 mentions
- **n-gram** — 15 mentions
- **estimate** — 15 mentions
- **sequence** — 14 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=47|Speech and Language Processing.pdf p. 47]]

## Liens
- Up: [[research/slp/n-gram-language-models]]
- Next: [[research/slp/evaluating-language-models-training-and-test-sets]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
