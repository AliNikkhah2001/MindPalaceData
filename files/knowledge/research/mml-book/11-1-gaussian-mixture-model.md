---
title: "11.1 Gaussian Mixture Model"
summary: "§Part II Central Machine Learning Problems › 11 Density Estim: 11.1 Gaussian Mixture Model In practice, the Gaussian (or similarly all other distributions we encountered so far) have limited modeling capabilities."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "355-355"
---

# 11.1 Gaussian Mixture Model

§Part II Central Machine Learning Problems › 11 Density Estimation with Gaussian Mixture Models › 11.1 Gaussian Mixture Model · pp. 355–355 · Mathematics for Machine Learning (MML Book)

## Extrait
11.1 Gaussian Mixture Model In practice, the Gaussian (or similarly all other distributions we encountered so far) have limited modeling capabilities. For example, a Gaussian approximation of the density that generated the data in Figure 11.1 would be a poor approximation. In the following, we will look at a more expressive family of distributions, which we can use for density estimation: mixture models. mixture model Mixture models can be used to describe a distribution p(x) by a convex combination of K simple (base) distributions p(x) = K X k=1 πkpk(x) (11.1) 0 ⩽πk ⩽1 , K X k=1 πk = 1 , (11.2) where the components pk are members of a family of basic distributions, e.g., Gaussians, Bernoullis, or Gammas, and the πk are mixture weights. mixture weight Mixture models are more expressive than the corresponding base distributions because they allow for multimodal data representations, i.e., they can describe datasets with multiple “clusters”, such as the example in Figure 11.1. We will focus on Gaussian mixture models (GMMs), where the basic distributions are Gaussians. For a given dataset, we aim to maximize the likelihood of the model parameters to train the GMM. For this purpose, we will use results from Chapter 5, Chapter 6, and Section 7.2.

## Key terms
- **gaussian** — 11 mentions
- **model** — 11 mentions
- **mixture** — 10 mentions
- **distribution** — 10 mentions
- **density** — 3 mentions
- **modeling** — 2 mentions
- **approximation** — 2 mentions
- **data** — 2 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=355|mml-book.pdf p. 355]]

## Liens
- Up: [[research/mml-book/11-density-estimation-with-gaussian-mixture-models]]
- Next: [[research/mml-book/11-2-parameter-learning-via-maximum-likelihood]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
