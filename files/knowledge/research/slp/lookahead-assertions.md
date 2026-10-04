---
title: "Lookahead Assertions"
summary: "§I Large Language Models › Words and Tokens › Regular Express: CHAPTER 2 • WORDS AND TOKENS Finally, there will be times when we need to predict the future: look ahead in the text to see if some pattern matches, but not yet advance the pointer we always keep to where we are in th"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "34-34"
---

# Lookahead Assertions

§I Large Language Models › Words and Tokens › Regular Expressions › Lookahead Assertions · pp. 34–34 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 2 • WORDS AND TOKENS Finally, there will be times when we need to predict the future: look ahead in the text to see if some pattern matches, but not yet advance the pointer we always keep to where we are in the text, so that we can then deal with the pattern if it occurs, but if it doesn’t we can check for something else instead. These lookahead assertions make use of the (? syntax that we saw in the previlookahead ous section for non-capture groups. The operator (?= pattern) is true if pattern occurs, but is zero-width, i.e. the match pointer doesn’t advance, just as we saw zero-width with anchors and boundary markers like \b. The operator (?! pattern) only returns true if a pattern does not match, but again is zero-width and doesn’t advance the pointer. Negative lookahead is commonly used when we are parsing some complex pattern but want to rule out a special case. For example suppose we want to capture the first word on the line, but only if it doesn’t start with the letter T. We can use negative lookahead to do this: r"ˆ(?![tT])(\w+)\b" (2.18) The first negative lookahead says that the line must not start with a t or T, but matches the empty string, not moving the match pointer.

## Key terms
- **pattern** — 7 mentions
- **word** — 6 mentions
- **doesn** — 5 mentions
- **text** — 4 mentions
- **pointer** — 4 mentions
- **lookahead** — 4 mentions
- **first** — 4 mentions
- **sequence** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=34|Speech and Language Processing.pdf p. 34]]

## Liens
- Up: [[research/slp/regular-expressions]]
- ← Prev: [[research/slp/substitutions-and-capture-groups]]
- Next: [[research/slp/regular-expressions-for-bpe-pre-tokenization]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
