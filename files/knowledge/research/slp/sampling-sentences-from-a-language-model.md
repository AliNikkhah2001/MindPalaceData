---
title: "Sampling sentences from a language model"
summary: "§I Large Language Models › N-gram Language Models › Sampling : CHAPTER 3 • N-GRAM LANGUAGE MODELS language that is deterministic (no probabilities), any word can follow any word, and whose vocabulary consists of only three colors: L = {red,blue,green} (3.18) The branching factor "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "56-56"
---

# Sampling sentences from a language model

§I Large Language Models › N-gram Language Models › Sampling sentences from a language model · pp. 56–56 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 3 • N-GRAM LANGUAGE MODELS language that is deterministic (no probabilities), any word can follow any word, and whose vocabulary consists of only three colors: L = {red,blue,green} (3.18) The branching factor of this language is 3. Now let’s make a probabilistic version of the same LM, let’s call it A, where each word follows each other with equal probability 1 3 (it was trained on a training set with equal counts for the 3 colors), and a test set T = “red red red red blue”. Let’s first convince ourselves that if we compute the perplexity of this artificial color language on this test set (or any such test set) we indeed get 3. By Eq. 3.15, the perplexity of A on T is: perplexityA(T) = PA(red red red red blue)−1 = 1 5!−1 = 1 −1 = 3 (3.19) But now suppose red was very likely in the training set of a different LM B, and so B has the following probabilities: P(red) = 0.8 P(green) = 0.1 P(blue) = 0.1 (3.20) We should expect the perplexity of the same test set red red red red blue for language model B to be lower since most of the time the next color will be red, which is very predictable, i.e. has a high probability. So the probability of the test set will be higher, and since perplexity is inversely related to probability, the perplexity will be lower.

## Key terms
- **language** — 9 mentions
- **model** — 7 mentions
- **blue** — 6 mentions
- **probability** — 6 mentions
- **perplexity** — 6 mentions
- **word** — 5 mentions
- **test** — 5 mentions
- **color** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=56|Speech and Language Processing.pdf p. 56]]

## Liens
- Up: [[research/slp/n-gram-language-models]]
- ← Prev: [[research/slp/evaluating-language-models-perplexity]]
- Next: [[research/slp/generalizing-vs-overfitting-the-training-set]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
