---
title: "More details on learning"
summary: "§I Large Language Models › Neural Networks › Training Neural : 6.6 • TRAINING NEURAL NETS We’ll also need the derivatives of each of the other activation functions. The derivative of tanh is: d tanh(z) dz = 1−tanh2(z) (6.39) The derivative of the ReLU is2 d ReLU(z) dz =  0 for z"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "151-151"
---

# More details on learning

§I Large Language Models › Neural Networks › Training Neural Nets › More details on learning · pp. 151–151 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
6.6 • TRAINING NEURAL NETS We’ll also need the derivatives of each of the other activation functions. The derivative of tanh is: d tanh(z) dz = 1−tanh2(z) (6.39) The derivative of the ReLU is2 d ReLU(z) dz =  0 for z < 0 1 for z ≥0 (6.40) We’ll give the start of the computation, computing the derivative of the loss function L with respect to z, or ∂L ∂z (and leaving the rest of the computation as an exercise for the reader). By the chain rule: ∂L ∂z = ∂L ∂a[2] ∂a[2] ∂z (6.41) So let’s first compute ∂L ∂a[2] , taking the derivative of Eq. 6.37, repeated here: LCE(a[2],y) = − h yloga[2] +(1−y)log(1−a[2]) i ∂L ∂a[2] = − y∂log(a[2]) ∂a[2] ! +(1−y)∂log(1−a[2]) ∂a[2] ! = −  y 1 a[2]  +(1−y) 1−a[2] (−1)  = −  y a[2] + y−1 1−a[2]  (6.42) Next, by the derivative of the sigmoid: ∂a[2] ∂z = a[2](1−a[2]) Finally, we can use the chain rule: ∂L ∂z = ∂L ∂a[2] ∂a[2] ∂z = −  y a[2] + y−1 1−a[2]  a[2](1−a[2]) = a[2] −y (6.43) Continuing the backward computation of the gradients (next by passing the gradients over b[2] 1 and the two product nodes, and so on, back to all the teal nodes), is left as an exercise for the reader. Optimization in neural networks is a non-convex optimization problem, more complex than for logistic regression, and for that and other reasons there are many best practices for successful learning.

## Key terms
- **derivative** — 7 mentions
- **computation** — 3 mentions
- **neural** — 2 mentions
- **tanh** — 2 mentions
- **relu** — 2 mentions
- **function** — 2 mentions
- **exercise** — 2 mentions
- **reader** — 2 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=151|Speech and Language Processing.pdf p. 151]]

## Liens
- Up: [[research/slp/training-neural-nets]]
- ← Prev: [[research/slp/backward-differentiation-on-computation-graphs]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
