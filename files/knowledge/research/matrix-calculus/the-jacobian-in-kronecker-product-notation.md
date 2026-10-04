---
title: "The Jacobian in Kronecker-product notation"
summary: "§Jacobians of Matrix Functions › Kronecker Products › The Jac: but this matrix is exactly the Kronecker product I ⊗B! Hence, we have derived that (I ⊗B) vec C = vec(BC). This is a little trickier, but again let’s simplify to the case where B = I, in which case BCAT = CAT ."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "26-26"
---

# The Jacobian in Kronecker-product notation

§Jacobians of Matrix Functions › Kronecker Products › The Jacobian in Kronecker-product notation · pp. 26–26 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
but this matrix is exactly the Kronecker product I ⊗B! Hence, we have derived that (I ⊗B) vec C = vec(BC). What about the AT term? This is a little trickier, but again let’s simplify to the case where B = I, in which case BCAT = CAT . To vectorize this, we need to look at the columns of CAT . What is the first column of CAT ? It is a linear combination of the columns of C whose coefficients are given by the first column of AT (= first row of A): column 1 of CAT = X j a1j⃗cj . Similarly for column 2, etc, and we then “stack” these columns to get vec(CAT ). But this is exactly the formula for multipling a matrix A by a vector, if the “elements” of the vector were the columns⃗cj. Written out explicitly, this becomes: vec(CAT ) =     P j a1j⃗cj P j a2j⃗cj ...    =     a11 I a12 I · · · a21 I a22 I · · · ... ... ...     | {z } A⊗I    ⃗ c1⃗ c2 ...     | {z } vec C , and hence we have derived (A ⊗I) vec C = vec(CAT ). The full identity (A ⊗B) vec(C) = vec(BCAT ) can then be obtained by straightforwardly combining these two derivations: replace CAT with BCAT in the second derivation, which replaces⃗cj with B⃗cj and hence I with B. So now we want to use Prop. 27 to calculate the Jacobian of f(A) = A2 in terms of the Kronecker product.

## Key terms
- **column** — 8 mentions
- **matrix** — 3 mentions
- **exactly** — 3 mentions
- **kronecker** — 3 mentions
- **product** — 3 mentions
- **bcat** — 3 mentions
- **first** — 3 mentions
- **these** — 3 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=26|Matrix Calculus.pdf p. 26]]

## Liens
- Up: [[research/matrix-calculus/kronecker-products]]
- ← Prev: [[research/matrix-calculus/key-kronecker-product-identity]]
- Next: [[research/matrix-calculus/the-computational-cost-of-kronecker-products]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
