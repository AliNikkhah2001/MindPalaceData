---
title: "Easy forward-mode AD"
summary: "§Forward and Reverse-Mode Automatic Differentiation › Automat: of Newton’s method applied to t2 −x = 0): simply repeat t ←(t + x/t)/2 until t converges to √x to any desired accuracy. Each iteration has one addition and two divisions."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "51-52"
---

# Easy forward-mode AD

§Forward and Reverse-Mode Automatic Differentiation › Automatic Differentiation via Dual Numbers › Easy forward-mode AD · pp. 51–52 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
of Newton’s method applied to t2 −x = 0): simply repeat t ←(t + x/t)/2 until t converges to √x to any desired accuracy. Each iteration has one addition and two divisions. For illustration purposes, 10 iterations suffice. Here is a short program in Julia that implements this algorithm, starting with a guess of 1 and then performing N steps (defaulting to N = 10): julia> function Babylonian(x; N = 10) t = (1+x)/2 # one step from t=1 for i = 2:N # remaining N-1 steps t = (t + x/t) / 2 end return t end If we run this function to compute the square root of x = 4, we will see that it converges very quickly: for only N = 3 steps, it obtains the correct answer (2) to nearly 3 decimal places, and well before N = 10 steps it has converged to 2 within the limits of the accuracy of computer arithmetic (about 16 digits). In fact, it roughly doubles the number of correct digits on every step: julia> Babylonian(4, N=1) 2.5 julia> Babylonian(4, N=2) 2.05 julia> Babylonian(4, N=3) 2.000609756097561 julia> Babylonian(4, N=4) 2.0000000929222947 julia> Babylonian(4, N=10) 2.0 Of course, any first-year calculus student knows the derivative of the square root, (√x)′ = 0.5/√x, which we could compute here via 0.5 / Babylonian(x), but we want to know how we can obtain this derivative automati- cally, directly from the Babylonian algorithm itself.

## Key terms
- **julia** — 20 mentions
- **derivative** — 17 mentions
- **babylonian** — 12 mentions
- **value** — 11 mentions
- **rule** — 9 mentions
- **number** — 7 mentions
- **deriv** — 7 mentions
- **step** — 6 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=51|Matrix Calculus.pdf p. 51]]

## Liens
- Up: [[research/matrix-calculus/automatic-differentiation-via-dual-numbers]]
- ← Prev: [[research/matrix-calculus/example-babylonian-square-root]]
- Next: [[research/matrix-calculus/dual-numbers]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
