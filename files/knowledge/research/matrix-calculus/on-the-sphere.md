---
title: "On the Sphere"
summary: "§Derivatives of Eigenproblems › Differentiating on the Unit S: Geometrically, we know that velocity vectors (equivalently, tangents) on the sphere are orthogonal to the radii. Out differentials say this algebraically, since given x ∈Sn we have xT x = 1, this implies that 2xT dx ="
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "96-96"
---

# On the Sphere

§Derivatives of Eigenproblems › Differentiating on the Unit Sphere › On the Sphere · pp. 96–96 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Geometrically, we know that velocity vectors (equivalently, tangents) on the sphere are orthogonal to the radii. Out differentials say this algebraically, since given x ∈Sn we have xT x = 1, this implies that 2xT dx = d(xT x) = d(1) = 0. In other words, at the point x on the sphere (a radius, if you will), dx, the linearization of the constraint of moving along the sphere satisfies dx ⊥x. This is our first example where we have seen the infinitesimal perturbation dx being constrained. See Figure 16. x x+dx dx ⟂x Figure 16: Differentials on a sphere (xT x = 1): the differential dx is constrained to be perpendicular to x. Let us simply consider the unit circle in the plane where x = (cos θ, sin θ) for some θ ∈[0, 2π). Then, xT dx = (cos θ, sin θ) · (−sin θ, cos θ)dθ = 0. Here, we can think of x as “extrinsic” coordinates, in that it is a vector in R2. On the other hand, θ is an “intrinsic” coordinate, as every point on the circle is specified by one θ. You may remember that the rank-1 matrix xxT , for any unit vector xT x = 1, is a projection matrix (meaning that it is equal to its square and it is symmetric) which projects vectors onto their components in the direction of x. Correspondingly, I −xxT is also a projection matrix, but onto the directions perpendicular to x: geometrically, the matrix removes components in the x direction.

## Key terms
- **sphere** — 4 mentions
- **vector** — 4 mentions
- **matrix** — 4 mentions
- **differential** — 3 mentions
- **direction** — 3 mentions
- **geometrically** — 2 mentions
- **point** — 2 mentions
- **constrained** — 2 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=96|Matrix Calculus.pdf p. 96]]

## Liens
- Up: [[research/matrix-calculus/differentiating-on-the-unit-sphere]]
- ← Prev: [[research/matrix-calculus/special-case-a-circle]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
