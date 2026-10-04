---
title: "Example: Minimizing arc length"
summary: "§Calculus of Variations › Example: Minimizing arc length: However, if we define a weighted discrete inner product ⟨u, v⟩= Pn k=1 ukvk∆x, then, according to Sec. 5, this changes the definition of the gradient, and in fact will remove the ∆x term to correspond to the continuous ver"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "76-76"
---

# Example: Minimizing arc length

§Calculus of Variations › Example: Minimizing arc length · pp. 76–76 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
just a sum without a ∆x. However, if we define a weighted discrete inner product ⟨u, v⟩= Pn k=1 ukvk∆x, then, according to Sec. 5, this changes the definition of the gradient, and in fact will remove the ∆x term to correspond to the continuous version. We now consider a more tricky example with an intuitive geometric interpretation. Example 46 Let u be a differentiable function on [0, 1] and consider the functional f(u) = Z 1 p 1 + u′(x)2 dx. Solve for ∇f when u(0) = u(1) = 0. Geometrically, you learned in first-year calculus that this is simply the length of the curve u(x) from x = 0 to x = 1. To differentiate this, first notice that ordinary single-variable calculus gives us the linearization d p 1 + v2  = p 1 + (v + dv)2 − p 1 + v2 = p 1 + v2 ′ dv = v √ 1 + v2 dv . Therefore, df = f(u + du) −f(u) = Z 1 p 1 + (u + du)′2 − p 1 + u′2  dx = Z 1 u′ √ 1 + u′2 du′dx. However, this is a linear operator on du′ and not (directly) on du. Abstractly, this is fine, because du′ is itself a linear operation on du, so we have f ′(u)[du] as the composition of two linear operations. However, it is more revealing to rewrite it explicitly in terms of du, for example in order to define ∇f. To accomplish this, we can apply integration by parts to obtain f ′(u)[du] = Z 1 u′ √ 1 + u′2 du′dx = u′ √ 1 + u′2 du − Z 1  u′ √ 1 + u′2 ′ du dx .

## Key terms
- **term** — 3 mentions
- **linear** — 3 mentions
- **define** — 2 mentions
- **consider** — 2 mentions
- **function** — 2 mentions
- **functional** — 2 mentions
- **geometrically** — 2 mentions
- **calculus** — 2 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=76|Matrix Calculus.pdf p. 76]]

## Liens
- Up: [[research/matrix-calculus/calculus-of-variations]]
- ← Prev: [[research/matrix-calculus/inner-products-of-functions]]
- Next: [[research/matrix-calculus/euler-lagrange-equations]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
