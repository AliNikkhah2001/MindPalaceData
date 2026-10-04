---
title: "Reverse mode"
summary: "§Differentiating ODE solutions › Example › Reverse mode: The Jacobian matrix ∂u ∂p =  ∂u ∂p1 ∂u ∂p2 ∂u ∂p3  is simply a row vector, and satisfies our “forward-mode” ODE: ∂ ∂t ∂u ∂p  = ∂f ∂u ∂u ∂p + ∂f ∂p = (p2 + 2p3u) ∂u ∂p +  u u2  for the initial condition ∂u ∂p t=0 = ∂u0"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "72-72"
---

# Reverse mode

§Differentiating ODE solutions › Example › Reverse mode · pp. 72–72 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
The Jacobian matrix ∂u ∂p =  ∂u ∂p1 ∂u ∂p2 ∂u ∂p3  is simply a row vector, and satisfies our “forward-mode” ODE: ∂ ∂t ∂u ∂p  = ∂f ∂u ∂u ∂p + ∂f ∂p = (p2 + 2p3u) ∂u ∂p +  u u2  for the initial condition ∂u ∂p t=0 = ∂u0 ∂p = 0. This is an inhomogeneous system of three coupled linear ODEs, which might look more conventional if we simply transpose both sides: ∂ ∂t    ∂u ∂p1 ∂u ∂p2 ∂u ∂p3    | {z } (∂u/∂p)T = (p2 + 2p3u)    ∂u ∂p1 ∂u ∂p2 ∂u ∂p3   +    u u2   . The fact that this depends on our “forward” solution u(p, t) makes it not so easy to solve by hand, but a computer can solve it numerically with no difficulty. On a computer, we would probably solve for u and ∂u/∂psimultaneously by combining the two ODEs into a single ODE with 4 components: ∂ ∂t u (∂u/∂p)T ! =       p1 + p2u + p3u2 (p2 + 2p3u) (∂u/∂p)T +    u u2          . Given ∂u/∂p, we can then plug this into the chain rule for G: ∇pG = 2 Z T [u(p, t) −u∗(t)] ∂u ∂p T dt (again, an integral that a computer could evaluate numerically). In reverse mode, we have an adjoint solution v(t) ∈R (the same shape as u) which solves our adjoint equation ∂v dt = ∂g ∂u T − ∂f ∂u T v = 2 [u(p, t) −u∗(t)] −(p2 + 2p3u) v with a final condition v(T) = 0.

## Key terms
- **solve** — 5 mentions
- **computer** — 4 mentions
- **solution** — 3 mentions
- **numerically** — 3 mentions
- **simply** — 2 mentions
- **condition** — 2 mentions
- **odes** — 2 mentions
- **forward** — 2 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=72|Matrix Calculus.pdf p. 72]]

## Liens
- Up: [[research/matrix-calculus/example]]
- ← Prev: [[research/matrix-calculus/forward-mode]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
