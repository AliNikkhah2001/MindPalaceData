---
title: Matrix Chain Rule & Kronecker Products
summary: Chain rule for vectorized matrix derivatives using Kronecker products; foundational for backpropagation.
course: ML Research
tags: [math, calculus, backprop]
book: Matrix Calculus.pdf
page: 16
read: false
---
# Matrix Chain Rule & Kronecker Products

> **Source**: [[pdf:Matrix Calculus.pdf#page=16|Matrix Calculus.pdf (p. 16)]]

## Definition & Core Intuition
Chain rule for vectorized matrix derivatives using Kronecker products; foundational for backpropagation.

## Mathematical Formulation
$$
\text{vec}(d\mathbf{Y}) = (\mathbf{B}^T \otimes \mathbf{A}) \text{vec}(d\mathbf{X})
$$

## Connected Learning Assets
- [[card:10|Review Flashcard #10]]

## Related Concepts
- [[concept:automatic-differentiation|Automatic Differentiation]]