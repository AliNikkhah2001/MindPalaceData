---
title: "Interpreting the Transformer"
summary: "§I Large Language Models › Transformers › Interpreting the Tr: 8.8 • DEALING WITH SCALE q4 k1 k2 k4 Q KT QKT v1 v2 v3 v4 V q4•k1 q4•k2 q4•k3 q4•k4 x = = x a4 A 1 x dk dk x N 1 x N N x dv 1 x dv k3 Figure 8.18 Parts of the attention computation (extracted from Fig."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "203-204"
---

# Interpreting the Transformer

§I Large Language Models › Transformers › Interpreting the Transformer · pp. 203–204 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
8.8 • DEALING WITH SCALE q4 k1 k2 k4 Q KT QKT v1 v2 v3 v4 V q4•k1 q4•k2 q4•k3 q4•k4 x = = x a4 A 1 x dk dk x N 1 x N N x dv 1 x dv k3 Figure 8.18 Parts of the attention computation (extracted from Fig. 8.11) showing, in black, the vectors that can be stored in the cache rather than recomputed when computing the attention score for the 4th token. As we mentioned above, it’s very common to take a language model and give it more information about a new domain by finetuning it (continuing to train it to predict upcoming words) on some additional data. Fine-tuning can be very difficult with very large language models, because there are enormous numbers of parameters to train; each pass of batch gradient descent has to backpropagate through many many huge layers. This makes finetuning huge language models extremely expensive in processing power, in memory, and in time. For this reason, there are alternative methods that allow a model to be finetuned without changing all the parameters. Such methods are called parameter-efficient fine tuning or sometimes PEFT, because we efficiently select a subset of parameters parameterefficient fine tuning PEFT to update when finetuning. For example we freeze some of the parameters (don’t change them), and only update some particular subset of parameters.

## Key terms
- **model** — 15 mentions
- **parameters** — 10 mentions
- **lora** — 10 mentions
- **update** — 8 mentions
- **learning** — 8 mentions
- **language** — 7 mentions
- **instead** — 7 mentions
- **finetuning** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=203|Speech and Language Processing.pdf p. 203]]

## Liens
- Up: [[research/slp/transformers]]
- ← Prev: [[research/slp/dealing-with-scale]]
- Next: [[research/slp/summary-7]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
