---
title: Dense Passage Retrieval (DPR)
summary: Dual-encoder architecture mapping questions and passages into low-dimensional dense space for MIPS search.
course: ML Research
tags: [dpr, retrieval, embeddings]
book: Retrieval-Augmented.pdf
page: 3
read: false
---
# Dense Passage Retrieval (DPR)

> **Source**: [[pdf:Retrieval-Augmented.pdf#page=3|Retrieval-Augmented.pdf (p. 3)]]

## Definition & Core Intuition
Dual-encoder architecture mapping questions and passages into low-dimensional dense space for MIPS search.

## Mathematical Formulation
$$
\text{sim}(q, p) = \mathbf{E}_Q(q)^T \mathbf{E}_P(p)
$$

## Connected Learning Assets

## Related Concepts
- [[concept:rag-architecture|Rag Architecture]]