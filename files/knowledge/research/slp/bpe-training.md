---
title: "BPE training"
summary: "§I Large Language Models › Words and Tokens › Subword Tokeniz: CHAPTER 2 • WORDS AND TOKENS (ULM) (Kudo, 2018).2 In this section we introduce the byte-pair encoding or BPE BPE algorithm (Sennrich et al., 2016; Gage, 1994); see Fig."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "22-23"
---

# BPE training

§I Large Language Models › Words and Tokens › Subword Tokenization: Byte-Pair Encoding › BPE training · pp. 22–23 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 2 • WORDS AND TOKENS (ULM) (Kudo, 2018).2 In this section we introduce the byte-pair encoding or BPE BPE algorithm (Sennrich et al., 2016; Gage, 1994); see Fig. 2.6. Like most tokenization schemes, the BPE algorithm has two parts: a trainer, and an encoder. In general in the token training phase we take a raw training corpus (usually roughly pre-separated into words, for example by whitespace) and induce a vocabulary, a set of tokens. Then a token encoder takes a raw test sentence and encodes it into the tokens in the vocabulary that were learned in training. The BPE training algorithm iteratively merges frequent neighboring tokens to create longer and longer tokens. The algorithm begins with a vocabulary that is just the set of all individual characters. It then examines the training corpus, and finds the two characters that are most frequently adjacent. Imagine our original corpus is 10 characters long, using a vocabulary of 5 characters, {A, B, C, D, E}: A B D C A B E C A B The most frequent neighboring pair of characters is “A B” so we merge those, add a new merged token ‘AB’ to the vocabulary, and replace every adjacent ‘A’ ‘B’ in the corpus with the new ‘AB’: AB D C AB E C AB Now we have a vocabulary of 6 possible tokens {A, B, C, D, E, AB}, and the corpus has length 7.

## Key terms
- **token** — 17 mentions
- **corpus** — 16 mentions
- **vocabulary** — 16 mentions
- **merge** — 14 mentions
- **character** — 13 mentions
- **algorithm** — 12 mentions
- **word** — 11 mentions
- **count** — 9 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=22|Speech and Language Processing.pdf p. 22]]

## Liens
- Up: [[research/slp/subword-tokenization-byte-pair-encoding]]
- Next: [[research/slp/bpe-encoder]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
