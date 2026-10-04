---
title: "5.7 Higher-Order Derivatives"
summary: "§Part I Mathematical Foundations › 5 Vector Calculus › 5.7 Hi: Vector Calculus where the gi(·) are elementary functions and xPa(xi) are the parent nodes of the variable xi in the graph."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "170-170"
---

# 5.7 Higher-Order Derivatives

§Part I Mathematical Foundations › 5 Vector Calculus › 5.7 Higher-Order Derivatives · pp. 170–170 · Mathematics for Machine Learning (MML Book)

## Extrait
Vector Calculus where the gi(·) are elementary functions and xPa(xi) are the parent nodes of the variable xi in the graph. Given a function defined in this way, we can use the chain rule to compute the derivative of the function in a stepby-step fashion. Recall that by definition f = xD and hence ∂f ∂xD = 1 . (5.144) For other variables xi, we apply the chain rule ∂f ∂xi = X xj:xi∈Pa(xj) ∂f ∂xj ∂xj ∂xi = X xj:xi∈Pa(xj) ∂f ∂xj ∂gj ∂xi , (5.145) where Pa(xj) is the set of parent nodes of xj in the computation graph. Equation (5.143) is the forward propagation of a function, whereas (5.145) Auto-differentiation in reverse mode requires a parse tree. is the backpropagation of the gradient through the computation graph. For neural network training, we backpropagate the error of the prediction with respect to the label. The automatic differentiation approach above works whenever we have a function that can be expressed as a computation graph, where the elementary functions are differentiable. In fact, the function may not even be a mathematical function but a computer program. However, not all computer programs can be automatically differentiated, e.g., if we cannot find differential elementary functions.

## Key terms
- **function** — 11 mentions
- **derivative** — 10 mentions
- **partial** — 8 mentions
- **respect** — 5 mentions
- **graph** — 4 mentions
- **elementary** — 3 mentions
- **variable** — 3 mentions
- **computation** — 3 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=170|mml-book.pdf p. 170]]

## Liens
- Up: [[research/mml-book/5-vector-calculus]]
- ← Prev: [[research/mml-book/5-6-backpropagation-and-automatic-differentiation]]
- Next: [[research/mml-book/5-8-linearization-and-multivariate-taylor-series]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
