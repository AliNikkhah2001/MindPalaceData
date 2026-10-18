---
title: Self-Attention Mechanism
summary: Calculates dynamic sequence representations by computing scaled dot-product attention over Queries, Keys, and Values.
course: ML Research
tags: [transformers, attention, nlp]
book: Speech and Language Processing Chapter 11.pdf
page: 8
read: false
---
# Self-Attention Mechanism

> **Source**: [[pdf:Speech and Language Processing Chapter 11.pdf#page=8|Speech and Language Processing Chapter 11.pdf (p. 8)]]

## Definition & Core Intuition
Calculates dynamic sequence representations by computing scaled dot-product attention over Queries, Keys, and Values.

## Mathematical Formulation
$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

## Connected Learning Assets