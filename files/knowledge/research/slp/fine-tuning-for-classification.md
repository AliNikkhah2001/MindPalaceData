---
title: "Fine-Tuning for Classification"
summary: "§I Large Language Models › Masked Language Models › Fine-Tuni: 9.4 • FINE-TUNING FOR CLASSIFICATION One problem with cosine that is not solved by standardization is that cosine tends to underestimate human judgments on similarity of word meaning for very frequent words (Zhou et a"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "219-220"
---

# Fine-Tuning for Classification

§I Large Language Models › Masked Language Models › Fine-Tuning for Classification · pp. 219–220 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
9.4 • FINE-TUNING FOR CLASSIFICATION One problem with cosine that is not solved by standardization is that cosine tends to underestimate human judgments on similarity of word meaning for very frequent words (Zhou et al., 2022). The power of pretrained language models lies in their ability to extract generalizations from large amounts of text-generalizations that are useful for myriad downstream applications. There are two ways to make practical use of the generalizations to solve downstream tasks. The most common way is to use natural language to prompt the model, putting it in a state where it contextually generates what we want. In this section we explore an alternative way to use pretrained language models for downstream applications: a version of the finetuning paradigm from Chapter 7. finetuning In the kind of finetuning used for masked language models, we add applicationspecific circuitry (often called a special head) on top of pretrained models, taking their output as its input. The finetuning process consists of using labeled data about the application to train these additional application-specific parameters. Typically, this training will either freeze or make only minimal adjustments to the pretrained language model parameters.

## Key terms
- **classification** — 18 mentions
- **model** — 16 mentions
- **sequence** — 14 mentions
- **input** — 13 mentions
- **language** — 12 mentions
- **finetuning** — 9 mentions
- **output** — 8 mentions
- **task** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=219|Speech and Language Processing.pdf p. 219]]

## Liens
- Up: [[research/slp/masked-language-models]]
- ← Prev: [[research/slp/contextual-embeddings]]
- Next: [[research/slp/fine-tuning-for-sequence-labeling-named-entity-recognition]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
