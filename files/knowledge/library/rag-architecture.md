---
title: RAG (Retrieval-Augmented Generation)
summary: Hybrid neural model combining parametric seq2seq generation with non-parametric dense vector retrieval.
course: ML Research
tags: [rag, nlp, information-retrieval, llm]
book: Retrieval-Augmented.pdf
page: 1
read: false
---
# RAG (Retrieval-Augmented Generation)

> **Source**: [[pdf:Retrieval-Augmented.pdf#page=1|Retrieval-Augmented.pdf (p. 1)]]

## Definition & Core Intuition
Hybrid neural model combining parametric seq2seq generation with non-parametric dense vector retrieval.

## Mathematical Formulation
$$
P(y|x) = \sum_{z \in \text{top-}k} P_\eta(z|x) \prod_{i=1}^N P_\theta(y_i|x, z, y_{1:i-1})
$$

## Connected Learning Assets
- [[quiz:3|Test with Quiz #3]]
- [[card:8|Review Flashcard #8]]