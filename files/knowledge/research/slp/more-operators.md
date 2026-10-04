---
title: "More Operators"
summary: "§I Large Language Models › Words and Tokens › Regular Express: 2.6 • REGULAR EXPRESSIONS of operator precedence, from highest precedence to lowest precedence. {} Sequences and anchors the ˆmy end$ Disjunction | Thus, because counters have a higher precedence than sequences, rthe"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "31-31"
---

# More Operators

§I Large Language Models › Words and Tokens › Regular Expressions › More Operators · pp. 31–31 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
2.6 • REGULAR EXPRESSIONS of operator precedence, from highest precedence to lowest precedence. Parenthesis () Counters * + ? {} Sequences and anchors the ˆmy end$ Disjunction | Thus, because counters have a higher precedence than sequences, r"the*" matches theeeee but not thethe. Because sequences have a higher precedence than disjunction, r"the|any" matches the or any but not thany or theny. Patterns can be ambiguous in another way. Consider the expression r"[a-z]*" when matching against the text once upon a time. Since r"[a-z]*" matches zero or more letters, this expression could match nothing, or just the first letter o, on, onc, or once. In these cases regular expressions always match the largest string they can; we say that patterns are greedy, expanding to cover as much of a string as they can. greedy There are, however, ways to enforce non-greedy matching, using another meannon-greedy ing of the ? qualifier. The operator *? is a Kleene star that matches as little text as *? possible. The operator +? is a Kleene plus that matches as little text as possible. +? Suppose we wanted to write a regex to find cases of the English article the. A simple (but incorrect) pattern might be: r"the" (2.14) One problem is that this pattern will miss the word when it begins a sentence and hence is capitalized (i.e., The).

## Key terms
- **false** — 6 mentions
- **precedence** — 5 mentions
- **matches** — 5 mentions
- **pattern** — 5 mentions
- **expression** — 4 mentions
- **text** — 4 mentions
- **string** — 4 mentions
- **operator** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=31|Speech and Language Processing.pdf p. 31]]

## Liens
- Up: [[research/slp/regular-expressions]]
- ← Prev: [[research/slp/a-simple-example]]
- Next: [[research/slp/substitutions-and-capture-groups]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
