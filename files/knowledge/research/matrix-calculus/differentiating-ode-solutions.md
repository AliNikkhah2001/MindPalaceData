---
title: "Differentiating ODE solutions"
summary: "§Differentiating ODE solutions: In this lecture, we will consider the problem of differentiating the solution of ordinary differential equations (ODEs) with respect to parameters that appear in the equations and/or initial conditions."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "65-73"
---

# Differentiating ODE solutions

§Differentiating ODE solutions · pp. 65–73 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
In this lecture, we will consider the problem of differentiating the solution of ordinary differential equations (ODEs) with respect to parameters that appear in the equations and/or initial conditions. This is as important topic in a surprising number of practical applications, such as evaluating the effect of uncertainties, fitting experimental data, or machine learning (which is increasingly combining ODE models with neural networks). As in previous lectures, we will find that there are crucial practical distinctions between “forward” and “reverse” (“adjoint”) techniques for computing these derivatives, depending upon the number of parameters and desired outputs. Although a basic familiarity with the concept of an ODE will be helpful to readers of this lecture, we will begin with a short review in order to establish our notation and terminology. The video lecture on this topic for IAP 2023 was given by Dr. Frank Schäfer (MIT). These notes follow the same basic approach, but differ in some minor notational details. An ordinary differential equation (ODE) is an equation for a function u(t) of “time”8 t ∈R in terms of one or more derivatives, most commonly in the first-order form du dt = f(u, t) for some right-hand-side function f.

## Key terms
- **solution** — 29 mentions
- **time** — 23 mentions
- **parameters** — 18 mentions
- **function** — 18 mentions
- **derivative** — 16 mentions
- **odes** — 12 mentions
- **these** — 10 mentions
- **depend** — 9 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=65|Matrix Calculus.pdf p. 65]]

## Liens
- ← Prev: [[research/matrix-calculus/forward-and-reverse-mode-automatic-differentiation]]
- Next: [[research/matrix-calculus/calculus-of-variations]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
