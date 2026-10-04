---
title: "Counting, Optionality, and Wildcards"
summary: "§I Large Language Models › Words and Tokens › Regular Express: CHAPTER 2 • WORDS AND TOKENS The regular expression r[1234567890] specifies any single digit. This can get awkward (imagine typing r[ABCDEFGHIJKLMNOPQRSTUVWXYZ] to mean an uppercase letter) so the brackets can als"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "28-28"
---

# Counting, Optionality, and Wildcards

§I Large Language Models › Words and Tokens › Regular Expressions › Counting, Optionality, and Wildcards · pp. 28–28 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 2 • WORDS AND TOKENS The regular expression r"[1234567890]" specifies any single digit. This can get awkward (imagine typing r"[ABCDEFGHIJKLMNOPQRSTUVWXYZ]" to mean an uppercase letter) so the brackets can also be used with a dash (-) to specify any one character in a range. The pattern r"[2-5]" specifies any one of the characters 2, 3, range 4, or 5. The pattern r"[b-g]" specifies one of the characters b, c, d, e, f, or g. Some other examples are shown in Fig. 2.9. Regex Match Example Patterns Matched r"[A-Z]" an upper case letter “we should call it ‘Drenched Blossoms’ ” r"[a-z]" a lower case letter “my beans were impatient to be hoed!” r"[0-9]" a single digit “Chapter 1: Down the Rabbit Hole” Figure 2.9 The use of the brackets [] plus the dash - to specify a range. The square braces can also be used to specify what a single character cannot be, by use of the caret ˆ. If the caret ˆ is the first symbol after the open square brace [, the resulting pattern is negated. For example, the pattern r"[ˆa]" matches any single character (including special characters) except a. This is only true when the caret is the first symbol after the open square brace. If it occurs anywhere else, it usually stands for a caret; Fig.

## Key terms
- **character** — 9 mentions
- **pattern** — 7 mentions
- **single** — 5 mentions
- **mean** — 5 mentions
- **match** — 5 mentions
- **caret** — 5 mentions
- **koala** — 5 mentions
- **letter** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=28|Speech and Language Processing.pdf p. 28]]

## Liens
- Up: [[research/slp/regular-expressions]]
- ← Prev: [[research/slp/character-disjunction-the-square-bracket]]
- Next: [[research/slp/anchors-and-boundaries]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
