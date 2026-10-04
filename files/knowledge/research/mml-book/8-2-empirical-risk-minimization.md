---
title: "8.2 Empirical Risk Minimization"
summary: "§Part II Central Machine Learning Problems › 8 When Models Me: the model to only fit the training data well, the predictor needs to perform well on unseen data. We simulate the behavior of our predictor on future unseen data using cross-validation (Section 8.2.4)."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "264-270"
---

# 8.2 Empirical Risk Minimization

§Part II Central Machine Learning Problems › 8 When Models Meet Data › 8.2 Empirical Risk Minimization · pp. 264–270 · Mathematics for Machine Learning (MML Book)

## Extrait
the model to only fit the training data well, the predictor needs to perform well on unseen data. We simulate the behavior of our predictor on future unseen data using cross-validation (Section 8.2.4). As we will see cross-validation in this chapter, to achieve the goal of performing well on unseen data, we will need to balance between fitting well on training data and finding “simple” explanations of the phenomenon. This trade-off is achieved using regularization (Section 8.2.3) or by adding a prior (Section 8.3.2). In philosophy, this is considered to be neither induction nor deduction, but is called abduction. According to the Stanford Encyclopedia of Philosophy, abduction abduction is the process of inference to the best explanation (Douven, 2017). A good movie title is “AI abduction”. We often need to make high-level modeling decisions about the structure of the predictor, such as the number of components to use or the class of probability distributions to consider. The choice of the number of components is an example of a hyperparameter, and this choice can afhyperparameter fect the performance of the model significantly. The problem of choosing among different models is called model selection, which we describe in model selection Section 8.6.

## Key terms
- **predictor** — 23 mentions
- **data** — 22 mentions
- **function** — 22 mentions
- **risk** — 21 mentions
- **training** — 14 mentions
- **empirical** — 14 mentions
- **model** — 13 mentions
- **loss** — 13 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=264|mml-book.pdf p. 264]]

## Liens
- Up: [[research/mml-book/8-when-models-meet-data]]
- ← Prev: [[research/mml-book/8-1-data-models-and-learning]]
- Next: [[research/mml-book/8-3-parameter-estimation]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
