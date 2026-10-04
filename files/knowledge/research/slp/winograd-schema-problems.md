---
title: "Winograd Schema problems"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : 23.9 • WINOGRAD SCHEMA PROBLEMS The weight wi for each entity can be set to different values to produce different versions of the algorithm."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "553-553"
---

# Winograd Schema problems

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › Winograd Schema problems · pp. 553–553 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
23.9 • WINOGRAD SCHEMA PROBLEMS The weight wi for each entity can be set to different values to produce different versions of the algorithm. Following a proposal from Denis and Baldridge (2009), the CoNLL coreference competitions were scored based on the average of MUC, CEAF-e, and B3 (Pradhan et al. 2011, Pradhan et al. 2012b), and so it is common in many evaluation campaigns to report an average of these 3 metrics. See Luo and Pradhan (2016) for a detailed description of the entire set of metrics; reference implementations of these should be used rather than attempting to reimplement from scratch (Pradhan et al., 2014). Alternative metrics have been proposed that deal with particular coreference domains or tasks. For example, consider the task of resolving mentions to named entities (persons, organizations, geopolitical entities), which might be useful for information extraction or knowledge base completion. A hypothesis chain that correctly contains all the pronouns referring to an entity, but has no version of the name itself, or is linked with a wrong name, is not useful for this task. We might instead want a metric that weights each mention by how informative it is (with names being most informative) (Chen and Ng, 2013) or a metric that considers a hypothesis to match a gold chain only if it contains at least one variant of a name (the NEC F1 metric of Agarwal et al.

## Key terms
- **metric** — 6 mentions
- **problem** — 6 mentions
- **winograd** — 5 mentions
- **coreference** — 5 mentions
- **task** — 5 mentions
- **pradhan** — 4 mentions
- **name** — 4 mentions
- **demonstrators** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=553|Speech and Language Processing.pdf p. 553]]

## Liens
- Up: [[research/slp/coreference-resolution-and-entity-linking]]
- ← Prev: [[research/slp/evaluation-of-coreference-resolution]]
- Next: [[research/slp/gender-bias-in-coreference]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
