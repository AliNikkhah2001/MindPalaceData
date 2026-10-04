---
title: "Anchors and Boundaries"
summary: "§I Large Language Models › Words and Tokens › Regular Express: That’s because Kleene star means “zero or more occurrences”. Instead, for the sheep language we’ll want rbaaa*, meaning b followed by aa followed by zero or more additional as."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "29-29"
---

# Anchors and Boundaries

§I Large Language Models › Words and Tokens › Regular Expressions › Anchors and Boundaries · pp. 29–29 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
2.6 • REGULAR EXPRESSIONS a. That’s because Kleene star means “zero or more occurrences”. Instead, for the sheep language we’ll want r"baaa*", meaning b followed by aa followed by zero or more additional as. More complex patterns can also be repeated. So r"[ab]*" means “zero or more a’s or b’s” (not “zero or more right square braces”). This will match strings like aaaa or ababab or bbbb, as well as the empty string. For specifying an integer (a string of digits) we can use r"[0-9][0-9]*". (Why isn’t it just r"[0-9]*"?) There is a slightly shorter way to specify “at least one” of some character: the Kleene +, which means “one or more occurrences of the immediately preceding Kleene + character or regular expression”. So r"[0-9]+" is the normal way to specify “a sequence of digits”, and we could also specify the sheep language as r"baa+!". Besides the Kleene * and Kleene + we can also use explicit numbers as counters, by enclosing them in curly brackets. The operator r"{3}" means “exactly 3 occurrences of the previous character or expression”. So r"ax{10}z" will match a followed by exactly 10 x’s followed by z. An important special character is the period (r"."), a wildcard expression that period matches any single character (except a newline).

## Key terms
- **expression** — 11 mentions
- **character** — 9 mentions
- **zero** — 8 mentions
- **matches** — 8 mentions
- **mean** — 8 mentions
- **line** — 7 mentions
- **occurrence** — 7 mentions
- **kleene** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=29|Speech and Language Processing.pdf p. 29]]

## Liens
- Up: [[research/slp/regular-expressions]]
- ← Prev: [[research/slp/counting-optionality-and-wildcards]]
- Next: [[research/slp/disjunction-grouping-and-precedence]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
