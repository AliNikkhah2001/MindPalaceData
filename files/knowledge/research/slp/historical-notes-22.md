---
title: "Historical Notes"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : 23.11 • SUMMARY (23.78) The secretary called the physiciani and told himi about a new patient [pro-stereotypical] (23.79) The secretary called the physiciani and told heri about a new patient [anti-stereotypical] Zhao"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "555-557"
---

# Historical Notes

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › Historical Notes · pp. 555–557 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
23.11 • SUMMARY (23.78) The secretary called the physiciani and told himi about a new patient [pro-stereotypical] (23.79) The secretary called the physiciani and told heri about a new patient [anti-stereotypical] Zhao et al. (2018a) consider a coreference system to be biased if it is more accurate at linking pronouns consistent with gender stereotypical occupations (e.g., him with physician in (23.78)) than linking pronouns inconsistent with gender-stereotypical occupations (e.g., her with physician in (23.79)). They show that coreference systems of all architectures (rule-based, feature-based machine learned, and end-toend-neural) all show significant bias, performing on average 21 F1 points worse in the anti-stereotypical cases. One possible source of this bias is that female entities are significantly underrepresented in the OntoNotes dataset, used to train most coreference systems. Zhao et al. (2018a) propose a way to overcome this bias: they generate a second gender-swapped dataset in which all male entities in OntoNotes are replaced with female ones and vice versa, and retrain coreference systems on the combined original and swapped OntoNotes data, also using debiased GloVE embeddings (Bolukbasi et al., 2016).

## Key terms
- **coreference** — 32 mentions
- **pronoun** — 16 mentions
- **system** — 15 mentions
- **model** — 10 mentions
- **algorithm** — 9 mentions
- **sentence** — 9 mentions
- **mention** — 8 mentions
- **bias** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=555|Speech and Language Processing.pdf p. 555]]

## Liens
- Up: [[research/slp/coreference-resolution-and-entity-linking]]
- ← Prev: [[research/slp/summary-22]]
- Next: [[research/slp/exercises-16]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
