---
title: "5.5 Useful Identities for Computing Gradients"
summary: "§Part I Mathematical Foundations › 5 Vector Calculus › 5.5 Us: Vector Calculus ∂pqij =        Riq if j = p, p̸ = q Rip if j = q, p̸ = q 2Riq if j = p, p = q otherwise . (5.98) From (5.94), we know that the desired gradient has the dimension (N × N) × (M × N), and every sin"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "164-164"
---

# 5.5 Useful Identities for Computing Gradients

§Part I Mathematical Foundations › 5 Vector Calculus › 5.5 Useful Identities for Computing Gradients · pp. 164–164 · Mathematics for Machine Learning (MML Book)

## Extrait
Vector Calculus ∂pqij =        Riq if j = p, p̸ = q Rip if j = q, p̸ = q 2Riq if j = p, p = q otherwise . (5.98) From (5.94), we know that the desired gradient has the dimension (N × N) × (M × N), and every single entry of this tensor is given by ∂pqij in (5.98), where p, q, j = 1, . . . , N and i = 1, . . . , M. In the following, we list some useful gradients that are frequently required in a machine learning context (Petersen and Pedersen, 2012). Here, we use tr(·) as the trace (see Definition 4.4), det(·) as the determinant (see Section 4.1) and f(X)−1 as the inverse of f(X), assuming it exists. ∂ ∂X f(X)⊤= ∂f(X) ∂X ⊤ (5.99) ∂ ∂X tr(f(X)) = tr ∂f(X) ∂X  (5.100) ∂ ∂X det(f(X)) = det(f(X))tr  f(X)−1 ∂f(X) ∂X  (5.101) ∂ ∂X f(X)−1 = −f(X)−1 ∂f(X) ∂X f(X)−1 (5.102) ∂a⊤X−1b ∂X = −(X−1)⊤ab⊤(X−1)⊤ (5.103) ∂x⊤a ∂x = a⊤ (5.104) ∂a⊤x ∂x = a⊤ (5.105) ∂a⊤Xb ∂X = ab⊤ (5.106) ∂x⊤Bx ∂x = x⊤(B + B⊤) (5.107) ∂ ∂s(x −As)⊤W (x −As) = −2(x −As)⊤W A for symmetric W (5.108) Remark. In this book, we only cover traces and transposes of matrices. However, we have seen that derivatives can be higher-dimensional tensors, in which case the usual trace and transpose are not defined. In these cases, the trace of a D×D×E×F tensor would be an E×F-dimensional matrix.

## Key terms
- **tensor** — 4 mentions
- **trace** — 4 mentions
- **case** — 3 mentions
- **pqij** — 2 mentions
- **gradient** — 2 mentions
- **transpose** — 2 mentions
- **vector** — 1 mentions
- **calculus** — 1 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=164|mml-book.pdf p. 164]]

## Liens
- Up: [[research/mml-book/5-vector-calculus]]
- ← Prev: [[research/mml-book/5-4-gradients-of-matrices]]
- Next: [[research/mml-book/5-6-backpropagation-and-automatic-differentiation]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
