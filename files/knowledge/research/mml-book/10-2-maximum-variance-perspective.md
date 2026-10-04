---
title: "10.2 Maximum Variance Perspective"
summary: "§Part II Central Machine Learning Problems › 10 Dimensionalit: Dimensionality Reduction with Principal Component Analysis Figure 10.3 Examples of handwritten digits from the MNIST dataset."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "326-330"
---

# 10.2 Maximum Variance Perspective

§Part II Central Machine Learning Problems › 10 Dimensionality Reduction with Principal Component Analysis › 10.2 Maximum Variance Perspective · pp. 326–330 · Mathematics for Machine Learning (MML Book)

## Extrait
Dimensionality Reduction with Principal Component Analysis Figure 10.3 Examples of handwritten digits from the MNIST dataset. http: //yann.lecun. com/exdb/mnist/. occurring example, which contains 60,000 examples of handwritten digits 0 through 9. Each digit is a grayscale image of size 28×28, i.e., it contains 784 pixels so that we can interpret every image in this dataset as a vector x ∈R784. Examples of these digits are shown in Figure 10.3. Figure 10.1 gave an example of how a two-dimensional dataset can be represented using a single coordinate. In Figure 10.1(b), we chose to ignore the x2-coordinate of the data because it did not add too much information so that the compressed data is similar to the original data in Figure 10.1(a). We could have chosen to ignore the x1-coordinate, but then the compressed data had been very dissimilar from the original data, and much information in the data would have been lost. If we interpret information content in the data as how “space filling” the dataset is, then we can describe the information contained in the data by looking at the spread of the data. From Section 6.4.1, we know that the variance is an indicator of the spread of the data, and we can derive PCA as a dimensionality reduction algorithm that maximizes the variance in the low-dimensional representation of the data to retain as much information as possible.

## Key terms
- **data** — 41 mentions
- **vector** — 18 mentions
- **variance** — 18 mentions
- **principal** — 15 mentions
- **component** — 15 mentions
- **matrix** — 15 mentions
- **eigenvector** — 15 mentions
- **first** — 12 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=326|mml-book.pdf p. 326]]

## Liens
- Up: [[research/mml-book/10-dimensionality-reduction-with-principal-component-analysis]]
- ← Prev: [[research/mml-book/10-1-problem-setting]]
- Next: [[research/mml-book/10-3-projection-perspective]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
