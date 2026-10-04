---
title: "3.6 Orthogonal Complement"
summary: "§Part I Mathematical Foundations › 3 Analytic Geometry › 3.6 : 3.6 Orthogonal Complement Let us introduce this more formally. Consider an n-dimensional vector space V and a basis {b1, ."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "85-85"
---

# 3.6 Orthogonal Complement

§Part I Mathematical Foundations › 3 Analytic Geometry › 3.6 Orthogonal Complement · pp. 85–85 · Mathematics for Machine Learning (MML Book)

## Extrait
3.6 Orthogonal Complement Let us introduce this more formally. Definition 3.9 (Orthonormal Basis). Consider an n-dimensional vector space V and a basis {b1, . . . , bn} of V . If ⟨bi, bj⟩= 0 for i̸ = j (3.33) ⟨bi, bi⟩= 1 (3.34) for all i, j = 1, . . . , n then the basis is called an orthonormal basis (ONB). orthonormal basis ONB If only (3.33) is satisfied, then the basis is called an orthogonal basis. Note orthogonal basis that (3.34) implies that every basis vector has length/norm 1. Recall from Section 2.6.1 that we can use Gaussian elimination to find a basis for a vector space spanned by a set of vectors. Assume we are given a set {˜b1, . . . , ˜bn} of non-orthogonal and unnormalized basis vectors. We concatenate them into a matrix ˜B = [˜b1, . . . , ˜bn] and apply Gaussian elim- ination to the augmented matrix (Section 2.3.2) [ ˜B ˜B ⊤| ˜B] to obtain an orthonormal basis. This constructive way to iteratively build an orthonormal basis {b1, . . . , bn} is called the Gram-Schmidt process (Strang, 2003). Example 3.8 (Orthonormal Basis) The canonical/standard basis for a Euclidean vector space Rn is an orthonormal basis, where the inner product is the dot product of vectors. In R2, the vectors b1 = √ 1  , b2 = √  1 −1  (3.35) form an orthonormal basis since b⊤ 1 b2 = 0 and ∥b1∥= 1 = ∥b2∥.

## Key terms
- **basis** — 18 mentions
- **vector** — 14 mentions
- **orthonormal** — 9 mentions
- **orthogonal** — 7 mentions
- **space** — 5 mentions
- **complement** — 3 mentions
- **called** — 3 mentions
- **consider** — 2 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=85|mml-book.pdf p. 85]]

## Liens
- Up: [[research/mml-book/3-analytic-geometry]]
- ← Prev: [[research/mml-book/3-5-orthonormal-basis]]
- Next: [[research/mml-book/3-7-inner-product-of-functions]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
