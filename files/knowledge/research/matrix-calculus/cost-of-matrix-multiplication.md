---
title: "Cost of Matrix Multiplication"
summary: "§Derivatives as Linear Operators › The Chain Rule › Cost of M: Then, df = f(x + dx) −f(x) = g(h(x + dx)) −g(h(x)) = g′(h(x))[h(x + dx) −h(x)] = g′(h(x))[h′(x)[dx]] = g′(h(x))h′(x)[dx] where g′(h(x))h′(x) is a composition of g′ and h′ as matrices."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "17-17"
---

# Cost of Matrix Multiplication

§Derivatives as Linear Operators › The Chain Rule › Cost of Matrix Multiplication · pp. 17–17 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
• Chain Rule: Let f(x) = g(h(x)). Then, df = f(x + dx) −f(x) = g(h(x + dx)) −g(h(x)) = g′(h(x))[h(x + dx) −h(x)] = g′(h(x))[h′(x)[dx]] = g′(h(x))h′(x)[dx] where g′(h(x))h′(x) is a composition of g′ and h′ as matrices. In other words, f ′(x) = g′(h(x))h′(x): the Jacobian (linear operator) f ′ is simply the product (composition) of the Jacobians, g′h′. Ordering matters because linear operators do not generally commute: left-to-right = outputs-to-inputs. Let’s look more carefully at the shapes of these Jacobian matrices in an example where each function maps a column vector to a column vector: Example 15 Let x ∈Rn, h(x) ∈Rp, and g(h(x)) ∈Rm. Then, let f(x) = g(h(x)) mapping from Rn to Rm. The chain rule then states that f ′(x) = g′(h(x))h′(x), which makes sense as g′ is an m × p matrix and h′ is a p × n matrix, so that the product gives an m × n matrix f ′! However, notice that this is not the same as h′(x)g′(h(x)) as you cannot (if n̸ = m) multiply a p×n and an m × p matrix together, and even if n = m you will get the wrong answer since they probably won’t commute. Not only does the order of the multiplication matter, but the associativity of matrix multiplication matters practically.

## Key terms
- **matrix** — 8 mentions
- **multiplication** — 6 mentions
- **product** — 4 mentions
- **matter** — 4 mentions
- **chain** — 3 mentions
- **rule** — 3 mentions
- **jacobian** — 3 mentions
- **function** — 3 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=17|Matrix Calculus.pdf p. 17]]

## Liens
- Up: [[research/matrix-calculus/the-chain-rule]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
