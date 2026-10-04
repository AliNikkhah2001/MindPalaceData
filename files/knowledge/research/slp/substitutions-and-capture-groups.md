---
title: "Substitutions and Capture Groups"
summary: "§I Large Language Models › Words and Tokens › Regular Express: CHAPTER 2 • WORDS AND TOKENS Regex Expansion Match First Matches \d [0-9] any digit Party␣of␣5 \D [ˆ0-9] any non-digit Blue␣moon \w [a-zA-Z0-9_] any alphanumeric/underscore Daiyu \W [ˆ\w] a non-alphanumeric !!!!"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "32-33"
---

# Substitutions and Capture Groups

§I Large Language Models › Words and Tokens › Regular Expressions › Substitutions and Capture Groups · pp. 32–33 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 2 • WORDS AND TOKENS Regex Expansion Match First Matches \d [0-9] any digit Party␣of␣5 \D [ˆ0-9] any non-digit Blue␣moon \w [a-zA-Z0-9_] any alphanumeric/underscore Daiyu \W [ˆ\w] a non-alphanumeric !!!! \s [␣\r\t\n\f] whitespace (space, tab) in Concord \S [ˆ\s] Non-whitespace in␣Concord Figure 2.13 Aliases for common sets of characters. How do we refer to characters that are special themselves (like ., *, -, [, and \) when we mean them literally, not in their special usage? That is, if we are trying to match a period, or a star, or a bracket or paren? To get the literal meaning of a special character, we need to precede them with a backslash, (i.e., r"\.", r"\*", r"\[", and r"\\"). Regex Match First Patterns Matched \* an asterisk “*” “K*A*P*L*A*N” \. a period “.” “Dr. Livingston, I presume” \? a question mark “Why don’t they come and lend a hand?” \n a newline \t a tab Figure 2.14 Some characters that need to be escaped (via backslash). An important use of regular expressions is in substitutions, where we want to resubstitution place one string with another. Regular expression can help us specify the string to be replaced as well as the replacement. In Python we use the function re.sub() (similar functions exist in other languages and environments).

## Key terms
- **group** — 17 mentions
- **string** — 12 mentions
- **pattern** — 12 mentions
- **capture** — 11 mentions
- **digit** — 7 mentions
- **want** — 7 mentions
- **substitution** — 7 mentions
- **date** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=32|Speech and Language Processing.pdf p. 32]]

## Liens
- Up: [[research/slp/regular-expressions]]
- ← Prev: [[research/slp/more-operators]]
- Next: [[research/slp/lookahead-assertions]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
