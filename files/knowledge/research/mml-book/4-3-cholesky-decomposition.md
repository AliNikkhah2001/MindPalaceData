---
title: "4.3 Cholesky Decomposition"
summary: "§Part I Mathematical Foundations › 4 Matrix Decompositions › : Matrix Decompositions on a different web site. The matrix A has the property that for any initial rank/importance vector x of a web site the sequence x, Ax, A2x, ."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "120-120"
---

# 4.3 Cholesky Decomposition

§Part I Mathematical Foundations › 4 Matrix Decompositions › 4.3 Cholesky Decomposition · pp. 120–120 · Mathematics for Machine Learning (MML Book)

## Extrait
Matrix Decompositions on a different web site. The matrix A has the property that for any initial rank/importance vector x of a web site the sequence x, Ax, A2x, . . . converges to a vector x∗. This vector is called the PageRank and satisfies PageRank Ax∗= x∗, i.e., it is an eigenvector (with corresponding eigenvalue 1) of A. After normalizing x∗, such that ∥x∗∥= 1, we can interpret the entries as probabilities. More details and different perspectives on PageRank can be found in the original technical report (Page et al., 1999). There are many ways to factorize special types of matrices that we encounter often in machine learning. In the positive real numbers, we have the square-root operation that gives us a decomposition of the number into identical components, e.g., 9 = 3 · 3. For matrices, we need to be careful that we compute a square-root-like operation on positive quantities. For symmetric, positive definite matrices (see Section 3.2.3), we can choose from a number of square-root equivalent operations. The Cholesky Cholesky decomposition decomposition/Cholesky factorization provides a square-root equivalent opCholesky factorization eration on symmetric, positive definite matrices that is useful in practice.

## Key terms
- **cholesky** — 8 mentions
- **positive** — 7 mentions
- **matrix** — 5 mentions
- **decomposition** — 5 mentions
- **matrices** — 4 mentions
- **symmetric** — 4 mentions
- **definite** — 4 mentions
- **factorization** — 4 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=120|mml-book.pdf p. 120]]

## Liens
- Up: [[research/mml-book/4-matrix-decompositions]]
- ← Prev: [[research/mml-book/4-2-eigenvalues-and-eigenvectors]]
- Next: [[research/mml-book/4-4-eigendecomposition-and-diagonalization]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
