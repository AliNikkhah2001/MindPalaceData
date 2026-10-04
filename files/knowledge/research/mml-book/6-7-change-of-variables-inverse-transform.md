---
title: "6.7 Change of Variables/Inverse Transform"
summary: "§Part I Mathematical Foundations › 6 Probability and Distribu: The canonical conjugate prior has the form p(µ | α, β) = µ 1 −µ exp  α log µ 1 −µ + (β + α) log(1 −µ) −Ac(γ)  , (6.122) where we defined γ := [α, β + α]⊤and hc(µ) := µ/(1 −µ)."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "220-226"
---

# 6.7 Change of Variables/Inverse Transform

§Part I Mathematical Foundations › 6 Probability and Distributions › 6.7 Change of Variables/Inverse Transform · pp. 220–226 · Mathematics for Machine Learning (MML Book)

## Extrait
The canonical conjugate prior has the form p(µ | α, β) = µ 1 −µ exp  α log µ 1 −µ + (β + α) log(1 −µ) −Ac(γ)  , (6.122) where we defined γ := [α, β + α]⊤and hc(µ) := µ/(1 −µ). Equation (6.122) then simplifies to p(µ | α, β) = exp [(α −1) log µ + (β −1) log(1 −µ) −Ac(α, β)] . (6.123) Putting this in non-exponential family form yields p(µ | α, β) ∝µα−1(1 −µ)β−1 , (6.124) which we identify as the Beta distribution (6.98). In example 6.12, we assumed that the Beta distribution is the conjugate prior of the Bernoulli distribution and showed that it was indeed the conjugate prior. In this example, we derived the form of the Beta distribution by looking at the canonical conjugate prior of the Bernoulli distribution in exponential family form. As mentioned in the previous section, the main motivation for exponential families is that they have finite-dimensional sufficient statistics. Additionally, conjugate distributions are easy to write down, and the conjugate distributions also come from an exponential family. From an inference perspective, maximum likelihood estimation behaves nicely because empirical estimates of sufficient statistics are optimal estimates of the population values of sufficient statistics (recall the mean and covariance of a Gaussian).

## Key terms
- **variable** — 34 mentions
- **random** — 29 mentions
- **distribution** — 28 mentions
- **function** — 20 mentions
- **transformation** — 12 mentions
- **inverse** — 10 mentions
- **change** — 7 mentions
- **theorem** — 7 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=220|mml-book.pdf p. 220]]

## Liens
- Up: [[research/mml-book/6-probability-and-distributions]]
- ← Prev: [[research/mml-book/6-6-conjugacy-and-the-exponential-family]]
- Next: [[research/mml-book/6-8-further-reading]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
