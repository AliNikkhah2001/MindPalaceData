---
title: "Simple Unix Tools for Word Tokenization"
summary: "§I Large Language Models › Words and Tokens › Simple Unix Too: 2.7 • SIMPLE UNIX TOOLS FOR WORD TOKENIZATION r’s|’t|’re|’ve|’m|’ll|’d| ?\p{L}+| ?\p{N}+| ?[ˆ\s\p{L}\p{N}]+|\s+(?!\S)|\s+ This is quite a complex regular expression, and also makes use of some advanced Unicode-relat"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "35-35"
---

# Simple Unix Tools for Word Tokenization

§I Large Language Models › Words and Tokens › Simple Unix Tools for Word Tokenization · pp. 35–35 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
2.7 • SIMPLE UNIX TOOLS FOR WORD TOKENIZATION r"’s|’t|’re|’ve|’m|’ll|’d| ?\p{L}+| ?\p{N}+| ?[ˆ\s\p{L}\p{N}]+|\s+(?!\S)|\s+" This is quite a complex regular expression, and also makes use of some advanced Unicode-related features we haven’t described yet. These features are part of a popular external Python 3 library called regex (which is more powerful than the internal Python 3 library called re). For example the regex library has special \p and \P operators that can match if the current character has particular Unicode codepoint properties. For example \p{L} matches any Unicode letter, \P{L} matches any non-letter, \p{N} matches any number, and \P{N} matches any non-number. Fig. 2.15 annotates the regular expression more clearly, and also shows the output of running the GPT-2 tokenizer on the sentence We’re 350 dogs! Um, lunch?. Note that the tokenizer splits We’re into We and ’re, that punctuation is split off from dogs and lunch, and that some tokens like dogs start with a space, and others like We and ! do not. For English it is possible to do simple naive word tokenization and frequency computation in a single Unix command-line. As Church (1994) points out, this can be useful when we need quick information about a text corpus.

## Key terms
- **word** — 5 mentions
- **character** — 5 mentions
- **matches** — 4 mentions
- **output** — 4 mentions
- **sort** — 4 mentions
- **line** — 4 mentions
- **unix** — 3 mentions
- **library** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=35|Speech and Language Processing.pdf p. 35]]

## Liens
- Up: [[research/slp/words-and-tokens]]
- ← Prev: [[research/slp/regular-expressions]]
- Next: [[research/slp/rule-based-tokenization]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
