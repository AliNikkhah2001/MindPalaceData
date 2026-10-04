---
title: "5.2 Partial Differentiation and Gradients"
summary: "§Part I Mathematical Foundations › 5 Vector Calculus › 5.2 Pa: Vector Calculus such that the derivative of h is given as h′(x) = g′(f)f ′(x) = (4f 3) · 2 (5.34) = 4(2x + 1)3 · 2 = 8(2x + 1)3 , (5.38) where we used the chain rule (5.32) and substituted the definition of f in (5.34"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "152-154"
---

# 5.2 Partial Differentiation and Gradients

§Part I Mathematical Foundations › 5 Vector Calculus › 5.2 Partial Differentiation and Gradients · pp. 152–154 · Mathematics for Machine Learning (MML Book)

## Extrait
Vector Calculus such that the derivative of h is given as h′(x) = g′(f)f ′(x) = (4f 3) · 2 (5.34) = 4(2x + 1)3 · 2 = 8(2x + 1)3 , (5.38) where we used the chain rule (5.32) and substituted the definition of f in (5.34) in g′(f). Differentiation as discussed in Section 5.1 applies to functions f of a scalar variable x ∈R. In the following, we consider the general case where the function f depends on one or more variables x ∈Rn, e.g., f(x) = f(x1, x2). The generalization of the derivative to functions of several variables is the gradient. We find the gradient of the function f with respect to x by varying one variable at a time and keeping the others constant. The gradient is then the collection of these partial derivatives. Definition 5.5 (Partial Derivative). For a function f : Rn →R, x 7→ f(x), x ∈Rn of n variables x1, . . . , xn we define the partial derivatives as partial derivative ∂f ∂x1 = lim h→0 f(x1 + h, x2, . . . , xn) −f(x) h ... ∂f ∂xn = lim h→0 f(x1, . . . , xn−1, xn + h) −f(x) h (5.39) and collect them in the row vector ∇xf = gradf = df dx = ∂f(x) ∂x1 ∂f(x) ∂x2 · · · ∂f(x) ∂xn  ∈R1×n , (5.40) where n is the number of variables and 1 is the dimension of the image/ range/codomain of f.

## Key terms
- **rule** — 25 mentions
- **derivative** — 20 mentions
- **gradient** — 17 mentions
- **partial** — 15 mentions
- **vector** — 14 mentions
- **chain** — 14 mentions
- **function** — 12 mentions
- **variable** — 8 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=152|mml-book.pdf p. 152]]

## Liens
- Up: [[research/mml-book/5-vector-calculus]]
- ← Prev: [[research/mml-book/5-1-differentiation-of-univariate-functions]]
- Next: [[research/mml-book/5-3-gradients-of-vector-valued-functions]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
