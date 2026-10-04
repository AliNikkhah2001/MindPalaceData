---
title: "Forward and Reverse-Mode Automatic Differentiation"
summary: "§Forward and Reverse-Mode Automatic Differentiation: The first time that Professor Edelman had heard about automatic differentiation (AD), it was easy for him to imagine what it was ."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "50-64"
---

# Forward and Reverse-Mode Automatic Differentiation

§Forward and Reverse-Mode Automatic Differentiation · pp. 50–64 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
The first time that Professor Edelman had heard about automatic differentiation (AD), it was easy for him to imagine what it was . . . but what he imagined was wrong! In his head, he thought it was straightforward symbolic differentiation applied to code-sort of like executing Mathematica or Maple, or even just automatically doing what he learned to do in his calculus class. For instance, just plugging in functions and their domains from something like the following first-year calculus table: Derivative Domain (sin x)′ = cos x −∞< x < ∞ (cos x)′ = −sin x −∞< x < ∞ (tan x)′ = sec2 x x̸ = π 2 + πn, n ∈Z (cot x)′ = −csc2 x x̸ = πn, n ∈Z (sec x)′ = tan x sec x x̸ = π 2 + πn, n ∈Z (csc x)′ = −cot x csc x x̸ = πn, n ∈Z And in any case, if it wasn’t just like executing Mathematica or Maple, then it must be finite differences, like one learns in a numerical computing class (or as we did in Sec. 4). It turns out that it is definitely not finite differences-AD algorithms are generally exact (in exact arithmetic, neglecting roundoff errors), not approximate. But it also doesn’t look much like conventional symbolic algebra: the computer doesn’t really construct a big “unrolled” symbolic expression and then differentiate it, the way you might imagine doing by hand or via computer-algebra software.

## Key terms
- **derivative** — 26 mentions
- **julia** — 26 mentions
- **rule** — 20 mentions
- **value** — 18 mentions
- **number** — 17 mentions
- **babylonian** — 15 mentions
- **deriv** — 12 mentions
- **type** — 10 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=50|Matrix Calculus.pdf p. 50]]

## Liens
- ← Prev: [[research/matrix-calculus/derivative-of-matrix-determinant-and-inverse]]
- Next: [[research/matrix-calculus/differentiating-ode-solutions]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
