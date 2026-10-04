---
title: "Jacobians of Matrix Functions"
summary: "§Jacobians of Matrix Functions: When we have a function that has matrices as inputs and/or outputs, we have already seen in the previous lectures that we can still define the derivative as a linear operator by a formula for f ′ mapping a small change in input to the corresponding"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "20-28"
---

# Jacobians of Matrix Functions

§Jacobians of Matrix Functions · pp. 20–28 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
When we have a function that has matrices as inputs and/or outputs, we have already seen in the previous lectures that we can still define the derivative as a linear operator by a formula for f ′ mapping a small change in input to the corresponding small change in output. However, when you first learned linear algebra, probably most linear operations were represented by matrices multiplying vectors, and it may take a while to get used to thinking of linear operations more generally. In this chapter, we discuss how it is still possible to represent f ′ by a Jacobian matrix even for matrix inputs/outputs, and how the most common technique to do this involves matrix “vectorization” and a new type of matrix operation, a Kronecker product. This gives us another way to think about our f ′ linear operators that is occasionally convenient, but at the same time it is important to become comfortable with other ways of writing down linear operators too-sometimes, the explicit Jacobian-matrix approach can obscure key structure, and it is often computationally inefficient as well. For this section of the notes, we refer to the linked Pluto Notebook for computational demonstrations of this material in Julia, illustrating multiple views of the derivative of the square A2 of 2 × 2 matrices A.

## Key terms
- **matrix** — 37 mentions
- **linear** — 17 mentions
- **matrices** — 16 mentions
- **function** — 15 mentions
- **vector** — 14 mentions
- **derivative** — 13 mentions
- **input** — 13 mentions
- **output** — 13 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=20|Matrix Calculus.pdf p. 20]]

## Liens
- ← Prev: [[research/matrix-calculus/derivatives-as-linear-operators]]
- Next: [[research/matrix-calculus/finite-difference-approximations]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
