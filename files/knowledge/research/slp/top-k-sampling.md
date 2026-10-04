---
title: "Top-k sampling"
summary: "§I Large Language Models › Transformers › More on Sampling › : 8.6 • MORE ON SAMPLING wi Sample token to generate at position i+1 feedforward layer norm attention layer norm U Input token Language Modeling Head Input Encoding E i + … logits feedforward layer norm layer norm Layer"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "199-199"
---

# Top-k sampling

§I Large Language Models › Transformers › More on Sampling › Top-k sampling · pp. 199–199 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
8.6 • MORE ON SAMPLING wi Sample token to generate at position i+1 feedforward layer norm attention layer norm U Input token Language Modeling Head Input Encoding E i + … logits feedforward layer norm layer norm Layer 1 Layer 2 h1 i = x2 i x1 i h2 i = x3 i feedforward layer norm layer norm hL i hL-1 i = xL i y1 y2 y|V| … Token probabilities u1 u2 u|V| … wi+1 Layer L extra layer norm Figure 8.16 A transformer language model (decoder-only), stacking transformer blocks and mapping from an input token wi to a predicted next token wi+1. words tend to be more creative and more diverse, but less factual and more likely to be incoherent or otherwise low-quality. Top-k sampling is a simple generalization of greedy decoding. Instead of choosing top-k sampling the single most probable word to generate, we first truncate the distribution to the top k most likely words, renormalize to produce a legitimate probability distribution, and then randomly sample from within these k words according to their renormalized probabilities. More formally: 1. Choose in advance a number of words k 2. For each word in the vocabulary V, use the language model to compute the likelihood of this word given the context p(wt|w<t) 3.

## Key terms
- **layer** — 10 mentions
- **word** — 10 mentions
- **norm** — 7 mentions
- **token** — 5 mentions
- **sampling** — 3 mentions
- **feedforward** — 3 mentions
- **input** — 3 mentions
- **language** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=199|Speech and Language Processing.pdf p. 199]]

## Liens
- Up: [[research/slp/more-on-sampling]]
- Next: [[research/slp/nucleus-or-top-p-sampling]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
