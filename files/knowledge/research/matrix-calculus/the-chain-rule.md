---
title: "The Chain Rule"
summary: "§Derivatives as Linear Operators › The Chain Rule: Then, df = dxT (Ax) + xT d(Ax) = dxT Ax | {z } = xT AT dx +xT Adx = xT (A + AT )dx = (∇f)T dx , and hence f ′(x) = xT (A + AT )."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "16-17"
---

# The Chain Rule

§Derivatives as Linear Operators › The Chain Rule · pp. 16–17 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Example 13 Let f(x) = xT Ax (mapping Rn →R). Then, df = dxT (Ax) + xT d(Ax) = dxT Ax | {z } = xT AT dx +xT Adx = xT (A + AT )dx = (∇f)T dx , and hence f ′(x) = xT (A + AT ). (In the common case where A is symmetric, this simplifies to f ′(x) = 2xT A.) Note that here we have applied Example 12 in computing d(Ax) = Adx. Furthermore, f is a scalar valued function, so we may also obtain the gradient ∇f = (A + AT )x as before (which simplifies to 2Ax if A is symmetric). Example 14 (Elementwise Products) Given x, y ∈Rm, define x .∗y =     x1y1 ... xmym    =       x1 x2 ... xm       | {z } diag(x)     y1 ... ym    , the element-wise product of vectors (also called the Hadamard product), where for convenience below we also define diag(x) as the m×m diagonal matrix with x on the diagonal. Then, given A ∈Rm,n, define f : Rn →Rm via f(x) = A(x .∗x). As an exercise, one can verify the following: (a) x .∗y = y .∗x, (b) A(x .∗y) = A diag(x) y. (c) d(x .∗y) = (dx) .∗y + x .∗(dy). So if we take y to be a constant and define g(x) = y .∗x, its Jacobian matrix is diag(y). (d) df = A(2x .∗dx) = 2A diag(x) dx = f ′(x)[dx], so the Jacobian matrix is J = 2A diag(x). (e) Notice that the directional derivative (Sec.

## Key terms
- **matrix** — 11 mentions
- **function** — 7 mentions
- **product** — 7 mentions
- **diag** — 6 mentions
- **rule** — 6 mentions
- **multiplication** — 6 mentions
- **jacobian** — 5 mentions
- **chain** — 5 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=16|Matrix Calculus.pdf p. 16]]

## Liens
- Up: [[research/matrix-calculus/derivatives-as-linear-operators]]
- ← Prev: [[research/matrix-calculus/revisiting-multivariable-calculus-part-2-vector-valued-functions]]
- Next: [[research/matrix-calculus/beyond-multi-variable-derivatives]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
