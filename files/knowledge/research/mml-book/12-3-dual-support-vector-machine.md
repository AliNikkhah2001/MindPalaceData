---
title: "12.3 Dual Support Vector Machine"
summary: "§Part II Central Machine Learning Problems › 12 Classificatio: 12.3 Dual Support Vector Machine negative log-likelihood. Furthermore, since the likelihood term for linear regression with Gaussian noise is Gaussian, the negative log-likelihood for each example is a squared error f"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "389-393"
---

# 12.3 Dual Support Vector Machine

§Part II Central Machine Learning Problems › 12 Classification with Support Vector Machines › 12.3 Dual Support Vector Machine · pp. 389–393 · Mathematics for Machine Learning (MML Book)

## Extrait
12.3 Dual Support Vector Machine negative log-likelihood. Furthermore, since the likelihood term for linear regression with Gaussian noise is Gaussian, the negative log-likelihood for each example is a squared error function. The squared error function is the loss function that is minimized when looking for the maximum likelihood solution. ♢ The description of the SVM in the previous sections, in terms of the variables w and b, is known as the primal SVM. Recall that we consider inputs x ∈RD with D features. Since w is of the same dimension as x, this means that the number of parameters (the dimension of w) of the optimization problem grows linearly with the number of features. In the following, we consider an equivalent optimization problem (the so-called dual view), which is independent of the number of features. Instead, the number of parameters increases with the number of examples in the training set. We saw a similar idea appear in Chapter 10, where we expressed the learning problem in a way that does not scale with the number of features. This is useful for problems where we have more features than the number of examples in the training dataset. The dual SVM also has the additional advantage that it easily allows kernels to be applied, as we shall see at the end of this chapter.

## Key terms
- **convex** — 20 mentions
- **dual** — 15 mentions
- **vector** — 12 mentions
- **constraint** — 12 mentions
- **hull** — 12 mentions
- **term** — 10 mentions
- **point** — 10 mentions
- **support** — 9 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=389|mml-book.pdf p. 389]]

## Liens
- Up: [[research/mml-book/12-classification-with-support-vector-machines]]
- ← Prev: [[research/mml-book/12-2-primal-support-vector-machine]]
- Next: [[research/mml-book/12-4-kernels]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
