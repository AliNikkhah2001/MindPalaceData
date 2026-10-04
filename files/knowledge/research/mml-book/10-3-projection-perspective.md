---
title: "10.3 Projection Perspective"
summary: "§Part II Central Machine Learning Problems › 10 Dimensionalit: 10.3 Projection Perspective Figure 10.6 Illustration of the projection approach: Find a subspace (line) that minimizes the length of the difference vector between projected (orange) and original (blue) data."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "331-338"
---

# 10.3 Projection Perspective

§Part II Central Machine Learning Problems › 10 Dimensionality Reduction with Principal Component Analysis › 10.3 Projection Perspective · pp. 331–338 · Mathematics for Machine Learning (MML Book)

## Extrait
10.3 Projection Perspective Figure 10.6 Illustration of the projection approach: Find a subspace (line) that minimizes the length of the difference vector between projected (orange) and original (blue) data. Taking all digits “8” in the MNIST training data, we compute the eigenvalues of the data covariance matrix. Figure 10.5(a) shows the 200 largest eigenvalues of the data covariance matrix. We see that only a few of them have a value that differs significantly from 0. Therefore, most of the variance, when projecting data onto the subspace spanned by the corresponding eigenvectors, is captured by only a few principal components, as shown in Figure 10.5(b). Overall, to find an M-dimensional subspace of RD that retains as much information as possible, PCA tells us to choose the columns of the matrix B in (10.3) as the M eigenvectors of the data covariance matrix S that are associated with the M largest eigenvalues. The maximum amount of variance PCA can capture with the first M principal components is VM = M X m=1 λm , (10.24) where the λm are the M largest eigenvalues of the data covariance matrix S. Consequently, the variance lost by data compression via PCA is JM := D X j=M+1 λj = VD −VM .

## Key terms
- **projection** — 23 mentions
- **coordinate** — 23 mentions
- **subspace** — 17 mentions
- **vector** — 17 mentions
- **optimal** — 14 mentions
- **data** — 13 mentions
- **basis** — 13 mentions
- **principal** — 11 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=331|mml-book.pdf p. 331]]

## Liens
- Up: [[research/mml-book/10-dimensionality-reduction-with-principal-component-analysis]]
- ← Prev: [[research/mml-book/10-2-maximum-variance-perspective]]
- Next: [[research/mml-book/10-4-eigenvector-computation-and-low-rank-approximations]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
