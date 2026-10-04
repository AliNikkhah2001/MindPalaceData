---
title: "Named Entities and Named Entity Tagging"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: 17.3 • NAMED ENTITIES AND NAMED ENTITY TAGGING The most-frequent-tag baseline has an accuracy of about 92%1. The baseline thus differs from the state-of-the-art and human ceiling (97%) by only 5%."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "395-396"
---

# Named Entities and Named Entity Tagging

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › Named Entities and Named Entity Tagging · pp. 395–396 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
17.3 • NAMED ENTITIES AND NAMED ENTITY TAGGING The most-frequent-tag baseline has an accuracy of about 92%1. The baseline thus differs from the state-of-the-art and human ceiling (97%) by only 5%. Part of speech tagging can tell us that words like Janet, Stanford University, and Colorado are all proper nouns; being a proper noun is a grammatical property of these words. But viewed from a semantic perspective, these proper nouns refer to different kinds of entities: Janet is a person, Stanford University is an organization, and Colorado is a location. Here we re-introduce the concept of a named entity, which was also introduced named entity in Section 9.5 for readers who haven’t yet read Chapter 9. A named entity is, roughly speaking, anything that can be referred to with a named entity proper name: a person, a location, an organization. The task of named entity recognition (NER) is to find spans of text that constitute proper names and tag the type of named entity recognition NER the entity. Four entity tags are most common: PER (person), LOC (location), ORG (organization), or GPE (geo-political entity). However, the term named entity is commonly extended to include things that aren’t entities per se, including dates, times, and other kinds of temporal expressions, and even numerical expressions like prices.

## Key terms
- **entity** — 23 mentions
- **named** — 20 mentions
- **tagging** — 16 mentions
- **entities** — 9 mentions
- **type** — 9 mentions
- **label** — 8 mentions
- **span** — 8 mentions
- **word** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=395|Speech and Language Processing.pdf p. 395]]

## Liens
- Up: [[research/slp/sequence-labeling-for-parts-of-speech-and-named-entities]]
- ← Prev: [[research/slp/part-of-speech-tagging]]
- Next: [[research/slp/hmm-part-of-speech-tagging]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
