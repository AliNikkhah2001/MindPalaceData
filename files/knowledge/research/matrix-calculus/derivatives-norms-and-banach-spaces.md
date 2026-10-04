---
title: "Derivatives, Norms, and Banach spaces"
summary: "§Derivatives in General Vector Spaces › Derivatives, Norms, a: We have that df = xT dA y = tr(xT dA y) = tr(yxT dA) = xyT |{z} ∇f , dA . More generally, for any scalar-valued function f(A), from the definition of Frobenius inner product it follows that: df = f(A + dA) −f(A) = ⟨∇f"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "37-38"
---

# Derivatives, Norms, and Banach spaces

§Derivatives in General Vector Spaces › Derivatives, Norms, and Banach spaces · pp. 37–38 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Example 36 Fix some constant x ∈Rm, y ∈Rn, and consider the function f : Rm×n →R given by f(A) = xT Ay. What is ∇f? We have that df = xT dA y = tr(xT dA y) = tr(yxT dA) = xyT |{z} ∇f , dA . More generally, for any scalar-valued function f(A), from the definition of Frobenius inner product it follows that: df = f(A + dA) −f(A) = ⟨∇f, dA⟩= X i,j (∇f)i,j dAi,j , and hence the components of the gradient are exactly the elementwise derivatives (∇f)i,j = ∂f ∂Ai,j , similar to the component-wise definition of the gradient vector from multivariable calculus! But for non-trivial matrix-input functions f(A) it can be extremely awkward to take the derivative with respect to each entry of A individually. Using the “holistic” matrix inner-product definition, we will soon be able to compute even more complicated matrix-valued gradients, including ∇(det A)! We have been using the term “norm” throughout this class, but what technically is a norm? Of course, there are familiar examples such as the Euclidean (“ℓ2”) norm ∥x∥= pP k x2 k for x ∈Rn, but it is useful to consider how this concept generalizes to other vector spaces. It turns out, in fact, that norms are crucial to the definition of a derivative!

## Key terms
- **space** — 14 mentions
- **norm** — 10 mentions
- **vector** — 7 mentions
- **banach** — 6 mentions
- **function** — 5 mentions
- **derivative** — 5 mentions
- **called** — 4 mentions
- **inner** — 3 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=37|Matrix Calculus.pdf p. 37]]

## Liens
- Up: [[research/matrix-calculus/derivatives-in-general-vector-spaces]]
- ← Prev: [[research/matrix-calculus/a-simple-matrix-dot-product-and-norm]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
