---
title: "4.6 Matrix Approximation"
summary: "§Part I Mathematical Foundations › 4 Matrix Decompositions › : 4.6 Matrix Approximation Sometimes this formulation is called the reduced SVD (e.g., Datta (2010)) reduced SVD or the SVD (e.g., Press et al."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "135-139"
---

# 4.6 Matrix Approximation

§Part I Mathematical Foundations › 4 Matrix Decompositions › 4.6 Matrix Approximation · pp. 135–139 · Mathematics for Machine Learning (MML Book)

## Extrait
4.6 Matrix Approximation Sometimes this formulation is called the reduced SVD (e.g., Datta (2010)) reduced SVD or the SVD (e.g., Press et al. (2007)). This alternative format changes merely how the matrices are constructed but leaves the mathematical structure of the SVD unchanged. The convenience of this alternative formulation is that Σ is diagonal, as in the eigenvalue decomposition. In Section 4.6, we will learn about matrix approximation techniques using the SVD, which is also called the truncated SVD. truncated SVD It is possible to define the SVD of a rank-r matrix A so that U is an m × r matrix, Σ a diagonal matrix r × r, and V an r × n matrix. This construction is very similar to our definition, and ensures that the diagonal matrix Σ has only nonzero entries along the diagonal. The main convenience of this alternative notation is that Σ is diagonal, as in the eigenvalue decomposition. A restriction that the SVD for A only applies to m × n matrices with m > n is practically unnecessary. When m < n, the SVD decomposition will yield Σ with more zero columns than rows and, consequently, the singular values σm+1, . . . , σn are 0. The SVD is used in a variety of applications in machine learning from least-squares problems in curve fitting to solving systems of linear equations.

## Key terms
- **matrix** — 37 mentions
- **approximation** — 23 mentions
- **matrices** — 18 mentions
- **norm** — 14 mentions
- **value** — 13 mentions
- **singular** — 11 mentions
- **image** — 11 mentions
- **vector** — 10 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=135|mml-book.pdf p. 135]]

## Liens
- Up: [[research/mml-book/4-matrix-decompositions]]
- ← Prev: [[research/mml-book/4-5-singular-value-decomposition]]
- Next: [[research/mml-book/4-7-matrix-phylogeny]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
