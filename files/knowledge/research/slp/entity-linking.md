---
title: "Entity Linking"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : CHAPTER 23 • COREFERENCE RESOLUTION AND ENTITY LINKING therefore want to maximize: X ˆy∈Y(i)∩GOLD(i) P(ˆy) (23.56) If a mention i is not in a gold cluster GOLD(i) = ϵ."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "548-551"
---

# Entity Linking

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › Entity Linking · pp. 548–551 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 23 • COREFERENCE RESOLUTION AND ENTITY LINKING therefore want to maximize: X ˆy∈Y(i)∩GOLD(i) P(ˆy) (23.56) If a mention i is not in a gold cluster GOLD(i) = ϵ. To turn this probability into a loss function, we’ll use the cross-entropy loss function we defined in Eq. 4.19 in Chapter 4, by taking the −log of the probability. If we then sum over all mentions, we get the final loss function for training: L = N X i=2 −log X ˆy∈Y(i)∩GOLD(i) P(ˆy) (23.57) Entity linking is the task of associating a mention in text with the representation of entity linking some real-world entity in an ontology or knowledge base (Ji and Grishman, 2011). It is the natural follow-on to coreference resolution; coreference resolution is the task of associating textual mentions that corefer to the same entity. Entity linking takes the further step of identifying who that entity is. It is especially important for any NLP task that links to a knowledge base. While there are all sorts of potential knowledge-bases, we’ll focus in this section on Wikipedia, since it’s widely used as an ontology for NLP tasks. In this usage, each unique Wikipedia page acts as the unique id for a particular entity. This task of deciding which Wikipedia page corresponding to an individual is being referred to by a text mention has its own name: wikification (Mihalcea and Csomai, 2007).

## Key terms
- **entity** — 41 mentions
- **wikipedia** — 28 mentions
- **mention** — 24 mentions
- **anchor** — 24 mentions
- **span** — 20 mentions
- **entities** — 17 mentions
- **linking** — 16 mentions
- **algorithm** — 14 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=548|Speech and Language Processing.pdf p. 548]]

## Liens
- Up: [[research/slp/coreference-resolution-and-entity-linking]]
- ← Prev: [[research/slp/a-neural-mention-ranking-algorithm]]
- Next: [[research/slp/evaluation-of-coreference-resolution]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
