---
title: "General second derivatives: Bilinear maps"
summary: "§Second Derivatives, Bilinear Maps, and Hessian Matrices › Ge: If we think of the Hessian as the Jacobian of ∇f, this tells us that H dx predicts the change in ∇f to first order: d(∇f) = ∇f|x+dx −∇f|x = H dx ."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "88-91"
---

# General second derivatives: Bilinear maps

§Second Derivatives, Bilinear Maps, and Hessian Matrices › General second derivatives: Bilinear maps · pp. 88–91 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
If we think of the Hessian as the Jacobian of ∇f, this tells us that H dx predicts the change in ∇f to first order: d(∇f) = ∇f|x+dx −∇f|x = H dx . Note that ∇f|x+dx means ∇f evaluated at x + dx, which is very different from df = (∇f)T dx, where we act f ′(x) = (∇f)T on dx. Instead of thinking of H of predicting the first-order change in ∇f, however, we can also think of it as predicting the second-order change in f, a quadratic approximation (which could be viewed as the first three terms in a multidimensional Taylor series): f(x + δx) = f(x) + (∇f)T δx + 1 2δxT H δx + o(∥δx∥2) , where both ∇f and H are evaluated at x, and we have switched from an infinitesimal dx to a finite change δx so that we emphasize the viewpoint of an approximation where terms higher than second-order in ∥δx∥are dropped. You can derive this in a variety of ways, e.g. by taking the derivative of both sides with respect to δx to reproduce ∇f|x+δx = ∇f|x + H δx + o(δx): a quadratic approximation for f corresponds to a linear approximation for ∇f. Related to this equation, another useful (and arguably more fundamental) relation that we can derive (and will derive much more generally below) is: dxT Hdx′ = f(x + dx + dx′) + f(x) −f(x + dx) −f(x + dx′) = f ′′(x)[dx, dx′] where dx and dx′ are two independent “infinitesimal” directions and we have dropped terms of higher than second order.

## Key terms
- **vector** — 19 mentions
- **change** — 16 mentions
- **matrix** — 14 mentions
- **derivative** — 10 mentions
- **linear** — 10 mentions
- **bilinear** — 10 mentions
- **function** — 10 mentions
- **jacobian** — 9 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=88|Matrix Calculus.pdf p. 88]]

## Liens
- Up: [[research/matrix-calculus/second-derivatives-bilinear-maps-and-hessian-matrices]]
- ← Prev: [[research/matrix-calculus/hessian-matrices-of-scalar-valued-functions]]
- Next: [[research/matrix-calculus/generalized-quadratic-approximation]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
