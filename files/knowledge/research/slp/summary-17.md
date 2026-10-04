---
title: "Summary"
summary: "§II Annotating Linguistic Structure › Context-Free Grammars a: (Should the complementizer to or the verb be the head of an infinite verb phrase?) Modern linguistic theories of syntax generally include a component that defines heads (see, e.g., (Pollard and Sag, 1994))."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "435-435"
---

# Summary

§II Annotating Linguistic Structure › Context-Free Grammars and Constituency Parsing › Summary · pp. 435–435 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
18.10 • SUMMARY most phrases. (Should the complementizer to or the verb be the head of an infinite verb phrase?) Modern linguistic theories of syntax generally include a component that defines heads (see, e.g., (Pollard and Sag, 1994)). An alternative approach to finding a head is used in most practical computational systems. Instead of specifying head rules in the grammar itself, heads are identified dynamically in the context of trees for specific sentences. In other words, once a sentence is parsed, the resulting tree is walked to decorate each node with the appropriate head. Most current systems rely on a simple set of handwritten rules, such as a practical one for Penn Treebank grammars given in Collins (1999) but developed originally by Magerman (1995). For example, the rule for finding the head of an NP is as follows (Collins, 1999, p. 238): • If the last word is tagged POS, return last-word. • Else search from right to left for the first child which is an NN, NNP, NNPS, NX, POS, or JJR. • Else search from left to right for the first child which is an NP. • Else search from right to left for the first child which is a $, ADJP, or PRN. • Else search from right to left for the first child which is a CD.

## Key terms
- **left** — 12 mentions
- **head** — 10 mentions
- **rule** — 8 mentions
- **search** — 7 mentions
- **right** — 7 mentions
- **first** — 7 mentions
- **grammar** — 6 mentions
- **else** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=435|Speech and Language Processing.pdf p. 435]]

## Liens
- Up: [[research/slp/context-free-grammars-and-constituency-parsing]]
- ← Prev: [[research/slp/heads-and-head-finding]]
- Next: [[research/slp/historical-notes-17]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
