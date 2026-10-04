---
title: "Subword Tokenization: Byte-Pair Encoding"
summary: "§I Large Language Models › Words and Tokens › Subword Tokeniz: 2.4 • SUBWORD TOKENIZATION: BYTE-PAIR ENCODING Unicode and Python: Starting with Python 3, all Python strings are stored internally as Unicode, each string a sequence of Unicode code points."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "21-24"
---

# Subword Tokenization: Byte-Pair Encoding

§I Large Language Models › Words and Tokens › Subword Tokenization: Byte-Pair Encoding · pp. 21–24 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
2.4 • SUBWORD TOKENIZATION: BYTE-PAIR ENCODING Unicode and Python: Starting with Python 3, all Python strings are stored internally as Unicode, each string a sequence of Unicode code points. Thus string functions and regular expressions all apply natively to code points. For example, functions like len() of a string return its length in characters, i.e., code points, not its length in bytes. When reading or writing from a file, however, the code points need to be encoded and decoding using a method like UTF-8. That is, every file is encoded in some encoding. If it’s not UTF-8, it’s an older encoding method like ASCII or Latin-1 (iso 8859 1). There is no such thing as a text file without an encoding. The encoding method is specified in Python when opening a file for reading and writing. Tokenization, the first stage of natural language processing, is the process of segtokenization menting the running input text into tokens. tokens We’ve seen three candidates for tokens: words, morphemes and characters. But each has problems as a unit. Words and morphemes seem approximately at the right level for NLP processing, since they tend to have consistent meanings, but they are challenging to define formally.

## Key terms
- **token** — 42 mentions
- **word** — 37 mentions
- **corpus** — 24 mentions
- **character** — 19 mentions
- **vocabulary** — 18 mentions
- **merge** — 18 mentions
- **algorithm** — 17 mentions
- **training** — 13 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=21|Speech and Language Processing.pdf p. 21]]

## Liens
- Up: [[research/slp/words-and-tokens]]
- ← Prev: [[research/slp/unicode]]
- Next: [[research/slp/corpora]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
