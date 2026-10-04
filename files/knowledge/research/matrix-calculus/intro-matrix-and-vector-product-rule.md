---
title: "Intro: Matrix and Vector Product Rule"
summary: "§Overview and Motivation › Intro: Matrix and Vector Product R: Then, notice that 2xT 0 dx = 2  T dx = .022. Hence, we have that f(x0 + dx) −f(x0) ≈2xT 0 dx = .022. As we will see right now, the 2xT 0 dx didn’t come from nowhere!"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "8-8"
---

# Intro: Matrix and Vector Product Rule

§Overview and Motivation › Intro: Matrix and Vector Product Rule · pp. 8–8 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Then, notice that 2xT 0 dx = 2  T dx = .022. Hence, we have that f(x0 + dx) −f(x0) ≈2xT 0 dx = .022. As we will see right now, the 2xT 0 dx didn’t come from nowhere! For matrices, we in fact still have a product rule! We will discuss this in much more detail in later chapters, but let’s begin here with a small taste. Theorem 2 (Differential Product Rule) Let A, B be two matrices. Then, we have the differential product rule for AB: d(AB) = (dA)B + A(dB). By the differential of the matrix A, we think of it as a small (unconstrained) change in the matrix A. Later, constraints may be places on the allowed perturbations. Notice however, that (by our table) the derivative of a matrix is a matrix! So generally speaking, the products will not commute. If x is a vector, then by the differential product rule we have d(xT x) = (dxT )x + xT (dx). However, notice that this is a dot product, and dot products commute (since P ai · bi = P bi · ai), we have that d(xT x) = (2x)T dx. Remark 3. The way the product rule works for vectors as matrices is that transposes “go for the ride.” See the next example below. Example 4 By the product rule. we have 1. d(uT v) = (du)T v + uT (dv) = vT du + uT dv since dot products commute.

## Key terms
- **product** — 10 mentions
- **rule** — 6 mentions
- **differential** — 4 mentions
- **matrix** — 4 mentions
- **notice** — 3 mentions
- **matrices** — 3 mentions
- **commute** — 3 mentions
- **later** — 2 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=8|Matrix Calculus.pdf p. 8]]

## Liens
- Up: [[research/matrix-calculus/overview-and-motivation]]
- ← Prev: [[research/matrix-calculus/first-derivatives]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
