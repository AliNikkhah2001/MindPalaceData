---
title: "Revisiting multivariable calculus, Part 2: Vector-valued functions"
summary: "§Derivatives as Linear Operators › Revisiting multivariable c: We can do this directly from the definition. df = f(x + dx) −f(x) = (x + dx)T A(x + dx) −xT Ax =  xT Ax + dxT Ax + xT Adx + :higher order dxT Adx − xT Ax = xT (A + AT ) | {z } f ′(x)=(∇f)T dx =⇒∇f = (A + AT"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "14-15"
---

# Revisiting multivariable calculus, Part 2: Vector-valued functions

§Derivatives as Linear Operators › Revisiting multivariable calculus, Part 2: Vector-valued functions · pp. 14–15 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Example 10 Consider f(x) = xT Ax where x ∈Rn and A is a square n × n matrix, and thus f(x) ∈R. Compute df, f ′(x), and ∇f. We can do this directly from the definition. df = f(x + dx) −f(x) = (x + dx)T A(x + dx) −xT Ax =  xT Ax + dxT Ax + xT Adx + :higher order dxT Adx − xT Ax = xT (A + AT ) | {z } f ′(x)=(∇f)T dx =⇒∇f = (A + AT )x . Here, we dropped terms with more than one dx factor as these are asymptotically negligible. Another trick was to combine dxT Ax and xT Adx by realizing that these are scalars and hence equal to their own transpose: dxT Ax = (dxT Ax)T = xT AT dx. Hence, we have found that f ′(x) = xT (A + AT ) = (∇f)T , or equivalently ∇f = [xT (A + AT )]T = (A + AT )x. It is, of course, also possible to compute the same gradient component-by-component, the way you probably learned to do in multivariable calculus. First, you would need to write f(x) explicitly in terms of the components of x, as f(x) = xT Ax = P i,j xiAi,jxj. Then, you would compute ∂f/∂xk for each k, taking care that x appears twice in the f summation. However, this approach is awkward, error-prone, labor-intensive, and quickly becomes worse as we move on to more complicated functions. It is much better, we feel, to get used to treating vectors and matrices as a whole, not as mere collections of numbers.

## Key terms
- **matrix** — 7 mentions
- **vector** — 6 mentions
- **linear** — 6 mentions
- **operator** — 6 mentions
- **compute** — 5 mentions
- **rule** — 4 mentions
- **consider** — 3 mentions
- **components** — 3 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=14|Matrix Calculus.pdf p. 14]]

## Liens
- Up: [[research/matrix-calculus/derivatives-as-linear-operators]]
- ← Prev: [[research/matrix-calculus/revisiting-multivariable-calculus-part-1-scalar-valued-functions]]
- Next: [[research/matrix-calculus/the-chain-rule]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
