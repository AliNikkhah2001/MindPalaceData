---
title: "The cross-entropy loss function"
summary: "§I Large Language Models › Logistic Regression › The cross-en: 4.5 • THE CROSS-ENTROPY LOSS FUNCTION to the true y. That is, if y is 1, then we want the system’s estimate ˆy = P(y = 1) to be high, i.e."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "79-80"
---

# The cross-entropy loss function

§I Large Language Models › Logistic Regression › The cross-entropy loss function · pp. 79–80 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.5 • THE CROSS-ENTROPY LOSS FUNCTION to the true y. That is, if y is 1, then we want the system’s estimate ˆy = P(y = 1) to be high, i.e. as close to 1 as possible. If y is in fact 0, then we want the system’s estimate ˆy = P(y = 1) to be low, i.e. as close to 0 as possible. This requires two components that we foreshadowed in the introduction to the chapter. The first is a metric for how close ˆy (the systems’s estimate of the probability that the observation is in the positive class) is to the true gold label y. Rather than measure similarity, we usually talk about the opposite of this: the distance between the system output and the gold output, and we call this distance the loss function or loss the cost function. In the next section we’ll introduce the loss function that is commonly used for logistic regression and also for neural networks, the cross-entropy loss. The second thing we need is an optimization algorithm for iteratively updating the weights so as to minimize this loss function. The standard algorithm for this is gradient descent; we’ll introduce the stochastic gradient descent algorithm in the following section. We’ll describe these algorithms for the simpler case of binary logistic regression in the next two sections, and then turn to multinomial logistic regression in Section 4.8.

## Key terms
- **loss** — 27 mentions
- **probability** — 15 mentions
- **function** — 12 mentions
- **correct** — 9 mentions
- **true** — 7 mentions
- **label** — 7 mentions
- **classifier** — 7 mentions
- **negative** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=79|Speech and Language Processing.pdf p. 79]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/learning-in-logistic-regression]]
- Next: [[research/slp/gradient-descent]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
