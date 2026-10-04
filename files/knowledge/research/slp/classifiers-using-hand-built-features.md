---
title: "Classifiers using hand-built features"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : 23.5 • CLASSIFIERS USING HAND-BUILT FEATURES Fig. 23.3 shows an example of the computation for the single candidate anaphor she."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "543-544"
---

# Classifiers using hand-built features

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › Classifiers using hand-built features · pp. 543–544 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
23.5 • CLASSIFIERS USING HAND-BUILT FEATURES Fig. 23.3 shows an example of the computation for the single candidate anaphor she. Once the antecedent is classified for each anaphor, transitive closure can be run over the pairwise decisions to get a complete clustering. Training is trickier in the mention-ranking model than the mention-pair model, because for each anaphor we don’t know which of all the possible gold antecedents to use for training. Instead, the best antecedent for each mention is latent; that is, for each mention we have a whole cluster of legal gold antecedents to choose from. Early work used heuristics to choose an antecedent, for example choosing the closest antecedent as the gold antecedent and all non-antecedents in a window of two sentences as the negative examples (Denis and Baldridge, 2008). Various kinds of ways to model latent antecedents exist (Fernandes et al. 2012, Chang et al. 2013, Durrett and Klein 2013). The simplest way is to give credit to any legal antecedent by summing over all of them, with a loss function that optimizes the likelihood of all correct antecedents from the gold clustering (Lee et al., 2017b). We’ll see the details in Section 23.6. Mention-ranking models can be implemented with hand-build features or with neural representation learning (which might also incorporate some hand-built features).

## Key terms
- **antecedent** — 33 mentions
- **mention** — 26 mentions
- **feature** — 23 mentions
- **cluster** — 22 mentions
- **anaphor** — 21 mentions
- **model** — 14 mentions
- **entity** — 12 mentions
- **word** — 11 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=543|Speech and Language Processing.pdf p. 543]]

## Liens
- Up: [[research/slp/coreference-resolution-and-entity-linking]]
- ← Prev: [[research/slp/architectures-for-coreference-algorithms]]
- Next: [[research/slp/a-neural-mention-ranking-algorithm]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
