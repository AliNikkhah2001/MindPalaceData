---
title: "Parallelizing computation using a single matrix X"
summary: "§I Large Language Models › Transformers › Parallelizing compu: 8.2 • TRANSFORMER BLOCKS Notice that the only component that takes as input information from other tokens (other residual streams) is multi-head attention, which (as we see from Eq."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "191-194"
---

# Parallelizing computation using a single matrix X

§I Large Language Models › Transformers › Parallelizing computation using a single matrix X · pp. 191–194 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
8.2 • TRANSFORMER BLOCKS Notice that the only component that takes as input information from other tokens (other residual streams) is multi-head attention, which (as we see from Eq. 8.27) looks at all the neighboring tokens in the context. The output from attention, however, is then added into this token’s embedding stream. In fact, Elhage et al. (2021) show that we can view attention heads as literally moving information from the residual stream of a neighboring token into the current stream. The high-dimensional embedding space at each position thus contains information about the current token and about neighboring tokens, albeit in different subspaces of the vector space. Fig. 8.8 shows a visualization of this movement. We therefore call the attention function the token-mixing component of the architecture, because it mixes information token-mixing from neighboring token streams into the current stream. Token A residual stream Token B residual stream Figure 8.8 An attention head can move information from token A’s residual stream into token B’s residual stream. Crucially, the input and output dimensions of transformer blocks are matched so they can be stacked. Each token vector xi at the input to the block has dimensionality d, and the output hi also has dimensionality d.

## Key terms
- **token** — 50 mentions
- **input** — 31 mentions
- **transformer** — 24 mentions
- **layer** — 20 mentions
- **shape** — 20 mentions
- **attention** — 18 mentions
- **block** — 16 mentions
- **matrix** — 16 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=191|Speech and Language Processing.pdf p. 191]]

## Liens
- Up: [[research/slp/transformers]]
- ← Prev: [[research/slp/transformer-blocks]]
- Next: [[research/slp/the-input-embeddings-for-token-and-position]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
