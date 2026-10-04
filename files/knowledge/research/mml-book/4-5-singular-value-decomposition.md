---
title: "4.5 Singular Value Decomposition"
summary: "§Part I Mathematical Foundations › 4 Matrix Decompositions › : 4.5 Singular Value Decomposition = det(D) = Y i dii (4.63b) allows for an efficient computation of the determinant of A."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "125-134"
---

# 4.5 Singular Value Decomposition

§Part I Mathematical Foundations › 4 Matrix Decompositions › 4.5 Singular Value Decomposition · pp. 125–134 · Mathematics for Machine Learning (MML Book)

## Extrait
4.5 Singular Value Decomposition = det(D) = Y i dii (4.63b) allows for an efficient computation of the determinant of A. The eigenvalue decomposition requires square matrices. It would be useful to perform a decomposition on general matrices. In the next section, we introduce a more general matrix decomposition technique, the singular value decomposition. The singular value decomposition (SVD) of a matrix is a central matrix decomposition method in linear algebra. It has been referred to as the “fundamental theorem of linear algebra” (Strang, 1993) because it can be applied to all matrices, not only to square matrices, and it always exists. Moreover, as we will explore in the following, the SVD of a matrix A, which represents a linear mapping Φ : V →W, quantifies the change between the underlying geometry of these two vector spaces. We recommend the work by Kalman (1996) and Roy and Banerjee (2014) for a deeper overview of the mathematics of the SVD. SVD theorem Theorem 4.22 (SVD Theorem). Let A ∈Rm×n be a rectangular matrix of rank r ∈[0, min(m, n)]. The SVD of A is a decomposition of the form SVD singular value decomposition = U A V ⊤ Σ m n m m m n n n (4.64) with an orthogonal matrix U ∈Rm×m with column vectors ui, i = 1, .

## Key terms
- **matrix** — 27 mentions
- **vector** — 25 mentions
- **singular** — 16 mentions
- **value** — 16 mentions
- **basis** — 15 mentions
- **decomposition** — 13 mentions
- **change** — 11 mentions
- **perform** — 9 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=125|mml-book.pdf p. 125]]

## Liens
- Up: [[research/mml-book/4-matrix-decompositions]]
- ← Prev: [[research/mml-book/4-4-eigendecomposition-and-diagonalization]]
- Next: [[research/mml-book/4-6-matrix-approximation]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
