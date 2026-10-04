---
title: "Functionals: Mapping functions to scalars"
summary: "§Calculus of Variations › Functionals: Mapping functions to s: In this lecture, we will apply our derivative machinery to a new type of input: neither scalars, nor column vectors, nor matrices, but rather the inputs will be functions u(x), which form a perfectly good vector space"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "74-74"
---

# Functionals: Mapping functions to scalars

§Calculus of Variations › Functionals: Mapping functions to scalars · pp. 74–74 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
In this lecture, we will apply our derivative machinery to a new type of input: neither scalars, nor column vectors, nor matrices, but rather the inputs will be functions u(x), which form a perfectly good vector space (and can even have norms and inner products).12 It turns out that there are lots of amazing applications for differentiating with respect to functions, and the resulting techniques are sometimes called the “calculus of variations” and/or “Frechét” derivatives. Example 44 For example, consider functions u(x) that map x ∈[0, 1] →u(x) ∈R. We may then define the function f: f(u) = Z 1 sin(u(x)) dx. Such a function, mapping an input function u to an output number, is sometimes called a “functional.” What is f ′ or ∇f in this case? Recall that, given any function f, we always define the derivative as a linear operator f ′(u) via the equation: df = f(u + du) −f(u) = f ′(u)[du] , where now du denotes an arbitrary “small-valued” function du(x) that represents a small change in u(x), as depicted in Fig. 12 for the analogous case of a non-infinitesimal δu(x). Here, we may compute this via linearization of the integrand: df = f(u + du) −f(u) = Z 1 sin(u(x) + du(x)) −sin(u(x)) dx = Z 1 cos(u(x)) du(x) dx = f ′(u)[du] , where in the last step we took du(x) to be arbitrarily small13 so that we could linearize sin(u + du) to first-order in du(x).

## Key terms
- **function** — 15 mentions
- **define** — 5 mentions
- **derivative** — 4 mentions
- **input** — 4 mentions
- **inner** — 4 mentions
- **product** — 4 mentions
- **perfectly** — 3 mentions
- **good** — 3 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=74|Matrix Calculus.pdf p. 74]]

## Liens
- Up: [[research/matrix-calculus/calculus-of-variations]]
- Next: [[research/matrix-calculus/inner-products-of-functions]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
