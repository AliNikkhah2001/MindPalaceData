---
title: "12.4 Kernels"
summary: "§Part II Central Machine Learning Problems › 12 Classificatio: Classification with Support Vector Machines This result can be seen by multiplying out the individual classes N X n=1 ynαn = X n:yn=+1 (+1)α+ n + X n:yn=−1 (−1)α− n (12.51a) = X n:yn=+1 α+ n − X n:yn=−1 α− n = 1 −1 = "
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "394-395"
---

# 12.4 Kernels

§Part II Central Machine Learning Problems › 12 Classification with Support Vector Machines › 12.4 Kernels · pp. 394–395 · Mathematics for Machine Learning (MML Book)

## Extrait
Classification with Support Vector Machines This result can be seen by multiplying out the individual classes N X n=1 ynαn = X n:yn=+1 (+1)α+ n + X n:yn=−1 (−1)α− n (12.51a) = X n:yn=+1 α+ n − X n:yn=−1 α− n = 1 −1 = 0 . (12.51b) The objective function (12.48) and the constraint (12.50), along with the assumption that α ⩾0, give us a constrained (convex) optimization problem. This optimization problem can be shown to be the same as that of the dual hard margin SVM (Bennett and Bredensteiner, 2000a). Remark. To obtain the soft margin dual, we consider the reduced hull. The reduced hull is similar to the convex hull but has an upper bound to the reduced hull size of the coefficients α. The maximum possible value of the elements of α restricts the size that the convex hull can take. In other words, the bound on α shrinks the convex hull to a smaller volume (Bennett and Bredensteiner, 2000b). ♢ Consider the formulation of the dual SVM (12.41). Notice that the inner product in the objective occurs only between examples xi and xj. There are no inner products between the examples and the parameters. Therefore, if we consider a set of features ϕ(xi) to represent xi, the only change in the dual SVM will be to replace the inner product.

## Key terms
- **kernel** — 25 mentions
- **feature** — 16 mentions
- **function** — 10 mentions
- **inner** — 7 mentions
- **product** — 7 mentions
- **hull** — 6 mentions
- **matrix** — 6 mentions
- **dual** — 5 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=394|mml-book.pdf p. 394]]

## Liens
- Up: [[research/mml-book/12-classification-with-support-vector-machines]]
- ← Prev: [[research/mml-book/12-3-dual-support-vector-machine]]
- Next: [[research/mml-book/12-5-numerical-solution]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
