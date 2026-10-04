---
title: "Handling discrete randomness"
summary: "§Derivatives of Random Functions › Handling discrete randomne: julia> mean(X′(10.0) for i in 1:10000) 1.011689946421105 So X′(p) does indeed average to 1, which makes sense since the expectation of Exp(p) is p, which has derivative 1 for any choice of p."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "84-86"
---

# Handling discrete randomness

§Derivatives of Random Functions › Handling discrete randomness · pp. 84–86 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
julia> mean(X′(10.0) for i in 1:10000) 1.011689946421105 So X′(p) does indeed average to 1, which makes sense since the expectation of Exp(p) is p, which has derivative 1 for any choice of p. However, the crux is that this notion of derivative also works for more complicated random variables that can be formed via composition of simple ones such as an exponential random variable. In fact, it turns out to obey the same chain rule as usual! Let’s demonstrate this. Using the dual numbers introduced in Chapter 8, we can differentiate the expectation of the square of a sample from an exponential distribution without having an analytic expression for this quantity. (The expression for X′ we derived is already implemented as a dual-number rule in Julia by the ForwardDiff.jl package.) The primal and dual values of the outputted dual number are samples from the joint distribution of (X(p), X′(p)). julia> using Distributions, ForwardDiff: Dual julia> sample_X(p) = rand(Exponential(p))^2 sample_X (generic function with 1 method) julia> sample_X(Dual(10.0, 1.0)) # sample a single dual number! Dual{Nothing}(153.74964559529033,30.749929119058066) julia> # obtain the derivative! julia> mean(sample_X(Dual(10.0, 1.0)).partials[1] for i in 1:10000) 40.016569793650525 Using the “reparameterization trick” to form a gradient estimator, as we have done here, is a fairly old idea.

## Key terms
- **julia** — 22 mentions
- **sample** — 14 mentions
- **derivative** — 11 mentions
- **probability** — 11 mentions
- **dual** — 9 mentions
- **variable** — 8 mentions
- **bernoulli** — 8 mentions
- **triple** — 8 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=84|Matrix Calculus.pdf p. 84]]

## Liens
- Up: [[research/matrix-calculus/derivatives-of-random-functions]]
- ← Prev: [[research/matrix-calculus/stochastic-differentials-and-the-reparameterization-trick]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
