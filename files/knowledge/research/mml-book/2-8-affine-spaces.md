---
title: "2.8 Affine Spaces"
summary: "§Part I Mathematical Foundations › 2 Linear Algebra › 2.8 Aff: 2.8 Affine Spaces In the following, we will take a closer look at spaces that are offset from the origin, i.e., spaces that are no longer vector subspaces."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "67-68"
---

# 2.8 Affine Spaces

§Part I Mathematical Foundations › 2 Linear Algebra › 2.8 Affine Spaces · pp. 67–68 · Mathematics for Machine Learning (MML Book)

## Extrait
2.8 Affine Spaces In the following, we will take a closer look at spaces that are offset from the origin, i.e., spaces that are no longer vector subspaces. Moreover, we will briefly discuss properties of mappings between these affine spaces, which resemble linear mappings. Remark. In the machine learning literature, the distinction between linear and affine is sometimes not clear so that we can find references to affine spaces/mappings as linear spaces/mappings. ♢ 2.8.1 Affine Subspaces Definition 2.25 (Affine Subspace). Let V be a vector space, x0 ∈V and U ⊆V a subspace. Then the subset L = x0 + U := {x0 + u : u ∈U} (2.130a) = {v ∈V |∃u ∈U : v = x0 + u} ⊆V (2.130b) is called affine subspace or linear manifold of V . U is called direction or affine subspace linear manifold direction direction space, and x0 is called support point. In Chapter 12, we refer to direction space support point such a subspace as a hyperplane. hyperplane Note that the definition of an affine subspace excludes 0 if x0 /∈U. Therefore, an affine subspace is not a (linear) subspace (vector subspace) of V for x0 /∈U. Examples of affine subspaces are points, lines, and planes in R3, which do not (necessarily) go through the origin.

## Key terms
- **affine** — 30 mentions
- **subspace** — 26 mentions
- **linear** — 17 mentions
- **space** — 17 mentions
- **mapping** — 13 mentions
- **vector** — 12 mentions
- **direction** — 8 mentions
- **point** — 8 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=67|mml-book.pdf p. 67]]

## Liens
- Up: [[research/mml-book/2-linear-algebra]]
- ← Prev: [[research/mml-book/2-7-linear-mappings]]
- Next: [[research/mml-book/2-9-further-reading]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
