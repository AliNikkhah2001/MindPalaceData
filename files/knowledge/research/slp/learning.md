---
title: "Learning"
summary: "§I Large Language Models › Automatic Speech Recognition › The: CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION Adding a language model Since an encoder-decoder model is essentially a conditional language model, encoder-decoders implicitly learn a language model for the output domain of"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "358-358"
---

# Learning

§I Large Language Models › Automatic Speech Recognition › The Encoder-Decoder Architecture for ASR › Learning · pp. 358–358 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION Adding a language model Since an encoder-decoder model is essentially a conditional language model, encoder-decoders implicitly learn a language model for the output domain of letters from their training data. However, the training data (speech paired with text transcriptions) may not include sufficient text to train a good language model. After all, it’s easier to find enormous amounts of pure text training data than it is to find text paired with speech. Thus we can can usually improve a model at least slightly by incorporating a very large language model. The simplest way to do this is to use beam search to get a final beam of hypothesized sentences; this beam is sometimes called an n-best list. We then use a n-best list language model to rescore each hypothesis on the beam. The scoring is done by inrescore terpolating the score assigned by the language model with the encoder-decoder score used to create the beam, with a weight λ tuned on a held-out set. Also, since most models prefer shorter sentences, ASR systems normally have some way of adding a length factor. One way to do this is to normalize the probability by the number of characters in the hypothesis |Y|c.

## Key terms
- **model** — 12 mentions
- **language** — 9 mentions
- **data** — 8 mentions
- **speech** — 5 mentions
- **encoder-decoder** — 5 mentions
- **training** — 5 mentions
- **beam** — 5 mentions
- **output** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=358|Speech and Language Processing.pdf p. 358]]

## Liens
- Up: [[research/slp/the-encoder-decoder-architecture-for-asr]]
- ← Prev: [[research/slp/inference]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
