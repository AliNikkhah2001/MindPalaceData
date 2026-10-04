---
title: "5.4 Gradients of Matrices"
summary: "§Part I Mathematical Foundations › 5 Vector Calculus › 5.4 Gr: 5.4 Gradients of Matrices Figure 5.7 Visualization of gradient computation of a matrix with respect to a vector. We are interested in computing the gradient of A ∈R4×2 with respect to a vector x ∈R3."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "161-163"
---

# 5.4 Gradients of Matrices

§Part I Mathematical Foundations › 5 Vector Calculus › 5.4 Gradients of Matrices · pp. 161–163 · Mathematics for Machine Learning (MML Book)

## Extrait
5.4 Gradients of Matrices Figure 5.7 Visualization of gradient computation of a matrix with respect to a vector. We are interested in computing the gradient of A ∈R4×2 with respect to a vector x ∈R3. We know that gradient dA dx ∈R4×2×3. We follow two equivalent approaches to arrive there: (a) collating partial derivatives into a Jacobian tensor; (b) flattening of the matrix into a vector, computing the Jacobian matrix, re-shaping into a Jacobian tensor. A ∈R4×2 x ∈R3 ∂A ∂x1 ∈R4×2 ∂A ∂x2 ∈R4×2 ∂A ∂x3 ∈R4×2 x1 x2 x3 dA dx ∈R4×2×3 Partial derivatives: collate (a) Approach 1: We compute the partial derivative ∂A ∂x1 , ∂A ∂x2 , ∂A ∂x3 , each of which is a 4 × 2 matrix, and collate them in a 4 × 2 × 3 tensor. A ∈R4×2 x ∈R3 x1 x2 x3 dA dx ∈R4×2×3 re-shape re-shape gradient A ∈R4×2 ˜A ∈R8 d ˜A dx ∈R8×3 (b) Approach 2: We re-shape (flatten) A ∈R4×2 into a vector ˜A ∈R8. Then, we compute the gradient d ˜ A dx ∈R8×3. We obtain the gradient tensor by re-shaping this gradient as illustrated above. 5.4 Gradients of Matrices We can think of a tensor as a multidimensional array. We will encounter situations where we need to take gradients of matrices with respect to vectors (or other matrices), which results in a multidimensional tensor.

## Key terms
- **gradient** — 21 mentions
- **vector** — 13 mentions
- **matrix** — 12 mentions
- **matrices** — 11 mentions
- **partial** — 11 mentions
- **tensor** — 11 mentions
- **derivative** — 11 mentions
- **respect** — 8 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=161|mml-book.pdf p. 161]]

## Liens
- Up: [[research/mml-book/5-vector-calculus]]
- ← Prev: [[research/mml-book/5-3-gradients-of-vector-valued-functions]]
- Next: [[research/mml-book/5-5-useful-identities-for-computing-gradients]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
