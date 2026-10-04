---
title: "Forward- vs. Reverse-mode Differentiation"
summary: "§Forward and Reverse-Mode Automatic Differentiation › Forward: Take, for instance, the following sink/source computational graph. If x, y here are our sources, and z is our sink, we want to compute the sum of products of weights on paths from sources to sinks."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "61-64"
---

# Forward- vs. Reverse-mode Differentiation

§Forward and Reverse-Mode Automatic Differentiation › Forward- vs. Reverse-mode Differentiation · pp. 61–64 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
p x q z y a c d b later. Take, for instance, the following sink/source computational graph. If x, y here are our sources, and z is our sink, we want to compute the sum of products of weights on paths from sources to sinks. If we were using forward mode, we would need to compute the paths dca and dcb, which requires four multiplications (and then you would add them together). If we were using reverse mode, we would only need compute acd and bcd and sum them; notice reverse mode (since we need only compute cd once), only takes 3 multiplications. In general, this can more efficiently resolve certain types of problems, such as the source/sink one. In this section, we briefly summarize the relative benefits and drawbacks of these two approaches to computation of derivatives (whether worked out by hand or using AD software). From a mathematical point of view, the two approaches are mirror images, but from a computational point of view they are quite different, because computer programs normally proceed “forwards” in time from inputs to outputs. Suppose we are differentiating a function f : Rn 7→Rm, mapping n scalar inputs (an n-dimensional input) to m scalar outputs (an m-dimensional output).

## Key terms
- **function** — 25 mentions
- **mode** — 21 mentions
- **input** — 17 mentions
- **reverse** — 16 mentions
- **derivative** — 16 mentions
- **output** — 15 mentions
- **differentiation** — 15 mentions
- **forward** — 12 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=61|Matrix Calculus.pdf p. 61]]

## Liens
- Up: [[research/matrix-calculus/forward-and-reverse-mode-automatic-differentiation]]
- ← Prev: [[research/matrix-calculus/automatic-differentiation-via-computational-graphs]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
