---
title: "Summary"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : 23.11 • SUMMARY (23.78) The secretary called the physiciani and told himi about a new patient [pro-stereotypical] (23.79) The secretary called the physiciani and told heri about a new patient [anti-stereotypical] Zhao"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "555-555"
---

# Summary

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › Summary · pp. 555–555 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
23.11 • SUMMARY (23.78) The secretary called the physiciani and told himi about a new patient [pro-stereotypical] (23.79) The secretary called the physiciani and told heri about a new patient [anti-stereotypical] Zhao et al. (2018a) consider a coreference system to be biased if it is more accurate at linking pronouns consistent with gender stereotypical occupations (e.g., him with physician in (23.78)) than linking pronouns inconsistent with gender-stereotypical occupations (e.g., her with physician in (23.79)). They show that coreference systems of all architectures (rule-based, feature-based machine learned, and end-toend-neural) all show significant bias, performing on average 21 F1 points worse in the anti-stereotypical cases. One possible source of this bias is that female entities are significantly underrepresented in the OntoNotes dataset, used to train most coreference systems. Zhao et al. (2018a) propose a way to overcome this bias: they generate a second gender-swapped dataset in which all male entities in OntoNotes are replaced with female ones and vice versa, and retrain coreference systems on the combined original and swapped OntoNotes data, also using debiased GloVE embeddings (Bolukbasi et al., 2016).

## Key terms
- **coreference** — 11 mentions
- **pronoun** — 11 mentions
- **system** — 8 mentions
- **bias** — 6 mentions
- **ontonotes** — 5 mentions
- **show** — 4 mentions
- **entities** — 4 mentions
- **dataset** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=555|Speech and Language Processing.pdf p. 555]]

## Liens
- Up: [[research/slp/coreference-resolution-and-entity-linking]]
- ← Prev: [[research/slp/gender-bias-in-coreference]]
- Next: [[research/slp/historical-notes-22]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
