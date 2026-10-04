---
title: "Differentiating the Symmetric Eigendecomposition"
summary: "§Derivatives of Eigenproblems › Differentiating on Orthogonal: When n = 3, airplane pilots know about “roll, pitch, and yaw”, which are the three parameters for the orthogonal matrices when n = 3."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "98-99"
---

# Differentiating the Symmetric Eigendecomposition

§Derivatives of Eigenproblems › Differentiating on Orthogonal Matrices › Differentiating the Symmetric Eigendecomposition · pp. 98–99 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
When n = 3, airplane pilots know about “roll, pitch, and yaw”, which are the three parameters for the orthogonal matrices when n = 3. In general, in Rn2, the orthogonal group has dimension n(n −1)/2. There are a few ways to see this. • Firstly, orthogonality QT Q = I imposes n(n + 1)/2 constraints, leaving n(n −1)/2 free parameters. • When we do QR decomposition, the R “eats” up n(n + 1)/2 of the parameters, again leaving n(n −1)/2 for Q. • Lastly, If we think about the symmetric eigenvalue problem where S = QΛQT , S has n(n + 1)/2 parameters and Λ has n, so Q has n(n −1)/2. Let S be a symmetric matrix, Λ be diagonal containing eigenvalues of S, and Q be orthogonal with column vectors as eigenvectors of S such that S = QΛQT . [For simplicity, let’s assume that the eigenvalues are “simple” (multiplicity 1); repeated eigenvalues turn out to greatly complicate the analysis of perturbations because of the ambiguity in their eigenvector basis.] Then, we have dS = dQ ΛQT + Q dΛ QT + QΛdQT , which may be written as QT dS Q = QT dQΛ −ΛQT dQ + dΛ. As an exercise, one may check that the left and right hand sides of the above are both symmetric. This may be easier if one looks at the diagonal entries on their own, as there (QT dS Q)ii = qT i dS qi.

## Key terms
- **eigenvalue** — 8 mentions
- **parameter** — 5 mentions
- **orthogonal** — 4 mentions
- **symmetric** — 4 mentions
- **diagonal** — 4 mentions
- **eigenvector** — 4 mentions
- **diag** — 4 mentions
- **matrices** — 2 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=98|Matrix Calculus.pdf p. 98]]

## Liens
- Up: [[research/matrix-calculus/differentiating-on-orthogonal-matrices]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
