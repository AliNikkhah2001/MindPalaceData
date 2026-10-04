---
title: "Masked Language Models"
summary: "§I Large Language Models › Masked Language Models: CHAPTER Masked Language Models Larvatus prodeo [Masked, I go forward] Descartes In the previous two chapters we introduced the transformer and saw how to pretrain a transformer language model as a causal or left-to-right language"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "207-225"
---

# Masked Language Models

§I Large Language Models › Masked Language Models · pp. 207–225 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER Masked Language Models Larvatus prodeo [Masked, I go forward] Descartes In the previous two chapters we introduced the transformer and saw how to pretrain a transformer language model as a causal or left-to-right language model. In this chapter we’ll introduce a second paradigm for pretrained language models, the bidirectional transformer encoder, and the most widely-used version, the BERT BERT model (Devlin et al., 2019). This model is trained via masked language modeling, masked language modeling where instead of predicting the following word, we mask a word in the middle and ask the model to guess the word given the words on both sides. This method thus allows the model to see both the right and left context. We also introduced finetuning in the prior chapter. Here we describe a new finetuning kind of finetuning, in which we take the transformer network learned by these pretrained models, add a neural net classifier after the top layer of the network, and train it on some additional labeled data to perform some downstream task like named entity tagging or natural language inference. As before, the intuition is that the pretraining phase learns a language model that instantiates rich representations of word meaning, that thus enables the model to more easily learn (‘be finetuned to’) the requirements of a downstream language understanding task.

## Key terms
- **model** — 49 mentions
- **token** — 30 mentions
- **language** — 28 mentions
- **attention** — 28 mentions
- **input** — 20 mentions
- **word** — 16 mentions
- **transformer** — 15 mentions
- **task** — 15 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=207|Speech and Language Processing.pdf p. 207]]

## Liens
- Up: [[research/slp/i-large-language-models]]
- ← Prev: [[research/slp/transformers]]
- Next: [[research/slp/post-training-instruction-tuning-alignment-and-test-time-compute]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
