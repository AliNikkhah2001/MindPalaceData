---
title: "7.1 Optimization Using Gradient Descent"
summary: "§Part I Mathematical Foundations › 7 Continuous Optimization : 7.1 Optimization Using Gradient Descent Figure 7.2 Example objective function. Negative gradients are indicated by arrows, and the global minimum is indicated by the dashed blue line."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "233-238"
---

# 7.1 Optimization Using Gradient Descent

§Part I Mathematical Foundations › 7 Continuous Optimization › 7.1 Optimization Using Gradient Descent · pp. 233–238 · Mathematics for Machine Learning (MML Book)

## Extrait
7.1 Optimization Using Gradient Descent Figure 7.2 Example objective function. Negative gradients are indicated by arrows, and the global minimum is indicated by the dashed blue line. −6 −5 −4 −3 −2 −1 Value of parameter −60 −40 −20 Objective x4 + 7x3 + 5x2 −17x + 3 right, but not how far (this is called the step-size). Furthermore, if we According to the Abel-Ruffini theorem, there is in general no algebraic solution for polynomials of degree 5 or more (Abel, 1826). had started at the right side (e.g., x0 = 0) the negative gradient would have led us to the wrong minimum. Figure 7.2 illustrates the fact that for x > −1, the negative gradient points toward the minimum on the right of the figure, which has a larger objective value. In Section 7.3, we will learn about a class of functions, called convex functions, that do not exhibit this tricky dependency on the starting point of the optimization algorithm. For convex functions, all local minimums are global minimum. It turns out that many machine learning objective For convex functions all local minima are global minimum. functions are designed such that they are convex, and we will see an example in Chapter 12. The discussion in this chapter so far was about a one-dimensional function, where we are able to visualize the ideas of gradients, descent directions, and optimal values.

## Key terms
- **gradient** — 43 mentions
- **descent** — 24 mentions
- **function** — 22 mentions
- **minimum** — 13 mentions
- **step-size** — 12 mentions
- **direction** — 10 mentions
- **value** — 9 mentions
- **point** — 8 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=233|mml-book.pdf p. 233]]

## Liens
- Up: [[research/mml-book/7-continuous-optimization]]
- Next: [[research/mml-book/7-2-constrained-optimization-and-lagrange-multipliers]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
