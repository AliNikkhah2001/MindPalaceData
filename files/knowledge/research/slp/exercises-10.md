---
title: "Exercises"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: 17.8 • SUMMARY guages need to label words with case and gender information. Tagsets for morphologically rich languages are therefore sequences of morphological tags rather than a single primitive tag."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "411-414"
---

# Exercises

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › Exercises · pp. 411–414 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
17.8 • SUMMARY guages need to label words with case and gender information. Tagsets for morphologically rich languages are therefore sequences of morphological tags rather than a single primitive tag. Here’s a Turkish example, in which the word izin has three possible morphological/part-of-speech tags and meanings (Hakkani-T¨ur et al., 2002): 1. Yerdeki izin temizlenmesi gerek. iz + Noun+A3sg+Pnon+Gen The trace on the floor should be cleaned. 2. ¨Uzerinde parmak izin kalmis¸. iz + Noun+A3sg+P2sg+Nom Your finger print is left on (it). 3. Ic¸eri girmek ic¸in izin alman gerekiyor. izin + Noun+A3sg+Pnon+Nom You need permission to enter. Using a morphological parse sequence like Noun+A3sg+Pnon+Gen as the partof-speech tag greatly increases the number of parts of speech, and so tagsets can be 4 to 10 times larger than the 50-100 tags we have seen for English. With such large tagsets, each word needs to be morphologically analyzed to generate the list of possible morphological tag sequences (part-of-speech tags) for the word. The role of the tagger is then to disambiguate among these tags. This method also helps with unknown words since morphological parsers can accept unknown stems and still segment the affixes properly.

## Key terms
- **word** — 33 mentions
- **tagger** — 20 mentions
- **sequence** — 15 mentions
- **algorithm** — 14 mentions
- **tags** — 12 mentions
- **tagging** — 11 mentions
- **part-of-speech** — 10 mentions
- **part** — 10 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=411|Speech and Language Processing.pdf p. 411]]

## Liens
- Up: [[research/slp/sequence-labeling-for-parts-of-speech-and-named-entities]]
- ← Prev: [[research/slp/historical-notes-16]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
