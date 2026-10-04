---
title: "Sensitivity analysis of ODE solutions"
summary: "§Differentiating ODE solutions › Sensitivity analysis of ODE : and in many practical applications one must resort to approximate numerical solutions. Fortunately, if you supply a computer program that can compute f(u, t), there are mature and sophisticated software libraries10 wh"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "66-70"
---

# Sensitivity analysis of ODE solutions

§Differentiating ODE solutions › Sensitivity analysis of ODE solutions · pp. 66–70 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
and in many practical applications one must resort to approximate numerical solutions. Fortunately, if you supply a computer program that can compute f(u, t), there are mature and sophisticated software libraries10 which can compute u(t) from u(0) for any desired set of times t, to any desired level of accuracy (for example, to 8 significant digits). For example, the most basic numerical ODE method computes the solution at a sequence of times tn = n∆t for n = 0, 1, 2, . . . simply by approximating du dt = f(u, t) using the finite difference u(tn+1)−u(tn) ∆t ≈f(u(tn), tn), giving us the “explicit” timestep algorithm: u(tn+1) ≈u(tn) + ∆t f(u(tn), tn). Using this technique, known as “Euler’s method,” we can march the solution forward in time: starting from our initial condition u0, we compute u(t1) = u(∆t), then u(t2) = u(2∆t) from u(∆t), and so forth. Of course, this might be rather inaccurate unless we make ∆t very small, necessitating many timesteps to reach a given time t, and there can arise other subtleties like “instabilities” where the error may accumulate exponentially rapidly with each timestep. It turns out that Euler’s method is mostly obsolete: there are much more sophisticated algorithms that robustly produce accurate solutions with far less computational cost.

## Key terms
- **solution** — 25 mentions
- **time** — 21 mentions
- **parameter** — 20 mentions
- **function** — 14 mentions
- **derivative** — 12 mentions
- **scalar** — 12 mentions
- **odes** — 10 mentions
- **depend** — 9 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=66|Matrix Calculus.pdf p. 66]]

## Liens
- Up: [[research/matrix-calculus/differentiating-ode-solutions]]
- ← Prev: [[research/matrix-calculus/ordinary-differential-equations-odes]]
- Next: [[research/matrix-calculus/example]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
