---
title: "Learning in Multinomial Logistic Regression"
summary: "§I Large Language Models › Logistic Regression › Learning in : 4.8 • LEARNING IN MULTINOMIAL LOGISTIC REGRESSION Binary Logistic Regression w [f ⨉1] Output sigmoid [1⨉f] Input words p(+) = 1- p(-) … y^ x y Input feature vector [scalar] positive lexicon words = 1 count of “no” = 0"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "89-89"
---

# Learning in Multinomial Logistic Regression

§I Large Language Models › Logistic Regression › Learning in Multinomial Logistic Regression · pp. 89–89 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.8 • LEARNING IN MULTINOMIAL LOGISTIC REGRESSION Binary Logistic Regression w [f ⨉1] Output sigmoid [1⨉f] Input words p(+) = 1- p(-) … y^ x y Input feature vector [scalar] positive lexicon words = 1 count of “no” = 0 wordcount =3 x1 x2 x3 xf dessert was great Weight vector W [f⨉1] Output softmax [K⨉f] Input words p(+) … y1 ^ y2 ^ y3 ^ x y Input feature vector [K⨉1] positive lexicon words = 1 count of “no” = 0 wordcount =3 x1 x2 x3 xf dessert was great p(-) p(neut) Weight matrix These f red weights are a row of W corresponding to weight vector w3, (= weights for class 3, = a prototype of class 3) Figure 4.6 Binary versus multinomial logistic regression. Binary logistic regression uses a single weight vector w, and has a scalar output ˆy. In multinomial logistic regression we have K separate weight vectors corresponding to the K classes, all packed into a single weight matrix W, and a vector output ˆy. We omit the biases from both figures for clarity. 4.8 Learning in Multinomial Logistic Regression The loss function for multinomial logistic regression generalizes the loss function for binary logistic regression from 2 to K classes. Recall that the cross-entropy loss for binary logistic regression (repeated from Eq.

## Key terms
- **regression** — 11 mentions
- **logistic** — 10 mentions
- **vector** — 10 mentions
- **weight** — 8 mentions
- **multinomial** — 7 mentions
- **binary** — 5 mentions
- **output** — 4 mentions
- **input** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=89|Speech and Language Processing.pdf p. 89]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/multinomial-logistic-regression]]
- Next: [[research/slp/evaluation-precision-recall-f-measure]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
