---
title: "Example: Matrix squaring"
summary: "§Finite-Difference Approximations › Example: Matrix squaring: The distinction becomes more important when discretizing (approximating) differential equations. We’ll look at other possibilities below."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "30-30"
---

# Example: Matrix squaring

§Finite-Difference Approximations › Example: Matrix squaring · pp. 30–30 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
The distinction becomes more important when discretizing (approximating) differential equations. We’ll look at other possibilities below. Remark 29. Note that this definition of forward and backward difference is not the same as forward- and backward- mode differentiation-these are unrelated concepts. If x is a scalar, we can also divide both sides by δx to get an approximation for f ′(x) instead of for df: f ′(x) ≈f(x + δx) −f(x) δx + (higher-order corrections) . This is a more common way to write the forward-difference approximation, but it only works for scalar x, whereas in this class we want to think of x as perhaps belonging to some other vector space. Finite-difference approximations come in many forms, but they are generally a last resort in cases where it’s too much effort to work out an analytical derivative and AD fails. But they are also useful to check your analytical derivatives and to quickly explore. Let’s try the finite-difference approximation for the square function f(A) = A2, where here A is a square matrix in Rm,m. By hand, we obtain the product rule df = A dA + dA A, i.e. f ′(A) is the linear operator f ′(A)[δA] = A δA + δA A. This is not equal to 2A δA because in general A and δA do not commute.

## Key terms
- **approximation** — 8 mentions
- **exact** — 7 mentions
- **answer** — 6 mentions
- **error** — 6 mentions
- **random** — 5 mentions
- **small** — 5 mentions
- **difference** — 4 mentions
- **relative** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=30|Matrix Calculus.pdf p. 30]]

## Liens
- Up: [[research/matrix-calculus/finite-difference-approximations]]
- ← Prev: [[research/matrix-calculus/finite-difference-approximations-easy-version]]
- Next: [[research/matrix-calculus/accuracy-of-finite-differences]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
