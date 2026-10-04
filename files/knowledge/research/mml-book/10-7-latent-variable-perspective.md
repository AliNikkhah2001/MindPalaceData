---
title: "10.7 Latent Variable Perspective"
summary: "§Part II Central Machine Learning Problems › 10 Dimensionalit: 10.7 Latent Variable Perspective cipal components, we effectively obtain a near-perfect reconstruction. If we were to choose 784 PCs, we would recover the exact digit without any compression loss."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "345-348"
---

# 10.7 Latent Variable Perspective

§Part II Central Machine Learning Problems › 10 Dimensionality Reduction with Principal Component Analysis › 10.7 Latent Variable Perspective · pp. 345–348 · Mathematics for Machine Learning (MML Book)

## Extrait
10.7 Latent Variable Perspective cipal components, we effectively obtain a near-perfect reconstruction. If we were to choose 784 PCs, we would recover the exact digit without any compression loss. Figure 10.13 shows the average squared reconstruction error, which is N N X n=1 ∥xn −˜xn∥ 2 = D X i=M+1 λi , (10.62) as a function of the number M of principal components. We can see that the importance of the principal components drops off rapidly, and only marginal gains can be achieved by adding more PCs. This matches exactly our observation in Figure 10.5, where we discovered that the most of the variance of the projected data is captured by only a few principal components. With about 550 PCs, we can essentially fully reconstruct the training data that contains the digit “8” (some pixels around the boundaries show no variation across the dataset as they are always black). Figure 10.13 Average squared reconstruction error as a function of the number of principal components. The average squared reconstruction error is the sum of the eigenvalues in the orthogonal complement of the principal subspace. Number of PCs Average squared reconstruction error In the previous sections, we derived PCA without any notion of a probabilistic model using the maximum-variance and the projection perspectives.

## Key terms
- **latent** — 23 mentions
- **model** — 22 mentions
- **variable** — 20 mentions
- **data** — 15 mentions
- **probabilistic** — 12 mentions
- **likelihood** — 12 mentions
- **principal** — 8 mentions
- **ppca** — 8 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=345|mml-book.pdf p. 345]]

## Liens
- Up: [[research/mml-book/10-dimensionality-reduction-with-principal-component-analysis]]
- ← Prev: [[research/mml-book/10-6-key-steps-of-pca-in-practice]]
- Next: [[research/mml-book/10-8-further-reading]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
