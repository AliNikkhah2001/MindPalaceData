---
title: "10.5 PCA in High Dimensions"
summary: "§Part II Central Machine Learning Problems › 10 Dimensionalit: 10.5 PCA in High Dimensions the null space of S and follows the iteration xk+1 = Sxk ∥Sxk∥, k = 0, 1, . (10.52) This means the vector xk is multiplied by S in every iteration and then If S is invertible, it is suffici"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "341-341"
---

# 10.5 PCA in High Dimensions

§Part II Central Machine Learning Problems › 10 Dimensionality Reduction with Principal Component Analysis › 10.5 PCA in High Dimensions · pp. 341–341 · Mathematics for Machine Learning (MML Book)

## Extrait
10.5 PCA in High Dimensions the null space of S and follows the iteration xk+1 = Sxk ∥Sxk∥, k = 0, 1, . . . . (10.52) This means the vector xk is multiplied by S in every iteration and then If S is invertible, it is sufficient to ensure that x0̸ = 0. normalized, i.e., we always have ∥xk∥= 1. This sequence of vectors converges to the eigenvector associated with the largest eigenvalue of S. The original Google PageRank algorithm (Page et al., 1999) uses such an algorithm for ranking web pages based on their hyperlinks. In order to do PCA, we need to compute the data covariance matrix. In D dimensions, the data covariance matrix is a D ×D matrix. Computing the eigenvalues and eigenvectors of this matrix is computationally expensive as it scales cubically in D. Therefore, PCA, as we discussed earlier, will be infeasible in very high dimensions. For example, if our xn are images with 10,000 pixels (e.g., 100 × 100 pixel images), we would need to compute the eigendecomposition of a 10,000 × 10,000 covariance matrix. In the following, we provide a solution to this problem for the case that we have substantially fewer data points than dimensions, i.e., N ≪D. Assume we have a centered dataset x1, .

## Key terms
- **matrix** — 10 mentions
- **data** — 8 mentions
- **covariance** — 7 mentions
- **dimensions** — 4 mentions
- **eigenvalue** — 4 mentions
- **points** — 4 mentions
- **vector** — 3 mentions
- **eigenvector** — 3 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=341|mml-book.pdf p. 341]]

## Liens
- Up: [[research/mml-book/10-dimensionality-reduction-with-principal-component-analysis]]
- ← Prev: [[research/mml-book/10-4-eigenvector-computation-and-low-rank-approximations]]
- Next: [[research/mml-book/10-6-key-steps-of-pca-in-practice]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
