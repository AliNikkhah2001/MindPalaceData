---
title: "Backward differentiation on computation graphs"
summary: "§I Large Language Models › Neural Networks › Training Neural : CHAPTER 6 • NEURAL NETWORKS operation left to right, passing the outputs of each computation as the input to the next node."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "148-150"
---

# Backward differentiation on computation graphs

§I Large Language Models › Neural Networks › Training Neural Nets › Backward differentiation on computation graphs · pp. 148–150 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 6 • NEURAL NETWORKS operation left to right, passing the outputs of each computation as the input to the next node. e=a+d d = 2b L=ce a=3 b=1 c=-2 e=5 d=2 L=-10 forward pass a b c Figure 6.15 Computation graph for the function L(a,b,c) = c(a+2b), with values for input nodes a = 3, b = 1, c = −2, showing the forward pass computation of L. The importance of the computation graph comes from the backward pass, which is used to compute the derivatives that we’ll need for the weight update. In this example our goal is to compute the derivative of the output function L with respect to each of the input variables, i.e., ∂L ∂a, ∂L ∂b, and ∂L ∂c . The derivative ∂L ∂a tells us how much a small change in a affects L. Backwards differentiation makes use of the chain rule in calculus, so let’s rechain rule mind ourselves of that. Suppose we are computing the derivative of a composite function f(x) = u(v(x)). The derivative of f(x) is the derivative of u(x) with respect to v(x) times the derivative of v(x) with respect to x: d f dx = du dv · dv dx (6.31) The chain rule extends to more than two functions. If computing the derivative of a composite function f(x) = u(v(w(x))), the derivative of f(x) is: d f dx = du dv · dv dw · dw dx (6.32) The intuition of backward differentiation is to pass gradients back from the final node to all the nodes in the graph.

## Key terms
- **node** — 18 mentions
- **derivative** — 18 mentions
- **gradient** — 17 mentions
- **computation** — 12 mentions
- **graph** — 12 mentions
- **pass** — 11 mentions
- **function** — 11 mentions
- **backward** — 11 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=148|Speech and Language Processing.pdf p. 148]]

## Liens
- Up: [[research/slp/training-neural-nets]]
- ← Prev: [[research/slp/computation-graphs]]
- Next: [[research/slp/more-details-on-learning]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
