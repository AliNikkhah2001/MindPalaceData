---
title: "Inner products of functions"
summary: "§Calculus of Variations › Inner products of functions: In this lecture, we will apply our derivative machinery to a new type of input: neither scalars, nor column vectors, nor matrices, but rather the inputs will be functions u(x), which form a perfectly good vector space (and ca"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "74-75"
---

# Inner products of functions

§Calculus of Variations › Inner products of functions · pp. 74–75 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
In this lecture, we will apply our derivative machinery to a new type of input: neither scalars, nor column vectors, nor matrices, but rather the inputs will be functions u(x), which form a perfectly good vector space (and can even have norms and inner products).12 It turns out that there are lots of amazing applications for differentiating with respect to functions, and the resulting techniques are sometimes called the “calculus of variations” and/or “Frechét” derivatives. Example 44 For example, consider functions u(x) that map x ∈[0, 1] →u(x) ∈R. We may then define the function f: f(u) = Z 1 sin(u(x)) dx. Such a function, mapping an input function u to an output number, is sometimes called a “functional.” What is f ′ or ∇f in this case? Recall that, given any function f, we always define the derivative as a linear operator f ′(u) via the equation: df = f(u + du) −f(u) = f ′(u)[du] , where now du denotes an arbitrary “small-valued” function du(x) that represents a small change in u(x), as depicted in Fig. 12 for the analogous case of a non-infinitesimal δu(x). Here, we may compute this via linearization of the integrand: df = f(u + du) −f(u) = Z 1 sin(u(x) + du(x)) −sin(u(x)) dx = Z 1 cos(u(x)) du(x) dx = f ′(u)[du] , where in the last step we took du(x) to be arbitrarily small13 so that we could linearize sin(u + du) to first-order in du(x).

## Key terms
- **function** — 20 mentions
- **inner** — 7 mentions
- **gradient** — 7 mentions
- **product** — 7 mentions
- **define** — 6 mentions
- **input** — 5 mentions
- **small** — 5 mentions
- **integral** — 5 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=74|Matrix Calculus.pdf p. 74]]

## Liens
- Up: [[research/matrix-calculus/calculus-of-variations]]
- ← Prev: [[research/matrix-calculus/functionals-mapping-functions-to-scalars]]
- Next: [[research/matrix-calculus/example-minimizing-arc-length]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
