---
title: "Scaling laws"
summary: "§I Large Language Models › Transformers › Dealing with Scale : 8.8 • DEALING WITH SCALE long and thanks for Next token all Loss … = −log yand … −log ythanks Stacked Transformer Blocks So long and thanks for … … … U Input tokens x1 x2 Language Modeling Head x3 x4 x5 Input Encoding"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "201-201"
---

# Scaling laws

§I Large Language Models › Transformers › Dealing with Scale › Scaling laws · pp. 201–201 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
8.8 • DEALING WITH SCALE long and thanks for Next token all Loss … = −log yand … −log ythanks Stacked Transformer Blocks So long and thanks for … … … U Input tokens x1 x2 Language Modeling Head x3 x4 x5 Input Encoding E + E + E + E + E + … … … … … U U U U … logits logits logits logits logits Figure 8.17 Training a transformer as a language model. Large language models are large. For example the Llama 3.1 405B Instruct model from Meta has 405 billion parameters (it has L=126 layers, model dimensionality d=16,384, and A=128 attention heads) and was trained on 15.6 terabytes of text tokens using a vocabulary of 128K tokens (Llama Team, 2024). So there is a lot of research on understanding how LLMs scale, and especially how to implement them given limited resources. In the next few sections we discuss how to think about scale (the concept of scaling laws), and important techniques for getting language models to work efficiently, such as the KV cache and parameter-efficient fine tuning (PEFT). The performance of large language models has shown to be mainly determined by 3 factors: model size (the number of parameters not counting embeddings), dataset size (the amount of training data), and the amount of compute used for training.

## Key terms
- **model** — 11 mentions
- **training** — 7 mentions
- **language** — 6 mentions
- **logits** — 5 mentions
- **parameters** — 5 mentions
- **scale** — 4 mentions
- **token** — 4 mentions
- **large** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=201|Speech and Language Processing.pdf p. 201]]

## Liens
- Up: [[research/slp/dealing-with-scale]]
- Next: [[research/slp/kv-cache]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
