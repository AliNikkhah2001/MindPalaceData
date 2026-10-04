---
title: "KV Cache"
summary: "§I Large Language Models › Transformers › Dealing with Scale : CHAPTER 8 • TRANSFORMERS or compute budget, if in each case the other two properties are held constant: L(N) = Nc N αN (8.49) L(D) = Dc D αD (8.50) L(C) = Cc C αC (8.51) The number of (non-embedding) parameters "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "202-202"
---

# KV Cache

§I Large Language Models › Transformers › Dealing with Scale › KV Cache · pp. 202–202 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 8 • TRANSFORMERS or compute budget, if in each case the other two properties are held constant: L(N) = Nc N αN (8.49) L(D) = Dc D αD (8.50) L(C) = Cc C αC (8.51) The number of (non-embedding) parameters N can be roughly computed as follows (ignoring biases, and with d as the input and output dimensionality of the model, dattn as the self-attention layer size, and dff the size of the feedforward layer): N ≈2 d nlayer(2 dattn +dff) ≈12 nlayer d2 (8.52) (assuming dattn = dff/4 = d) Thus GPT-3, with n = 96 layers and dimensionality d = 12288, has 12 × 96 × 122882 ≈175 billion parameters. The values of Nc, Dc, Cc, αN, αD, and αC depend on the exact transformer architecture, tokenization, and vocabulary size, so rather than all the precise values, scaling laws focus on the relationship with loss.3 Scaling laws can be useful in deciding how to train a model to a particular performance, for example by looking at early in the training curve, or performance with smaller amounts of data, to predict what the loss would be if we were to add more data or increase model size. Other aspects of scaling laws can also tell us how much data we need to add when scaling up a model. We saw in Fig.

## Key terms
- **value** — 8 mentions
- **token** — 5 mentions
- **model** — 4 mentions
- **size** — 4 mentions
- **scaling** — 4 mentions
- **vector** — 4 mentions
- **cache** — 4 mentions
- **compute** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=202|Speech and Language Processing.pdf p. 202]]

## Liens
- Up: [[research/slp/dealing-with-scale]]
- ← Prev: [[research/slp/scaling-laws]]
- Next: [[research/slp/parameter-efficient-fine-tuning]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
