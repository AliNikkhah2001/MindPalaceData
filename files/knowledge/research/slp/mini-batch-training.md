---
title: "Mini-batch training"
summary: "§I Large Language Models › Logistic Regression › Gradient Des: 4.6 • GRADIENT DESCENT The single update step requires that we compute the gradient, multiplied by the learning rate θt+1 = θt −η∇θL(f(x(i);θ),y(i)) In our mini example there are three parameters, so the gradient vect"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "85-85"
---

# Mini-batch training

§I Large Language Models › Logistic Regression › Gradient Descent › Mini-batch training · pp. 85–85 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.6 • GRADIENT DESCENT The single update step requires that we compute the gradient, multiplied by the learning rate θt+1 = θt −η∇θL(f(x(i);θ),y(i)) In our mini example there are three parameters, so the gradient vector has 3 dimensions, for w1, w2, and b. We can compute the first gradient as follows: ∇w,bL =   ∂LCE(ˆy,y) ∂w1 ∂LCE(ˆy,y) ∂w2 ∂LCE(ˆy,y) ∂b  =   (σ(w ·x+b)−y)x1 (σ(w ·x+b)−y)x2 σ(w ·x+b)−y  =   (σ(0)−1)x1 (σ(0)−1)x2 σ(0)−1  =   −0.5x1 −0.5x2 −0.5  =   −1.5 −1.0 −0.5   Now that we have a gradient, we compute the new parameter vector θ 1 by moving θ 0 in the opposite direction from the gradient: θ 1 =   w1 w2 b  −η   −1.5 −1.0 −0.5  =   .15 .1 .05   So after one step of gradient descent, the weights have shifted to be: w1 = .15, w2 = .1, and b = .05. Note that this observation x happened to be a positive example. We would expect that after seeing more negative examples with high counts of negative words, that the weight w2 would shift to have a negative value. Stochastic gradient descent is called stochastic because it chooses a single random example at a time, moving the weights so as to improve performance on that single example. That can result in very choppy movements, so it’s common to compute the gradient over batches of training instances rather than a single instance.

## Key terms
- **gradient** — 13 mentions
- **training** — 10 mentions
- **compute** — 6 mentions
- **descent** — 5 mentions
- **single** — 5 mentions
- **batch** — 5 mentions
- **weight** — 4 mentions
- **mini-batch** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=85|Speech and Language Processing.pdf p. 85]]

## Liens
- Up: [[research/slp/gradient-descent]]
- ← Prev: [[research/slp/working-through-an-example]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
