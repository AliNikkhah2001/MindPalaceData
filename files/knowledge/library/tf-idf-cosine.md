---
title: TF-IDF Cosine Retrieval
summary: Sparse lexical retrieval measuring term frequency weighted by inverse document frequency, scored by cosine angle.
course: ML Research
tags: [nlp, information-retrieval, sparse]
book: Speech and Language Processing Chapter 11.pdf
page: 5
read: false
---
# TF-IDF Cosine Retrieval

> **Source**: [[pdf:Speech and Language Processing Chapter 11.pdf#page=5|Speech and Language Processing Chapter 11.pdf (p. 5)]]

## Definition & Core Intuition
Sparse lexical retrieval measuring term frequency weighted by inverse document frequency, scored by cosine angle.

## Mathematical Formulation
$$
\text{TF-IDF}(t, d) = \text{TF}(t, d) \cdot \log\left(\frac{N}{|\{d \in D : t \in d\}|}\right)
$$

## Connected Learning Assets
- [[card:7|Review Flashcard #7]]