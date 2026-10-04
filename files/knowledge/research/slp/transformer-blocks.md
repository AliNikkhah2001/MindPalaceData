---
title: "Transformer Blocks"
summary: "§I Large Language Models › Transformers › Transformer Blocks: CHAPTER 8 • TRANSFORMERS dv = 64, A = 8, and d = 512). Thus for each head i, we have weight layers WQi of shape [d ×dk], WKi of shape [d ×dk], and WVi of shape [d ×dv]."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "188-190"
---

# Transformer Blocks

§I Large Language Models › Transformers › Transformer Blocks · pp. 188–190 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 8 • TRANSFORMERS dv = 64, A = 8, and d = 512). Thus for each head i, we have weight layers WQi of shape [d ×dk], WKi of shape [d ×dk], and WVi of shape [d ×dv]. Below are the equations for attention augmented with multiple heads; Fig. 8.6 shows an intuition. qc i = xiWQc; kc j = xjWKc; vc j = xjWVc; ∀c 1 ≤c ≤A (8.15) scorec(xi,xj) = qc i ·kc j √dk (8.16) αc ij = softmax(scorec(xi,xj)) ∀j ≤i (8.17) headc i = X j≤i αc ijvc j (8.18) ai = (head1 ⊕head2...⊕headA)WO (8.19) MultiHeadAttention(xi,[x1,··· ,xi−1]) = ai (8.20) Note in Eq. 8.20 that MultiHeadAttention is a function of the current input xi, as well as all the other inputs. For the causal or left-to-right attention that we use in this chapter, the other inputs are only to the left, but we’ll also see a version of attention in Chapter 9 where attention is a function of the tokens to the right as well. We’ll return to this idea about causal inputs in Eq. 8.34 when we introduce the idea of masking the right context. The output of each of the A heads is of shape [1 × dv], and so the output of the multi-head layer with A heads consists of A vectors of shape [1 × dv]. These are concatenated to produce a single output with dimensionality [1×Adv].

## Key terms
- **layer** — 42 mentions
- **vector** — 15 mentions
- **norm** — 15 mentions
- **transformer** — 14 mentions
- **attention** — 13 mentions
- **input** — 13 mentions
- **head** — 12 mentions
- **output** — 12 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=188|Speech and Language Processing.pdf p. 188]]

## Liens
- Up: [[research/slp/transformers]]
- ← Prev: [[research/slp/attention]]
- Next: [[research/slp/parallelizing-computation-using-a-single-matrix-x]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
