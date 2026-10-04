---
title: "Nonlinear Optimization"
summary: "§Nonlinear Root-Finding, Optimization, and Adjoint Differenti: x f(x) initial x xnew f(xnew) root f(x) one Newton step Figure 5: Single step of the scalar Newton’s method to solve f(x) = 0 for an example nonlinear function f(x) = 2 cos(x) −x + x2/10."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "40-41"
---

# Nonlinear Optimization

§Nonlinear Root-Finding, Optimization, and Adjoint Differentiation › Optimization › Nonlinear Optimization · pp. 40–41 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
x f(x) initial x xnew f(xnew) root f(x) one Newton step Figure 5: Single step of the scalar Newton’s method to solve f(x) = 0 for an example nonlinear function f(x) = 2 cos(x) −x + x2/10. Given a starting guess (x = 2.3 in this example), we use f(x) and f ′(x) to form a linear (affine) approximation of f, and then our next step xnew is the root of this approximation. As long as the initial guess is not too far from the root, Newton’s method converges extremely rapidly to the exact root (black dot). • and then use this to update the value of x we linearized near-i.e., letting the new x be xnew = xold −f ′(x)−1f(x) . That’s it! Once we have the Jacobian, we can just solve a linear system on each step. This again converges amazingly fast, doubling the number of digits of accuracy in each step. (This is known as “quadratic convergence.”) However, there is a caveat: we need some starting guess for x, and the guess needs to be sufficiently close to the root for the algorithm to make reliable progress. (If you start with an initial x far from a root, Newton’s method can fail to converge and/or it can jump around in intricate and surprising ways-google “Newton fractal” for some fascinating examples.) This is a widely used and very practical application of Jacobians and derivatives!

## Key terms
- **step** — 13 mentions
- **function** — 7 mentions
- **downhill** — 7 mentions
- **root** — 6 mentions
- **newton** — 6 mentions
- **there** — 5 mentions
- **optimization** — 5 mentions
- **direction** — 5 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=40|Matrix Calculus.pdf p. 40]]

## Liens
- Up: [[research/matrix-calculus/optimization]]
- Next: [[research/matrix-calculus/engineering-physical-optimization]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
