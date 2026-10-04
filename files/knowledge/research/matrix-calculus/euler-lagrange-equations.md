---
title: "Euler–Lagrange equations"
summary: "§Calculus of Variations › Euler–Lagrange equations: a u that minimizes the functional f (the shortest curve), we must have the following result: 0 = ∇f = −  u′ √ 1 + u′2 ′ = − u′′√ 1 + u′2 −u′ u′′u′ √ 1+u′2 1 + u′2 = −u′′(1 + u′2) −u′′u′2 (1 + u′2)3/2 = − u′′ (1 + u′2)3/2 ."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "77-78"
---

# Euler–Lagrange equations

§Calculus of Variations › Euler–Lagrange equations · pp. 77–78 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
a u that minimizes the functional f (the shortest curve), we must have the following result: 0 = ∇f = −  u′ √ 1 + u′2 ′ = − u′′√ 1 + u′2 −u′ u′′u′ √ 1+u′2 1 + u′2 = −u′′(1 + u′2) −u′′u′2 (1 + u′2)3/2 = − u′′ (1 + u′2)3/2 . Hence, ∇f = 0 =⇒u′′(x) = 0 =⇒u(x) = ax + b for constants a, b; and for these boundary conditions a = b = 0. In other words, u is the horizontal straight line segment! Thus, we have recovered the familiar result that straight line segments in R2 are the shortest curves between two points! Remark 47. Notice that the expression u′′ (1+u′2)3/2 is the formula from multivariable calculus for the curvature of the curve defined by y = u(x). It is not a coincidence that the gradient of arc length is the (negative) curvature, and the minimum arc length occurs for zero gradient = zero curvature. This style of calculation is part of the subject known as the calculus of variations. Of course, the final answer in the example above (a straight line) may have been obvious, but a similar approach can be applied to many more interesting problems. We can generalize the approach as follows: Example 48 Let f(u) = R b a F(u, u′, x) dx where u is a differentiable function on [a, b]. Suppose the endpoints of u are fixed (i.e.

## Key terms
- **curve** — 4 mentions
- **calculus** — 4 mentions
- **straight** — 3 mentions
- **line** — 3 mentions
- **curvature** — 3 mentions
- **zero** — 3 mentions
- **fixed** — 3 mentions
- **minimizes** — 2 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=77|Matrix Calculus.pdf p. 77]]

## Liens
- Up: [[research/matrix-calculus/calculus-of-variations]]
- ← Prev: [[research/matrix-calculus/example-minimizing-arc-length]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
