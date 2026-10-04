---
title: "Derivative of Matrix Determinant and Inverse"
summary: "§Derivative of Matrix Determinant and Inverse: This section of notes follows this Julia notebook. This notebook is a little bit short, but is an important and useful calculation."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "47-49"
---

# Derivative of Matrix Determinant and Inverse

§Derivative of Matrix Determinant and Inverse · pp. 47–49 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
This section of notes follows this Julia notebook. This notebook is a little bit short, but is an important and useful calculation. Theorem 39 Given A is a square matrix, we have ∇(det A) = cofactor(A) = (det A)A−T := adj(AT ) = adj(A)T where adj is the “adjugate”. (You may not have heard of the matrix adjugate, but this formula tells us that it is simply adj(A) = det(A)A−1, or cofactor(A) = adj(AT ).) Furthermore, d(det A) = tr(det(A)A−1dA) = tr(adj(A)dA) = tr(cofactor(A)T dA). You may remember that each entry (i, j) of the cofactor matrix is (−1)i+j times the determinant obtained by deleting row i and column j from A. Here are some 2 × 2 calculuations to obtain some intuition about these functions: M = a c b d ! (4) =⇒cofactor(M) = d −c −b a ! (5) adj(M) = d −b −c a ! (6) (M)−1 = ad −bc d −b −c a ! . (7) Numerically, as is done in the notebook, you can construct a random n × n matrix A (say, 9 × 9), consider e.g. dA = .00001A, and see numerically that det(A + dA) −det(A) ≈tr(adj(A)dA), which numerically supports our claim for the theorem. We now prove the theorem in two ways. Firstly, there is a direct proof where you just differentiate the scalar with respect to every input using the cofactor expansion of the determinant based on the i-th row.

## Key terms
- **matrix** — 10 mentions
- **derivative** — 9 mentions
- **cofactor** — 8 mentions
- **determinant** — 6 mentions
- **notebook** — 5 mentions
- **theorem** — 5 mentions
- **function** — 5 mentions
- **simply** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=47|Matrix Calculus.pdf p. 47]]

## Liens
- ← Prev: [[research/matrix-calculus/nonlinear-root-finding-optimization-and-adjoint-differentiation]]
- Next: [[research/matrix-calculus/forward-and-reverse-mode-automatic-differentiation]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
