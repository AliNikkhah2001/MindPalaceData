---
title: "3.4 Angles and Orthogonality"
summary: "§Part I Mathematical Foundations › 3 Analytic Geometry › 3.4 : The mapping d : V × V →R (3.22) (x, y) 7→d(x, y) (3.23) is called a metric. Similar to the length of a vector, the distance between vectors does not require an inner product: a norm is sufficient."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "82-83"
---

# 3.4 Angles and Orthogonality

§Part I Mathematical Foundations › 3 Analytic Geometry › 3.4 Angles and Orthogonality · pp. 82–83 · Mathematics for Machine Learning (MML Book)

## Extrait
The mapping d : V × V →R (3.22) (x, y) 7→d(x, y) (3.23) is called a metric. metric Remark. Similar to the length of a vector, the distance between vectors does not require an inner product: a norm is sufficient. If we have a norm induced by an inner product, the distance may vary depending on the choice of the inner product. ♢ A metric d satisfies the following: 1. d is positive definite, i.e., d(x, y) ⩾0 for all x, y ∈V and d(x, y) = positive definite 0 ⇐⇒x = y . 2. d is symmetric, i.e., d(x, y) = d(y, x) for all x, y ∈V . symmetric triangle inequality 3. Triangle inequality: d(x, z) ⩽d(x, y) + d(y, z) for all x, y, z ∈V . Remark. At first glance, the lists of properties of inner products and metrics look very similar. However, by comparing Definition 3.3 with Definition 3.6 we observe that ⟨x, y⟩and d(x, y) behave in opposite directions. Very similar x and y will result in a large value for the inner product and a small value for the metric. ♢ 3.4 Angles and Orthogonality Figure 3.4 When restricted to [0, π] then f(ω) = cos(ω) returns a unique number in the interval [−1, 1]. π/2 π ω −1 cos(ω) In addition to enabling the definition of lengths of vectors, as well as the distance between two vectors, inner products also capture the geometry of a vector space by defining the angle ω between two vectors.

## Key terms
- **vector** — 23 mentions
- **product** — 19 mentions
- **angle** — 16 mentions
- **inner** — 15 mentions
- **orthogonal** — 6 mentions
- **metric** — 5 mentions
- **similar** — 4 mentions
- **orthogonality** — 4 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=82|mml-book.pdf p. 82]]

## Liens
- Up: [[research/mml-book/3-analytic-geometry]]
- ← Prev: [[research/mml-book/3-3-lengths-and-distances]]
- Next: [[research/mml-book/3-5-orthonormal-basis]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
