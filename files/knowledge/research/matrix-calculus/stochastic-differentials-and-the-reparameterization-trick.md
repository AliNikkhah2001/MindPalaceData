---
title: "Stochastic differentials and the reparameterization trick"
summary: "§Derivatives of Random Functions › Stochastic differentials a: satisfying E[X′(p)] = E[X(p)]′ = ∂E[X(p)] ∂p . (11) Of course, there are infinitely many such estimators. For example, given any estimator X′(p) we can add any other random variable that has zero average without chang"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "81-83"
---

# Stochastic differentials and the reparameterization trick

§Derivatives of Random Functions › Stochastic differentials and the reparameterization trick · pp. 81–83 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
satisfying E[X′(p)] = E[X(p)]′ = ∂E[X(p)] ∂p . (11) Of course, there are infinitely many such estimators. For example, given any estimator X′(p) we can add any other random variable that has zero average without changing the expectation value. But in practice there are two additional considerations: (1) we want X′(p) to be easy to compute/sample (about as easy as X(p)), and (2) we want the variance (the “spread”) of X′(p) to be small enough that we don’t need too many samples to estimate its average accurately (hopefully no worse than estimating E[X(p)]). Let’s begin by answering our first question (Question 50): how does X(p) respond to a change in p? Let us consider a specific p and write down a stochastic differential, taking a small but non-infinitesimal δp to avoid thinking about infinitesimals for now: δX(p) = X(p + δp) −X(p), (12) where δp represents an arbitrary small change in p. What sort of object is δX(p)? Since we’re subtracting two random variables, it ought to itself be a random variable. However, δX(p) is still not fully specified! We have only specified the marginal distributions of X(p) and X(p+δp): to be able to subtract the two, we need to know their joint distribution.

## Key terms
- **sample** — 35 mentions
- **random** — 17 mentions
- **julia** — 17 mentions
- **function** — 14 mentions
- **distribution** — 11 mentions
- **variable** — 9 mentions
- **method** — 9 mentions
- **probability** — 9 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=81|Matrix Calculus.pdf p. 81]]

## Liens
- Up: [[research/matrix-calculus/derivatives-of-random-functions]]
- ← Prev: [[research/matrix-calculus/stochastic-programs]]
- Next: [[research/matrix-calculus/handling-discrete-randomness]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
