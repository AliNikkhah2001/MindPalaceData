---
title: "Distant Supervision for Relation Extraction"
summary: "§II Annotating Linguistic Structure › Information Extraction:: CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME From these results, we can use the context of words between the entity mentions, the words before mention one, the word after mention two, and the named"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "470-471"
---

# Distant Supervision for Relation Extraction

§II Annotating Linguistic Structure › Information Extraction: Relations, Events, and Time › Relation Extraction Algorithms › Distant Supervision for Relation Extraction · pp. 470–471 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME From these results, we can use the context of words between the entity mentions, the words before mention one, the word after mention two, and the named entity types of the two mentions, and perhaps other features, to extract general patterns such as the following: / [ORG], which uses [LOC] as a hub / / [ORG]’s hub at [LOC] / / [LOC], a main hub for [ORG] / These new patterns can then be used to search for additional tuples. Bootstrapping systems also assign confidence values to new tuples to avoid seconfidence values mantic drift. In semantic drift, an erroneous pattern leads to the introduction of semantic drift erroneous tuples, which, in turn, lead to the creation of problematic patterns and the meaning of the extracted relations ‘drifts’. Consider the following example: (20.9) Sydney has a ferry hub at Circular Quay. If accepted as a positive example, this expression could lead to the incorrect introduction of the tuple ⟨Sydney,CircularQuay⟩. Patterns based on this tuple could propagate further errors into the database. Confidence values for patterns are based on balancing two factors: the pattern’s performance with respect to the current set of tuples and the pattern’s productivity in terms of the number of matches it produces in the document collection.

## Key terms
- **tuple** — 19 mentions
- **pattern** — 17 mentions
- **feature** — 10 mentions
- **relation** — 9 mentions
- **training** — 8 mentions
- **mention** — 7 mentions
- **confidence** — 7 mentions
- **these** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=470|Speech and Language Processing.pdf p. 470]]

## Liens
- Up: [[research/slp/relation-extraction-algorithms]]
- ← Prev: [[research/slp/semisupervised-relation-extraction-via-bootstrapping]]
- Next: [[research/slp/unsupervised-relation-extraction]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
