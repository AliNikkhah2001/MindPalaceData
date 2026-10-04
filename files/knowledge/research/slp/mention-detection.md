---
title: "Mention Detection"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : CHAPTER 23 • COREFERENCE RESOLUTION AND ENTITY LINKING Exactly what counts as a mention and what links are annotated differs from task to task and dataset to dataset."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "538-540"
---

# Mention Detection

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › Mention Detection · pp. 538–540 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 23 • COREFERENCE RESOLUTION AND ENTITY LINKING Exactly what counts as a mention and what links are annotated differs from task to task and dataset to dataset. For example some coreference datasets do not label singletons, making the task much simpler. Resolvers can achieve much higher scores on corpora without singletons, since singletons constitute the majority of mentions in running text, and they are often hard to distinguish from non-referential NPs. Some tasks use gold mention-detection (i.e. the system is given human-labeled mention boundaries and the task is just to cluster these gold mentions), which eliminates the need to detect and segment mentions from running text. Coreference is usually evaluated by the CoNLL F1 score, which combines three metrics: MUC, B3, and CEAFe; Section 23.8 gives the details. Let’s mention a few characteristics of one popular coreference dataset, OntoNotes (Pradhan et al. 2007c, Pradhan et al. 2007a), and the CoNLL 2012 Shared Task based on it (Pradhan et al., 2012a). OntoNotes contains hand-annotated Chinese and English coreference datasets of roughly one million words each, consisting of newswire, magazine articles, broadcast news, broadcast conversations, web data and conversational speech data, as well as about 300,000 words of annotated Arabic newswire.

## Key terms
- **mention** — 44 mentions
- **coreference** — 17 mentions
- **detection** — 15 mentions
- **system** — 14 mentions
- **anaphoricity** — 11 mentions
- **task** — 10 mentions
- **dataset** — 9 mentions
- **singleton** — 9 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=538|Speech and Language Processing.pdf p. 538]]

## Liens
- Up: [[research/slp/coreference-resolution-and-entity-linking]]
- ← Prev: [[research/slp/coreference-tasks-and-datasets]]
- Next: [[research/slp/architectures-for-coreference-algorithms]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
