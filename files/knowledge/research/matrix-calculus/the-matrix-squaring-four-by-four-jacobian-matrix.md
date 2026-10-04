---
title: "The matrix-squaring four-by-four Jacobian matrix"
summary: "§Jacobians of Matrix Functions › A simple example: The two-by: that the primary way to study matrix functions like this should be to view them as having matrix inputs (A) and matrix outputs (A2), and that one should likewise generally view the derivatives as linear operators on m"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "23-23"
---

# The matrix-squaring four-by-four Jacobian matrix

§Jacobians of Matrix Functions › A simple example: The two-by-two matrix-square function › The matrix-squaring four-by-four Jacobian matrix · pp. 23–23 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
that the primary way to study matrix functions like this should be to view them as having matrix inputs (A) and matrix outputs (A2), and that one should likewise generally view the derivatives as linear operators on matrices, not vectorized versions thereof. However, it is still useful to be familiar with the vectorization viewpoint in order to have the benefit of an alternative perspective. To understand Jacobians of functions (from matrices to matrices), let’s begin by considering a basic question: Question 24. What is the size of the Jacobian of the matrix-square function? Well, if we view the matrix squaring function via its vectorized equivalent ˜f, mapping R4 7→R4 (4-component column vectors to 4-component column vectors), the Jacobian would be a 4×4 matrix (formed from the derivatives of each output component with respect to each input component). Now let’s think about a more general square matrix A: an m × m matrix. If we wanted to find the Jacobian of f(A) = A2, we could do so by the same process and (symbolically) obtain an m2 × m2 matrix (since there are m2 inputs, the entries of A, and m2 outputs, the entries of A2). Explicit computation of these m4 partial derivatives is rather tedious even for small m, but is a task that symbolic computational tools in e.g.

## Key terms
- **matrix** — 16 mentions
- **matrices** — 8 mentions
- **jacobian** — 8 mentions
- **derivative** — 7 mentions
- **column** — 6 mentions
- **vectors** — 5 mentions
- **output** — 5 mentions
- **input** — 5 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=23|Matrix Calculus.pdf p. 23]]

## Liens
- Up: [[research/matrix-calculus/a-simple-example-the-two-by-two-matrix-square-function]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
