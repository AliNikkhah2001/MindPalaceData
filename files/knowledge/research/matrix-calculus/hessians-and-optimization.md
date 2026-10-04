---
title: "Hessians and optimization"
summary: "§Second Derivatives, Bilinear Maps, and Hessian Matrices › He: and check that the right-hand side reproduces f ′′(x). (Note how dx and dx′ appear symmetrically in this formula, which reflects the symmetry of f ′′.) Many important applications of second derivatives, Hessians, and "
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "93-94"
---

# Hessians and optimization

§Second Derivatives, Bilinear Maps, and Hessian Matrices › Hessians and optimization · pp. 93–94 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
and check that the right-hand side reproduces f ′′(x). (Note how dx and dx′ appear symmetrically in this formula, which reflects the symmetry of f ′′.) Many important applications of second derivatives, Hessians, and quadratic approximations arise in optimization: minimization (or maximization) of functions f(x).16 When searching for a local minimum (or maximum) of a complicated function f(x), a common procedure is to approximate f(x + δx) by a simpler “model” function for small δx, and then to optimize this model to obtain a potential optimization step. For example, approximating f(x+δx) ≈f(x)+f ′(x)[δx] (an affine model, colloquially called “linear”) leads to gradient descent and related algorithms. A better approximation for f(x + δx) will often lead to faster-converging algorithms, and so a natural idea is to exploit the second derivative f ′′ to make a quadratic model, as above, and accelerate optimization. For unconstrained optimization, minimizing f(x) corresponds to finding a root of the derivative f ′ = 0 (i.e., ∇f = 0), and a quadratic approximation for f yields a first-order (affine) approximation f ′(x + δx) ≈f ′(x) + f ′′(x)[δx] for the derivative f ′. In Rn, this is δ(∇f) ≈Hδx.

## Key terms
- **optimization** — 13 mentions
- **quadratic** — 12 mentions
- **hessian** — 10 mentions
- **eigenvalues** — 9 mentions
- **model** — 8 mentions
- **approximation** — 8 mentions
- **derivative** — 8 mentions
- **algorithm** — 8 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=93|Matrix Calculus.pdf p. 93]]

## Liens
- Up: [[research/matrix-calculus/second-derivatives-bilinear-maps-and-hessian-matrices]]
- ← Prev: [[research/matrix-calculus/generalized-quadratic-approximation]]
- Next: [[research/matrix-calculus/further-reading-2]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
