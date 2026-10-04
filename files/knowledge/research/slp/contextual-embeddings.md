---
title: "Contextual Embeddings"
summary: "§I Large Language Models › Masked Language Models › Contextua: CHAPTER 9 • MASKED LANGUAGE MODELS a whole. Approximately 40 passes (epochs) over the training data was required for the model to converge."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "214-218"
---

# Contextual Embeddings

§I Large Language Models › Masked Language Models › Contextual Embeddings · pp. 214–218 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 9 • MASKED LANGUAGE MODELS a whole. Approximately 40 passes (epochs) over the training data was required for the model to converge. Some models, like the RoBERTa model, drop the next sentence prediction objective, and therefore change the training regime a bit. Instead of sampling pairs of sentence, the input is simply a series of contiguous sentences, still beginning with the special [CLS] token. If the document runs out before 512 tokens are reached, an extra separator token is added, and sentences from the next document are packed in, until we reach a total of 512 tokens. Usually large batch sizes are used, between 8K and 32K tokens. Multilingual models have an additional decision to make: what data to use to build the vocabulary? Recall that all language models use subword tokenization (BPE or SentencePiece Unigram LM are the two most common algorithms). What text should be used to learn this multilingual tokenization, given that it’s easier to get much more text in some languages than others? One option would be to create this vocabulary-learning dataset by sampling sentences from our training data (perhaps web text from Common Crawl), randomly. In that case we will choose a lot of sentences from languages with lots of web representation like English, and the tokens will be biased toward rare English tokens instead of creating frequent tokens from languages with less data.

## Key terms
- **word** — 44 mentions
- **sense** — 39 mentions
- **model** — 26 mentions
- **embedding** — 25 mentions
- **language** — 23 mentions
- **contextual** — 21 mentions
- **token** — 20 mentions
- **meaning** — 15 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=214|Speech and Language Processing.pdf p. 214]]

## Liens
- Up: [[research/slp/masked-language-models]]
- ← Prev: [[research/slp/training-bidirectional-encoders]]
- Next: [[research/slp/fine-tuning-for-classification]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
