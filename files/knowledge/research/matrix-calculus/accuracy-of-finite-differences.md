---
title: "Accuracy of Finite Differences"
summary: "§Finite-Difference Approximations › Accuracy of Finite Differ: A is a 4 × 4 matrix with unit-variance Gaussian random entries, and δA is similarly a unit-variance Gaussian random perturbation scaled by a factor s ranging from 1 to 10−16."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "31-31"
---

# Accuracy of Finite Differences

§Finite-Difference Approximations › Accuracy of Finite Differences · pp. 31–31 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Figure 4: Forward-difference accuracy for f(A) = A2, showing the relative error in δf = f(A + δA) −f(A) versus the linearization f ′(A)δA, as a function of the magnitude ∥δA∥. A is a 4 × 4 matrix with unit-variance Gaussian random entries, and δA is similarly a unit-variance Gaussian random perturbation scaled by a factor s ranging from 1 to 10−16. Definition 30 Note that the norm of a matrix that we are using, computed by norm(A) in Julia, is just the direct analogue of the familiar Euclidean norm for the case of vectors. It is simply the square root of the sum of the matrix entries squared: ∥A∥:= sX i,j |Aij|2 = q tr(AT A) . This is called the Frobenius norm. Now how accurate is our finite-difference approximation above? How should we choose the size of δx? Let’s again consider the example f(A) = A2, and plot the relative error as a function of ∥δA∥. This plot will be done logarithmically (on a log-log scale) so that we can see power-law relationships as straight lines. We notice two main features as we decrease δA: 1. The relative error at first decreases linearly with ∥δA∥. This is called first-order accuracy. Why? 2. When δA gets too small, the error increases. Why?

## Key terms
- **error** — 4 mentions
- **norm** — 4 mentions
- **relative** — 3 mentions
- **matrix** — 3 mentions
- **accuracy** — 2 mentions
- **function** — 2 mentions
- **unit-variance** — 2 mentions
- **gaussian** — 2 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=31|Matrix Calculus.pdf p. 31]]

## Liens
- Up: [[research/matrix-calculus/finite-difference-approximations]]
- ← Prev: [[research/matrix-calculus/example-matrix-squaring]]
- Next: [[research/matrix-calculus/order-of-accuracy]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
