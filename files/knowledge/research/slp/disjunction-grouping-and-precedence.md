---
title: "Disjunction, Grouping, and Precedence"
summary: "§I Large Language Models › Words and Tokens › Regular Express: CHAPTER 2 • WORDS AND TOKENS Regex Match ˆ start of line $ end of line \b word boundary \B non-word boundary Figure 2.12 Anchors in regular expressions."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "30-30"
---

# Disjunction, Grouping, and Precedence

§I Large Language Models › Words and Tokens › Regular Expressions › Disjunction, Grouping, and Precedence · pp. 30–30 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 2 • WORDS AND TOKENS Regex Match ˆ start of line $ end of line \b word boundary \B non-word boundary Figure 2.12 Anchors in regular expressions. A “word” for the purposes of a regex is defined (based on words in programming languages) as a sequence of digits, underscores, or letters. Thus r"\b99\b" will match the string 99 in There are 99 bottles of beer on the wall (because 99 follows a space) but not 99 in There are 299 bottles of beer on the wall (since 99 follows a number). But it will match 99 in $99 (since 99 follows a dollar sign ($), which is not a digit, underscore, or letter). Note that all these anchors and boundary operators technically match the empty string, meaning that they don’t eat up any characters of the string. The carat in the pattern r"ˆThe" matches the start of "The" but doesn’t actually advance over the first character T. And the pattern r"the\b the" matches the the; the \b is aware of the fact that the space is a boundary, but it matches the empty string right before the space, not the space, so that the space character is available to be matched. Suppose we need to search for texts about pets; perhaps we are particularly interested in cats and dogs.

## Key terms
- **operator** — 14 mentions
- **string** — 10 mentions
- **match** — 9 mentions
- **column** — 9 mentions
- **space** — 8 mentions
- **pattern** — 7 mentions
- **disjunction** — 6 mentions
- **word** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=30|Speech and Language Processing.pdf p. 30]]

## Liens
- Up: [[research/slp/regular-expressions]]
- ← Prev: [[research/slp/anchors-and-boundaries]]
- Next: [[research/slp/a-simple-example]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
