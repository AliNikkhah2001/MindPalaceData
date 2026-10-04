---
title: "10.6 Key Steps of PCA in Practice"
summary: "§Part II Central Machine Learning Problems › 10 Dimensionalit: Dimensionality Reduction with Principal Component Analysis and we get a new eigenvector/eigenvalue equation: λm remains eigenvalue, which confirms our results from Section 4.5.3 that the nonzero eigenvalues of XX⊤equa"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "342-344"
---

# 10.6 Key Steps of PCA in Practice

§Part II Central Machine Learning Problems › 10 Dimensionality Reduction with Principal Component Analysis › 10.6 Key Steps of PCA in Practice · pp. 342–344 · Mathematics for Machine Learning (MML Book)

## Extrait
Dimensionality Reduction with Principal Component Analysis and we get a new eigenvector/eigenvalue equation: λm remains eigenvalue, which confirms our results from Section 4.5.3 that the nonzero eigenvalues of XX⊤equal the nonzero eigenvalues of X⊤X. We obtain the eigenvector of the matrix N X⊤X ∈RN×N associated with λm as cm := X⊤bm. Assuming we have no duplicate data points, this matrix has rank N and is invertible. This also implies that N X⊤X has the same (nonzero) eigenvalues as the data covariance matrix S. But this is now an N × N matrix, so that we can compute the eigenvalues and eigenvectors much more efficiently than for the original D ×D data covariance matrix. Now that we have the eigenvectors of N X⊤X, we are going to recover the original eigenvectors, which we still need for PCA. Currently, we know the eigenvectors of N X⊤X. If we left-multiply our eigenvalue/ eigenvector equation with X, we get N XX⊤ | {z } S Xcm = λmXcm (10.57) and we recover the data covariance matrix again. This now also means that we recover Xcm as an eigenvector of S. Remark. If we want to apply the PCA algorithm that we discussed in Section 10.6, we need to normalize the eigenvectors Xcm of S so that they have norm 1.

## Key terms
- **data** — 24 mentions
- **eigenvector** — 14 mentions
- **matrix** — 14 mentions
- **principal** — 11 mentions
- **eigenvalue** — 11 mentions
- **original** — 11 mentions
- **digit** — 11 mentions
- **dataset** — 10 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=342|mml-book.pdf p. 342]]

## Liens
- Up: [[research/mml-book/10-dimensionality-reduction-with-principal-component-analysis]]
- ← Prev: [[research/mml-book/10-5-pca-in-high-dimensions]]
- Next: [[research/mml-book/10-7-latent-variable-perspective]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
