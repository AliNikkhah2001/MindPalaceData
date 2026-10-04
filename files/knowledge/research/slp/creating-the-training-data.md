---
title: "Creating the Training data"
summary: "§I Large Language Models › Machine Translation › Machine Tran: 12.2 • MACHINE TRANSLATION USING ENCODER-DECODER 2. Repeat until there are V wordpieces: (a) Train an n-gram language model on the training corpus, using the current set of wordpieces."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "273-274"
---

# Creating the Training data

§I Large Language Models › Machine Translation › Machine Translation using Encoder-Decoder › Creating the Training data · pp. 273–274 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
12.2 • MACHINE TRANSLATION USING ENCODER-DECODER 2. Repeat until there are V wordpieces: (a) Train an n-gram language model on the training corpus, using the current set of wordpieces. (b) Consider the set of possible new wordpieces made by concatenating two wordpieces from the current lexicon. Choose the one new wordpiece that most increases the language model probability of the training corpus. Recall that with BPE we had to specify the number of merges to perform; in wordpiece, by contrast, we specify the total vocabulary, which is a more intuitive parameter. A vocabulary of 8K to 32K word pieces is commonly used. An even more commonly used tokenization algorithm is (somewhat ambiguously) called the unigram algorithm (Kudo, 2018) or sometimes the SentencePiece unigram SentencePiece algorithm, and is used in systems like ALBERT (Lan et al., 2020) and T5 (Raffel et al., 2020). (Because unigram is the default tokenization algorithm used in a library called SentencePiece that adds a useful wrapper around tokenization algorithms (Kudo and Richardson, 2018b), authors often say they are using SentencePiece tokenization but really mean they are using the unigram algorithm). In unigram t…

## Key terms
- **sentence** — 24 mentions
- **algorithm** — 12 mentions
- **alignment** — 12 mentions
- **language** — 10 mentions
- **token** — 10 mentions
- **corpus** — 9 mentions
- **unigram** — 9 mentions
- **tokenization** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=273|Speech and Language Processing.pdf p. 273]]

## Liens
- Up: [[research/slp/machine-translation-using-encoder-decoder]]
- ← Prev: [[research/slp/tokenization]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
