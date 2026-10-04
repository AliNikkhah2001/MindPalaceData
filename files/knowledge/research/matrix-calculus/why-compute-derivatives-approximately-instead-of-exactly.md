---
title: "Why compute derivatives approximately instead of exactly?"
summary: "§Finite-Difference Approximations › Why compute derivatives a: In this section, we will be referring to this Julia notebook for calculations that are not included here. Working out derivatives by hand is a notoriously error-prone procedure for complicated functions."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "29-29"
---

# Why compute derivatives approximately instead of exactly?

§Finite-Difference Approximations › Why compute derivatives approximately instead of exactly? · pp. 29–29 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
In this section, we will be referring to this Julia notebook for calculations that are not included here. Working out derivatives by hand is a notoriously error-prone procedure for complicated functions. Even if every individual step is straightforward, there are so many opportunities to make a mistake, either in the derivation or in its implementation on a computer. Whenever you implement a derivatives, you should always double- check for mistakes by comparing it to an independent calculation. The simplest such check is a finite-difference approximation, in which we estimate the derivative(s) by comparing f(x) and f(x + δx) for one or more “finite” (non-infinitesimal) perturbations δx. There are many finite-difference techniques at varying levels of sophistication, as we will discuss below. They all incur an intrinsic truncation error due to the fact that δx is not infinitesimal. (And we will also see that you can’t make δx too small, either, or roundoff errors start exploding!) Moreover, finite differences become expensive for higher-dimensional x (in which you need a separate finite difference for each input dimension to compute the full Jacobian). This makes them an approach of last resort for computing derivatives accurately.

## Key terms
- **derivative** — 12 mentions
- **difference** — 8 mentions
- **there** — 5 mentions
- **check** — 5 mentions
- **finite-difference** — 5 mentions
- **approximation** — 5 mentions
- **finite** — 5 mentions
- **small** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=29|Matrix Calculus.pdf p. 29]]

## Liens
- Up: [[research/matrix-calculus/finite-difference-approximations]]
- Next: [[research/matrix-calculus/finite-difference-approximations-easy-version]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
