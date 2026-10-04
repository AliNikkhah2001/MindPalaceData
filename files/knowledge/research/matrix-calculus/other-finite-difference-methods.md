---
title: "Other finite-difference methods"
summary: "§Finite-Difference Approximations › Other finite-difference m: The truncation error is the inaccuracy arising from the fact that the input perturbation δx is not infinitesimal: we are computing a difference, not a derivative."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "32-33"
---

# Other finite-difference methods

§Finite-Difference Approximations › Other finite-difference methods · pp. 32–33 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
The truncation error is the inaccuracy arising from the fact that the input perturbation δx is not infinitesimal: we are computing a difference, not a derivative. If the truncation error in the derivative scales proportional ∥δx∥n, we call the approximation n-th order accurate. For forward differences, here, the order is n=1. Why? For any f(x) with a nonzero second derivative (think of the Taylor series), we have f(x + δx) = f(x) + f ′(x)δx + (terms proportional to ∥δx∥2) + o(∥δx∥2) | {z } i.e. higher-order terms That is, the terms we dropped in our forward-difference approximations are proportional to ∥δx∥2. But that means that the relative error is linear: relative error = ∥f(x + δx) −f(x) −f ′(x)δx∥ ∥f ′(x)δx∥ = (terms proportional to ∥δx∥2) + o(∥δx∥2) proportional to ∥δx∥ = (terms proportional to ∥δx∥) + o(∥δx∥) This is first-order accuracy. Truncation error in a finite-difference approximation is the inherent error in the formula for non-infinitesimal δx. Does that mean we should just make δx as small as we possibly can? The reason why the error increased for very small δA was due to roundoff errors. The computer only stores a finite number of significant digits (about 15 decimal digits) for each real number and rounds off the rest on each operation - this is called floating-point arithmetic.

## Key terms
- **error** — 14 mentions
- **difference** — 9 mentions
- **digits** — 8 mentions
- **proportional** — 7 mentions
- **truncation** — 6 mentions
- **terms** — 5 mentions
- **finite-difference** — 5 mentions
- **finite** — 5 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=32|Matrix Calculus.pdf p. 32]]

## Liens
- Up: [[research/matrix-calculus/finite-difference-approximations]]
- ← Prev: [[research/matrix-calculus/roundoff-error]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
