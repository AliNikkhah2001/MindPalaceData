---
title: "Gradient Descent"
summary: "§I Large Language Models › Logistic Regression › Gradient Des: 4.6 • GRADIENT DESCENT Our goal with gradient descent is to find the optimal weights: minimize the loss function we’ve defined for the model."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "81-85"
---

# Gradient Descent

§I Large Language Models › Logistic Regression › Gradient Descent · pp. 81–85 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.6 • GRADIENT DESCENT Our goal with gradient descent is to find the optimal weights: minimize the loss function we’ve defined for the model. In Eq. 4.21 below, we’ll explicitly represent the fact that the cross-entropy loss function LCE is parameterized by the weights. In machine learning in general we refer to the parameters being learned as θ; in the case of logistic regression θ = {w,b}. So we’ll represent ˆy(i) as f(x(i);θ) to make the dependence on θ more obvious. The goal is to find the set of weights which minimizes the loss function, averaged over all examples: ˆθ = argmin θ m m X i=1 LCE(f(x(i);θ),y(i)) (4.21) How shall we find the minimum of this (or any) loss function? Gradient descent is a method that finds a minimum of a function by figuring out in which direction (in the space of the parameters θ) the function’s slope is rising the most steeply, and moving in the opposite direction. The intuition is that if you are hiking in a canyon and trying to descend most quickly down to the river at the bottom, you might look around yourself in all directions, find the direction where the ground is sloping the steepest, and walk downhill in that direction. For logistic regression, this loss function is conveniently convex.

## Key terms
- **gradient** — 39 mentions
- **function** — 27 mentions
- **loss** — 23 mentions
- **direction** — 17 mentions
- **descent** — 16 mentions
- **slope** — 14 mentions
- **algorithm** — 12 mentions
- **learning** — 11 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=81|Speech and Language Processing.pdf p. 81]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/the-cross-entropy-loss-function]]
- Next: [[research/slp/multinomial-logistic-regression]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
