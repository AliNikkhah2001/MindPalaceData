---
title: "Learning in Logistic Regression"
summary: "§I Large Language Models › Logistic Regression › Learning in : CHAPTER 4 • LOGISTIC REGRESSION But it turns out that we can slightly modify our original equation Eq. We’ll use matrix arithmetic to assign a class to all the examples with one matrix operation!"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "78-78"
---

# Learning in Logistic Regression

§I Large Language Models › Logistic Regression › Learning in Logistic Regression · pp. 78–78 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 4 • LOGISTIC REGRESSION But it turns out that we can slightly modify our original equation Eq. 4.5 to do this much more efficiently. We’ll use matrix arithmetic to assign a class to all the examples with one matrix operation! First, we’ll pack all the input feature vectors for each input x into a single input matrix X, where each row i is a row vector consisting of the feature vector for input example x(i) (i.e., the vector x(i)). Assuming each example has f features and weights, X will therefore be a matrix of shape [m× f], as follows: X =   x(1) x(1) ... x(1) f x(2) x(2) ... x(2) f x(3) x(3) ... x(3) f ...   (4.12) Now if we introduce b as a vector of length m which consists of the scalar bias term b repeated m times, b = [b,b,...,b], and ˆy = [ˆy(1), ˆy(2)..., ˆy(m)] as the vector of outputs (one scalar ˆy(i) = P(y(i) = 1) for each input x(i) and its feature vector x(i)), and represent the weight vector w as a column vector, we can compute all the outputs with a single matrix multiplication and one addition: ˆy = σ(Xw +b) (4.13) You should convince yourself that Eq. 4.13 computes the same thing as our for-loop in Eq. 4.11. For example ˆy(1), the first entry of the output vector ˆy, will correctly be: ˆy(1) = σ  [x(1) 1 ,x(1) 2 ,...,x(1) f ]·[w1,w2,...,w f ]+b  (4.14) Note that we had to reorder X and w from the order they appeared in Eq.

## Key terms
- **vector** — 13 mentions
- **matrix** — 7 mentions
- **input** — 7 mentions
- **feature** — 4 mentions
- **compute** — 4 mentions
- **shape** — 3 mentions
- **weight** — 3 mentions
- **output** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=78|Speech and Language Processing.pdf p. 78]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/classification-with-logistic-regression]]
- Next: [[research/slp/the-cross-entropy-loss-function]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
