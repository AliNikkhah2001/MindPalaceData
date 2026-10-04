---
title: "Semisupervised Relation Extraction via Bootstrapping"
summary: "§II Annotating Linguistic Structure › Information Extraction:: 20.2 • RELATION EXTRACTION ALGORITHMS ENCODER [CLS] [SUBJ_PERSON] was born in [OBJ_LOC] , Michigan Linear Classifier p(relation|SUBJ,OBJ) Figure 20.6 Relation extraction as a linear layer on top of an encoder (in this"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "469-469"
---

# Semisupervised Relation Extraction via Bootstrapping

§II Annotating Linguistic Structure › Information Extraction: Relations, Events, and Time › Relation Extraction Algorithms › Semisupervised Relation Extraction via Bootstrapping · pp. 469–469 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
20.2 • RELATION EXTRACTION ALGORITHMS ENCODER [CLS] [SUBJ_PERSON] was born in [OBJ_LOC] , Michigan Linear Classifier p(relation|SUBJ,OBJ) Figure 20.6 Relation extraction as a linear layer on top of an encoder (in this case BERT), with the subject and object entities replaced in the input by their NER tags (Zhang et al. 2017, Joshi et al. 2020). curacies. But labeling a large training set is extremely expensive and supervised models are brittle: they don’t generalize well to different text genres. For this reason, much research in relation extraction has focused on the semi-supervised and unsupervised approaches we turn to next. Supervised machine learning assumes that we have lots of labeled data. Unfortunately, this is expensive. But suppose we just have a few high-precision seed patterns, like those in Section 20.2.1, or perhaps a few seed tuples. That’s enough seed patterns seed tuples to bootstrap a classifier! Bootstrapping proceeds by taking the entities in the seed bootstrapping pair, and then finding sentences (on the web, or whatever dataset we are using) that contain both entities. From all such sentences, we extract and generalize the context around the entities to learn new patterns.

## Key terms
- **tuples** — 10 mentions
- **relation** — 9 mentions
- **seed** — 8 mentions
- **entities** — 6 mentions
- **patterns** — 6 mentions
- **sentences** — 6 mentions
- **ryanair** — 5 mentions
- **charleroi** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=469|Speech and Language Processing.pdf p. 469]]

## Liens
- Up: [[research/slp/relation-extraction-algorithms]]
- ← Prev: [[research/slp/relation-extraction-via-supervised-learning]]
- Next: [[research/slp/distant-supervision-for-relation-extraction]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
