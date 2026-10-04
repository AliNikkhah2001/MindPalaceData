---
title: "Matrix Calculus (MIT 18.S096 Notes)"
summary: "Derivatives as linear operators: the MIT course notes that turn backprop from symbol-pushing into geometry. Direct companion to the MML Book's calculus chapters, but with the chain rule, Jacobians, and matrix-function derivatives worked for ML use."
level: "research"
series: "D:\\Research"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop]
---

# Matrix Calculus (MIT 18.S096 Notes)

## Pourquoi ce nœud — explication
Derivatives as linear operators: the MIT course notes that turn backprop from symbol-pushing into geometry. Direct companion to the MML Book's calculus chapters, but with the chain rule, Jacobians, and matrix-function derivatives worked for ML use.

Source file: `Matrix Calculus.pdf` · [[index-research]]

```mermaid
graph LR
    ScalarCalc --> MultiCalc
    MultiCalc --> Jacobians
    Jacobians --> ChainRule
    ChainRule --> Backprop
```

En bref: $$\frac{d}{d\mathbf{X}}\,\mathrm{tr}(\mathbf{AXB}) = \mathbf{A}^\top\mathbf{B}^\top$$

## Contents (95 sections — every entry links somewhere)
- [[research/matrix-calculus/a-simple-example-the-two-by-two-matrix-square-function|a simple example the two by two matrix square function]]
- [[research/matrix-calculus/a-simple-matrix-dot-product-and-norm|a simple matrix dot product and norm]]
- [[research/matrix-calculus/accuracy-of-finite-differences|accuracy of finite differences]]
- [[research/matrix-calculus/adjoint-method-example|adjoint method example]]
- [[research/matrix-calculus/adjoint-methods-and-ad|adjoint methods and ad]]
- [[research/matrix-calculus/applications-2|applications 2]]
- [[research/matrix-calculus/applications|applications]]
- [[research/matrix-calculus/automatic-differentiation-via-computational-graphs|automatic differentiation via computational graphs]]
- [[research/matrix-calculus/automatic-differentiation-via-dual-numbers|automatic differentiation via dual numbers]]
- [[research/matrix-calculus/beyond-multi-variable-derivatives|beyond multi variable derivatives]]
- [[research/matrix-calculus/calculus-of-variations|calculus of variations]]
- [[research/matrix-calculus/characteristic-polynomial|characteristic polynomial]]
- [[research/matrix-calculus/computing-hessians|computing hessians]]
- [[research/matrix-calculus/cost-of-matrix-multiplication|cost of matrix multiplication]]
- [[research/matrix-calculus/derivative-of-matrix-determinant-and-inverse|derivative of matrix determinant and inverse]]
- [[research/matrix-calculus/derivatives-as-linear-operators|derivatives as linear operators]]
- [[research/matrix-calculus/derivatives-in-general-vector-spaces|derivatives in general vector spaces]]
- [[research/matrix-calculus/derivatives-norms-and-banach-spaces|derivatives norms and banach spaces]]
- [[research/matrix-calculus/derivatives-of-eigenproblems|derivatives of eigenproblems]]
- [[research/matrix-calculus/derivatives-of-matrix-functions-linear-operators|derivatives of matrix functions linear operators]]
- [[research/matrix-calculus/derivatives-of-random-functions|derivatives of random functions]]
- [[research/matrix-calculus/differentiating-ode-solutions|differentiating ode solutions]]
- [[research/matrix-calculus/differentiating-on-orthogonal-matrices|differentiating on orthogonal matrices]]
- [[research/matrix-calculus/differentiating-on-the-unit-sphere|differentiating on the unit sphere]]
- [[research/matrix-calculus/differentiating-the-symmetric-eigendecomposition|differentiating the symmetric eigendecomposition]]
- [[research/matrix-calculus/directional-derivatives|directional derivatives]]
- [[research/matrix-calculus/dual-numbers|dual numbers]]
- [[research/matrix-calculus/easy-forward-mode-ad|easy forward mode ad]]
- [[research/matrix-calculus/engineering-physical-optimization|engineering physical optimization]]
- [[research/matrix-calculus/euler-lagrange-equations|euler lagrange equations]]
- [[research/matrix-calculus/example-babylonian-square-root|example babylonian square root]]
- [[research/matrix-calculus/example-matrix-squaring|example matrix squaring]]
- [[research/matrix-calculus/example-minimizing-arc-length|example minimizing arc length]]
- [[research/matrix-calculus/example|example]]
- [[research/matrix-calculus/finite-difference-approximations-easy-version|finite difference approximations easy version]]
- [[research/matrix-calculus/finite-difference-approximations|finite difference approximations]]
- [[research/matrix-calculus/first-derivatives|first derivatives]]
- [[research/matrix-calculus/forward-and-reverse-mode-automatic-differentiation|forward and reverse mode automatic differentiation]]
- [[research/matrix-calculus/forward-mode|forward mode]]
- [[research/matrix-calculus/forward-over-reverse-mode-second-derivatives|forward over reverse mode second derivatives]]
- [[research/matrix-calculus/forward-sensitivity-analysis-of-odes|forward sensitivity analysis of odes]]
- [[research/matrix-calculus/forward-vs-reverse-mode-differentiation|forward vs reverse mode differentiation]]
- [[research/matrix-calculus/functionals-mapping-functions-to-scalars|functionals mapping functions to scalars]]
- [[research/matrix-calculus/further-reading-2|further reading 2]]
- [[research/matrix-calculus/further-reading|further reading]]
- [[research/matrix-calculus/general-second-derivatives-bilinear-maps|general second derivatives bilinear maps]]
- [[research/matrix-calculus/generalized-quadratic-approximation|generalized quadratic approximation]]
- [[research/matrix-calculus/handling-discrete-randomness|handling discrete randomness]]
- [[research/matrix-calculus/hessian-matrices-of-scalar-valued-functions|hessian matrices of scalar valued functions]]
- [[research/matrix-calculus/hessians-and-optimization|hessians and optimization]]
- [[research/matrix-calculus/inner-products-of-functions|inner products of functions]]
- [[research/matrix-calculus/intro-matrix-and-vector-product-rule|intro matrix and vector product rule]]
- [[research/matrix-calculus/introduction-2|introduction 2]]
- [[research/matrix-calculus/introduction|introduction]]
- [[research/matrix-calculus/jacobian-of-the-inverse|jacobian of the inverse]]
- [[research/matrix-calculus/jacobians-of-matrix-functions|jacobians of matrix functions]]
- [[research/matrix-calculus/key-kronecker-product-identity|key kronecker product identity]]
- [[research/matrix-calculus/kronecker-products|kronecker products]]
- [[research/matrix-calculus/linear-operators|linear operators]]
- [[research/matrix-calculus/minima-maxima-and-saddle-points|minima maxima and saddle points]]
- [[research/matrix-calculus/multidimensional-functions|multidimensional functions]]
- [[research/matrix-calculus/naive-symbolic-differentiation|naive symbolic differentiation]]
- [[research/matrix-calculus/newton-like-methods|newton like methods]]
- [[research/matrix-calculus/newton-s-method|newton s method]]
- [[research/matrix-calculus/nonlinear-equations|nonlinear equations]]
- [[research/matrix-calculus/nonlinear-optimization|nonlinear optimization]]
- [[research/matrix-calculus/nonlinear-root-finding-optimization-and-adjoint-differentiation|nonlinear root finding optimization and adjoint differentiation]]
- [[research/matrix-calculus/on-the-sphere|on the sphere]]
- [[research/matrix-calculus/optimization|optimization]]
- [[research/matrix-calculus/order-of-accuracy|order of accuracy]]
- [[research/matrix-calculus/ordinary-differential-equations-odes|ordinary differential equations odes]]
- [[research/matrix-calculus/other-finite-difference-methods|other finite difference methods]]
- [[research/matrix-calculus/overview-and-motivation|overview and motivation]]
- [[research/matrix-calculus/reverse-adjoint-sensitivity-analysis-of-odes|reverse adjoint sensitivity analysis of odes]]
- [[research/matrix-calculus/reverse-mode-adjoint-differentiation|reverse mode adjoint differentiation]]
- [[research/matrix-calculus/reverse-mode-automatic-differentiation-on-graphs|reverse mode automatic differentiation on graphs]]
- [[research/matrix-calculus/reverse-mode|reverse mode]]
- [[research/matrix-calculus/revisiting-multivariable-calculus-part-1-scalar-valued-functions|revisiting multivariable calculus part 1 scalar valued functions]]
- [[research/matrix-calculus/revisiting-multivariable-calculus-part-2-vector-valued-functions|revisiting multivariable calculus part 2 vector valued functions]]
- [[research/matrix-calculus/revisiting-single-variable-calculus|revisiting single variable calculus]]
- [[research/matrix-calculus/roundoff-error|roundoff error]]
- [[research/matrix-calculus/scalar-functions|scalar functions]]
- [[research/matrix-calculus/second-derivatives-bilinear-maps-and-hessian-matrices|second derivatives bilinear maps and hessian matrices]]
- [[research/matrix-calculus/sensitivity-analysis-of-ode-solutions|sensitivity analysis of ode solutions]]
- [[research/matrix-calculus/special-case-a-circle|special case a circle]]
- [[research/matrix-calculus/stochastic-differentials-and-the-reparameterization-trick|stochastic differentials and the reparameterization trick]]
- [[research/matrix-calculus/stochastic-programs|stochastic programs]]
- [[research/matrix-calculus/the-chain-rule|the chain rule]]
- [[research/matrix-calculus/the-computational-cost-of-kronecker-products|the computational cost of kronecker products]]
- [[research/matrix-calculus/the-jacobian-in-kronecker-product-notation|the jacobian in kronecker product notation]]
- [[research/matrix-calculus/the-logarithmic-derivative|the logarithmic derivative]]
- [[research/matrix-calculus/the-matrix-squaring-four-by-four-jacobian-matrix|the matrix squaring four by four jacobian matrix]]
- [[research/matrix-calculus/two-derivations|two derivations]]
- [[research/matrix-calculus/where-we-go-from-here|where we go from here]]
- [[research/matrix-calculus/why-compute-derivatives-approximately-instead-of-exactly|why compute derivatives approximately instead of exactly]]

## Practice — open in app
- [[pdf:Matrix Calculus.pdf|Open Matrix Calculus.pdf]]
- [[quiz:3|ML starter quiz]]

## Liens
- [[mml-book]]
- [[index-research]]

#ml #math #calculus #backprop #research #lecture
