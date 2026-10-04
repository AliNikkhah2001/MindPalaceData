---
title: "Features in a CRF POS Tagger"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES Let’s look at some of these features in detail, since the reason to use a discriminative sequence model is that it’s easier to incorporate a lot of"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "406-406"
---

# Features in a CRF POS Tagger

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › Conditional Random Fields (CRFs) › Features in a CRF POS Tagger · pp. 406–406 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES Let’s look at some of these features in detail, since the reason to use a discriminative sequence model is that it’s easier to incorporate a lot of features.2 Again, in a linear-chain CRF, each local feature fk at position i can depend on any information from: (yi−1,yi,X,i). So some legal features representing common situations might be the following: 1{xi = the, yi = DET} 1{yi = PROPN, xi+1 = Street, yi−1 = NUM} 1{yi = VERB, yi−1 = AUX} For simplicity, we’ll assume all CRF features take on the value 1 or 0. Above, we explicitly use the notation 1{x} to mean “1 if x is true, and 0 otherwise”. From now on, we’ll leave off the 1 when we define features, but you can assume each feature has it there implicitly. Although the idea of what features to use is done by the system designer by hand, the specific features are automatically populated by using feature templates as we feature templates briefly mentioned in Chapter 4. Here are some templates that only use information from (yi−1,yi,X,i): ⟨yi,xi⟩,⟨yi,yi−1⟩,⟨yi,xi−1,xi+2⟩ These templates automatically populate the set of features from every instance in the training and test set.

## Key terms
- **feature** — 23 mentions
- **word** — 13 mentions
- **templates** — 5 mentions
- **shape** — 5 mentions
- **these** — 4 mentions
- **following** — 3 mentions
- **value** — 3 mentions
- **back** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=406|Speech and Language Processing.pdf p. 406]]

## Liens
- Up: [[research/slp/conditional-random-fields-crfs]]
- Next: [[research/slp/features-for-crf-named-entity-recognizers]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
