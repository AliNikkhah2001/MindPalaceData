---
title: Jacobian Matrix
summary: Matrix of all first-order partial derivatives of a vector-valued function; the canonical local linear map.
course: ML Research
tags: [math, calculus, linear-algebra, optimization]
book: Matrix Calculus.pdf
page: 14
read: false
---
# Jacobian Matrix

> **Source**: [[pdf:Matrix Calculus.pdf#page=14|Matrix Calculus.pdf (p. 14)]]

## Definition & Core Intuition
Matrix of all first-order partial derivatives of a vector-valued function; the canonical local linear map.

## Mathematical Formulation
$$
J = \frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix} \frac{\partial y_1}{\partial x_1} & \cdots & \frac{\partial y_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial y_m}{\partial x_1} & \cdots & \frac{\partial y_m}{\partial x_n} \end{bmatrix}
$$

## Connected Learning Assets
- [[quiz:3|Test with Quiz #3]]
- [[card:3|Review Flashcard #3]]

## Related Concepts
- [[concept:matrix-chain-rule|Matrix Chain Rule]]
- [[concept:hessian-matrix|Hessian Matrix]]