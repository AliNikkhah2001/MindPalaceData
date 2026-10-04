---
title: "Code Points"
summary: "§I Large Language Models › Words and Tokens › Unicode › Code : 2.3 • UNICODE Spanish) to scripts of ancient languages (Cuneiform, Ugaritic, Egyptian Hieroglyph, Pahlavi), as well as mathematical symbols, emojis, currency symbols, and more."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "19-19"
---

# Code Points

§I Large Language Models › Words and Tokens › Unicode › Code Points · pp. 19–19 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
2.3 • UNICODE Spanish) to scripts of ancient languages (Cuneiform, Ugaritic, Egyptian Hieroglyph, Pahlavi), as well as mathematical symbols, emojis, currency symbols, and more. How does it work? Unicode assigns a unique id, called a code point, for each one code point of these 150,000 characters. The code point is an abstract representation of the character, and each code point is represented by a number, traditionally written in hexadecimal, from number 0 through 0x10FFFF (which is 1,114,111 decimal). Having over a million code points means there is a lot of room for new characters. It is traditional to represent these code points with the prefix “U+” (which just means “the following is a Unicode hex representation of a code point”). So the code point for the character a is U+0061 which is the same as 0x0061. (Note that Unicode was designed to be backwards compatible with ASCII, which means that the first 127 code points, including the code for a, are identical with ASCII.) Here are some sample code points; some (but not all) come with descriptions: U+0061 a LATIN SMALL LETTER A U+0062 b LATIN SMALL LETTER B U+0063 c LATIN SMALL LETTER C U+00F9 `u LATIN SMALL LETTER U WITH GRAVE U…

## Key terms
- **code** — 16 mentions
- **point** — 15 mentions
- **character** — 9 mentions
- **representation** — 7 mentions
- **latin** — 7 mentions
- **small** — 7 mentions
- **letter** — 7 mentions
- **unicode** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=19|Speech and Language Processing.pdf p. 19]]

## Liens
- Up: [[research/slp/unicode]]
- Next: [[research/slp/utf-8-encoding]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
