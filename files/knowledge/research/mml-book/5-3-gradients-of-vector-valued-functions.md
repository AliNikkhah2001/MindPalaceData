---
title: "5.3 Gradients of Vector-Valued Functions"
summary: "§Part I Mathematical Foundations › 5 Vector Calculus › 5.3 Gr: 5.3 Gradients of Vector-Valued Functions and the gradient is obtained by the matrix multiplication df d(s, t) = ∂f ∂x ∂x ∂(s, t) = h ∂f ∂x1 ∂f ∂x2 i | {z } = ∂f ∂x   ∂x1 ∂s ∂x1 ∂t ∂x2 ∂s ∂x2 ∂t   | {z } = ∂x ∂(s"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "155-160"
---

# 5.3 Gradients of Vector-Valued Functions

§Part I Mathematical Foundations › 5 Vector Calculus › 5.3 Gradients of Vector-Valued Functions · pp. 155–160 · Mathematics for Machine Learning (MML Book)

## Extrait
5.3 Gradients of Vector-Valued Functions and the gradient is obtained by the matrix multiplication df d(s, t) = ∂f ∂x ∂x ∂(s, t) = h ∂f ∂x1 ∂f ∂x2 i | {z } = ∂f ∂x   ∂x1 ∂s ∂x1 ∂t ∂x2 ∂s ∂x2 ∂t   | {z } = ∂x ∂(s, t) . (5.53) This compact way of writing the chain rule as a matrix multiplication only The chain rule can be written as a matrix multiplication. makes sense if the gradient is defined as a row vector. Otherwise, we will need to start transposing gradients for the matrix dimensions to match. This may still be straightforward as long as the gradient is a vector or a matrix; however, when the gradient becomes a tensor (we will discuss this in the following), the transpose is no longer a triviality. Remark (Verifying the Correctness of a Gradient Implementation). The definition of the partial derivatives as the limit of the corresponding difference quotient (see (5.39)) can be exploited when numerically checking the correctness of gradients in computer programs: When we compute Gradient checking gradients and implement them, we can use finite differences to numerically test our computation and implementation: We choose the value h to be small (e.g., h = 10−4) and compare the finite-difference approximation from (5.39) with our (analytic) implementation of the gradient.

## Key terms
- **gradient** — 23 mentions
- **vector** — 18 mentions
- **jacobian** — 16 mentions
- **function** — 15 mentions
- **derivative** — 15 mentions
- **matrix** — 14 mentions
- **transformation** — 12 mentions
- **partial** — 11 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=155|mml-book.pdf p. 155]]

## Liens
- Up: [[research/mml-book/5-vector-calculus]]
- ← Prev: [[research/mml-book/5-2-partial-differentiation-and-gradients]]
- Next: [[research/mml-book/5-4-gradients-of-matrices]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
