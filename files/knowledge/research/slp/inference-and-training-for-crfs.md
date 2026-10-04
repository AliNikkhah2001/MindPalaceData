---
title: "Inference and Training for CRFs"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES prefix(xi) = L suffix(xi) = tane prefix(xi) = L’ suffix(xi) = ane prefix(xi) = L’O suffix(xi) = ne prefix(xi) = L’Oc suffix(xi) = e word-shape(xi) "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "408-408"
---

# Inference and Training for CRFs

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › Conditional Random Fields (CRFs) › Inference and Training for CRFs · pp. 408–408 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES prefix(xi) = L suffix(xi) = tane prefix(xi) = L’ suffix(xi) = ane prefix(xi) = L’O suffix(xi) = ne prefix(xi) = L’Oc suffix(xi) = e word-shape(xi) = X’Xxxxxxxx short-word-shape(xi) = X’Xx Figure 17.16 illustrates the result of adding part-of-speech tags and some shape information to our earlier example. Words POS Short shape Gazetteer BIO Label Jane NNP Xx B-PER Villanueva NNP Xx I-PER of IN x O United NNP Xx B-ORG Airlines NNP Xx I-ORG Holding NNP Xx I-ORG discussed VBD x O the DT x O Chicago NNP Xx B-LOC route NN x O . . . O Figure 17.16 Some NER features for a sample sentence, assuming that Chicago and Villanueva are listed as locations in a gazetteer. We assume features only take on the values 0 or 1, so the first POS feature, for example, would be represented as 1{POS = NNP}. How do we find the best tag sequence ˆY for a given input X? We start with Eq. 17.22: ˆY = argmax Y∈Y P(Y|X) = argmax Y∈Y Z(X)exp K X k=1 wkFk(X,Y) ! (17.27) = argmax Y∈Y exp K X k=1 wk n X i=1 fk(yi−1,yi,X,i) ! (17.28) = argmax Y∈Y K X k=1 wk n X i=1 fk(yi−1,yi,X,i) (17.29) = argmax Y∈Y n X i=1 K X k=1 wk fk(yi−1,yi,X,i) (17.30) We can ignore the exp function and the denominator Z(X), as we do above, because exp doesn’t change the argmax, and the denominator Z(X) is constant for a given observation sequence X.

## Key terms
- **argmax** — 6 mentions
- **sequence** — 4 mentions
- **prefix** — 4 mentions
- **suffix** — 4 mentions
- **feature** — 3 mentions
- **value** — 3 mentions
- **shape** — 2 mentions
- **gazetteer** — 2 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=408|Speech and Language Processing.pdf p. 408]]

## Liens
- Up: [[research/slp/conditional-random-fields-crfs]]
- ← Prev: [[research/slp/features-for-crf-named-entity-recognizers]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
