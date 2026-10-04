---
title: "9.2 Parameter Estimation"
summary: "§Part II Central Machine Learning Problems › 9 Linear Regress: Linear Regression Figure 9.2 Linear regression example. (a) Example functions that fall into this category; (b) training set; (c) maximum likelihood estimate."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "298-308"
---

# 9.2 Parameter Estimation

§Part II Central Machine Learning Problems › 9 Linear Regression › 9.2 Parameter Estimation · pp. 298–308 · Mathematics for Machine Learning (MML Book)

## Extrait
Linear Regression Figure 9.2 Linear regression example. (a) Example functions that fall into this category; (b) training set; (c) maximum likelihood estimate. −10 x −20 y (a) Example functions (straight lines) that can be described using the linear model in (9.4). −10 −5 x −10 y (b) Training set. −10 −5 x −10 y (c) Maximum likelihood estimate. refers to models that are “linear in the parameters”, i.e., models that describe a function by a linear combination of input features. Here, a “feature” is a representation ϕ(x) of the inputs x. In the following, we will discuss in more detail how to find good parameters θ and how to evaluate whether a parameter set “works well”. For the time being, we assume that the noise variance σ2 is known. Consider the linear regression setting (9.4) and assume we are given a training set D := {(x1, y1), . . . , (xN, yN)} consisting of N inputs xn ∈ training set RD and corresponding observations/targets yn ∈R, n = 1, . . . , N. The Figure 9.3 Probabilistic graphical model for linear regression. Observed random variables are shaded, deterministic/ known values are without circles. θ yn σ xn n = 1, . . . , N corresponding graphical model is given in Figure 9.3.

## Key terms
- **likelihood** — 29 mentions
- **parameter** — 23 mentions
- **linear** — 22 mentions
- **regression** — 19 mentions
- **model** — 14 mentions
- **function** — 14 mentions
- **maximum** — 13 mentions
- **input** — 12 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=298|mml-book.pdf p. 298]]

## Liens
- Up: [[research/mml-book/9-linear-regression]]
- ← Prev: [[research/mml-book/9-1-problem-formulation]]
- Next: [[research/mml-book/9-3-bayesian-linear-regression]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
