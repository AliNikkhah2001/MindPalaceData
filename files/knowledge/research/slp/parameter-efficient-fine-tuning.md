---
title: "Parameter Efficient Fine Tuning"
summary: "§I Large Language Models › Transformers › Dealing with Scale : 8.8 • DEALING WITH SCALE q4 k1 k2 k4 Q KT QKT v1 v2 v3 v4 V q4•k1 q4•k2 q4•k3 q4•k4 x = = x a4 A 1 x dk dk x N 1 x N N x dv 1 x dv k3 Figure 8.18 Parts of the attention computation (extracted from Fig."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "203-203"
---

# Parameter Efficient Fine Tuning

§I Large Language Models › Transformers › Dealing with Scale › Parameter Efficient Fine Tuning · pp. 203–203 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
8.8 • DEALING WITH SCALE q4 k1 k2 k4 Q KT QKT v1 v2 v3 v4 V q4•k1 q4•k2 q4•k3 q4•k4 x = = x a4 A 1 x dk dk x N 1 x N N x dv 1 x dv k3 Figure 8.18 Parts of the attention computation (extracted from Fig. 8.11) showing, in black, the vectors that can be stored in the cache rather than recomputed when computing the attention score for the 4th token. As we mentioned above, it’s very common to take a language model and give it more information about a new domain by finetuning it (continuing to train it to predict upcoming words) on some additional data. Fine-tuning can be very difficult with very large language models, because there are enormous numbers of parameters to train; each pass of batch gradient descent has to backpropagate through many many huge layers. This makes finetuning huge language models extremely expensive in processing power, in memory, and in time. For this reason, there are alternative methods that allow a model to be finetuned without changing all the parameters. Such methods are called parameter-efficient fine tuning or sometimes PEFT, because we efficiently select a subset of parameters parameterefficient fine tuning PEFT to update when finetuning. For example we freeze some of the parameters (don’t change them), and only update some particular subset of parameters.

## Key terms
- **lora** — 9 mentions
- **parameters** — 8 mentions
- **update** — 7 mentions
- **finetuning** — 6 mentions
- **layers** — 6 mentions
- **model** — 5 mentions
- **instead** — 5 mentions
- **attention** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=203|Speech and Language Processing.pdf p. 203]]

## Liens
- Up: [[research/slp/dealing-with-scale]]
- ← Prev: [[research/slp/kv-cache]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
