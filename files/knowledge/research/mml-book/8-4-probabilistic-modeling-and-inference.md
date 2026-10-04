---
title: "8.4 Probabilistic Modeling and Inference"
summary: "§Part II Central Machine Learning Problems › 8 When Models Me: this is the model class we would want to work with since it has good generalization properties. In practice, we often define very rich model classes Mθ with many parameters, such as deep neural networks."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "278-283"
---

# 8.4 Probabilistic Modeling and Inference

§Part II Central Machine Learning Problems › 8 When Models Meet Data › 8.4 Probabilistic Modeling and Inference · pp. 278–283 · Mathematics for Machine Learning (MML Book)

## Extrait
this is the model class we would want to work with since it has good generalization properties. In practice, we often define very rich model classes Mθ with many parameters, such as deep neural networks. To mitigate the problem of overfitting, we can use regularization (Section 8.2.3) or priors (Section 8.3.2). We will discuss how to choose the model class in Section 8.6. When considering probabilistic models, the principle of maximum likelihood estimation generalizes the idea of least-squares regression for linear models, which we will discuss in detail in Chapter 9. When restricting the predictor to have linear form with an additional nonlinear function φ applied to the output, i.e., p(yn|xn, θ) = φ(θ⊤xn) , (8.21) we can consider other models for other prediction tasks, such as binary classification or modeling count data (McCullagh and Nelder, 1989). An alternative view of this is to consider likelihoods that are from the exponential family (Section 6.6). The class of models, which have linear dependence between parameters and data, and have potentially nonlinear transformation φ (called a link function), is referred to as generalized link function generalized linear model linear models (Agresti, 2002, chapter 4).

## Key terms
- **model** — 38 mentions
- **parameter** — 35 mentions
- **likelihood** — 17 mentions
- **distribution** — 17 mentions
- **variable** — 15 mentions
- **inference** — 14 mentions
- **probabilistic** — 13 mentions
- **prediction** — 13 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=278|mml-book.pdf p. 278]]

## Liens
- Up: [[research/mml-book/8-when-models-meet-data]]
- ← Prev: [[research/mml-book/8-3-parameter-estimation]]
- Next: [[research/mml-book/8-5-directed-graphical-models]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
