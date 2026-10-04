---
title: "3.8 Orthogonal Projections"
summary: "§Part I Mathematical Foundations › 3 Analytic Geometry › 3.8 : 3.8 Orthogonal Projections for lower and upper limits a, b < ∞, respectively. As with our usual inner product, we can define norms and orthogonality by looking at the inner product."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "87-96"
---

# 3.8 Orthogonal Projections

§Part I Mathematical Foundations › 3 Analytic Geometry › 3.8 Orthogonal Projections · pp. 87–96 · Mathematics for Machine Learning (MML Book)

## Extrait
3.8 Orthogonal Projections for lower and upper limits a, b < ∞, respectively. As with our usual inner product, we can define norms and orthogonality by looking at the inner product. If (3.37) evaluates to 0, the functions u and v are orthogonal. To make the preceding inner product mathematically precise, we need to take care of measures and the definition of integrals, leading to the definition of a Hilbert space. Furthermore, unlike inner products on finite-dimensional vectors, inner products on functions may diverge (have infinite value). All this requires diving into some more intricate details of real and functional analysis, which we do not cover in this book. Example 3.9 (Inner Product of Functions) If we choose u = sin(x) and v = cos(x), the integrand f(x) = u(x)v(x) Figure 3.8 f(x) = sin(x) cos(x). −2.5 0.0 2.5 x −0.5 0.0 0.5 sin(x) cos(x) of (3.37), is shown in Figure 3.8. We see that this function is odd, i.e., f(−x) = −f(x). Therefore, the integral with limits a = −π, b = π of this product evaluates to 0. Therefore, sin and cos are orthogonal functions. Remark. It also holds that the collection of functions {1, cos(x), cos(2x), cos(3x), . . . } (3.38) is orthogonal if we integrate from −π to π, i.e., any pair of functions are orthogonal to each other.

## Key terms
- **projection** — 37 mentions
- **product** — 22 mentions
- **subspace** — 17 mentions
- **inner** — 16 mentions
- **vector** — 16 mentions
- **orthogonal** — 13 mentions
- **onto** — 13 mentions
- **data** — 12 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=87|mml-book.pdf p. 87]]

## Liens
- Up: [[research/mml-book/3-analytic-geometry]]
- ← Prev: [[research/mml-book/3-7-inner-product-of-functions]]
- Next: [[research/mml-book/3-9-rotations]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
