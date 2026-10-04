---
title: "4.2 Eigenvalues and Eigenvectors"
summary: "§Part I Mathematical Foundations › 4 Matrix Decompositions › : 4.2 Eigenvalues and Eigenvectors c0 = det(A) , (4.23) cn−1 = (−1)n−1tr(A) . (4.24) The characteristic polynomial (4.22a) will allow us to compute eigenvalues and eigenvectors, covered in the next section."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "111-119"
---

# 4.2 Eigenvalues and Eigenvectors

§Part I Mathematical Foundations › 4 Matrix Decompositions › 4.2 Eigenvalues and Eigenvectors · pp. 111–119 · Mathematics for Machine Learning (MML Book)

## Extrait
4.2 Eigenvalues and Eigenvectors c0 = det(A) , (4.23) cn−1 = (−1)n−1tr(A) . (4.24) The characteristic polynomial (4.22a) will allow us to compute eigenvalues and eigenvectors, covered in the next section. We will now get to know a new way to characterize a matrix and its associated linear mapping. Recall from Section 2.7.1 that every linear mapping has a unique transformation matrix given an ordered basis. We can interpret linear mappings and their associated transformation matrices by performing an “eigen” analysis. As we will see, the eigenvalues of a linEigen is a German word meaning “characteristic”, “self”, or “own”. ear mapping will tell us how a special set of vectors, the eigenvectors, is transformed by the linear mapping. Definition 4.6. Let A ∈Rn×n be a square matrix. Then λ ∈R is an eigenvalue of A and x ∈Rn\{0} is the corresponding eigenvector of A if eigenvalue eigenvector Ax = λx . (4.25) We call (4.25) the eigenvalue equation. eigenvalue equation Remark. In the linear algebra literature and software, it is often a convention that eigenvalues are sorted in descending order, so that the largest eigenvalue and associated eigenvector are called the first eigenvalue and its associated eigenvector, and the second largest called the second eigenvalue and its associated eigenvector, and so on.

## Key terms
- **eigenvalue** — 47 mentions
- **eigenvector** — 30 mentions
- **matrix** — 14 mentions
- **eigenspace** — 13 mentions
- **vector** — 13 mentions
- **mapping** — 11 mentions
- **characteristic** — 10 mentions
- **associated** — 10 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=111|mml-book.pdf p. 111]]

## Liens
- Up: [[research/mml-book/4-matrix-decompositions]]
- ← Prev: [[research/mml-book/4-1-determinant-and-trace]]
- Next: [[research/mml-book/4-3-cholesky-decomposition]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
