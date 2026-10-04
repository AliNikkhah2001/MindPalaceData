---
title: "Minima, maxima, and saddle points"
summary: "§Second Derivatives, Bilinear Maps, and Hessian Matrices › He: When using automatic differentiation (AD), Hessians are often computed by a combination of forward and reverse modes (Sec."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "94-94"
---

# Minima, maxima, and saddle points

§Second Derivatives, Bilinear Maps, and Hessian Matrices › Hessians and optimization › Minima, maxima, and saddle points · pp. 94–94 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
less computing it. When using automatic differentiation (AD), Hessians are often computed by a combination of forward and reverse modes (Sec. 8.4.1), but AD does not circumvent the fundamental scaling difficulty for large n. Instead of computing H explicitly, however, one can instead approximate the Hessian in various ways; in the context of optimization, approximate Hessians are found in “quasi-Newton” methods such as the famous “BFGS” algorithm and its variants. One can also derive efficient methods to compute Hessian-vector products Hv without computing H explicitly, e.g. for use in Newton-Krylov methods. (Such a product Hv is equivalent to a directional derivative of f ′, which is efficiently computed by “forward-over-reverse” AD as in Sec. 8.4.1.) Generalizing the rules you may recall from single- and multi-variable calculus, we can use the second derivative to determine whether an extremum is a minimum, maximum, or saddle point. Firstly, an extremum of a scalar function f is a point x0 such that f ′(x0) = 0. That is, f ′(x0)[δx] = 0 for any δx. Equivalently, ∇f x0 = f ′(x0)T = 0. Using our quadratic approximation around x0, we then have that f(x0 + δx) = f(x0) + f ′(x0)[δx] | {z } =0 +1 2f ′′(x0)[δx, δx] + o(∥δx∥2).

## Key terms
- **eigenvalues** — 9 mentions
- **point** — 6 mentions
- **hessian** — 5 mentions
- **computing** — 4 mentions
- **methods** — 4 mentions
- **minimum** — 4 mentions
- **positive-definite** — 4 mentions
- **check** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=94|Matrix Calculus.pdf p. 94]]

## Liens
- Up: [[research/matrix-calculus/hessians-and-optimization]]
- ← Prev: [[research/matrix-calculus/computing-hessians]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
