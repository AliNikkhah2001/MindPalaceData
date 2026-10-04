---
title: "11.3 EM Algorithm"
summary: "§Part II Central Machine Learning Problems › 11 Density Estim: Density Estimation with Gaussian Mixture Models Example 11.5 (Weight Parameter Updates) Figure 11.7 Effect of updating the mixture weights in a GMM."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "366-368"
---

# 11.3 EM Algorithm

§Part II Central Machine Learning Problems › 11 Density Estimation with Gaussian Mixture Models › 11.3 EM Algorithm · pp. 366–368 · Mathematics for Machine Learning (MML Book)

## Extrait
Density Estimation with Gaussian Mixture Models Example 11.5 (Weight Parameter Updates) Figure 11.7 Effect of updating the mixture weights in a GMM. (a) GMM before updating the mixture weights; (b) GMM after updating the mixture weights while retaining the means and variances. Note the different scales of the vertical axes. −4 −2 x 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 p(x) π1N(x|µ1, σ2 1) π2N(x|µ2, σ2 2) π3N(x|µ3, σ2 3) GMM density (a) GMM density and individual components prior to updating the mixture weights. −4 −2 x 0.00 0.05 0.10 0.15 0.20 0.25 0.30 p(x) π1N(x|µ1, σ2 1) π2N(x|µ2, σ2 2) π3N(x|µ3, σ2 3) GMM density (b) GMM density and individual components after updating the mixture weights. In our running example from Figure 11.3, the mixture weights are updated as follows: π1 : 1 3 →0.29 (11.50) π2 : 1 3 →0.29 (11.51) π3 : 1 3 →0.42 (11.52) Here we see that the third component gets more weight/importance, while the other components become slightly less important. Figure 11.7 illustrates the effect of updating the mixture weights. Figure 11.7(a) is identical to Figure 11.6(b) and shows the GMM density and its individual components prior to updating the mixture weights. Figure 11.7(b) shows the GMM density after updating the mixture weights.

## Key terms
- **mixture** — 19 mentions
- **weight** — 13 mentions
- **iteration** — 13 mentions
- **parameter** — 11 mentions
- **log-likelihood** — 11 mentions
- **density** — 10 mentions
- **component** — 10 mentions
- **algorithm** — 10 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=366|mml-book.pdf p. 366]]

## Liens
- Up: [[research/mml-book/11-density-estimation-with-gaussian-mixture-models]]
- ← Prev: [[research/mml-book/11-2-parameter-learning-via-maximum-likelihood]]
- Next: [[research/mml-book/11-4-latent-variable-perspective]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
