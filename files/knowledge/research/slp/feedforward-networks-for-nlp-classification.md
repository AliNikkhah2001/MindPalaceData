---
title: "Feedforward networks for NLP: Classification"
summary: "§I Large Language Models › Neural Networks › Feedforward netw: CHAPTER 6 • NEURAL NETWORKS Replacing the bias unit In describing networks, we will sometimes use a slightly simplified notation that represents exactly the same function without referring to an explicit bias node b."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "138-139"
---

# Feedforward networks for NLP: Classification

§I Large Language Models › Neural Networks › Feedforward networks for NLP: Classification · pp. 138–139 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 6 • NEURAL NETWORKS Replacing the bias unit In describing networks, we will sometimes use a slightly simplified notation that represents exactly the same function without referring to an explicit bias node b. Instead, we add a dummy node a0 to each layer whose value will always be 1. Thus layer 0, the input layer, will have a dummy node a[0] 0 = 1, layer 1 will have a[1] 0 = 1, and so on. This dummy node still has an associated weight, and that weight represents the bias value b. For example instead of an equation like h = σ(Wx+b) (6.15) we’ll use: h = σ(Wx) (6.16) But now instead of our vector x having n0 values: x = x1,...,xn0, it will have n0 + 1 values, with a new 0th dummy value x0 = 1: x = x0,...,xn0. And instead of computing each h j as follows: h j = σ n0 X i=1 Wji xi +b j ! , (6.17) we’ll instead use: h j = σ n0 X i=0 Wji xi ! , (6.18) where the value Wj0 replaces what had been b j. Fig. 6.9 shows a visualization. x1 x2 xn0 … … +1 b … U W h1 y1 y2 yn2 h2 h3 hn1 x1 x2 xn0 … … x0=1 … U W h1 y1 y2 yn2 h2 h3 hn1 (a) (b) Figure 6.9 Replacing the bias node (shown in a) with x0 (b). We’ll continue showing the bias as b when we go over the learning algorithm in Section 6.6, but going forward in the book, for most figures and some equations we’ll use this simplified notation without explicit bias terms.

## Key terms
- **layer** — 13 mentions
- **network** — 11 mentions
- **classifier** — 9 mentions
- **node** — 7 mentions
- **feature** — 7 mentions
- **bias** — 6 mentions
- **instead** — 6 mentions
- **value** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=138|Speech and Language Processing.pdf p. 138]]

## Liens
- Up: [[research/slp/neural-networks]]
- ← Prev: [[research/slp/feedforward-neural-networks]]
- Next: [[research/slp/embeddings-as-the-input-to-neural-net-classifiers]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
