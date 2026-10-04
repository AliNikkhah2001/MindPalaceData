---
title: "Naive symbolic differentiation"
summary: "§Forward and Reverse-Mode Automatic Differentiation › Naive s: Once we implement the multiplication rule for dual numbers in Julia, then ϵ2 = 0 follows from the special case a = c = 0 and b = d = 1: julia> ϵ = D(0,1) 0.0 + 1.0ϵ julia> ϵ * ϵ 0.0 + 0.0ϵ julia> ϵ^2 0.0 + 0.0ϵ (We di"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "54-55"
---

# Naive symbolic differentiation

§Forward and Reverse-Mode Automatic Differentiation › Naive symbolic differentiation · pp. 54–55 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Once we implement the multiplication rule for dual numbers in Julia, then ϵ2 = 0 follows from the special case a = c = 0 and b = d = 1: julia> ϵ = D(0,1) 0.0 + 1.0ϵ julia> ϵ * ϵ 0.0 + 0.0ϵ julia> ϵ^2 0.0 + 0.0ϵ (We didn’t define a rule for powers D(a, b)n, so how did it compute ϵ2? The answer is that Julia implements xn via repeated multiplication by default, so it sufficed to define the ∗rule.) Now, we can compute the derivative of the Babylonian algorithm at x = 49 as above by: julia> Babylonian(x + ϵ) 7.0 + 0.07142857142857142ϵ with the “infinitesimal part” being the derivative 0.5/ √ 49 = 0.0714 · · · . A nice thing about this dual-number viewpoint is that it corresponds directly to our notion of a derivative as linearization: f(x + ϵ) = f(x) + f ′(x)ϵ + (higher-order terms) , with the dual-number rule ϵ2 = 0 corresponding to dropping the higher-order terms. Forward-mode AD implements the exact analytical derivative by propagating chain rules, but it is completely different from what many people imagine AD might be: evaluating a program symbolically to obtain a giant symbolic expression, and then differentiating this giant expression to obtain the derivative. A basic issue with this approach is that the size of these symbolic expressions can quickly explode as the program runs.

## Key terms
- **iteration** — 9 mentions
- **derivative** — 8 mentions
- **julia** — 7 mentions
- **expression** — 7 mentions
- **rule** — 6 mentions
- **compute** — 5 mentions
- **babylonian** — 5 mentions
- **symbolic** — 5 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=54|Matrix Calculus.pdf p. 54]]

## Liens
- Up: [[research/matrix-calculus/forward-and-reverse-mode-automatic-differentiation]]
- ← Prev: [[research/matrix-calculus/automatic-differentiation-via-dual-numbers]]
- Next: [[research/matrix-calculus/automatic-differentiation-via-computational-graphs]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
