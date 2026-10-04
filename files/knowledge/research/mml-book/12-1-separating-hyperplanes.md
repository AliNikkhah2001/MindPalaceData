---
title: "12.1 Separating Hyperplanes"
summary: "§Part II Central Machine Learning Problems › 12 Classificatio: Classification with Support Vector Machines In the following, we formalize the idea of finding a linear separator of the two classes."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "378-379"
---

# 12.1 Separating Hyperplanes

§Part II Central Machine Learning Problems › 12 Classification with Support Vector Machines › 12.1 Separating Hyperplanes · pp. 378–379 · Mathematics for Machine Learning (MML Book)

## Extrait
Classification with Support Vector Machines In the following, we formalize the idea of finding a linear separator of the two classes. We introduce the idea of the margin and then extend linear separators to allow for examples to fall on the “wrong” side, incurring a classification error. We present two equivalent ways of formalizing the SVM: the geometric view (Section 12.2.4) and the loss function view (Section 12.2.5). We derive the dual version of the SVM using Lagrange multipliers (Section 7.2). The dual SVM allows us to observe a third way of formalizing the SVM: in terms of the convex hulls of the examples of each class (Section 12.3.2). We conclude by briefly describing kernels and how to numerically solve the nonlinear kernel-SVM optimization problem. Given two examples represented as vectors xi and xj, one way to compute the similarity between them is using an inner product ⟨xi, xj⟩. Recall from Section 3.2 that inner products are closely related to the angle between two vectors. The value of the inner product between two vectors depends on the length (norm) of each vector. Furthermore, inner products allow us to rigorously define geometric concepts such as orthogonality and projections.

## Key terms
- **hyperplane** — 20 mentions
- **vector** — 17 mentions
- **positive** — 8 mentions
- **negative** — 8 mentions
- **side** — 6 mentions
- **inner** — 6 mentions
- **product** — 6 mentions
- **classification** — 5 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=378|mml-book.pdf p. 378]]

## Liens
- Up: [[research/mml-book/12-classification-with-support-vector-machines]]
- Next: [[research/mml-book/12-2-primal-support-vector-machine]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
