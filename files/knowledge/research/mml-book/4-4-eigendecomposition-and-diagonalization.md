---
title: "4.4 Eigendecomposition and Diagonalization"
summary: "§Part I Mathematical Foundations › 4 Matrix Decompositions › : 4.4 Eigendecomposition and Diagonalization Comparing the left-hand side of (4.45) and the right-hand side of (4.46) shows that there is a simple pattern in the diagonal elements lii: l11 = √a11 , l22 = q a22 −l2 21 , "
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "121-124"
---

# 4.4 Eigendecomposition and Diagonalization

§Part I Mathematical Foundations › 4 Matrix Decompositions › 4.4 Eigendecomposition and Diagonalization · pp. 121–124 · Mathematics for Machine Learning (MML Book)

## Extrait
4.4 Eigendecomposition and Diagonalization Comparing the left-hand side of (4.45) and the right-hand side of (4.46) shows that there is a simple pattern in the diagonal elements lii: l11 = √a11 , l22 = q a22 −l2 21 , l33 = q a33 −(l2 31 + l2 32) . (4.47) Similarly for the elements below the diagonal (lij, where i > j), there is also a repeating pattern: l21 = 1 l11 a21 , l31 = 1 l11 a31 , l32 = 1 l22 (a32 −l31l21) . (4.48) Thus, we constructed the Cholesky decomposition for any symmetric, positive definite 3 × 3 matrix. The key realization is that we can backward calculate what the components lij for the L should be, given the values aij for A and previously computed values of lij. The Cholesky decomposition is an important tool for the numerical computations underlying machine learning. Here, symmetric positive definite matrices require frequent manipulation, e.g., the covariance matrix of a multivariate Gaussian variable (see Section 6.5) is symmetric, positive definite. The Cholesky factorization of this covariance matrix allows us to generate samples from a Gaussian distribution. It also allows us to perform a linear transformation of random variables, which is heavily exploited when computing gradients in deep stochastic models, such as the variational auto-encoder (Jimenez Rezende et al., 2014; Kingma and Welling, 2014).

## Key terms
- **matrix** — 26 mentions
- **diagonal** — 18 mentions
- **eigenvectors** — 13 mentions
- **basis** — 12 mentions
- **eigendecomposition** — 10 mentions
- **decomposition** — 10 mentions
- **matrices** — 9 mentions
- **eigenvalue** — 9 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=121|mml-book.pdf p. 121]]

## Liens
- Up: [[research/mml-book/4-matrix-decompositions]]
- ← Prev: [[research/mml-book/4-3-cholesky-decomposition]]
- Next: [[research/mml-book/4-5-singular-value-decomposition]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
