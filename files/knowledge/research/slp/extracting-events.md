---
title: "Extracting Events"
summary: "§II Annotating Linguistic Structure › Information Extraction:: CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME has the relation phrases has a hub in and is the headquarters of (it also has has and is, but longer phrases are preferred)."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "474-474"
---

# Extracting Events

§II Annotating Linguistic Structure › Information Extraction: Relations, Events, and Time › Extracting Events · pp. 474–474 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME has the relation phrases has a hub in and is the headquarters of (it also has has and is, but longer phrases are preferred). Step 3 finds United to the left and Chicago to the right of has a hub in, and skips over which to find Chicago to the left of is the headquarters of. The final output is: r1: <United, has a hub in, Chicago> r2: <Chicago, is the headquarters of, United Continental Holdings> The great advantage of unsupervised relation extraction is its ability to handle a huge number of relations without having to specify them in advance. The disadvantage is the need to map all the strings into some canonical form for adding to databases or knowledge graphs. Current methods focus heavily on relations expressed with verbs, and so will miss many relations that are expressed nominally. Supervised relation extraction systems are evaluated by using test sets with humanannotated, gold-standard relations and computing precision, recall, and F-measure. Labeled precision and recall require the system to classify the relation correctly, whereas unlabeled methods simply measure a system’s ability to detect entities that are related.

## Key terms
- **relation** — 20 mentions
- **precision** — 7 mentions
- **system** — 7 mentions
- **event** — 7 mentions
- **text** — 6 mentions
- **extraction** — 5 mentions
- **methods** — 5 mentions
- **recall** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=474|Speech and Language Processing.pdf p. 474]]

## Liens
- Up: [[research/slp/information-extraction-relations-events-and-time]]
- ← Prev: [[research/slp/relation-extraction-algorithms]]
- Next: [[research/slp/representing-time]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
