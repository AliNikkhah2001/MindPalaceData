---
title: "Characteristic Polynomial"
summary: "§Derivative of Matrix Determinant and Inverse › Applications : There is also a fancier proof of the theorem using linearization near the identity. Firstly, note that it is easy to see from the properties of determinants that det(I + dA) −1 = tr(dA), and thus det(A + A(A−1dA)) −de"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "48-48"
---

# Characteristic Polynomial

§Derivative of Matrix Determinant and Inverse › Applications › Characteristic Polynomial · pp. 48–48 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
There is also a fancier proof of the theorem using linearization near the identity. Firstly, note that it is easy to see from the properties of determinants that det(I + dA) −1 = tr(dA), and thus det(A + A(A−1dA)) −det(A) = det(A)(det(I + A−1dA) −1) = det(A) tr(A−1dA) = tr(det(A)A−1dA) = tr(adj(A)dA). This also implies the theorem. We now use this as an application to find the derivative of a characteristic polynomial evaluated at x. Let p(x) = det(xI −A), a scalar function of x. Recall that through factorization, p(x) may be written in terms of eigenvalues λi. So we may ask: what is the derivative of p(x), the characteristic polynomial at x? Using freshman calculus, we could simply compute d dx Y i (x −λi) = X i Y j̸=i (x −λj) = Y (x −λi){ X i (x −λi)−1}, as long as x̸ = λi. This is a perfectly good simply proof, but with our new technology we have a new proof: d(det(xI −A)) = det(xI −A) tr((xI −A)−1d(xI −A)) = det(xI −A) tr(xI −A)−1dx. Note that here we used that d(xI −A) = dx I when A is constant and tr(Adx) = tr(A)dx since dx is a scalar. We may again check this computationally as we do in the notebook. We can similarly compute using the chain rule that d(log(det(A))) = d(det A) det A = det(A−1)d(det(A)) = tr(A−1dA).

## Key terms
- **derivative** — 4 mentions
- **determinant** — 4 mentions
- **note** — 3 mentions
- **function** — 3 mentions
- **roots** — 3 mentions
- **theorem** — 2 mentions
- **find** — 2 mentions
- **characteristic** — 2 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=48|Matrix Calculus.pdf p. 48]]

## Liens
- Up: [[research/matrix-calculus/applications-2]]
- Next: [[research/matrix-calculus/the-logarithmic-derivative]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
