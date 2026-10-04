---
title: "Features in Multinomial Logistic Regression"
summary: "§I Large Language Models › Logistic Regression › Multinomial : CHAPTER 4 • LOGISTIC REGRESSION set of K weight vectors as a weight matrix W and a bias vector b. Each row k of W corresponds to the vector of weights wk."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "88-88"
---

# Features in Multinomial Logistic Regression

§I Large Language Models › Logistic Regression › Multinomial logistic regression › Features in Multinomial Logistic Regression · pp. 88–88 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 4 • LOGISTIC REGRESSION set of K weight vectors as a weight matrix W and a bias vector b. Each row k of W corresponds to the vector of weights wk. W thus has shape [K × f], for K the number of output classes and f the number of input features. The bias vector b has one value for each of the K output classes. If we represent the weights in this way, we can compute ˆy, the vector of output probabilities for each of the K classes, by a single elegant equation: ˆy = softmax(Wx+b) (4.36) If you work out the matrix arithmetic, you can see that the estimated score of the first output class ˆy1 (before we take the softmax) will correctly turn out to be w1 ·x+b1. One helpful interpretation of the weight matrix W is to see each row wk as a prototype of class k. The weight vector wk that is learned represents the class as prototype a kind of template. Since two vectors that are more similar to each other have a higher dot product with each other, the dot product acts as a similarity function. Logistic regression is thus learning a protoype representation for each class, such that incoming vectors are assigned the class k they are most similar to from the K classes (Doumbouya et al., 2025).

## Key terms
- **weight** — 16 mentions
- **feature** — 12 mentions
- **vector** — 10 mentions
- **class** — 10 mentions
- **logistic** — 6 mentions
- **regression** — 6 mentions
- **output** — 6 mentions
- **classes** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=88|Speech and Language Processing.pdf p. 88]]

## Liens
- Up: [[research/slp/multinomial-logistic-regression]]
- ← Prev: [[research/slp/applying-softmax-in-logistic-regression]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
