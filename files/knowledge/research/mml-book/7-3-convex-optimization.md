---
title: "7.3 Convex Optimization"
summary: "§Part I Mathematical Foundations › 7 Continuous Optimization : Continuous Optimization We can model equality constraints by replacing them with two inequality constraints. That is for each equality constraint hj(x) = 0 we equivalently replace it by two constraints hj(x) ⩽0 and hj"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "242-251"
---

# 7.3 Convex Optimization

§Part I Mathematical Foundations › 7 Continuous Optimization › 7.3 Convex Optimization · pp. 242–251 · Mathematics for Machine Learning (MML Book)

## Extrait
Continuous Optimization We can model equality constraints by replacing them with two inequality constraints. That is for each equality constraint hj(x) = 0 we equivalently replace it by two constraints hj(x) ⩽0 and hj(x) ⩾0. It turns out that the resulting Lagrange multipliers are then unconstrained. Therefore, we constrain the Lagrange multipliers corresponding to the inequality constraints in (7.28) to be non-negative, and leave the Lagrange multipliers corresponding to the equality constraints unconstrained. ♢ We focus our attention of a particularly useful class of optimization problems, where we can guarantee global optimality. When f(·) is a convex function, and when the constraints involving g(·) and h(·) are convex sets, this is called a convex optimization problem. In this setting, we have strong convex optimization problem strong duality duality: The optimal solution of the dual problem is the same as the optimal solution of the primal problem. The distinction between convex functions and convex sets are often not strictly presented in machine learning literature, but one can often infer the implied meaning from context. Definition 7.2. A set C is a convex set if for any x, y ∈C and for any scalar convex set θ with 0 ⩽θ ⩽1, we have θx + (1 −θ)y ∈C .

## Key terms
- **convex** — 48 mentions
- **function** — 42 mentions
- **optimization** — 11 mentions
- **constraint** — 10 mentions
- **problem** — 10 mentions
- **sets** — 8 mentions
- **log2** — 8 mentions
- **inequality** — 7 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=242|mml-book.pdf p. 242]]

## Liens
- Up: [[research/mml-book/7-continuous-optimization]]
- ← Prev: [[research/mml-book/7-2-constrained-optimization-and-lagrange-multipliers]]
- Next: [[research/mml-book/7-4-further-reading]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
