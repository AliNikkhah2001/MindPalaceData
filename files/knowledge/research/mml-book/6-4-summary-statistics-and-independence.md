---
title: "6.4 Summary Statistics and Independence"
summary: "§Part I Mathematical Foundations › 6 Probability and Distribu: The quantity p(y) := Z p(y | x)p(x)dx = EX[p(y | x)] (6.27) is the marginal likelihood/evidence. The right-hand side of (6.27) uses the marginal likelihood evidence expectation operator which we define in Section 6.4."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "192-202"
---

# 6.4 Summary Statistics and Independence

§Part I Mathematical Foundations › 6 Probability and Distributions › 6.4 Summary Statistics and Independence · pp. 192–202 · Mathematics for Machine Learning (MML Book)

## Extrait
The quantity p(y) := Z p(y | x)p(x)dx = EX[p(y | x)] (6.27) is the marginal likelihood/evidence. The right-hand side of (6.27) uses the marginal likelihood evidence expectation operator which we define in Section 6.4.1. By definition, the marginal likelihood integrates the numerator of (6.23) with respect to the latent variable x. Therefore, the marginal likelihood is independent of x, and it ensures that the posterior p(x | y) is normalized. The marginal likelihood can also be interpreted as the expected likelihood where we take the expectation with respect to the prior p(x). Beyond normalization of the posterior, the marginal likelihood also plays an important role in Bayesian model selection, as we will discuss in Section 8.6. Due to the integration in (8.44), the evidence is often hard to compute. Bayes’ theorem is also called the “probabilistic inverse.” Bayes’ theorem (6.23) allows us to invert the relationship between x and y given by the likelihood. Therefore, Bayes’ theorem is sometimes called the probabilistic inverse. We will discuss Bayes’ theorem further in probabilistic inverse Section 8.4. Remark. In Bayesian statistics, the posterior distribution is the quantity of interest as it encapsulates all available information from the prior and the data.

## Key terms
- **variable** — 24 mentions
- **random** — 23 mentions
- **value** — 21 mentions
- **distribution** — 17 mentions
- **expected** — 13 mentions
- **mean** — 13 mentions
- **median** — 13 mentions
- **posterior** — 12 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=192|mml-book.pdf p. 192]]

## Liens
- Up: [[research/mml-book/6-probability-and-distributions]]
- ← Prev: [[research/mml-book/6-3-sum-rule-product-rule-and-bayes-theorem]]
- Next: [[research/mml-book/6-5-gaussian-distribution]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
