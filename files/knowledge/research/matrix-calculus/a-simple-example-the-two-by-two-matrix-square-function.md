---
title: "A simple example: The two-by-two matrix-square function"
summary: "§Jacobians of Matrix Functions › A simple example: The two-by: f ′(A)[X + Y ] = (X + Y )A + A(X + Y ) = XA + Y A + AX + AY = XA + AX + Y A + AY = f ′(A)[X] + f ′(A)[Y ] . This is a perfectly good way to define a linear operation!"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "21-22"
---

# A simple example: The two-by-two matrix-square function

§Jacobians of Matrix Functions › A simple example: The two-by-two matrix-square function · pp. 21–22 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
f ′(A)[X + Y ] = (X + Y )A + A(X + Y ) = XA + Y A + AX + AY = XA + AX + Y A + AY = f ′(A)[X] + f ′(A)[Y ] . This is a perfectly good way to define a linear operation! We are not expressing it here in the familiar form f ′(A)[X] = (some matrix?) × (X vector?), and that’s okay! A formula like XA + AX is easy to write down, easy to understand, and easy to compute with. But sometimes you still may want to think of f ′ as a single “Jacobian” matrix, using the most familiar language of linear algebra, and it is possible to do that! If you took a sufficiently abstract linear-algebra course, you may have learned that any linear operator can be represented by a matrix once you choose a basis for the input and output vector spaces. Here, however, we will be much more concrete, because there is a conventional “Cartesian” basis for matrices A called “vectorization”, and in this basis linear operators like AX + XA are particularly easy to represent in matrix form once we introduce a new type of matrix product that has widespread applications in “multidimensional” linear algebra. To begin with, let’s look in more detail at our matrix-square function f(A) = A2 for the simple case of 2 × 2 matrices, which are described by only four scalars, so that we can look at every term in the derivative explicitly.

## Key terms
- **matrix** — 14 mentions
- **vector** — 8 mentions
- **function** — 7 mentions
- **column** — 7 mentions
- **linear** — 5 mentions
- **basis** — 5 mentions
- **vectorization** — 5 mentions
- **easy** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=21|Matrix Calculus.pdf p. 21]]

## Liens
- Up: [[research/matrix-calculus/jacobians-of-matrix-functions]]
- ← Prev: [[research/matrix-calculus/derivatives-of-matrix-functions-linear-operators]]
- Next: [[research/matrix-calculus/kronecker-products]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
