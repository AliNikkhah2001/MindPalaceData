---
title: "9.5 Further Reading"
summary: "§Part II Central Machine Learning Problems › 9 Linear Regress: 9.5 Further Reading When the basis is not orthogonal, one can convert a set of linearly independent basis functions to an orthogonal basis by using the Gram-Schmidt process; see Section 3.8.3 and (Strang, 2003)."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "321-322"
---

# 9.5 Further Reading

§Part II Central Machine Learning Problems › 9 Linear Regression › 9.5 Further Reading · pp. 321–322 · Mathematics for Machine Learning (MML Book)

## Extrait
9.5 Further Reading When the basis is not orthogonal, one can convert a set of linearly independent basis functions to an orthogonal basis by using the Gram-Schmidt process; see Section 3.8.3 and (Strang, 2003). In this chapter, we discussed linear regression for Gaussian likelihoods and conjugate Gaussian priors on the parameters of the model. This allowed for closed-form Bayesian inference. However, in some applications we may want to choose a different likelihood function. For example, in a binary classification setting, we observe only two possible (categorical) classification outcomes, and a Gaussian likelihood is inappropriate in this setting. Instead, we can choose a Bernoulli likelihood that will return a probability of the predicted label to be 1 (or 0). We refer to the books by Barber (2012), Bishop (2006), and Murphy (2012) for an in-depth introduction to classification problems. A different example where non-Gaussian likelihoods are important is count data. Counts are non-negative integers, and in this case a Binomial or Poisson likelihood would be a better choice than a Gaussian. All these examples fall into the category of generalized linear models, a flexgeneralized linear model ible generalization of linear regression that allows for response variables that have error distributions other than a Gaussian distribution.

## Key terms
- **linear** — 23 mentions
- **regression** — 20 mentions
- **function** — 19 mentions
- **model** — 18 mentions
- **gaussian** — 14 mentions
- **parameter** — 13 mentions
- **distribution** — 9 mentions
- **prior** — 9 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=321|mml-book.pdf p. 321]]

## Liens
- Up: [[research/mml-book/9-linear-regression]]
- ← Prev: [[research/mml-book/9-4-maximum-likelihood-as-orthogonal-projection]]
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
