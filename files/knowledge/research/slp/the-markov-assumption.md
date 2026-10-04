---
title: "The Markov assumption"
summary: "§I Large Language Models › N-gram Language Models › N-Grams ›: CHAPTER 3 • N-GRAM LANGUAGE MODELS bility: P(X1...Xn) = P(X1)P(X2|X1)P(X3|X1:2)...P(Xn|X1:n−1) = n Y k=1 P(Xk|X1:k−1) (3.3) Applying the chain rule to words, we get P(w1:n) = P(w1)P(w2|w1)P(w3|w1:2)...P(wn|w1:n−1) = n"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "48-48"
---

# The Markov assumption

§I Large Language Models › N-gram Language Models › N-Grams › The Markov assumption · pp. 48–48 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 3 • N-GRAM LANGUAGE MODELS bility: P(X1...Xn) = P(X1)P(X2|X1)P(X3|X1:2)...P(Xn|X1:n−1) = n Y k=1 P(Xk|X1:k−1) (3.3) Applying the chain rule to words, we get P(w1:n) = P(w1)P(w2|w1)P(w3|w1:2)...P(wn|w1:n−1) = n Y k=1 P(wk|w1:k−1) (3.4) The chain rule shows the link between computing the joint probability of a sequence and computing the conditional probability of a word given previous words. Equation 3.4 suggests that we could estimate the joint probability of an entire sequence of words by multiplying together a number of conditional probabilities. But using the chain rule doesn’t really seem to help us! We don’t know any way to compute the exact probability of a word given a long sequence of preceding words, P(wn|w1:n−1). As we said above, we can’t just estimate by counting the number of times every word occurs following every long string in some corpus, because language is creative and any particular context might have never occurred before! The intuition of the n-gram model is that instead of computing the probability of a word given its entire history, we can approximate the history by just the last few words. The bigram model, for example, approximates the probability of a word given bigram all the previous words P(wn|w1:n−1) by using only the conditional probability given the preceding word P(wn|wn−1).

## Key terms
- **word** — 20 mentions
- **probability** — 13 mentions
- **n-gram** — 6 mentions
- **model** — 6 mentions
- **conditional** — 5 mentions
- **computing** — 4 mentions
- **sequence** — 4 mentions
- **bigram** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=48|Speech and Language Processing.pdf p. 48]]

## Liens
- Up: [[research/slp/n-grams]]
- Next: [[research/slp/how-to-estimate-probabilities]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
