---
title: "3.10 Further Reading"
summary: "§Part I Mathematical Foundations › 3 Analytic Geometry › 3.10: trix Rij(θ) :=   Ii−1 · · · · · · cos θ −sin θ Ij−i−1 sin θ cos θ · · · · · · In−j   ∈Rn×n , (3.80) for 1 ⩽i < j ⩽n and θ ∈R."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "100-101"
---

# 3.10 Further Reading

§Part I Mathematical Foundations › 3 Analytic Geometry › 3.10 Further Reading · pp. 100–101 · Mathematics for Machine Learning (MML Book)

## Extrait
trix Rij(θ) :=   Ii−1 · · · · · · cos θ −sin θ Ij−i−1 sin θ cos θ · · · · · · In−j   ∈Rn×n , (3.80) for 1 ⩽i < j ⩽n and θ ∈R. Then Rij(θ) is called a Givens rotation. Givens rotation Essentially, Rij(θ) is the identity matrix In with rii = cos θ , rij = −sin θ , rji = sin θ , rjj = cos θ . (3.81) In two dimensions (i.e., n = 2), we obtain (3.76) as a special case. 3.9.4 Properties of Rotations Rotations exhibit a number of useful properties, which can be derived by considering them as orthogonal matrices (Definition 3.8): Rotations preserve distances, i.e., ∥x−y∥= ∥Rθ(x)−Rθ(y)∥. In other words, rotations leave the distance between any two points unchanged after the transformation. Rotations preserve angles, i.e., the angle between Rθx and Rθy equals the angle between x and y. Rotations in three (or more) dimensions are generally not commutative. Therefore, the order in which rotations are applied is important, even if they rotate about the same point. Only in two dimensions vector rotations are commutative, such that R(ϕ)R(θ) = R(θ)R(ϕ) for all ϕ, θ ∈[0, 2π). They form an Abelian group (with multiplication) only if they rotate about the same point (e.g., the origin). In this chapter, we gave a brief overview of some of the important concepts of analytic geometry, which we will use in later chapters of the book.

## Key terms
- **rotation** — 10 mentions
- **orthogonal** — 6 mentions
- **method** — 6 mentions
- **linear** — 5 mentions
- **kernel** — 5 mentions
- **important** — 4 mentions
- **point** — 4 mentions
- **inner** — 4 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=100|mml-book.pdf p. 100]]

## Liens
- Up: [[research/mml-book/3-analytic-geometry]]
- ← Prev: [[research/mml-book/3-9-rotations]]
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
