---
title: "Earlier Finite-State Template-Filling Systems"
summary: "§II Annotating Linguistic Structure › Information Extraction:: 20.8 • TEMPLATE FILLING set of features can be used: tokens, embeddings, word shapes, part-of-speech tags, syntactic chunk tags, and named entity tags."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "485-485"
---

# Earlier Finite-State Template-Filling Systems

§II Annotating Linguistic Structure › Information Extraction: Relations, Events, and Time › Template Filling › Earlier Finite-State Template-Filling Systems · pp. 485–485 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
20.8 • TEMPLATE FILLING set of features can be used: tokens, embeddings, word shapes, part-of-speech tags, syntactic chunk tags, and named entity tags. The second system has the job of role-filler extraction. A separate classifier is role-filler extraction trained to detect each role (LEAD-AIRLINE, AMOUNT, and so on). This can be a binary classifier that is run on every noun-phrase in the parsed input sentence, or a sequence model run over sequences of words. Each role classifier is trained on the labeled data in the training set. Again, the usual set of features can be used, but now trained only on an individual noun phrase or the fillers of a single slot. Multiple non-identical text segments might be labeled with the same slot label. For example in our sample text, the strings United or United Airlines might be labeled as the LEAD AIRLINE. These are not incompatible choices and the coreference resolution techniques introduced in Chapter 23 can provide a path to a solution. A variety of annotated collections have been used to evaluate this style of approach to template filling, including sets of job announcements, conference calls for papers, restaurant guides, and biological texts.

## Key terms
- **template** — 13 mentions
- **slot** — 5 mentions
- **text** — 5 mentions
- **bridgestone** — 5 mentions
- **sports** — 5 mentions
- **joint** — 5 mentions
- **venture** — 5 mentions
- **taiwan** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=485|Speech and Language Processing.pdf p. 485]]

## Liens
- Up: [[research/slp/template-filling]]
- ← Prev: [[research/slp/machine-learning-approaches-to-template-filling]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
