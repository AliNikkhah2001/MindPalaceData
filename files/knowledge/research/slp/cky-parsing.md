---
title: "CKY Parsing"
summary: "§II Annotating Linguistic Structure › Context-Free Grammars a: CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING Book the flight through Houston S, VP, Verb, Nominal, Noun S,VP,X2 S,VP,X2 Det NP NP Nominal, Noun Nominal Prep PP NP, ProperNoun [0,1] [0,2] [0,3] [0,4] [0,"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "428-428"
---

# CKY Parsing

§II Annotating Linguistic Structure › Context-Free Grammars and Constituency Parsing › CKY Parsing: A Dynamic Programming Approach › CKY Parsing · pp. 428–428 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING Book the flight through Houston S, VP, Verb, Nominal, Noun S,VP,X2 S,VP,X2 Det NP NP Nominal, Noun Nominal Prep PP NP, ProperNoun [0,1] [0,2] [0,3] [0,4] [0,5] [1,2] [1,3] [2,3] [1,4] [2,5] [2,4] [3,4] [4,5] [3,5] [1,5] Figure 18.11 Completed parse table for Book the flight through Houston. function CKY-PARSE(words, grammar) returns table for j←from 1 to LENGTH(words) do for all {A | A →words[j] ∈grammar} table[j −1, j]←table[ j −1, j] ∪A for i←from j −2 down to 0 do for k←i+1 to j −1 do for all {A | A →BC ∈grammar and B ∈table[i,k] and C ∈table[k, j]} table[i,j]←table[i,j] ∪A Figure 18.12 The CKY algorithm. At each such split, the algorithm considers whether the contents of the two cells can be combined in a way that is sanctioned by a rule in the grammar. If such a rule exists, the non-terminal on its left-hand side is entered into the table. Figure 18.14 shows how the five cells of column 5 of the table are filled after the word Houston is read. The arrows point out the two spans that are being used to add an entry to the table. Note that the action in cell [0,5] indicates the presence of three alternative parses for this input, one where the PP modifies the flight, one where it modifies the booking, and one that captures the second argument in the original VP →Verb NP PP rule, now captured indirectly with the VP →X2 PP rule.

## Key terms
- **parse** — 5 mentions
- **grammar** — 5 mentions
- **algorithm** — 4 mentions
- **rule** — 4 mentions
- **word** — 4 mentions
- **cell** — 4 mentions
- **change** — 4 mentions
- **flight** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=428|Speech and Language Processing.pdf p. 428]]

## Liens
- Up: [[research/slp/cky-parsing-a-dynamic-programming-approach]]
- ← Prev: [[research/slp/cky-recognition]]
- Next: [[research/slp/cky-in-practice]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
