---
title: "Further Reading"
summary: "§Second Derivatives, Bilinear Maps, and Hessian Matrices › Fu: All of this formalism about “bilinear forms” and so forth may seem like a foray into abstraction for the sake of abstraction."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "95-95"
---

# Further Reading

§Second Derivatives, Bilinear Maps, and Hessian Matrices › Further Reading · pp. 95–95 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
All of this formalism about “bilinear forms” and so forth may seem like a foray into abstraction for the sake of abstraction. Can’t we always reduce things to ordinary matrices by choosing a basis (“vectorizing” our inputs and outputs)? However, we often don’t want to do this for the same reason that we often prefer to express first derivatives as linear operators rather than as explicit Jacobian matrices. Writing linear or bilinear operators as explicit matrices, e.g. vec(A dA + dA A) = (I ⊗A + AT ⊗I) vec(dA) as in Sec. 3, often disguises the underlying structure of the operator and introduces a lot of algebraic complexity for no purpose, as well as being potentially computationally costly (e.g. exchanging small matrices A for large ones I ⊗A). As we discussed in this chapter, an important generalization of quadratic operations to arbitrary vector spaces come in the form of bilinear maps and bilinear forms, and there are many textbooks and other sources discussing these ideas and variations thereof. For example, we saw that the second derivative can be seen as a symmetric bilinear form. This is closely related to a quadratic form Q[x], which what we get by plugging the same vector twice into a symmetric bilinear form B[x, y] = B[y, x], i.e.

## Key terms
- **form** — 9 mentions
- **quadratic** — 8 mentions
- **hessian** — 7 mentions
- **bilinear** — 6 mentions
- **derivative** — 6 mentions
- **matrices** — 5 mentions
- **normal** — 5 mentions
- **operator** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=95|Matrix Calculus.pdf p. 95]]

## Liens
- Up: [[research/matrix-calculus/second-derivatives-bilinear-maps-and-hessian-matrices]]
- ← Prev: [[research/matrix-calculus/hessians-and-optimization]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
