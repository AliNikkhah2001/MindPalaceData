---
title: "3.5 Orthonormal Basis"
summary: "§Part I Mathematical Foundations › 3 Analytic Geometry › 3.5 : we get that the angle ω between x and y is given by cos ω = ⟨x, y⟩ ∥x∥∥y∥= −1 3 =⇒ω ≈1.91 rad ≈109.5◦, (3.28) and x and y are not orthogonal."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "84-84"
---

# 3.5 Orthonormal Basis

§Part I Mathematical Foundations › 3 Analytic Geometry › 3.5 Orthonormal Basis · pp. 84–84 · Mathematics for Machine Learning (MML Book)

## Extrait
we get that the angle ω between x and y is given by cos ω = ⟨x, y⟩ ∥x∥∥y∥= −1 3 =⇒ω ≈1.91 rad ≈109.5◦, (3.28) and x and y are not orthogonal. Therefore, vectors that are orthogonal with respect to one inner product do not have to be orthogonal with respect to a different inner product. Definition 3.8 (Orthogonal Matrix). A square matrix A ∈Rn×n is an orthogonal matrix if and only if its columns are orthonormal so that orthogonal matrix AA⊤= I = A⊤A , (3.29) which implies that A−1 = A⊤, (3.30) i.e., the inverse is obtained by simply transposing the matrix. It is convention to call these matrices “orthogonal” but a more precise description would be “orthonormal”. Transformations by orthogonal matrices are special because the length of a vector x is not changed when transforming it using an orthogonal matrix A. For the dot product, we obtain Transformations with orthogonal matrices preserve distances and angles. ∥Ax∥ 2 = (Ax)⊤(Ax) = x⊤A⊤Ax = x⊤Ix = x⊤x = ∥x∥ 2 . (3.31) Moreover, the angle between any two vectors x, y, as measured by their inner product, is also unchanged when transforming both of them using an orthogonal matrix A. Assuming the dot product as the inner product, the angle of the images Ax and Ay is given as cos ω = (Ax)⊤(Ay) ∥Ax∥∥Ay∥= x⊤A⊤Ay q x⊤A⊤Axy⊤A⊤Ay = x⊤y ∥x∥∥y∥, (3.32) which gives exactly the angle between x and y.

## Key terms
- **orthogonal** — 14 mentions
- **vector** — 11 mentions
- **angle** — 7 mentions
- **product** — 7 mentions
- **matrix** — 7 mentions
- **basis** — 6 mentions
- **inner** — 5 mentions
- **matrices** — 5 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=84|mml-book.pdf p. 84]]

## Liens
- Up: [[research/mml-book/3-analytic-geometry]]
- ← Prev: [[research/mml-book/3-4-angles-and-orthogonality]]
- Next: [[research/mml-book/3-6-orthogonal-complement]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
