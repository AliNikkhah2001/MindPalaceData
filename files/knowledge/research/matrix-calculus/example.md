---
title: "Example"
summary: "§Differentiating ODE solutions › Example: To eliminate the ∂u ∂p T term, therefore, we make the choice v(T) = 0 . Instead of an initial condition, our adjoint ODE has a final condition."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "71-72"
---

# Example

§Differentiating ODE solutions › Example · pp. 71–72 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
don’t depend on p). To eliminate the ∂u ∂p T term, therefore, we make the choice v(T) = 0 . Instead of an initial condition, our adjoint ODE has a final condition. That’s no problem for a numerical solver: it just means that the adjoint ODE is integrated backwards in time, starting from t = T and working down to t = 0. Once we have solved the adjoint ODE for v(t), we can plug it into our equation for G′ to obtain our gradient by a simple integral: ∇pG = (G′)T = − ∂u0 ∂p T v(0) + Z T "∂g ∂p T − ∂f ∂p T v # dt . (If you want to be fancy, you can compute this R T 0 simultaneously with v itself, by augmenting the adjoint ODE with an additional set of unknowns and equations representing the G′ integrand. But that’s mainly just a computational convenience and doesn’t change anything fundamental about the process.) The only remaining annoyance is that the adjoint ODE depends on u(p, t) for all t ∈[0, T]. Normally, if we are solving the “forward” ODE for u(p, t) numerically, we can “march” the solution u forwards in time and only store the solution at a few of the most recent timesteps. Since the adjoint ODE starts at t = T, however, we can only start integrating v after we have completed the calculation of u.

## Key terms
- **adjoint** — 8 mentions
- **time** — 6 mentions
- **solve** — 6 mentions
- **condition** — 5 mentions
- **numerically** — 5 mentions
- **solution** — 5 mentions
- **computer** — 5 mentions
- **forward** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=71|Matrix Calculus.pdf p. 71]]

## Liens
- Up: [[research/matrix-calculus/differentiating-ode-solutions]]
- ← Prev: [[research/matrix-calculus/sensitivity-analysis-of-ode-solutions]]
- Next: [[research/matrix-calculus/further-reading]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
