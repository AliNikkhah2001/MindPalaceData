---
title: "2.5 Linear Independence"
summary: "§Part I Mathematical Foundations › 2 Linear Algebra › 2.5 Lin: Every subspace U ⊆(Rn, +, ·) is the solution space of a homogeneous system of linear equations Ax = 0 for x ∈Rn. ♢ In the following, we will have a close look at what we can do with vectors (elements of the vector spa"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "46-49"
---

# 2.5 Linear Independence

§Part I Mathematical Foundations › 2 Linear Algebra › 2.5 Linear Independence · pp. 46–49 · Mathematics for Machine Learning (MML Book)

## Extrait
Linear Algebra Remark. Every subspace U ⊆(Rn, +, ·) is the solution space of a homogeneous system of linear equations Ax = 0 for x ∈Rn. ♢ In the following, we will have a close look at what we can do with vectors (elements of the vector space). In particular, we can add vectors together and multiply them with scalars. The closure property guarantees that we end up with another vector in the same vector space. It is possible to find a set of vectors with which we can represent every vector in the vector space by adding them together and scaling them. This set of vectors is a basis, and we will discuss them in Section 2.6.1. Before we get there, we will need to introduce the concepts of linear combinations and linear independence. Definition 2.11 (Linear Combination). Consider a vector space V and a finite number of vectors x1, . . . , xk ∈V . Then, every v ∈V of the form v = λ1x1 + · · · + λkxk = k X i=1 λixi ∈V (2.65) with λ1, . . . , λk ∈R is a linear combination of the vectors x1, . . . , xk. linear combination The 0-vector can always be written as the linear combination of k vectors x1, . . . , xk because 0 = Pk i=1 0xi is always true. In the following, we are interested in non-trivial linear combinations of a set of vectors to represent 0, i.e., linear combinations of vectors x1, .

## Key terms
- **vector** — 57 mentions
- **linearly** — 30 mentions
- **linear** — 23 mentions
- **column** — 21 mentions
- **independent** — 16 mentions
- **combination** — 13 mentions
- **dependent** — 12 mentions
- **space** — 10 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=46|mml-book.pdf p. 46]]

## Liens
- Up: [[research/mml-book/2-linear-algebra]]
- ← Prev: [[research/mml-book/2-4-vector-spaces]]
- Next: [[research/mml-book/2-6-basis-and-rank]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
