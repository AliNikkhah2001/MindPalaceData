---
title: "Features for CRF Named Entity Recognizers"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: 17.5 • CONDITIONAL RANDOM FIELDS (CRFS) prefix(xi) = w prefix(xi) = we suffix(xi) = ed suffix(xi) = d word-shape(xi) = xxxx-xxxxxxx short-word-shape(xi) = x-x The known-word templates are computed for every word seen "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "407-407"
---

# Features for CRF Named Entity Recognizers

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › Conditional Random Fields (CRFs) › Features for CRF Named Entity Recognizers · pp. 407–407 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
17.5 • CONDITIONAL RANDOM FIELDS (CRFS) prefix(xi) = w prefix(xi) = we suffix(xi) = ed suffix(xi) = d word-shape(xi) = xxxx-xxxxxxx short-word-shape(xi) = x-x The known-word templates are computed for every word seen in the training set; the unknown word features can also be computed for all words in training, or only on training words whose frequency is below some threshold. The result of the known-word templates and word-signature features is a very large set of features. Generally a feature cutoff is used in which features are thrown out if they have count < 5 in the training set. Remember that in a CRF we don’t learn weights for each of these local features fk. Instead, we first sum the values of each local feature (for example feature f3743) over the entire sentence, to create each global feature (for example F3743). It is those global features that will then be multiplied by weight w3743. Thus for training and inference there is always a fixed set of K features with K weights, even though the length of each sentence is different. A CRF for NER makes use of very similar features to a POS tagger, as shown in Figure 17.15. identity of wi, identity of neighboring words embeddings…

## Key terms
- **feature** — 17 mentions
- **word** — 13 mentions
- **gazetteer** — 6 mentions
- **training** — 5 mentions
- **neighboring** — 5 mentions
- **shape** — 4 mentions
- **prefix** — 3 mentions
- **suffix** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=407|Speech and Language Processing.pdf p. 407]]

## Liens
- Up: [[research/slp/conditional-random-fields-crfs]]
- ← Prev: [[research/slp/features-in-a-crf-pos-tagger]]
- Next: [[research/slp/inference-and-training-for-crfs]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
