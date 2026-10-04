---
title: "Key Kronecker-product identity"
summary: "§Jacobians of Matrix Functions › Kronecker Products › Key Kro: products: Problem 26 From the definition of the Kronecker product, derive the following identities: 1. A ⊗B is orthogonal (its transpose is its inverse) if A and B are orthogonal."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "25-25"
---

# Key Kronecker-product identity

§Jacobians of Matrix Functions › Kronecker Products › Key Kronecker-product identity · pp. 25–25 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
products: Problem 26 From the definition of the Kronecker product, derive the following identities: 1. (A ⊗B)T = AT ⊗BT . 2. (A ⊗B)(C ⊗D) = (AC) ⊗(BD). 3. (A ⊗B)−1 = A−1 ⊗B−1. (Follows from property 2.) 4. A ⊗B is orthogonal (its transpose is its inverse) if A and B are orthogonal. (From properties 1 & 3.) 5. det(A ⊗B) = det(A)m det(B)n, where A ∈Rn,n and B ∈Rm,m. 6. tr(A ⊗B) = (tr A)(tr B). 7. Given eigenvectors/values Au = λu and Bv = µv of A and B, then λµ is an eigenvalue of A ⊗B with eigenvector u ⊗v. (Also, since u ⊗v = vec X where X = vuT , you can relate this via Prop. 27 below to the identity BXAT = Bv(Au)T = λµX.) In order to convert linear operations like AX + XA into Kronecker products via vectorization, the key identity is: Proposition 27 Given (compatibly sized) matrices A, B, C, we have (A ⊗B) vec(C) = vec(BCAT ). We can thus view A ⊗B as a vectorized equivalent of the linear operation C 7→BCAT . We are tempted to introduce a parallel notation (A ⊗B)[C] = BCAT for the “non-vectorized” version of this operation, although this notation is not standard. One possible mnemonic for this identity is that the B is just to the left of the C while the A “circles around” to the right and gets transposed.

## Key terms
- **identity** — 5 mentions
- **bcat** — 4 mentions
- **product** — 3 mentions
- **operation** — 3 mentions
- **kronecker** — 2 mentions
- **orthogonal** — 2 mentions
- **eigenvector** — 2 mentions
- **linear** — 2 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=25|Matrix Calculus.pdf p. 25]]

## Liens
- Up: [[research/matrix-calculus/kronecker-products]]
- Next: [[research/matrix-calculus/the-jacobian-in-kronecker-product-notation]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
