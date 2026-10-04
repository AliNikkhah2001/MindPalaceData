---
title: "Loss function"
summary: "§I Large Language Models › Neural Networks › Training Neural : 6.6 • TRAINING NEURAL NETS size of 3, given one-hot input vectors for each input context word, are: e = [Ext−3;Ext−2;Ext−1] h = σ(We+b) z = Uh ˆy = softmax(z) (6.24) Note thatwe we use semicolons to mean concatenation"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "145-145"
---

# Loss function

§I Large Language Models › Neural Networks › Training Neural Nets › Loss function · pp. 145–145 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
6.6 • TRAINING NEURAL NETS size of 3, given one-hot input vectors for each input context word, are: e = [Ext−3;Ext−2;Ext−1] h = σ(We+b) z = Uh ˆy = softmax(z) (6.24) Note thatwe we use semicolons to mean concatenation of vectors, so we form the embedding layer e by concatenating the 3 embeddings for the three context vectors. We’ll return to this idea of using neural networks to do language modeling in Chapter 7 and Chapter 8 when we introduce transformer language models. A feedforward neural net is an instance of supervised machine learning in which we know the correct output y for each observation x. What the system produces, via Eq. 6.13, is ˆy, the system’s estimate of the true y. The goal of the training procedure is to learn parameters W[i] and b[i] for each layer i that make ˆy for each training observation as close as possible to the true y. In general, we do all this by drawing on the methods we introduced in Chapter 4 for logistic regression, so the reader should be comfortable with that chapter before proceeding. We’ll explore the algorithm on simple generic networks rather than networks designed for sentiment or language modeling. First, we’ll need a loss function that models the distance between the system output and the gold output, and it’s common to use the loss function used for logistic regression, the cross-entropy loss.

## Key terms
- **loss** — 15 mentions
- **function** — 8 mentions
- **layer** — 7 mentions
- **network** — 7 mentions
- **neural** — 6 mentions
- **regression** — 6 mentions
- **logistic** — 5 mentions
- **parameters** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=145|Speech and Language Processing.pdf p. 145]]

## Liens
- Up: [[research/slp/training-neural-nets]]
- Next: [[research/slp/computing-the-gradient]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
