---
title: "Logit Lens"
summary: "§I Large Language Models › Transformers › Interpreting the Tr: 8.9 • INTERPRETING THE TRANSFORMER which is a kind of abstract component of a network. The induction head circuit is part of the attention computation in transformers, discovered by looking at mini language models wit"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "205-205"
---

# Logit Lens

§I Large Language Models › Transformers › Interpreting the Transformer › Logit Lens · pp. 205–205 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
8.9 • INTERPRETING THE TRANSFORMER which is a kind of abstract component of a network. The induction head circuit is part of the attention computation in transformers, discovered by looking at mini language models with only 1-2 attention heads. The function of the induction head is to predict repeated sequences. For example if it sees the pattern AB...A in an input sequence, it predicts that B will follow, instantiating the pattern completion rule AB...A→B. It does this by having a prefix matching component of the attention computation that, when looking at the current token A, searches back over the context to find a prior instance of A. If it finds one, the induction head has a copying mechanism that “copies” the token B that followed the earlier A, by increasing the probability the B will occur next. Fig. 8.20 shows an example. Figure 8.20 An induction head looking at vintage uses the prefix matching mechanism to find a prior instance of vintage, and the copying mechanism to predict that cars will occur again. Figure from Crosbie and Shutova (2022). Olsson et al. (2022) propose that a generalized fuzzy version of this pattern completion rule, implementing a rule like A*B*...A→B, where A* ≈A and B* ≈B (by ≈we mean they are semantically similar in some way), might be responsible for in-context learning.

## Key terms
- **head** — 10 mentions
- **induction** — 7 mentions
- **transformer** — 5 mentions
- **attention** — 4 mentions
- **find** — 4 mentions
- **learning** — 4 mentions
- **logit** — 4 mentions
- **internal** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=205|Speech and Language Processing.pdf p. 205]]

## Liens
- Up: [[research/slp/interpreting-the-transformer]]
- ← Prev: [[research/slp/in-context-learning-and-induction-heads]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
