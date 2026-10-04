---
title: "Unicode"
summary: "§I Large Language Models › Words and Tokens › Unicode: CHAPTER 2 • WORDS AND TOKENS Nonetheless, the fact morphemes can be hard to define, and that many languages can have complex morphemes that aren’t easy to break up into pieces makes it very difficult to use morphemes as a sta"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "18-20"
---

# Unicode

§I Large Language Models › Words and Tokens › Unicode · pp. 18–20 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 2 • WORDS AND TOKENS Nonetheless, the fact morphemes can be hard to define, and that many languages can have complex morphemes that aren’t easy to break up into pieces makes it very difficult to use morphemes as a standard for tokenization cross-lingually. Another option we could consider for tokenization is the level of the individual character. How do we even represent characters across languages and writing system? The Unicode standard is a method for representing text written using any character Unicode in any script of the languages of the world (including dead languages like Sumerian cuneiform, and invented languages like Klingon). Let’s start with a brief historical note about an English-specific subset of Unicode (technically called ‘Basic Latin’ in Unicode, and commonly referred to as ASCII). Starting in the 1960s, the Latin characters used to write English (like the ones used in this sentence), were represented with a code called ASCII (American Standard ASCII Code for Information Interchange). ASCII represented each character with a single byte. A byte can represent 256 different characters, but ASCII only used 127 of them; the high-order bit of ASCII bytes is always set to 0.

## Key terms
- **character** — 36 mentions
- **byte** — 33 mentions
- **code** — 28 mentions
- **point** — 22 mentions
- **ascii** — 18 mentions
- **unicode** — 16 mentions
- **encoding** — 16 mentions
- **latin** — 11 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=18|Speech and Language Processing.pdf p. 18]]

## Liens
- Up: [[research/slp/words-and-tokens]]
- ← Prev: [[research/slp/morphemes-parts-of-words]]
- Next: [[research/slp/subword-tokenization-byte-pair-encoding]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
