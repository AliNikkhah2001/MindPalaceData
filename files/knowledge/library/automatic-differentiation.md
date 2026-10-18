---
title: Automatic Differentiation (AD)
summary: Evaluation of derivatives by applying the chain rule to elementary arithmetic operations; forward and reverse modes.
course: ML Research
tags: [ad, deep-learning, algorithms]
book: Matrix Calculus.pdf
page: 28
read: false
---
# Automatic Differentiation (AD)

> **Source**: [[pdf:Matrix Calculus.pdf#page=28|Matrix Calculus.pdf (p. 28)]]

## Definition & Core Intuition
Evaluation of derivatives by applying the chain rule to elementary arithmetic operations; forward and reverse modes.

## Mathematical Formulation
$$
\bar{x}_i = \sum_{j \in \text{children}(i)} \bar{x}_j \frac{\partial \phi_j}{\partial x_i}
$$

## Connected Learning Assets