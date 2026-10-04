---
title: "Reverse/adjoint sensitivity analysis of ODEs"
summary: "§Differentiating ODE solutions › Sensitivity analysis of ODE : Equating the right-hand sides of the two lines, we see that we have an ODE ∂ ∂t ∂u ∂p  = ∂f ∂u ∂u ∂p + ∂f ∂p for the derivative ∂u ∂p , whose initial condition is obtained simply by differentiating the initial condi"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "69-70"
---

# Reverse/adjoint sensitivity analysis of ODEs

§Differentiating ODE solutions › Sensitivity analysis of ODE solutions › Reverse/adjoint sensitivity analysis of ODEs · pp. 69–70 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
and second derivatives. Equating the right-hand sides of the two lines, we see that we have an ODE ∂ ∂t ∂u ∂p  = ∂f ∂u ∂u ∂p + ∂f ∂p for the derivative ∂u ∂p , whose initial condition is obtained simply by differentiating the initial condition u(p, 0) = u0(p) for u: ∂u ∂p t=0 = ∂u0 ∂p . We can therefore plug this into any ODE solver technique (usually numerical methods, unless we are extremely lucky and can solve this ODE analytically for a particular f) to find ∂u ∂p at any desired time t. Simple, right? The only thing that might seem a little weird here is the shape of the solution: ∂u ∂p is a linear operator, but how can the solution of an ODE be a linear operator? It turns out that there is nothing wrong with this, but it is helpful to think about a few examples: • If u, p ∈R are scalars (that is, we have a single scalar ODE with a single scalar parameter), then ∂u ∂p is just a (time-dependent) number, and our ODE for ∂u ∂p is an ordinary scalar ODE with an ordinary scalar initial condition. • If u ∈Rn (a “system” of n ODEs) and p ∈R is a scalar, then ∂u ∂p ∈Rn is another column vector and our ODE for ∂u ∂p is another system of n ODEs. So, we solve two ODEs of the same size n to obtain u and ∂u ∂p.

## Key terms
- **scalar** — 9 mentions
- **term** — 9 mentions
- **initial** — 7 mentions
- **condition** — 7 mentions
- **odes** — 6 mentions
- **vector** — 6 mentions
- **large** — 6 mentions
- **method** — 6 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=69|Matrix Calculus.pdf p. 69]]

## Liens
- Up: [[research/matrix-calculus/sensitivity-analysis-of-ode-solutions]]
- ← Prev: [[research/matrix-calculus/forward-sensitivity-analysis-of-odes]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
