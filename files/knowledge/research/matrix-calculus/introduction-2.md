---
title: "Introduction"
summary: "§Derivatives of Random Functions › Introduction: These notes are from a guest lecture by Gaurav Arya in IAP 2023. In this class, we’ve learned how to take derivatives of all sorts of crazy functions."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "79-79"
---

# Introduction

§Derivatives of Random Functions › Introduction · pp. 79–79 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
These notes are from a guest lecture by Gaurav Arya in IAP 2023. In this class, we’ve learned how to take derivatives of all sorts of crazy functions. Recall one of our first examples: f(A) = A2, (8) where A is a matrix. To differentiate this function, we had to go back to the drawing board, and ask: Question 50. If we perturb the input slightly, how does the output change? To this end, we wrote down something like: δf = (A + δA)2 −A2 = A(δA) + (δA)A + (δA)2 | {z } neglected . (9) We called δf and δA differentials in the limit where δA became arbitrarily small. We then had to ask: Question 51. What terms in the differential can we neglect? We decided that (δA)2 should be neglected, justifying this by the fact that (δA)2 is “higher-order”. We were left with the derivative operator δA 7→A(δA)+(δA)A: the best possible linear approximation to f in a neighbourhood of A. At a high level, the main challenge here was dealing with complicated input and output spaces: f was matrix-valued, and also matrix-accepting. We had to ask ourselves: in this case, what should the notion of a derivative even mean? In this lecture, we will face a similar challenge, but with an even weirder type of function.

## Key terms
- **function** — 5 mentions
- **output** — 5 mentions
- **input** — 4 mentions
- **derivative** — 4 mentions
- **random** — 4 mentions
- **question** — 3 mentions
- **complicated** — 3 mentions
- **real** — 3 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=79|Matrix Calculus.pdf p. 79]]

## Liens
- Up: [[research/matrix-calculus/derivatives-of-random-functions]]
- Next: [[research/matrix-calculus/stochastic-programs]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
