---
title: "Historical Notes"
summary: "§I Large Language Models › N-gram Language Models › Historica: CHAPTER 3 • N-GRAM LANGUAGE MODELS lower cross-entropy. (The cross-entropy can never be lower than the true entropy, so a model cannot err by underestimating the true entropy.) We are finally ready to see the relation"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "66-66"
---

# Historical Notes

§I Large Language Models › N-gram Language Models › Historical Notes · pp. 66–66 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 3 • N-GRAM LANGUAGE MODELS lower cross-entropy. (The cross-entropy can never be lower than the true entropy, so a model cannot err by underestimating the true entropy.) We are finally ready to see the relation between perplexity and cross-entropy as we saw it in Eq. 3.40. Cross-entropy is defined in the limit as the length of the observed word sequence goes to infinity. We approximate this cross-entropy by relying on a (sufficiently long) sequence of fixed length. This approximation to the cross-entropy of a model M = P(wi|wi−N+1:i−1) on a sequence of words W is H(W) = −1 N logP(w1w2 ...wN) (3.42) The perplexity of a model P on a sequence of words W is now formally defined as perplexity 2 raised to the power of this cross-entropy: Perplexity(W) = 2H(W) = P(w1w2 ...wN)−1 N = N s P(w1w2 ...wN) This chapter introduced language modeling via the n-gram model, a classic model that allows us to introduce many of the basic concepts in language modeling. • Language models offer a way to assign a probability to a sentence or other sequence of words or tokens, and to predict a word or token from preceding words or tokens. • N-grams are perhaps the simplest kind of language model. They are Markov models that estimate words from a fixed window of previous words.

## Key terms
- **model** — 15 mentions
- **n-gram** — 8 mentions
- **language** — 8 mentions
- **word** — 8 mentions
- **cross-entropy** — 7 mentions
- **perplexity** — 6 mentions
- **sequence** — 5 mentions
- **markov** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=66|Speech and Language Processing.pdf p. 66]]

## Liens
- Up: [[research/slp/n-gram-language-models]]
- ← Prev: [[research/slp/summary-2]]
- Next: [[research/slp/exercises-2]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
