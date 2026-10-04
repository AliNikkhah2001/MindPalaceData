---
title: "Dual numbers"
summary: "§Forward and Reverse-Mode Automatic Differentiation › Automat: Essentially, however, this is the same as our little D implementation, but implemented with greater generality and sophistication (e.g."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "53-53"
---

# Dual numbers

§Forward and Reverse-Mode Automatic Differentiation › Automatic Differentiation via Dual Numbers › Dual numbers · pp. 53–53 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Essentially, however, this is the same as our little D implementation, but implemented with greater generality and sophistication (e.g. chain rules for more operations, support for more numeric types, partial derivatives with respect to multiple variables, etc.): just as we did, ForwardDiff augments every value with a second number that tracks the derivative, and propagates both quantities through the calculation. We could have also implemented the same idea specifically for the Bablylonian algorithm, by writing a new function dBabylonian that tracks both the variable t and its derivative t′ = dt/dx through the course of the calculation: julia> function dBabylonian(x; N = 10) t = (1+x)/2 t′ = 1/2 for i = 1:N t = (t+x/t)/2 t′= (t′+(t-x*t′)/t^2)/2 end return t′ end julia> dBabylonian(49) 0.07142857142857142 This is doing exactly the same calculations as calling Babylonian(D(x,1)) or ForwardDiff.derivative(Babylonian, 49), but needs a lot more human effort-we’d have to do this for every computer program we write, rather than implementing a new number type once. There is a pleasing algebraic way to think about our new number type D(a, b) instead of the “value & derivative” viewpoint above.

## Key terms
- **rule** — 9 mentions
- **number** — 8 mentions
- **derivative** — 5 mentions
- **julia** — 5 mentions
- **deriv** — 5 mentions
- **type** — 4 mentions
- **implemented** — 3 mentions
- **calculation** — 3 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=53|Matrix Calculus.pdf p. 53]]

## Liens
- Up: [[research/matrix-calculus/automatic-differentiation-via-dual-numbers]]
- ← Prev: [[research/matrix-calculus/easy-forward-mode-ad]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
