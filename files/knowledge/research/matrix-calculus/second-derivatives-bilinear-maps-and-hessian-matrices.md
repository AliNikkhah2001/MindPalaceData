---
title: "Second Derivatives, Bilinear Maps, and Hessian Matrices"
summary: "§Second Derivatives, Bilinear Maps, and Hessian Matrices: Second Derivatives, Bilinear Maps, and Hessian Matrices In this chapter, we apply the principles of this course to second derivatives, which are conceptually just derivatives of derivatives but turn out to have many intere"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "87-95"
---

# Second Derivatives, Bilinear Maps, and Hessian Matrices

§Second Derivatives, Bilinear Maps, and Hessian Matrices · pp. 87–95 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Second Derivatives, Bilinear Maps, and Hessian Matrices In this chapter, we apply the principles of this course to second derivatives, which are conceptually just derivatives of derivatives but turn out to have many interesting ramifications. We begin with a (probably) familiar case of scalar-valued functions from multi-variable calculus, in which the second derivative is simply a matrix called the Hessian. Subsequently, however, we will show that similar principles can be applied to more complicated input and output spaces, generalizing to a notion of f ′′ as a symmetric bilinear map. Recall that for a function f(x) ∈R that maps column vectors x ∈Rn to scalars (f : Rn 7→R), the first derivative f ′ can be expressed in terms of the familiar gradient ∇f = (f ′)T of multivariable calculus: ∇f =       ∂f ∂x1 ∂f ∂x2... ∂f ∂xn       . If we think of ∇f as a new (generally nonlinear) function mapping x ∈Rn 7→∇f ∈Rn, then its derivative is an n × n Jacobian matrix (a linear operator mapping vectors to vectors), which we can write down explicitly in terms of second derivatives of f: (∇f)′ =     ∂2f ∂x2 · · · ∂2f ∂xn∂x1 ... ... ... ∂2f ∂x1∂xn · · · ∂2f ∂xn∂xn    = H . This matrix, denoted here by H, is known as the Hessian of f, which has entries: Hi,j = ∂2f ∂xj∂xi = ∂2f ∂xi∂xj = Hj,i .

## Key terms
- **vector** — 22 mentions
- **derivative** — 19 mentions
- **matrix** — 16 mentions
- **change** — 16 mentions
- **function** — 12 mentions
- **hessian** — 10 mentions
- **linear** — 10 mentions
- **second** — 9 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=87|Matrix Calculus.pdf p. 87]]

## Liens
- ← Prev: [[research/matrix-calculus/derivatives-of-random-functions]]
- Next: [[research/matrix-calculus/derivatives-of-eigenproblems]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
