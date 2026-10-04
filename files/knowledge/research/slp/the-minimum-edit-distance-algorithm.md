---
title: "The Minimum Edit Distance Algorithm"
summary: "§I Large Language Models › Words and Tokens › Minimum Edit Di: 2.9 • MINIMUM EDIT DISTANCE of words is to some reference sequence of words. Edit distance gives us a way to quantify these intuitions about string similarity."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "39-42"
---

# The Minimum Edit Distance Algorithm

§I Large Language Models › Words and Tokens › Minimum Edit Distance › The Minimum Edit Distance Algorithm · pp. 39–42 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
2.9 • MINIMUM EDIT DISTANCE of words is to some reference sequence of words. Edit distance gives us a way to quantify these intuitions about string similarity. More formally, the minimum edit distance between two strings is defined as the minimum edit distance minimum number of editing operations (operations like insertion, deletion, substitution) needed to transform one string into another. In this section we’ll introduce edit distance for single words, but the algorithm applies equally to entire strings. The gap between intention and execution, for example, is 5 (delete an i, substitute e for n, substitute x for t, insert c, substitute u for n). It’s much easier to see this by looking at the most important visualization for string distances, an alignment alignment between the two strings, shown in Fig. 2.17. Given two sequences, an alignment is a correspondence between substrings of the two sequences. Thus, we say I aligns with the empty string, N with E, and so on. Beneath the aligned strings is another representation; a series of symbols expressing an operation list for converting the top string into the bottom string: d for deletion, s for substitution, i for insertion. I N T E * N T I O N | | | | | | | | | | * E X E C U T I O N d s s i s Figure 2.17 Representing the minimum edit distance between two strings as an alignment.

## Key terms
- **distance** — 37 mentions
- **edit** — 27 mentions
- **string** — 27 mentions
- **minimum** — 23 mentions
- **algorithm** — 18 mentions
- **cell** — 17 mentions
- **alignment** — 16 mentions
- **cost** — 16 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=39|Speech and Language Processing.pdf p. 39]]

## Liens
- Up: [[research/slp/minimum-edit-distance]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
