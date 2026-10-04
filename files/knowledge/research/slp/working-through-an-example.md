---
title: "Working through an example"
summary: "§I Large Language Models › Logistic Regression › Gradient Des: CHAPTER 4 • LOGISTIC REGRESSION function STOCHASTIC GRADIENT DESCENT(L(), f(), x, y) returns θ # where: L is the loss function # f is a function parameterized by θ # x is the set of training inputs x(1), x(2),..., x(m"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "84-84"
---

# Working through an example

§I Large Language Models › Logistic Regression › Gradient Descent › Working through an example · pp. 84–84 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 4 • LOGISTIC REGRESSION function STOCHASTIC GRADIENT DESCENT(L(), f(), x, y) returns θ # where: L is the loss function # f is a function parameterized by θ # x is the set of training inputs x(1), x(2),..., x(m) # y is the set of training outputs (labels) y(1), y(2),..., y(m) θ ←0 # (or small random values) repeat til done # see caption For each training tuple (x(i), y(i)) (in random order) 1. Optional (for reporting): # How are we doing on this tuple? Compute ˆy(i) = f(x(i);θ) # What is our estimated output ˆy? Compute the loss L(ˆy(i),y(i)) # How far off is ˆy(i) from the true output y(i)? 2. g←∇θL(f(x(i);θ),y(i)) # How should we move θ to maximize loss? 3. θ ←θ −η g # Go the other way instead return θ Figure 4.5 The stochastic gradient descent algorithm. Step 1 (computing the loss) is used mainly to report how well we are doing on the current tuple; we don’t need to compute the loss in order to compute the gradient. The algorithm can terminate when it converges (when the gradient norm < ϵ), or when progress halts (for example when the loss starts going up on a held-out set). Weights are initialized to 0 for logistic regression, but to small random values for neural networks, as we’ll see in Chapter 6.

## Key terms
- **loss** — 7 mentions
- **algorithm** — 7 mentions
- **gradient** — 6 mentions
- **function** — 5 mentions
- **training** — 5 mentions
- **learning** — 5 mentions
- **descent** — 4 mentions
- **random** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=84|Speech and Language Processing.pdf p. 84]]

## Liens
- Up: [[research/slp/gradient-descent]]
- ← Prev: [[research/slp/the-stochastic-gradient-descent-algorithm]]
- Next: [[research/slp/mini-batch-training]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
