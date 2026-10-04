---
title: "2.6 Basis and Rank"
summary: "§Part I Mathematical Foundations › 2 Linear Algebra › 2.6 Bas: Linear Algebra are linearly independent. The reduced row-echelon form of the corresponding linear equation system with coefficient matrix A =   −4 −2 −2 −10 −1 −1 −3   (2.75) is given as   −7 −15 −18  "
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "50-53"
---

# 2.6 Basis and Rank

§Part I Mathematical Foundations › 2 Linear Algebra › 2.6 Basis and Rank · pp. 50–53 · Mathematics for Machine Learning (MML Book)

## Extrait
Linear Algebra are linearly independent. The reduced row-echelon form of the corresponding linear equation system with coefficient matrix A =   −4 −2 −2 −10 −1 −1 −3   (2.75) is given as   −7 −15 −18  . (2.76) We see that the corresponding linear equation system is non-trivially solvable: The last column is not a pivot column, and x4 = −7x1−15x2−18x3. Therefore, x1, . . . , x4 are linearly dependent as x4 can be expressed as a linear combination of x1, . . . , x3. In a vector space V , we are particularly interested in sets of vectors A that possess the property that any vector v ∈V can be obtained by a linear combination of vectors in A. These vectors are special vectors, and in the following, we will characterize them. 2.6.1 Generating Set and Basis Definition 2.13 (Generating Set and Span). Consider a vector space V = (V, +, ·) and set of vectors A = {x1, . . . , xk} ⊆V. If every vector v ∈ V can be expressed as a linear combination of x1, . . . , xk, A is called a generating set of V . The set of all linear combinations of vectors in A is generating set called the span of A. If A spans the vector space V , we write V = span[A] span or V = span[x1, . . . , xk]. Generating sets are sets of vectors that span vector (sub)spaces, i.e., every vector can be represented as a linear combination of the vectors in the generating set.

## Key terms
- **vector** — 44 mentions
- **basis** — 25 mentions
- **space** — 17 mentions
- **rank** — 17 mentions
- **linear** — 15 mentions
- **linearly** — 13 mentions
- **span** — 13 mentions
- **independent** — 12 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=50|mml-book.pdf p. 50]]

## Liens
- Up: [[research/mml-book/2-linear-algebra]]
- ← Prev: [[research/mml-book/2-5-linear-independence]]
- Next: [[research/mml-book/2-7-linear-mappings]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
