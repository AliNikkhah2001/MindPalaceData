---
title: "Coreference Tasks and Datasets"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : 23.2 • COREFERENCE TASKS AND DATASETS Verb Semantics: Some verbs semantically emphasize one of their arguments, biasing the interpretation of subsequent pronouns."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "537-537"
---

# Coreference Tasks and Datasets

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › Coreference Tasks and Datasets · pp. 537–537 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
23.2 • COREFERENCE TASKS AND DATASETS Verb Semantics: Some verbs semantically emphasize one of their arguments, biasing the interpretation of subsequent pronouns. Compare (23.40) and (23.41). (23.40) John telephoned Bill. He lost the laptop. (23.41) John criticized Bill. He lost the laptop. These examples differ only in the verb used in the first sentence, yet “he” in (23.40) is typically resolved to John, whereas “he” in (23.41) is resolved to Bill. This may be partly due to the link between implicit causality and saliency: the implicit cause of a “criticizing” event is its object, whereas the implicit cause of a “telephoning” event is its subject. In such verbs, the entity which is the implicit cause may be more salient. Selectional Restrictions: Many other kinds of semantic knowledge can play a role in referent preference. For example, the selectional restrictions that a verb places on its arguments (Chapter 21) can help eliminate referents, as in (23.42). (23.42) I ate the soup in my new bowl after cooking it for hours There are two possible referents for it, the soup and the bowl. The verb eat, however, requires that its direct object denote something edible, and this constraint can rule out bowl as a possible referent.

## Key terms
- **coreference** — 7 mentions
- **megabucks** — 7 mentions
- **verb** — 6 mentions
- **link** — 4 mentions
- **implicit** — 4 mentions
- **referent** — 4 mentions
- **task** — 4 mentions
- **victoria** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=537|Speech and Language Processing.pdf p. 537]]

## Liens
- Up: [[research/slp/coreference-resolution-and-entity-linking]]
- ← Prev: [[research/slp/coreference-phenomena-linguistic-background]]
- Next: [[research/slp/mention-detection]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
