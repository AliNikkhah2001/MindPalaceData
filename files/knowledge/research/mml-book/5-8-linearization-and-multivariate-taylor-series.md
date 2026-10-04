---
title: "5.8 Linearization and Multivariate Taylor Series"
summary: "§Part I Mathematical Foundations › 5 Vector Calculus › 5.8 Li: 5.8 Linearization and Multivariate Taylor Series Figure 5.12 Linear approximation of a function. The original function f is linearized at x0 = −2 using a first-order Taylor series expansion."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "171-175"
---

# 5.8 Linearization and Multivariate Taylor Series

§Part I Mathematical Foundations › 5 Vector Calculus › 5.8 Linearization and Multivariate Taylor Series · pp. 171–175 · Mathematics for Machine Learning (MML Book)

## Extrait
5.8 Linearization and Multivariate Taylor Series Figure 5.12 Linear approximation of a function. The original function f is linearized at x0 = −2 using a first-order Taylor series expansion. −4 −2 x −2 −1 f(x) f(x) f(x0) f(x0) + f ′(x0)(x −x0) If f(x, y) is a twice (continuously) differentiable function, then ∂2f ∂x∂y = ∂2f ∂y∂x , (5.146) i.e., the order of differentiation does not matter, and the corresponding Hessian matrix Hessian matrix H =   ∂2f ∂x2 ∂2f ∂x∂y ∂2f ∂x∂y ∂2f ∂y2   (5.147) is symmetric. The Hessian is denoted as ∇2 x,yf(x, y). Generally, for x ∈Rn and f : Rn →R, the Hessian is an n × n matrix. The Hessian measures the curvature of the function locally around (x, y). Remark (Hessian of a Vector Field). If f : Rn →Rm is a vector field, the Hessian is an (m × n × n)-tensor. ♢ The gradient ∇f of a function f is often used for a locally linear approximation of f around x0: f(x) ≈f(x0) + (∇xf)(x0)(x −x0) . (5.148) Here (∇xf)(x0) is the gradient of f with respect to x, evaluated at x0. Figure 5.12 illustrates the linear approximation of a function f at an input x0. The original function is approximated by a straight line. This approximation is locally accurate, but the farther we move away from x0 the worse the approximation gets.

## Key terms
- **taylor** — 18 mentions
- **series** — 16 mentions
- **vector** — 13 mentions
- **function** — 11 mentions
- **term** — 10 mentions
- **expansion** — 9 mentions
- **hessian** — 9 mentions
- **polynomial** — 9 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=171|mml-book.pdf p. 171]]

## Liens
- Up: [[research/mml-book/5-vector-calculus]]
- ← Prev: [[research/mml-book/5-7-higher-order-derivatives]]
- Next: [[research/mml-book/5-9-further-reading]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
