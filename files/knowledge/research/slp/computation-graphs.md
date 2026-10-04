---
title: "Computation Graphs"
summary: "§I Large Language Models › Neural Networks › Training Neural : 6.6 • TRAINING NEURAL NETS How do we compute the gradient of this loss function? Computing the gradient requires the partial derivative of the loss function with respect to each parameter."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "147-147"
---

# Computation Graphs

§I Large Language Models › Neural Networks › Training Neural Nets › Computation Graphs · pp. 147–147 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
6.6 • TRAINING NEURAL NETS How do we compute the gradient of this loss function? Computing the gradient requires the partial derivative of the loss function with respect to each parameter. For a network with one weight layer and sigmoid output (which is what logistic regression is), we could simply use the derivative of the loss that we used for logistic regression in Eq. 6.29 (and derived in Section 4.15): ∂LCE(ˆy,y) ∂wj = (ˆy−y)x j = (σ(w ·x+b)−y)xj (6.29) Or for a network with one weight layer and softmax output (=multinomial logistic regression), we could use the derivative of the softmax loss from Eq. 4.41, shown for a particular weight wk and input xi ∂LCE(ˆy,y) ∂wk,i = −(yk −ˆyk)xi = −(yk −p(yk = 1|x))xi = − yk − exp(wk ·x+bk) PK j=1 exp(w j ·x+b j) ! xi (6.30) But these derivatives only give correct updates for one weight layer: the last one! For deep networks, computing the gradients for each weight is much more complex, since we are computing the derivative with respect to weight parameters that appear all the way back in the very early layers of the network, even though the loss is computed only at the very end of the network. The solution to computing this gradient is an algorithm called error backpropagation or backprop (Rumelhart et al., 1986).

## Key terms
- **computing** — 6 mentions
- **network** — 6 mentions
- **weight** — 6 mentions
- **computation** — 6 mentions
- **graph** — 6 mentions
- **loss** — 5 mentions
- **derivative** — 5 mentions
- **gradient** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=147|Speech and Language Processing.pdf p. 147]]

## Liens
- Up: [[research/slp/training-neural-nets]]
- ← Prev: [[research/slp/computing-the-gradient]]
- Next: [[research/slp/backward-differentiation-on-computation-graphs]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
