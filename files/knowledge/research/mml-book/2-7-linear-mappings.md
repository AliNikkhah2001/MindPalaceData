---
title: "2.7 Linear Mappings"
summary: "§Part I Mathematical Foundations › 2 Linear Algebra › 2.7 Lin: We use Gaussian elimination to determine the rank:   −2 −3   ⇝· · · ⇝    . (2.84) Here, we see that the number of linearly independent rows and columns is 2, such that rk(A) = 2."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "54-66"
---

# 2.7 Linear Mappings

§Part I Mathematical Foundations › 2 Linear Algebra › 2.7 Linear Mappings · pp. 54–66 · Mathematics for Machine Learning (MML Book)

## Extrait
Linear Algebra A =   −2 −3  . We use Gaussian elimination to determine the rank:   −2 −3   ⇝· · · ⇝    . (2.84) Here, we see that the number of linearly independent rows and columns is 2, such that rk(A) = 2. In the following, we will study mappings on vector spaces that preserve their structure, which will allow us to define the concept of a coordinate. In the beginning of the chapter, we said that vectors are objects that can be added together and multiplied by a scalar, and the resulting object is still a vector. We wish to preserve this property when applying the mapping: Consider two real vector spaces V, W. A mapping Φ : V →W preserves the structure of the vector space if Φ(x + y) = Φ(x) + Φ(y) (2.85) Φ(λx) = λΦ(x) (2.86) for all x, y ∈V and λ ∈R. We can summarize this in the following definition: Definition 2.15 (Linear Mapping). For vector spaces V, W, a mapping Φ : V →W is called a linear mapping (or vector space homomorphism/ linear mapping vector space homomorphism linear transformation) if linear transformation ∀x, y ∈V ∀λ, ψ ∈R : Φ(λx + ψy) = λΦ(x) + ψΦ(y) . (2.87) It turns out that we can represent linear mappings as matrices (Section 2.7.1). Recall that we can also collect a set of vectors as columns of a matrix.

## Key terms
- **vector** — 41 mentions
- **mapping** — 30 mentions
- **linear** — 29 mentions
- **basis** — 22 mentions
- **coordinate** — 21 mentions
- **space** — 20 mentions
- **representation** — 10 mentions
- **ordered** — 10 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=54|mml-book.pdf p. 54]]

## Liens
- Up: [[research/mml-book/2-linear-algebra]]
- ← Prev: [[research/mml-book/2-6-basis-and-rank]]
- Next: [[research/mml-book/2-8-affine-spaces]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
