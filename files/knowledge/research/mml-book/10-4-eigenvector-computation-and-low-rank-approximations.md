---
title: "10.4 Eigenvector Computation and Low-Rank Approximations"
summary: "§Part II Central Machine Learning Problems › 10 Dimensionalit: 10.4 Eigenvector Computation and Low-Rank Approximations cluster. Four embeddings of the digits “0” and “1” in the principal subspace are highlighted in red with their corresponding original digit."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "339-340"
---

# 10.4 Eigenvector Computation and Low-Rank Approximations

§Part II Central Machine Learning Problems › 10 Dimensionality Reduction with Principal Component Analysis › 10.4 Eigenvector Computation and Low-Rank Approximations · pp. 339–340 · Mathematics for Machine Learning (MML Book)

## Extrait
10.4 Eigenvector Computation and Low-Rank Approximations cluster. Four embeddings of the digits “0” and “1” in the principal subspace are highlighted in red with their corresponding original digit. The figure reveals that the variation within the set of “0” is significantly greater than the variation within the set of “1”. In the previous sections, we obtained the basis of the principal subspace as the eigenvectors that are associated with the largest eigenvalues of the data covariance matrix S = 1 N N X n=1 xnx⊤ n = 1 N XX⊤, (10.45) X = [x1, . . . , xN] ∈RD×N . (10.46) Note that X is a D × N matrix, i.e., it is the transpose of the “typical” data matrix (Bishop, 2006; Murphy, 2012). To get the eigenvalues (and the corresponding eigenvectors) of S, we can follow two approaches: Use eigendecomposition or SVD to compute eigenvectors. We perform an eigendecomposition (see Section 4.2) and compute the eigenvalues and eigenvectors of S directly. We use a singular value decomposition (see Section 4.5). Since S is symmetric and factorizes into XX⊤(ignoring the factor 1 N ), the eigenvalues of S are the squared singular values of X. More specifically, the SVD of X is given by X |{z} D×N = U |{z} D×D Σ |{z} D×N V ⊤ |{z} N×N , (10.47) where U ∈RD×D and V ⊤∈RN×N are orthogonal matrices and Σ ∈ RD×N is a matrix whose only nonzero entries are the singular values σii ⩾ 0.

## Key terms
- **eigenvector** — 14 mentions
- **eigenvalues** — 12 mentions
- **matrix** — 9 mentions
- **singular** — 9 mentions
- **value** — 9 mentions
- **theorem** — 6 mentions
- **data** — 5 mentions
- **largest** — 4 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=339|mml-book.pdf p. 339]]

## Liens
- Up: [[research/mml-book/10-dimensionality-reduction-with-principal-component-analysis]]
- ← Prev: [[research/mml-book/10-3-projection-perspective]]
- Next: [[research/mml-book/10-5-pca-in-high-dimensions]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
