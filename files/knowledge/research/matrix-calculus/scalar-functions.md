---
title: "Scalar Functions"
summary: "§Nonlinear Root-Finding, Optimization, and Adjoint Differenti: Nonlinear Root-Finding, Optimization, and Adjoint Differentiation The next part is based on these slides. Today, we want to talk about why we are computing derivatives in the first place."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "39-39"
---

# Scalar Functions

§Nonlinear Root-Finding, Optimization, and Adjoint Differentiation › Newton's Method › Scalar Functions · pp. 39–39 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
Nonlinear Root-Finding, Optimization, and Adjoint Differentiation The next part is based on these slides. Today, we want to talk about why we are computing derivatives in the first place. In particular, we will drill down on this a little bit and then talk about computation of derivatives. 6.1 Newton’s Method One common application of derivatives is to solve nonlinear equations via linearization. For instance, suppose we have a scalar function f : R →R and we wanted to solve f(x) = 0 for a root x. Of course, we could solve such an equation explicitly in simple cases, such as when f is linear or quadratic, but if the function is something more arbitrary like f(x) = x3 −sin(cos x) you might not be able to obtain closed-form solutions. However, there is a nice way to obtain the solution approximately to any accuracy you want, as long if you know approximately where the root is. The method we are talking about is known as Newton’s method, which is really a linear-algebra technique. It takes in the function and a guess for the root, approximates it by a straight line (whose root is easy to find), which is then an approximate root that we can use as a new guess. In particular, the method (depicted in Fig.

## Key terms
- **method** — 8 mentions
- **newton** — 7 mentions
- **root** — 6 mentions
- **solve** — 5 mentions
- **function** — 5 mentions
- **derivatives** — 3 mentions
- **linear** — 3 mentions
- **nonlinear** — 2 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=39|Matrix Calculus.pdf p. 39]]

## Liens
- Up: [[research/matrix-calculus/newton-s-method]]
- Next: [[research/matrix-calculus/multidimensional-functions]] →
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section
