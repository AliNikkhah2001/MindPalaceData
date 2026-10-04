---
title: "Automatic Differentiation via Computational Graphs"
summary: "§Forward and Reverse-Mode Automatic Differentiation › Automat: Let’s now get into automatic differentiation via computational graphs. For this section, we consider the following simple motivating example."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "56-60"
---

# Automatic Differentiation via Computational Graphs

§Forward and Reverse-Mode Automatic Differentiation › Automatic Differentiation via Computational Graphs · pp. 56–60 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Let’s now get into automatic differentiation via computational graphs. For this section, we consider the following simple motivating example. Example 40 Define the following functions:          a(x, y) = sin x b(x, y) = 1 y · a(x, y) z(x, y) = b(x, y) + x. Compute ∂z ∂x and ∂z ∂y. There are a few ways to solve this problem. Firstly, of course, one can compute this symbolically, noting that z(x, y) = b(x, y) + x = 1 y a(x, y) + x = sin x y + x, which implies ∂z ∂x = cos x y + 1 and ∂z ∂y = −sin x y2 . However, one can also use a Computational Graph (see Figure of Computational Graph below) where the edge from node A to node B is labelled with ∂B ∂A. a(x, y) x b(x, y) z(x, y) y cos x y −a(x,y) y2 Figure 7: A computational graph corresponding to example 40, representing the computation of an output z(x, y) from two inputs x, y, with intermediate quantities a(x, y) and b(x, y). The nodes are labelled by values, and edges are labelled with the derivatives of the values with respect to the preceding values. Now how do we use this directed acyclic graph (DAG) to find the derivatives? Well one view (called the “forward view”) is given by following the paths from the inputs to the outputs and (left) multiplying as you go, adding together multiple paths.

## Key terms
- **path** — 19 mentions
- **product** — 14 mentions
- **value** — 12 mentions
- **graph** — 11 mentions
- **computational** — 8 mentions
- **derivative** — 8 mentions
- **following** — 6 mentions
- **functions** — 6 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=56|Matrix Calculus.pdf p. 56]]

## Liens
- Up: [[research/matrix-calculus/forward-and-reverse-mode-automatic-differentiation]]
- ← Prev: [[research/matrix-calculus/naive-symbolic-differentiation]]
- Next: [[research/matrix-calculus/forward-vs-reverse-mode-differentiation]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
