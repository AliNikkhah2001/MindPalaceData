---
title: "Finite-Difference Approximations"
summary: "§Finite-Difference Approximations: In this section, we will be referring to this Julia notebook for calculations that are not included here. Working out derivatives by hand is a notoriously error-prone procedure for complicated functions."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "29-33"
---

# Finite-Difference Approximations

§Finite-Difference Approximations · pp. 29–33 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
In this section, we will be referring to this Julia notebook for calculations that are not included here. Working out derivatives by hand is a notoriously error-prone procedure for complicated functions. Even if every individual step is straightforward, there are so many opportunities to make a mistake, either in the derivation or in its implementation on a computer. Whenever you implement a derivatives, you should always double- check for mistakes by comparing it to an independent calculation. The simplest such check is a finite-difference approximation, in which we estimate the derivative(s) by comparing f(x) and f(x + δx) for one or more “finite” (non-infinitesimal) perturbations δx. There are many finite-difference techniques at varying levels of sophistication, as we will discuss below. They all incur an intrinsic truncation error due to the fact that δx is not infinitesimal. (And we will also see that you can’t make δx too small, either, or roundoff errors start exploding!) Moreover, finite differences become expensive for higher-dimensional x (in which you need a separate finite difference for each input dimension to compute the full Jacobian). This makes them an approach of last resort for computing derivatives accurately.

## Key terms
- **error** — 26 mentions
- **approximation** — 18 mentions
- **derivative** — 18 mentions
- **difference** — 17 mentions
- **small** — 13 mentions
- **finite-difference** — 12 mentions
- **relative** — 11 mentions
- **check** — 8 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=29|Matrix Calculus.pdf p. 29]]

## Liens
- ← Prev: [[research/matrix-calculus/jacobians-of-matrix-functions]]
- Next: [[research/matrix-calculus/derivatives-in-general-vector-spaces]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
