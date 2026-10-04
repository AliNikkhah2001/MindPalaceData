---
title: "6.3 Sum Rule, Product Rule, and Bayes' Theorem"
summary: "§Part I Mathematical Foundations › 6 Probability and Distribu: 6.3 Sum Rule, Product Rule, and Bayes’ Theorem Table 6.1 Nomenclature for probability distributions. Type “Point probability” “Interval probability” Discrete P(X = x) Not applicable Probability mass function Continuou"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "189-191"
---

# 6.3 Sum Rule, Product Rule, and Bayes' Theorem

§Part I Mathematical Foundations › 6 Probability and Distributions › 6.3 Sum Rule, Product Rule, and Bayes' Theorem · pp. 189–191 · Mathematics for Machine Learning (MML Book)

## Extrait
6.3 Sum Rule, Product Rule, and Bayes’ Theorem Table 6.1 Nomenclature for probability distributions. Type “Point probability” “Interval probability” Discrete P(X = x) Not applicable Probability mass function Continuous p(x) P(X ⩽x) Probability density function Cumulative distribution function density can be greater than 1. However, it needs to hold that Z 1.6 0.9 p(x)dx = 1 . (6.19) Remark. There is an additional subtlety with regards to discrete probability distributions. The states z1, . . . , zd do not in principle have any structure, i.e., there is usually no way to compare them, for example z1 = red, z2 = green, z3 = blue. However, in many machine learning applications discrete states take numerical values, e.g., z1 = −1.1, z2 = 0.3, z3 = 1.5, where we could say z1 < z2 < z3. Discrete states that assume numerical values are particularly useful because we often consider expected values (Section 6.4.1) of random variables. ♢ Unfortunately, machine learning literature uses notation and nomenclature that hides the distinction between the sample space Ω, the target space T , and the random variable X. For a value x of the set of possible outcomes of the random variable X, i.e., x ∈T , p(x) denotes the probWe think of the outcome x as the argument that results in the probability p(x).

## Key terms
- **rule** — 30 mentions
- **variable** — 29 mentions
- **distribution** — 25 mentions
- **random** — 24 mentions
- **probability** — 23 mentions
- **product** — 11 mentions
- **discrete** — 11 mentions
- **bayes** — 10 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=189|mml-book.pdf p. 189]]

## Liens
- Up: [[research/mml-book/6-probability-and-distributions]]
- ← Prev: [[research/mml-book/6-2-discrete-and-continuous-probabilities]]
- Next: [[research/mml-book/6-4-summary-statistics-and-independence]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section
