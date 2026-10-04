---
title: "Unsupervised Relation Extraction"
summary: "§II Annotating Linguistic Structure › Information Extraction:: CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME relations, the classifier will also need to be able to label an example as no-relation."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "472-473"
---

# Unsupervised Relation Extraction

§II Annotating Linguistic Structure › Information Extraction: Relations, Events, and Time › Relation Extraction Algorithms › Unsupervised Relation Extraction · pp. 472–473 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME relations, the classifier will also need to be able to label an example as no-relation. This label is trained by randomly selecting entity pairs that do not appear in any Freebase relation, extracting features for them, and building a feature vector for each such tuple. The final algorithm is sketched in Fig. 20.8. function DISTANT SUPERVISION(Database D, Text T) returns relation classifier C foreach relation R foreach tuple (e1,e2) of entities with relation R in D sentences←Sentences in T that contain e1 and e2 f←Frequent features in sentences observations←observations + new training tuple (e1, e2, f, R) C←Train supervised classifier on observations return C Figure 20.8 The distant supervision algorithm for relation extraction. A neural classifier would skip the feature set f. Distant supervision shares advantages with each of the methods we’ve examined. Like supervised classification, distant supervision uses a classifier with lots of features, and supervised by detailed hand-created knowledge. Like pattern-based classifiers, it can make use of high-precision evidence for the relation between entities. Indeed, distance supervision systems learn patterns just like the hand-built patterns of early relation extractors.

## Key terms
- **relation** — 32 mentions
- **classifier** — 12 mentions
- **feature** — 10 mentions
- **extraction** — 9 mentions
- **supervision** — 9 mentions
- **distant** — 8 mentions
- **system** — 7 mentions
- **sentence** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=472|Speech and Language Processing.pdf p. 472]]

## Liens
- Up: [[research/slp/relation-extraction-algorithms]]
- ← Prev: [[research/slp/distant-supervision-for-relation-extraction]]
- Next: [[research/slp/evaluation-of-relation-extraction]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
