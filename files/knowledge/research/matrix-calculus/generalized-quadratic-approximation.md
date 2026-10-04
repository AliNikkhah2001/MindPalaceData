---
title: "Generalized quadratic approximation"
summary: "§Second Derivatives, Bilinear Maps, and Hessian Matrices › Ge: Express f ′′(A) as a rule for f ′′(A)[dA, dA′] in terms of dA and dA′. From lecture 3, we have the first derivative f ′(A)[dA] = df = det(A) tr(A−1dA)."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "92-92"
---

# Generalized quadratic approximation

§Second Derivatives, Bilinear Maps, and Hessian Matrices › Generalized quadratic approximation · pp. 92–92 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Example 59 Let f(A) = det A for A an n × n matrix. Express f ′′(A) as a rule for f ′′(A)[dA, dA′] in terms of dA and dA′. From lecture 3, we have the first derivative f ′(A)[dA] = df = det(A) tr(A−1dA). Now, we want to compute the change d′(df) = d′(f ′(A)[dA]) = f ′(A+dA′)[dA]−f ′(A)[dA] in this formula, i.e. the differential (denoted d′) where we change A by dA′ while treating dA as a constant: f ′′(A)[dA, dA′] = d′(det A tr(A−1dA)) = det A tr(A−1dA′) tr(A−1dA) −det A tr(A−1 dA′A−1 dA) = f ′′(A)[dA′, dA] where the last line (symmetry) can be derived explicitly by the cyclic property of the trace (although of course it must be true for any f ′′). Although f ′′ here is a perfectly good bilinear form acting on matrices dA, dA′, it is not very natural to express f ′′ as a “Hessian matrix.” If we really wanted to express f ′′ in terms of an explicit Hessian matrix, we could use the the “vectorization” approach of Sec. 3. Let us consider, for example, the term tr(A−1 dA′A−1 dA) using Kronecker products (Sec. 3). In general, for matrices X, Y, B, C: (vec X)T (B ⊗C) vec Y = (vec X)T vec (CY BT ) = tr(XT CY BT ) = tr(BT XT CY ) , recalling that (vec X)T vec Y = tr(XT Y ) is the Frobenius inner product (Sec.

## Key terms
- **matrix** — 6 mentions
- **hessian** — 5 mentions
- **express** — 3 mentions
- **form** — 3 mentions
- **matrices** — 3 mentions
- **term** — 3 mentions
- **product** — 3 mentions
- **approximation** — 3 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=92|Matrix Calculus.pdf p. 92]]

## Liens
- Up: [[research/matrix-calculus/second-derivatives-bilinear-maps-and-hessian-matrices]]
- ← Prev: [[research/matrix-calculus/general-second-derivatives-bilinear-maps]]
- Next: [[research/matrix-calculus/hessians-and-optimization]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
