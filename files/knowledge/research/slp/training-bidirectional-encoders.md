---
title: "Training Bidirectional Encoders"
summary: "§I Large Language Models › Masked Language Models › Training : CHAPTER 9 • MASKED LANGUAGE MODELS • Input context window N=512 tokens, and model dimensionality d=1024, hence X, the input to the model, is of shape [N ×d] = [512×1024]."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "210-213"
---

# Training Bidirectional Encoders

§I Large Language Models › Masked Language Models › Training Bidirectional Encoders · pp. 210–213 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 9 • MASKED LANGUAGE MODELS • Input context window N=512 tokens, and model dimensionality d=1024, hence X, the input to the model, is of shape [N ×d] = [512×1024]. • L=24 layers of transformer blocks, with A=16 multihead attention layers each • The resulting model has about 550M parameters. Note that 550M parameters is relatively small as large language models go (Llama 3 has 405B parameters, so is 3 orders of magnitude bigger). Indeed, masked language models tend to be much smaller than causal language models. We trained causal transformer language models in Chapter 8 by making them iteratively predict the next word in a text. But eliminating the causal mask in attention makes the guess-the-next-word language modeling task trivial-the answer is directly available from the context-so we’re in need of a new training scheme. Instead of trying to predict the next word, the model learns to perform a fill-in-theblank task, technically called the cloze task (Taylor, 1953). To see this, let’s return cloze task to the motivating example from Chapter 3. Instead of predicting which words are likely to come next in this example: The water of Walden Pond is so beautifully we’re asked to predict a missing item given the rest of the sentence.

## Key terms
- **token** — 49 mentions
- **model** — 36 mentions
- **training** — 28 mentions
- **input** — 25 mentions
- **sentence** — 22 mentions
- **loss** — 18 mentions
- **language** — 17 mentions
- **masked** — 16 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=210|Speech and Language Processing.pdf p. 210]]

## Liens
- Up: [[research/slp/masked-language-models]]
- ← Prev: [[research/slp/bidirectional-transformer-encoders]]
- Next: [[research/slp/contextual-embeddings]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
