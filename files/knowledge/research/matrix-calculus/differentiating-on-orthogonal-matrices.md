---
title: "Differentiating on Orthogonal Matrices"
summary: "§Derivatives of Eigenproblems › Differentiating on Orthogonal: that if xT dx = 0 and A is a symmetric matrix, we have d 1 2xT Ax  = (Ax)T dx = xT A(dx) = xT A(I −xxT )dx = ((I −xxT )Ax)T dx."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "97-99"
---

# Differentiating on Orthogonal Matrices

§Derivatives of Eigenproblems › Differentiating on Orthogonal Matrices · pp. 97–99 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
that if xT dx = 0 and A is a symmetric matrix, we have d 1 2xT Ax  = (Ax)T dx = xT A(dx) = xT A(I −xxT )dx = ((I −xxT )Ax)T dx. In other words, (I −xxT )Ax is the gradient of 1 2xT Ax on the sphere. So what did we just do? To obtain the gradient on the sphere, we needed (i) a linearization of the function that is correct on tangents, and (ii) a direction that is tangent (i.e. satisfies the linearized constraint). Using this, we obtain the gradient of a general scalar function on the sphere: Theorem 60 Given f : Sn →R, we have df = g(x)T dx = ((I −xxT )g(x))T dx. The proof of this is precisely the same as we did before for f(x) = 1 2xT Ax. Let Q be an orthogonal matrix. Then, computationally (as is done in the Julia notebook), one can see that QT dQ is an anti-symmetric matrix (sometimes called skew-symmetric). Definition 61 A matrix M is anti-symmetric if M = −M T . Note that all anti-symmetric matrices thus have zeroes on their diagonals. In fact, we can prove that QT dQ is anti-symmetric. Theorem 62 Given Q is an orthogonal matrix, we have that QT dQ is anti-symmetric. Proof. The constraint of being orthogonal implies that QT Q = I. Differentiating this equation, we obtain QT dQ + dQT Q = 0 =⇒QT dQ = −(QT dQ)T .

## Key terms
- **orthogonal** — 9 mentions
- **eigenvalue** — 8 mentions
- **matrix** — 7 mentions
- **anti-symmetric** — 6 mentions
- **parameter** — 6 mentions
- **symmetric** — 5 mentions
- **matrices** — 5 mentions
- **diagonal** — 5 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=97|Matrix Calculus.pdf p. 97]]

## Liens
- Up: [[research/matrix-calculus/derivatives-of-eigenproblems]]
- ← Prev: [[research/matrix-calculus/differentiating-on-the-unit-sphere]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
