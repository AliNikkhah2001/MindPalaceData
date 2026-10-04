---
title: "Further reading"
summary: "§Differentiating ODE solutions › Further reading: Problem 43 Suppose that G(p) takes the form of a sum of K terms: G(p) = K X k=1 gk(p, u(p, tk)) for times tk ∈(0, T) and functions gk(p, u)."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "73-73"
---

# Further reading

§Differentiating ODE solutions › Further reading · pp. 73–73 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Problem 43 Suppose that G(p) takes the form of a sum of K terms: G(p) = K X k=1 gk(p, u(p, tk)) for times tk ∈(0, T) and functions gk(p, u). For example, this could arise in least-square fitting of experimental data u∗(tk) at K discrete times, with gk(u(p, tk)) = ∥u∗(tk) −u(p, tk)∥2 measuring the squared difference between u(p, tk) and the measured data at time tk. 1. Show that such a G(p) can be expressed as a special case of our formulation in this chapter, by defining our function g(u, t) using a sum of Dirac delta functions δ(t −tk). 2. Explain how this affects the adjoint solution v(t): in particular, how the introduction of delta-function terms on the right-hand side of dv/dt causes v(t) to have a sequence of discontinuous jumps. (In several popular numerical ODE solvers, such discontinuities can be incorporated via discrete-time “callbacks”.) 3. Explain how these delta functions may also introduce a summation into the computation of ∇pG, but only if gk depends explicitly on p (not just via u). A classic reference on reverse/adjoint differentiation of ODEs (and generalizations thereof), using notation sim- ilar to that used today (except that the adjoint solution v is denoted λ(t), in an homage to Lagrange multipliers), is Cao et al.

## Key terms
- **adjoint** — 6 mentions
- **solution** — 6 mentions
- **odes** — 5 mentions
- **https** — 5 mentions
- **function** — 4 mentions
- **recurrence** — 4 mentions
- **exactly** — 4 mentions
- **approximate** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=73|Matrix Calculus.pdf p. 73]]

## Liens
- Up: [[research/matrix-calculus/differentiating-ode-solutions]]
- ← Prev: [[research/matrix-calculus/example]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
