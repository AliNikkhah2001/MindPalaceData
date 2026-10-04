---
title: "Derivatives in General Vector Spaces"
summary: "§Derivatives in General Vector Spaces: Matrix calculus requires us to generalize concepts of derivative and gradient further, to functions whose inputs and/or outputs are not simply scalars or column vectors."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "34-38"
---

# Derivatives in General Vector Spaces

§Derivatives in General Vector Spaces · pp. 34–38 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Matrix calculus requires us to generalize concepts of derivative and gradient further, to functions whose inputs and/or outputs are not simply scalars or column vectors. To achieve this, we extend the notion of the ordinary vector dot product and ordinary Euclidean vector “length” to general inner products and norms on vector spaces. Our first example will consider familiar matrices from this point of view. Recall from linear algebra that we can call any set V a “vector space” if its elements can be added/subtracted x±y and multiplied by scalars αx (subject to some basic arithmetic axioms, e.g. the distributive law). For example, the set of m × n matrices themselves form a vector space, or even the set of continuous functions u(x) (mapping R →R)-the key fact is that we can add/subtract/scale them and get elements of the same set. It turns out to be extraordinarily useful to extend differentiation to such spaces, e.g. for functions that map matrices to matrices or functions to numbers. Doing so crucially relies on our input/output vector spaces V having a norm and, ideally, an inner product. Recall that for scalar-valued functions f(x) ∈R with vector inputs x ∈Rn (i.e. n-component “column vectors") we have that df = f(x + dx) −f(x) = f ′(x)[dx] ∈R.

## Key terms
- **product** — 34 mentions
- **vector** — 31 mentions
- **space** — 31 mentions
- **inner** — 27 mentions
- **function** — 15 mentions
- **gradient** — 13 mentions
- **norm** — 10 mentions
- **linear** — 9 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=34|Matrix Calculus.pdf p. 34]]

## Liens
- ← Prev: [[research/matrix-calculus/finite-difference-approximations]]
- Next: [[research/matrix-calculus/nonlinear-root-finding-optimization-and-adjoint-differentiation]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
