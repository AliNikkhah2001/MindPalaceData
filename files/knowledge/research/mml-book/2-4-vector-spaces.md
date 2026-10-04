---
title: "2.4 Vector Spaces"
summary: "§Part I Mathematical Foundations › 2 Linear Algebra › 2.4 Vec: 2.4 Vector Spaces and use the Moore-Penrose pseudo-inverse (A⊤A)−1A⊤to determine the Moore-Penrose pseudo-inverse solution (2.59) that solves Ax = b, which also corresponds to the minimum norm least-squares solution."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "41-45"
---

# 2.4 Vector Spaces

§Part I Mathematical Foundations › 2 Linear Algebra › 2.4 Vector Spaces · pp. 41–45 · Mathematics for Machine Learning (MML Book)

## Extrait
2.4 Vector Spaces and use the Moore-Penrose pseudo-inverse (A⊤A)−1A⊤to determine the Moore-Penrose pseudo-inverse solution (2.59) that solves Ax = b, which also corresponds to the minimum norm least-squares solution. A disadvantage of this approach is that it requires many computations for the matrix-matrix product and computing the inverse of A⊤A. Moreover, for reasons of numerical precision it is generally not recommended to compute the inverse or pseudo-inverse. In the following, we therefore briefly discuss alternative approaches to solving systems of linear equations. Gaussian elimination plays an important role when computing determinants (Section 4.1), checking whether a set of vectors is linearly independent (Section 2.5), computing the inverse of a matrix (Section 2.2.2), computing the rank of a matrix (Section 2.6.2), and determining a basis of a vector space (Section 2.6.1). Gaussian elimination is an intuitive and constructive way to solve a system of linear equations with thousands of variables. However, for systems with millions of variables, it is impractical as the required number of arithmetic operations scales cubically in the number of simultaneous equations. In …

## Key terms
- **vector** — 37 mentions
- **element** — 25 mentions
- **group** — 23 mentions
- **operation** — 19 mentions
- **multiplication** — 18 mentions
- **space** — 15 mentions
- **inverse** — 14 mentions
- **linear** — 11 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=41|mml-book.pdf p. 41]]

## Liens
- Up: [[research/mml-book/2-linear-algebra]]
- ← Prev: [[research/mml-book/2-3-solving-systems-of-linear-equations]]
- Next: [[research/mml-book/2-5-linear-independence]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
