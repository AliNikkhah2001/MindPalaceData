---
title: "7.4 Further Reading"
summary: "§Part I Mathematical Foundations › 7 Continuous Optimization : Continuous Optimization The Legendre-Fenchel conjugate turns out to be quite useful for machine learning problems that can be expressed as convex optimization problems."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "252-252"
---

# 7.4 Further Reading

§Part I Mathematical Foundations › 7 Continuous Optimization › 7.4 Further Reading · pp. 252–252 · Mathematics for Machine Learning (MML Book)

## Extrait
Continuous Optimization The Legendre-Fenchel conjugate turns out to be quite useful for machine learning problems that can be expressed as convex optimization problems. In particular, for convex loss functions that apply independently to each example, the conjugate loss is a convenient way to derive a dual problem. Continuous optimization is an active area of research, and we do not try to provide a comprehensive account of recent advances. From a gradient descent perspective, there are two major weaknesses which each have their own set of literature. The first challenge is the fact that gradient descent is a first-order algorithm, and does not use information about the curvature of the surface. When there are long valleys, the gradient points perpendicularly to the direction of interest. The idea of momentum can be generalized to a general class of acceleration methods (Nesterov, 2018). Conjugate gradient methods avoid the issues faced by gradient descent by taking previous directions into account (Shewchuk, 1994). Second-order methods such as Newton methods use the Hessian to provide information about the curvature. Many of the choices for choosing step-sizes and ideas like momentum arise by considering the curvature of the objective function (Goh, 2017; Bottou et al., 2018).

## Key terms
- **gradient** — 9 mentions
- **methods** — 9 mentions
- **optimization** — 7 mentions
- **descent** — 7 mentions
- **problem** — 5 mentions
- **there** — 5 mentions
- **function** — 5 mentions
- **continuous** — 4 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=252|mml-book.pdf p. 252]]

## Liens
- Up: [[research/mml-book/7-continuous-optimization]]
- ← Prev: [[research/mml-book/7-3-convex-optimization]]
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
