---
title: "Exercises"
summary: "§II Annotating Linguistic Structure › Information Extraction:: CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME No. Step Description Tokens Tokenize input stream of characters Complex Words Multiword phrases, numbers, and proper names."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "486-488"
---

# Exercises

§II Annotating Linguistic Structure › Information Extraction: Relations, Events, and Time › Exercises · pp. 486–488 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME No. Step Description Tokens Tokenize input stream of characters Complex Words Multiword phrases, numbers, and proper names. Basic phrases Segment sentences into noun and verb groups Complex phrases Identify complex noun groups and verb groups Semantic Patterns Identify entities and events, insert into templates. Merging Merge references to the same entity or event Figure 20.20 Levels of processing in FASTUS (Hobbs et al., 1997). Each level extracts a specific type of information which is then passed on to the next higher level. on hand-built regular expressions like the following (NG indicates Noun-Group and VG Verb-Group), which matches the first sentence of the news story above. NG(Company/ies) VG(Set-up) NG(Joint-Venture) with NG(Company/ies) VG(Produce) NG(Product) The result of processing these two sentences is the five draft templates (Fig. 20.21) that must then be merged into the single hierarchical structure shown in Fig. 20.19. The merging algorithm, after performing coreference resolution, merges two activities that are likely to be describing the same events. # Template/Slot Value 1 RELATIONSHIP: TIE-UP ENT…

## Key terms
- **system** — 13 mentions
- **event** — 9 mentions
- **relation** — 8 mentions
- **extraction** — 7 mentions
- **expressions** — 6 mentions
- **template** — 6 mentions
- **slot** — 5 mentions
- **approaches** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=486|Speech and Language Processing.pdf p. 486]]

## Liens
- Up: [[research/slp/information-extraction-relations-events-and-time]]
- ← Prev: [[research/slp/historical-notes-19]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
