---
title: "Processing many examples at once"
summary: "§I Large Language Models › Logistic Regression › Classificati: 4.3 • CLASSIFICATION WITH LOGISTIC REGRESSION designed features and instead focus on representation learning: ways to learn features automatically in an unsupervised way from the input."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "77-77"
---

# Processing many examples at once

§I Large Language Models › Logistic Regression › Classification with Logistic Regression › Processing many examples at once · pp. 77–77 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.3 • CLASSIFICATION WITH LOGISTIC REGRESSION designed features and instead focus on representation learning: ways to learn features automatically in an unsupervised way from the input. We’ll introduce methods for representation learning in Chapter 5 and Chapter 6. Scaling input features: When different input features have extremely different ranges of values, it’s common to rescale them so they have comparable ranges. We standardize input values by centering them to result in a zero mean and a standard standardize deviation of one (this transformation is sometimes called the z-score). That is, if µi z-score is the mean of the values of feature xi across the m observations in the input dataset, and σi is the standard deviation of the values of features xi across the input dataset, we can replace each feature xi by a new feature x′ i computed as follows: µi = 1 m m X j=1 x(j) i σi = v u u t 1 m m X j=1  x(j) i −µi 2 x′ i = xi −µi σi (4.9) Alternatively, we can normalize the input features values to lie between 0 and 1: normalize x′ i = xi −min(xi) max(xi)−min(xi) (4.10) Having input data with comparable range is useful when comparing values across features. Data scaling is especially important in large neural networks, since it helps speed up gradient descent.

## Key terms
- **input** — 11 mentions
- **feature** — 11 mentions
- **value** — 8 mentions
- **test** — 7 mentions
- **data** — 4 mentions
- **scaling** — 3 mentions
- **follows** — 3 mentions
- **range** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=77|Speech and Language Processing.pdf p. 77]]

## Liens
- Up: [[research/slp/classification-with-logistic-regression]]
- ← Prev: [[research/slp/other-classification-tasks-and-features]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
