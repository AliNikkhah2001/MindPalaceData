---
title: "7.2 Constrained Optimization and Lagrange Multipliers"
summary: "§Part I Mathematical Foundations › 7 Continuous Optimization : 7.2 Constrained Optimization and Lagrange Multipliers Figure 7.4 Illustration of constrained optimization. The unconstrained problem (indicated by the contour lines) has a minimum on the right side (indicated by the c"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "239-241"
---

# 7.2 Constrained Optimization and Lagrange Multipliers

§Part I Mathematical Foundations › 7 Continuous Optimization › 7.2 Constrained Optimization and Lagrange Multipliers · pp. 239–241 · Mathematics for Machine Learning (MML Book)

## Extrait
7.2 Constrained Optimization and Lagrange Multipliers Figure 7.4 Illustration of constrained optimization. The unconstrained problem (indicated by the contour lines) has a minimum on the right side (indicated by the circle). The box constraints (−1 ⩽x ⩽1 and −1 ⩽y ⩽1) require that the optimal solution is within the box, resulting in an optimal value indicated by the star. −3 −2 −1 x1 −3 −2 −1 x2 such as training deep neural networks on millions of images (Dean et al., 2012), topic models (Hoffman et al., 2013), reinforcement learning (Mnih et al., 2015), or training of large-scale Gaussian process models (Hensman et al., 2013; Gal et al., 2014). In the previous section, we considered the problem of solving for the minimum of a function min x f(x) , (7.16) where f : RD →R. In this section, we have additional constraints. That is, for real-valued functions gi : RD →R for i = 1, . . . , m, we consider the constrained optimization problem (see Figure 7.4 for an illustration) min x f(x) (7.17) subject to gi(x) ⩽0 for all i = 1, . . . , m . It is worth pointing out that the functions f and gi could be non-convex in general, and we will consider the convex case in the next section. One obvious, but not very practical, way of converting the constrained problem (7.17) into an unconstrained one is to use an indicator function J(x) = f(x) + m X i=1 1(gi(x)) , (7.18) ©2024 M.

## Key terms
- **problem** — 18 mentions
- **function** — 14 mentions
- **optimization** — 10 mentions
- **duality** — 9 mentions
- **constraint** — 8 mentions
- **lagrangian** — 8 mentions
- **inequality** — 8 mentions
- **lagrange** — 7 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=239|mml-book.pdf p. 239]]

## Liens
- Up: [[research/mml-book/7-continuous-optimization]]
- ← Prev: [[research/mml-book/7-1-optimization-using-gradient-descent]]
- Next: [[research/mml-book/7-3-convex-optimization]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
