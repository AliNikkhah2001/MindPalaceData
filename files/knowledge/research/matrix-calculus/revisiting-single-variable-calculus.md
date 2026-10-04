---
title: "Revisiting single-variable calculus"
summary: "§Derivatives as Linear Operators › Revisiting single-variable: 𝑥 small change in “output” small change in “input” linear term higher-order terms δ𝑓= 𝑓𝑥+ 𝛿𝑥−𝑓𝑥= 𝑓! 𝑥𝛿𝑥 + 𝑜(𝛿𝑥) Figure 1: The essence of a derivative is linearization: predicting a small change δf in the output f(x) f"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "9-9"
---

# Revisiting single-variable calculus

§Derivatives as Linear Operators › Revisiting single-variable calculus · pp. 9–9 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
𝑓𝑥 𝑥 𝑥+ 𝛿𝑥 𝑓𝑥+ 𝛿𝑥 𝛿𝑥 𝛿𝑓 slope 𝑓! 𝑥 small change in “output” small change in “input” linear term higher-order terms δ𝑓= 𝑓𝑥+ 𝛿𝑥−𝑓𝑥= 𝑓! 𝑥𝛿𝑥 + 𝑜(𝛿𝑥) Figure 1: The essence of a derivative is linearization: predicting a small change δf in the output f(x) from a small change δx in the input x, to first order in δx. We are now going to revisit the notion of a derivative in a way that we can generalize to higher-order arrays and other vector spaces. We will get into more detail on differentiation as a linear operator, and in particular, will dive deeper into some of the facts we have stated thus far. In a first-semester single-variable calculus course (like 18.01 at MIT), the derivative f ′(x) is introduced as the slope of the tangent line at the point (x, f(x)), which can also be viewed as a linear approximation of f near x. In particular, as depicted in Fig. 1, this is equivalent to a prediction of the change δf in the “output” of f(x) from a small change δx in the “input” to first order (linear) in δx: δf = f(x + δx) −f(x) = f ′(x) δx + (higher-order terms) | {z } o(δx) . We can more precisely express these higher-order terms using asymptotic “little-o” notation “o(δx)”, which denotes any function whose magnitude shrinks much faster than |δx| as δx →0, so that for sufficiently small δx it is negligible compared to the linear f ′(x) δx term.

## Key terms
- **small** — 7 mentions
- **term** — 7 mentions
- **change** — 6 mentions
- **linear** — 5 mentions
- **higher-order** — 5 mentions
- **derivative** — 5 mentions
- **output** — 3 mentions
- **input** — 3 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=9|Matrix Calculus.pdf p. 9]]

## Liens
- Up: [[research/matrix-calculus/derivatives-as-linear-operators]]
- Next: [[research/matrix-calculus/linear-operators]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
