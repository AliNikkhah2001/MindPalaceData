---
title: "Statistical Significance Testing"
summary: "§I Large Language Models › Logistic Regression › Statistical : CHAPTER 4 • LOGISTIC REGRESSION and in general decide what the best model is. Once we come up with what we think is the best model, we run it on the (hitherto unseen) test set to report its performance."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "94-96"
---

# Statistical Significance Testing

§I Large Language Models › Logistic Regression › Statistical Significance Testing · pp. 94–96 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 4 • LOGISTIC REGRESSION and in general decide what the best model is. Once we come up with what we think is the best model, we run it on the (hitherto unseen) test set to report its performance. While the use of a devset avoids overfitting the test set, having a fixed training set, devset, and test set creates another problem: in order to save lots of data for training, the test set (or devset) might not be large enough to be representative. Wouldn’t it be better if we could somehow use all our data for training and still use all our data for test? We can do this by cross-validation. cross-validation In cross-validation, we choose a number k, and partition our data into k disjoint subsets called folds. Now we choose one of those k folds as a test set, train our folds classifier on the remaining k −1 folds, and then compute the error rate on the test set. Then we repeat with another fold as the test set, again training on the other k−1 folds. We do this sampling process k times and average the test set error rate from these k runs to get an average error rate. If we choose k = 10, we would train 10 different models (each on 90% of our data), test the model 10 times, and average these 10 values.

## Key terms
- **test** — 44 mentions
- **better** — 17 mentions
- **hypothesis** — 13 mentions
- **fold** — 10 mentions
- **system** — 10 mentions
- **p-value** — 10 mentions
- **classifier** — 9 mentions
- **sets** — 9 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=94|Speech and Language Processing.pdf p. 94]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/test-sets-and-cross-validation]]
- Next: [[research/slp/avoiding-harms-in-classification]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
