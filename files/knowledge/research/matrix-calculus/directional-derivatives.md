---
title: "Directional derivatives"
summary: "§Derivatives as Linear Operators › Linear operators › Directi: Some examples of linear operators include • Multiplication by scalars α, i.e. Also multiplication of column vectors v by matrices A, i.e."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "12-12"
---

# Directional derivatives

§Derivatives as Linear Operators › Linear operators › Directional derivatives · pp. 12–12 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Some examples of linear operators include • Multiplication by scalars α, i.e. Lv = αv. Also multiplication of column vectors v by matrices A, i.e. Lv = Av. • Some functions like f(x) = x2 are obviously nonlinear. But what about f(x) = x + 1? This may look linear if you plot it, but it is not a linear operation, because f(2x) = 2x + 1̸ = 2f(x)-such functions, which are linear plus a nonzero constant, are known as affine. • There are also many other examples of linear operations that are not so convenient or easy to write down as matrix-vector products. For example, if A is a 3 × 3 matrix, then L[A] = AB + CA is a linear operator given 3 × 3 matrices B, C. The transpose f(x) = xT of a column vector x is linear, but is not given by any matrix multiplied by x. Or, if we consider vector spaces of functions, then the calculus operations of differentiation and integration are linear operators too! There is an equivalent way to interpret this linear-operator viewpoint of a derivative, which you may have seen before in multivariable calculus: as a directional derivative. If we have a function f(x) of arbitrary vectors x, then the directional derivative at x in a direction (vector) v is defined as: ∂ ∂αf(x + αv) α=0 = lim δα→0 f(x + δα v) −f(x) δα (1) where α is a scalar.

## Key terms
- **linear** — 12 mentions
- **vector** — 12 mentions
- **operator** — 6 mentions
- **derivative** — 6 mentions
- **scalar** — 6 mentions
- **function** — 5 mentions
- **arbitrary** — 5 mentions
- **column** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=12|Matrix Calculus.pdf p. 12]]

## Liens
- Up: [[research/matrix-calculus/linear-operators]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
