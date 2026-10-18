---
title: Byte Pair Encoding (BPE)
summary: Data compression algorithm adapted for subword tokenization; iteratively merges most frequent byte/character pairs.
course: ML Research
tags: [nlp, tokenization, llm]
book: Speech and Language Processing Chapter 11.pdf
page: 1
read: false
---
# Byte Pair Encoding (BPE)

> **Source**: [[pdf:Speech and Language Processing Chapter 11.pdf#page=1|Speech and Language Processing Chapter 11.pdf (p. 1)]]

## Definition & Core Intuition
Data compression algorithm adapted for subword tokenization; iteratively merges most frequent byte/character pairs.

## Mathematical Formulation
$$
\text{merge}(c_1, c_2) \to c_{\text{new}} \quad \text{where} \quad (c_1, c_2) = \arg\max \text{freq}(a, b)
$$

## Connected Learning Assets
- [[quiz:3|Test with Quiz #3]]
- [[card:4|Review Flashcard #4]]

## Related Concepts
- [[concept:self-attention|Self Attention]]