---
title: "Bidirectional Transformer Encoders"
summary: "§I Large Language Models › Masked Language Models › Bidirecti: CHAPTER Masked Language Models Larvatus prodeo [Masked, I go forward] Descartes In the previous two chapters we introduced the transformer and saw how to pretrain a transformer language model as a causal or left-to-ri"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "207-209"
---

# Bidirectional Transformer Encoders

§I Large Language Models › Masked Language Models › Bidirectional Transformer Encoders · pp. 207–209 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER Masked Language Models Larvatus prodeo [Masked, I go forward] Descartes In the previous two chapters we introduced the transformer and saw how to pretrain a transformer language model as a causal or left-to-right language model. In this chapter we’ll introduce a second paradigm for pretrained language models, the bidirectional transformer encoder, and the most widely-used version, the BERT BERT model (Devlin et al., 2019). This model is trained via masked language modeling, masked language modeling where instead of predicting the following word, we mask a word in the middle and ask the model to guess the word given the words on both sides. This method thus allows the model to see both the right and left context. We also introduced finetuning in the prior chapter. Here we describe a new finetuning kind of finetuning, in which we take the transformer network learned by these pretrained models, add a neural net classifier after the top layer of the network, and train it on some additional labeled data to perform some downstream task like named entity tagging or natural language inference. As before, the intuition is that the pretraining phase learns a language model that instantiates rich representations of word meaning, that thus enables the model to more easily learn (‘be finetuned to’) the requirements of a downstream language understanding task.

## Key terms
- **model** — 34 mentions
- **attention** — 26 mentions
- **token** — 24 mentions
- **language** — 19 mentions
- **bidirectional** — 14 mentions
- **transformer** — 13 mentions
- **input** — 12 mentions
- **word** — 11 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=207|Speech and Language Processing.pdf p. 207]]

## Liens
- Up: [[research/slp/masked-language-models]]
- Next: [[research/slp/training-bidirectional-encoders]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
