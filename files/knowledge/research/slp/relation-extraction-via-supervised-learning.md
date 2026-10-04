---
title: "Relation Extraction via Supervised Learning"
summary: "§II Annotating Linguistic Structure › Information Extraction:: 20.2 • RELATION EXTRACTION ALGORITHMS NP {, NP}* {,} (and|or) other NPH temples, treasuries, and other important civic buildings NPH such as {NP,}* {(or|and)} NP red algae such as Gelidium such NPH as {NP,}* {(or|and)"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "467-468"
---

# Relation Extraction via Supervised Learning

§II Annotating Linguistic Structure › Information Extraction: Relations, Events, and Time › Relation Extraction Algorithms › Relation Extraction via Supervised Learning · pp. 467–468 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
20.2 • RELATION EXTRACTION ALGORITHMS NP {, NP}* {,} (and|or) other NPH temples, treasuries, and other important civic buildings NPH such as {NP,}* {(or|and)} NP red algae such as Gelidium such NPH as {NP,}* {(or|and)} NP such authors as Herrick, Goldsmith, and Shakespeare NPH {,} including {NP,}* {(or|and)} NP common-law countries, including Canada and England NPH {,} especially {NP}* {(or|and)} NP European countries, especially France, England, and Spain Figure 20.4 Hand-built lexico-syntactic patterns for finding hypernyms, using {} to mark optionality (Hearst 1992a, Hearst 1998). Figure 20.4 shows five patterns Hearst (1992a, 1998) suggested for inferring the hyponym relation; we’ve shown NPH as the parent/hyponym. Modern versions of the pattern-based approach extend it by adding named entity constraints. For example if our goal is to answer questions about “Who holds what office in which organization?”, we can use patterns like the following: PER, POSITION of ORG: George Marshall, Secretary of State of the United States PER (named|appointed|chose|etc.) PER Prep? POSITION Truman appointed Marshall Secretary of State PER [be]? (named|appointed|etc.) Prep? ORG POSITION George Marshall was named US Secretary of State Hand-built patterns have the advantage of high-precision and they can be tailored to specific domains.

## Key terms
- **relation** — 23 mentions
- **entities** — 10 mentions
- **extraction** — 7 mentions
- **named** — 7 mentions
- **classifier** — 7 mentions
- **entity** — 6 mentions
- **supervised** — 6 mentions
- **airlines** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=467|Speech and Language Processing.pdf p. 467]]

## Liens
- Up: [[research/slp/relation-extraction-algorithms]]
- ← Prev: [[research/slp/using-patterns-to-extract-relations]]
- Next: [[research/slp/semisupervised-relation-extraction-via-bootstrapping]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
