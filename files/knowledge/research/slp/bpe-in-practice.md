---
title: "BPE in practice"
summary: "§I Large Language Models › Words and Tokens › Subword Tokeniz: CHAPTER 2 • WORDS AND TOKENS Once we’ve learned our vocabulary, the BPE encoder is used to tokenize a test sentence. The encoder just runs on the test data the merges we have learned from the training data."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "24-24"
---

# BPE in practice

§I Large Language Models › Words and Tokens › Subword Tokenization: Byte-Pair Encoding › BPE in practice · pp. 24–24 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 2 • WORDS AND TOKENS Once we’ve learned our vocabulary, the BPE encoder is used to tokenize a test sentence. The encoder just runs on the test data the merges we have learned from the training data. It runs them greedily, in the order we learned them. (Thus the frequencies in the test data don’t play a role, just the frequencies in the training data). So first we segment each test sentence word into characters. Then we apply the first rule: replace every instance of n e in the test corpus with ne, and then the second rule: replace every instance of ne w in the test corpus with new, and so on. By the end of course many of the merges simple recreated words in the training set. But the merges also created knowledge of morphemes like the re- prefix (that might appear in perhaps unseen combinations like revisit or rearrange), or the morpheme new without an initial space (hence word-internal) that might appear at the start of sentences or in words unseen in training like anew. Of course in real settings BPE is run with tens of thousands of merges on a very large input corpus, to produce vocabulary sizes of 50,000, 100,000, or even 200,000 tokens. The result is that most words can be represented as single tokens, and only the rarer words (and unknown words) will have to be represented by multiple tokens.

## Key terms
- **token** — 14 mentions
- **word** — 13 mentions
- **byte** — 7 mentions
- **test** — 6 mentions
- **sentence** — 5 mentions
- **appear** — 5 mentions
- **data** — 4 mentions
- **merges** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=24|Speech and Language Processing.pdf p. 24]]

## Liens
- Up: [[research/slp/subword-tokenization-byte-pair-encoding]]
- ← Prev: [[research/slp/bpe-encoder]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
