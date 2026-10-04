---
title: "3.1 Norms"
summary: "§Part I Mathematical Foundations › 3 Analytic Geometry › 3.1 : 3.1 Norms Figure 3.3 For different norms, the red lines indicate the set of vectors with norm 1. Left: Manhattan norm; Right: Euclidean distance."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "77-77"
---

# 3.1 Norms

§Part I Mathematical Foundations › 3 Analytic Geometry › 3.1 Norms · pp. 77–77 · Mathematics for Machine Learning (MML Book)

## Extrait
3.1 Norms Figure 3.3 For different norms, the red lines indicate the set of vectors with norm 1. Left: Manhattan norm; Right: Euclidean distance. ∥x∥1 = 1 ∥x∥2 = 1 When we think of geometric vectors, i.e., directed line segments that start at the origin, then intuitively the length of a vector is the distance of the “end” of this directed line segment from the origin. In the following, we will discuss the notion of the length of vectors using the concept of a norm. Definition 3.1 (Norm). A norm on a vector space V is a function norm ∥· ∥: V →R , (3.1) x 7→∥x∥, (3.2) which assigns each vector x its length ∥x∥∈R, such that for all λ ∈R length and x, y ∈V the following hold: absolutely homogeneous Absolutely homogeneous: ∥λx∥= |λ|∥x∥ triangle inequality Triangle inequality: ∥x + y∥⩽∥x∥+ ∥y∥ positive definite Positive definite: ∥x∥⩾0 and ∥x∥= 0 ⇐⇒x = 0 Figure 3.2 Triangle inequality. a b c ≤a + b In geometric terms, the triangle inequality states that for any triangle, the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side; see Figure 3.2 for an illustration. Definition 3.1 is in terms of a general vector space V (Section 2.4), but in this book we will only consider a finite-dimensional vector space Rn.

## Key terms
- **norm** — 14 mentions
- **vector** — 12 mentions
- **length** — 6 mentions
- **manhattan** — 5 mentions
- **triangle** — 5 mentions
- **inequality** — 4 mentions
- **line** — 3 mentions
- **space** — 3 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=77|mml-book.pdf p. 77]]

## Liens
- Up: [[research/mml-book/3-analytic-geometry]]
- Next: [[research/mml-book/3-2-inner-products]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
