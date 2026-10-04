---
title: "Where We Go From Here"
summary: "§Where We Go From Here: There are many topics that we did not have time to cover, even in 16 hours of lectures. If you came into this class thinking that taking derivatives is easy and you already learned everything there is to know about it in first-year calculus, hopefully we’v"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "100-101"
---

# Where We Go From Here

§Where We Go From Here · pp. 100–101 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
There are many topics that we did not have time to cover, even in 16 hours of lectures. If you came into this class thinking that taking derivatives is easy and you already learned everything there is to know about it in first-year calculus, hopefully we’ve convinced you that it is an enormously rich subject that is impossible to exhaust in a single course. Some of the things it might have been nice to include are: • When automatic differentiation (AD) hits something it cannot handle, you may have to write a custom Jacobian-vector product (a “Jvp,” “frule,” or “pushforward”) in forward-mode, and/or a custon row vector- Jacobian product (a “vJp,” “rrule,” “pullback,” or “JacobianT -vector product”) in reverse-mode. In Julia with Zygote AD, this is done using the ChainRules packages. In Python with JAX, this is done with jax.custon_jvp and/or jax.custon_vjp respectively. In principle, this is straightforward, but the APIs can take some getting used to because the of the generality that they support. • For functions f(z) with complex arguments z (i.e. complex vector spaces), you cannot take “ordinary” complex derivatives whenever the function involves the conjugate z, for example, |z|, Re(z), and Im(z).

## Key terms
- **derivative** — 10 mentions
- **function** — 7 mentions
- **eigenvalue** — 6 mentions
- **calculus** — 4 mentions
- **complex** — 4 mentions
- **problem** — 4 mentions
- **course** — 3 mentions
- **write** — 3 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=100|Matrix Calculus.pdf p. 100]]

## Liens
- ← Prev: [[research/matrix-calculus/derivatives-of-eigenproblems]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
