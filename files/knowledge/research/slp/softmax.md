---
title: "Softmax"
summary: "§I Large Language Models › Logistic Regression › Multinomial : 4.7 • MULTINOMIAL LOGISTIC REGRESSION multiple classes). Let’s use the following representation: the output y for each input x will be a vector of length K."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "87-87"
---

# Softmax

§I Large Language Models › Logistic Regression › Multinomial logistic regression › Softmax · pp. 87–87 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.7 • MULTINOMIAL LOGISTIC REGRESSION multiple classes). Let’s use the following representation: the output y for each input x will be a vector of length K. If class c is the correct class, we’ll set yc = 1, and set all the other elements of y to be 0, i.e., yc = 1 and y j = 0 ∀j̸ = c. A vector like this y, with one value=1 and the rest 0, is called a one-hot vector. The job of the classifier is to produce an estimate vector ˆy. For each class k, the value ˆyk will be the classifier’s estimate of the probability P(yk = 1|x). The multinomial logistic classifier uses a generalization of the sigmoid, called the softmax function, to compute p(yk = 1|x). The softmax function takes a vector softmax z = [z1,z2,...,zK] of K arbitrary values and maps them to a probability distribution, with each value in the range [0,1], and all the values summing to 1. Like the sigmoid, it is an exponential function. For a vector z of dimensionality K, the softmax is defined as: softmax(zi) = exp(zi) PK j=1 exp(z j) 1 ≤i ≤K (4.33) The softmax of an input vector z = [z1,z2,...,zK] is thus a vector itself: softmax(z) = " exp(z1) PK i=1 exp(zi) , exp(z2) PK i=1 exp(zi) ,..., exp(zK) PK i=1 exp(zi) # (4.34) The denominator PK i=1 exp(zi) is used to normalize all the values into probabilities.

## Key terms
- **vector** — 14 mentions
- **softmax** — 11 mentions
- **input** — 7 mentions
- **value** — 7 mentions
- **sigmoid** — 5 mentions
- **probability** — 4 mentions
- **logistic** — 3 mentions
- **classes** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=87|Speech and Language Processing.pdf p. 87]]

## Liens
- Up: [[research/slp/multinomial-logistic-regression]]
- Next: [[research/slp/applying-softmax-in-logistic-regression]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
