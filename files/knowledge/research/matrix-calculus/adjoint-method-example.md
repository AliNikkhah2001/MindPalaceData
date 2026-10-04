---
title: "Adjoint-method example"
summary: "§Nonlinear Root-Finding, Optimization, and Adjoint Differenti: You can also apply adjoint/reverse differentiation to nonlinear equations. For instance, consider the gradient of the scalar function g(p) = f(x(p)), where x(p) ∈Rn solves some system of n equations h(p, x) = 0 ∈Rn."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "44-46"
---

# Adjoint-method example

§Nonlinear Root-Finding, Optimization, and Adjoint Differentiation › Reverse-mode ``Adjoint'' Differentiation › Adjoint-method example · pp. 44–46 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
You can also apply adjoint/reverse differentiation to nonlinear equations. For instance, consider the gradient of the scalar function g(p) = f(x(p)), where x(p) ∈Rn solves some system of n equations h(p, x) = 0 ∈Rn. By the chain rule, h(p, x) = 0 =⇒∂h ∂p dp + ∂h ∂xdx = 0 =⇒dx = − ∂h ∂x −1 ∂h ∂p dp . (This is an instance of the Implicit Function Theorem: as long as ∂h ∂x is nonsingular, we can locally define a function x(p) from an implicit equation h = 0, here by linearization.) Hence, dg = f ′(x)dx = −f ′(x) ∂h ∂x −1 | {z } vT ∂h ∂p dp . Associating left-to-right again leads to a single “adjoint” equation: (∂h/∂x)T v = f ′(x)T = ∇xf. In other words, it again only takes two solves to get both g and ∇g-one nonlinear “forward” solve for x and one linear “adjoint” solve for v! Thereafter, all derivatives ∂g/∂pk are cheap dot products. (Note that the linear “adjoint” solve involves the transposed Jacobian ∂h/∂x. Except for the transpose, this is very similar to the cost of a single Newton step to solve h = 0 for x. So the adjoint problem should be cheaper than the forward problem.) If you use automatic differentiation (AD) systems, why do you need to learn this stuff? Doesn’t the AD do everything for you?

## Key terms
- **solve** — 14 mentions
- **adjoint** — 9 mentions
- **problem** — 8 mentions
- **solution** — 6 mentions
- **tridiagonal** — 6 mentions
- **differentiation** — 5 mentions
- **function** — 5 mentions
- **matrix** — 5 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=44|Matrix Calculus.pdf p. 44]]

## Liens
- Up: [[research/matrix-calculus/reverse-mode-adjoint-differentiation]]
- ← Prev: [[research/matrix-calculus/adjoint-methods-and-ad]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
