---
title: "Conditional Generation of Text: The Intuition"
summary: "§I Large Language Models › Large Language Models › Conditiona: CHAPTER 7 • LARGE LANGUAGE MODELS predicts the next word only from the prior words. Decoders are generative models, meaning that, given input tokens, they generate novel output tokens."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "158-158"
---

# Conditional Generation of Text: The Intuition

§I Large Language Models › Large Language Models › Conditional Generation of Text: The Intuition · pp. 158–158 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 7 • LARGE LANGUAGE MODELS predicts the next word only from the prior words. Decoders are generative models, meaning that, given input tokens, they generate novel output tokens. We’ll discuss decoders in the rest of this chapter and in Chapter 8. The encoder takes as input a sequence of tokens and outputs a vector repreencoder sentation for each token. Encoders are usually masked language models, meaning they are trained by masking out a word, and learning to predict it by looking at surrounding words on both sides. Masked language models like BERT, RoBERTA, and others in the BERT family are encoder models. Encoder models are not generative models; they aren’t used to generate text. Instead encoder models are often used to create classifiers, for example where the input is text and the output is a label, for example for sentiment or topic or other classes. This is done by finetuning them (training them on supervised data). We’ll introduce encoder models in Chapter 9. The encoder-decoder takes as input a sequence of tokens and outputs a series encoder- decoder of tokens. What makes it different than the decoder-only models, is that an encoderdecoder has a much looser relationship between the input tokens and the output tokens, and they are used to map between different kinds of tokens.

## Key terms
- **token** — 23 mentions
- **model** — 14 mentions
- **input** — 12 mentions
- **output** — 9 mentions
- **language** — 8 mentions
- **text** — 8 mentions
- **encoder** — 6 mentions
- **architecture** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=158|Speech and Language Processing.pdf p. 158]]

## Liens
- Up: [[research/slp/large-language-models]]
- ← Prev: [[research/slp/three-architectures-for-language-models]]
- Next: [[research/slp/prompting]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
