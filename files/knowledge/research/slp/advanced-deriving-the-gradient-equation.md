---
title: "Advanced: Deriving the Gradient Equation"
summary: "§I Large Language Models › Logistic Regression › Advanced: De: 4.15 • ADVANCED: DERIVING THE GRADIENT EQUATION Both L1 and L2 regularization have Bayesian interpretations as constraints on the prior of how weights should look."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "101-101"
---

# Advanced: Deriving the Gradient Equation

§I Large Language Models › Logistic Regression › Advanced: Deriving the Gradient Equation · pp. 101–101 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.15 • ADVANCED: DERIVING THE GRADIENT EQUATION Both L1 and L2 regularization have Bayesian interpretations as constraints on the prior of how weights should look. L1 regularization can be viewed as a Laplace prior on the weights. L2 regularization corresponds to assuming that weights are distributed according to a Gaussian distribution with mean µ = 0. In a Gaussian or normal distribution, the further away a value is from the mean, the lower its probability (scaled by the variance σ). By using a Gaussian prior on the weights, we are saying that weights prefer to have the value 0. A Gaussian for a weight θj is q 2πσ2 j exp −(θj −µj)2 2σ2 j ! (4.54) If we multiply each weight by a Gaussian prior on the weight, we are thus maximizing the following constraint: ˆθ = argmax θ m Y i=1 P(y(i)|x(i))× n Y j=1 q 2πσ2 j exp −(θj −µj)2 2σ2 j ! (4.55) which in log space, with µ = 0, and assuming 2σ2 = 1, corresponds to ˆθ = argmax θ m X i=1 logP(y(i)|x(i))−α n X j=1 θ 2 j (4.56) which is in the same form as Eq. 4.51. In this section we give the derivation of the gradient of the cross-entropy loss function LCE for logistic regression. Let’s start with some quick calculus refreshers. First, the derivative of ln(x): d dx ln(x) = 1 x (4.57) Second, the (very elegant) derivative of the sigmoid: dσ(z) dz = σ(z)(1−σ(z)) (4.58) Finally, the chain rule of derivatives.

## Key terms
- **weight** — 10 mentions
- **derivative** — 8 mentions
- **gaussian** — 5 mentions
- **prior** — 4 mentions
- **regularization** — 3 mentions
- **function** — 3 mentions
- **respect** — 3 mentions
- **gradient** — 2 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=101|Speech and Language Processing.pdf p. 101]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/advanced-regularization]]
- Next: [[research/slp/summary-3]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
