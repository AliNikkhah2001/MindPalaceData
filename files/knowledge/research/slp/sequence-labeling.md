---
title: "Sequence Labeling"
summary: "§I Large Language Models › Masked Language Models › Fine-Tuni: 9.5 • FINE-TUNING FOR SEQUENCE LABELING: NAMED ENTITY RECOGNITION Words IO Label BIO Label BIOES Label Jane I-PER B-PER B-PER Villanueva I-PER I-PER E-PER of O O O United I-ORG B-ORG B-ORG Airlines I-ORG I-ORG I-ORG H"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "223-223"
---

# Sequence Labeling

§I Large Language Models › Masked Language Models › Fine-Tuning for Sequence Labeling: Named Entity Recognition › Sequence Labeling · pp. 223–223 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
9.5 • FINE-TUNING FOR SEQUENCE LABELING: NAMED ENTITY RECOGNITION Words IO Label BIO Label BIOES Label Jane I-PER B-PER B-PER Villanueva I-PER I-PER E-PER of O O O United I-ORG B-ORG B-ORG Airlines I-ORG I-ORG I-ORG Holding I-ORG I-ORG E-ORG discussed O O O the O O O Chicago I-LOC B-LOC S-LOC route O O O . O O O Figure 9.12 NER as a sequence model, showing IO, BIO, and BIOES taggings. In sequence labeling, we pass the final output vector corresponding to each input token to a classifier that produces a softmax distribution over the possible set of tags. For a single feedforward layer classifier, the set of weights to be learned is WK of size [d × k], where k is the number of possible tags for the task. A greedy approach, where the argmax tag for each token is taken as a likely answer, can be used to generate the final output tag sequence. Fig. 9.13 illustrates an example of this approach, where yi is a vector of probabilities over tags, and k indexes the tags. yi = softmax(hL i WK) (9.12) ti = argmaxk(yi) (9.13) Alternatively, the distribution over labels provided by the softmax for each input token can be passed to a conditional random field (CRF) layer which can take global tag-level transitions into account (see Chapter 17 on CRFs).

## Key terms
- **i-org** — 8 mentions
- **sequence** — 5 mentions
- **label** — 4 mentions
- **i-per** — 4 mentions
- **token** — 4 mentions
- **tags** — 4 mentions
- **labeling** — 3 mentions
- **b-per** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=223|Speech and Language Processing.pdf p. 223]]

## Liens
- Up: [[research/slp/fine-tuning-for-sequence-labeling-named-entity-recognition]]
- ← Prev: [[research/slp/bio-tagging]]
- Next: [[research/slp/evaluating-named-entity-recognition]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
