---
title: "Forward sensitivity analysis of ODEs"
summary: "§Differentiating ODE solutions › Sensitivity analysis of ODE : In both cases, since these are scalar-valued functions, for optimization/fitting one would like to know the gradient ∇pg or ∇pG, such that, as usual, g(u(p + dp, t), t) −g(u(p, t), t) = (∇pg)T dp so that ±∇pg is the s"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "68-68"
---

# Forward sensitivity analysis of ODEs

§Differentiating ODE solutions › Sensitivity analysis of ODE solutions › Forward sensitivity analysis of ODEs · pp. 68–68 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
data at a sequence of discrete times. In both cases, since these are scalar-valued functions, for optimization/fitting one would like to know the gradient ∇pg or ∇pG, such that, as usual, g(u(p + dp, t), t) −g(u(p, t), t) = (∇pg)T dp so that ±∇pg is the steepest ascent/descent direction for maximization/minimization of g, respectively. It is worth emphasizing that gradients (which we only define for scalar-valued functions) have the same shape as their inputs p, so ∇pg is a vector of length N (the number of parameters) that depends on p and t. These are “just derivatives,” but probably you can see the difficulty: if we don’t have a formula (explicit solution) for u(p, t), only some numerical software that can crank out numbers for u(p, t) given any parameters p and t, how do we apply differentiation rules to find ∂u/∂p or ∇pg? Of course, we could use finite differences as in Sec. 4-just crank through numerical solutions for p and p + δp and subtract them-but that will be quite slow if we want to differentiate with respect to many parameters (N ≫1), not to mention giving potentially poor accuracy. In fact, people often have huge numbers of parameters inside an ODE that they want to differentiate.

## Key terms
- **parameters** — 7 mentions
- **derivative** — 7 mentions
- **these** — 5 mentions
- **solution** — 5 mentions
- **function** — 5 mentions
- **time** — 5 mentions
- **number** — 4 mentions
- **turns** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=68|Matrix Calculus.pdf p. 68]]

## Liens
- Up: [[research/matrix-calculus/sensitivity-analysis-of-ode-solutions]]
- Next: [[research/matrix-calculus/reverse-adjoint-sensitivity-analysis-of-odes]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
