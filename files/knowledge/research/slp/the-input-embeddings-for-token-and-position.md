---
title: "The input: embeddings for token and position"
summary: "§I Large Language Models › Transformers › The input: embeddin: 8.4 • THE INPUT: EMBEDDINGS FOR TOKEN AND POSITION N tokens is normed in parallel in the LayerNorm. Crucially, the input and output dimensions of transformer blocks are matched so they can be stacked."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "195-196"
---

# The input: embeddings for token and position

§I Large Language Models › Transformers › The input: embeddings for token and position · pp. 195–196 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
8.4 • THE INPUT: EMBEDDINGS FOR TOKEN AND POSITION N tokens is normed in parallel in the LayerNorm. Crucially, the input and output dimensions of transformer blocks are matched so they can be stacked. Since each token xi at the input to the block is represented by an embedding of dimensionality [1×d], that means the input X and output H are both of shape [N ×d]. Let’s talk about where the input X comes from. Given a sequence of N tokens (N is the context length in tokens), the matrix X of shape [N × d] has an embedding for embedding each word in the context. The transformer does this by separately computing two embeddings: an input token embedding, and an input positional embedding. A token embedding, introduced in Chapter 6, is a vector of dimension d that will be our initial representation for the input token. (As we pass vectors up through the transformer layers in the residual stream, this embedding representation will change and grow, incorporating context and playing a different role depending on the kind of language model we are building.) The set of initial embeddings are stored in the embedding matrix E, which has a row for each of the |V| tokens in the vocabulary. (Reminder that V here means the vocabulary of tokens, this V is not related to the value vector.) Thus each word is a row vector of d dimensions, and E has shape [|V|×d].

## Key terms
- **embedding** — 44 mentions
- **token** — 23 mentions
- **input** — 20 mentions
- **position** — 18 mentions
- **word** — 13 mentions
- **vector** — 13 mentions
- **matrix** — 11 mentions
- **positional** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=195|Speech and Language Processing.pdf p. 195]]

## Liens
- Up: [[research/slp/transformers]]
- ← Prev: [[research/slp/parallelizing-computation-using-a-single-matrix-x]]
- Next: [[research/slp/the-language-modeling-head]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
