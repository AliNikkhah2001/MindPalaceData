---
title: "Linear operators"
summary: "§Derivatives as Linear Operators › Linear operators: In differential notation, we can express the same idea as: df = f(x + dx) −f(x) = f ′(x) dx. In this notation we implicitly drop the o(δx) term that vanishes in the limit as δx becomes infinitesimally small."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "10-11"
---

# Linear operators

§Derivatives as Linear Operators › Linear operators · pp. 10–11 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
and other vector spaces. In differential notation, we can express the same idea as: df = f(x + dx) −f(x) = f ′(x) dx. In this notation we implicitly drop the o(δx) term that vanishes in the limit as δx becomes infinitesimally small. We will use this as the more generalized definition of a derivative. In this formulation, we avoid dividing by dx, because soon we will allow x (and hence dx) to be something other than a number-if dx is a vector, we won’t be able to divide by it! From the perspective of linear algebra, given a function f, we consider the derivative of f, to be the linear operator f ′(x) such that df = f(x + dx) −f(x) = f ′(x)[dx]. As above, you should think of the differential notation dx as representing an arbitrary small change in x, where we are implicitly dropping any o(dx) terms, i.e. terms that decay faster than linearly as dx →0. Often, we will omit the square brackets and write simply f ′(x)dx instead of f ′(x)[dx], but this should be understood as the linear operator f ′(x) acting on dx-don’t write dx f ′(x), which will generally be nonsense! This definition will allow us to extend differentiation to arbitrary vector spaces of inputs x and outputs f(x). (More technically, we will require vector spaces with a norm ∥x∥, called “Banach spaces,” in order to precisely define the o(δx) terms that are dropped.

## Key terms
- **vector** — 21 mentions
- **space** — 17 mentions
- **linear** — 15 mentions
- **operator** — 13 mentions
- **derivative** — 11 mentions
- **change** — 11 mentions
- **small** — 10 mentions
- **notation** — 9 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=10|Matrix Calculus.pdf p. 10]]

## Liens
- Up: [[research/matrix-calculus/derivatives-as-linear-operators]]
- ← Prev: [[research/matrix-calculus/revisiting-single-variable-calculus]]
- Next: [[research/matrix-calculus/revisiting-multivariable-calculus-part-1-scalar-valued-functions]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
