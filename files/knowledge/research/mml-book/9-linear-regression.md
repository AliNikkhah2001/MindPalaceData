---
title: "9 Linear Regression"
summary: "§Part II Central Machine Learning Problems › 9 Linear Regress: Linear Regression In the following, we will apply the mathematical concepts from Chapters 2, 5, 6, and 7 to solve linear regression (curve fitting) problems."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "295-322"
---

# 9 Linear Regression

§Part II Central Machine Learning Problems › 9 Linear Regression · pp. 295–322 · Mathematics for Machine Learning (MML Book)

## Extrait
Linear Regression In the following, we will apply the mathematical concepts from Chapters 2, 5, 6, and 7 to solve linear regression (curve fitting) problems. In regression, we aim to find a function f that maps inputs x ∈RD to correregression sponding function values f(x) ∈R. We assume we are given a set of training inputs xn and corresponding noisy observations yn = f(xn)+ϵ, where ϵ is an i.i.d. random variable that describes measurement/observation noise and potentially unmodeled processes (which we will not consider further in this chapter). Throughout this chapter, we assume zero-mean Gaussian noise. Our task is to find a function that not only models the training data, but generalizes well to predicting function values at input locations that are not part of the training data (see Chapter 8). An illustration of such a regression problem is given in Figure 9.1. A typical regression setting is given in Figure 9.1(a): For some input values xn, we observe (noisy) function values yn = f(xn) + ϵ. The task is to infer the function f that generated the data and generalizes well to function values at new input locations. A possible solution is given in Figure 9.1(b), where we also show three distributions centered at the function values f(x) that represent the noise in the data.

## Key terms
- **function** — 37 mentions
- **regression** — 32 mentions
- **model** — 31 mentions
- **linear** — 25 mentions
- **parameter** — 22 mentions
- **noise** — 14 mentions
- **data** — 14 mentions
- **input** — 14 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=295|mml-book.pdf p. 295]]

## Liens
- Up: [[research/mml-book/part-ii-central-machine-learning-problems]]
- ← Prev: [[research/mml-book/8-when-models-meet-data]]
- Next: [[research/mml-book/10-dimensionality-reduction-with-principal-component-analysis]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
