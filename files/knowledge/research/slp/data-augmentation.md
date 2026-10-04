---
title: "Data Augmentation"
summary: "§I Large Language Models › Machine Translation › Translating : 12.5 • TRANSLATING IN LOW-RESOURCE SITUATIONS The intuition of minimum Bayes risk is that instead of trying to choose the translation which is most probable, we choose the one that is likely to have the least error."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "281-281"
---

# Data Augmentation

§I Large Language Models › Machine Translation › Translating in low-resource situations › Data Augmentation · pp. 281–281 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
12.5 • TRANSLATING IN LOW-RESOURCE SITUATIONS The intuition of minimum Bayes risk is that instead of trying to choose the translation which is most probable, we choose the one that is likely to have the least error. For example, we might want our decoding algorithm to find the translation which has the highest score on some evaluation metric. For example in Section 12.6 we will introduce metrics like chrF or BERTScore that measure the goodness-of-fit between a candidate translation and a set of reference human translations. A translation that maximizes this score, especially with a hypothetically huge set of perfect human translations is likely to be a good one (have minimum risk) even if it is not the most probable translation by our particular probability estimator. In practice, we don’t know the perfect set of translations for a given sentence. So the standard simplification used in MBR decoding algorithms is to instead choose the candidate translation which is most similar (by some measure of goodness-offit) with some set of candidate translations. We’re essentially approximating the enormous space of all possible translations U with a smaller set of possible candidate translations Y.

## Key terms
- **translation** — 20 mentions
- **candidate** — 8 mentions
- **languages** — 5 mentions
- **choose** — 4 mentions
- **resource** — 4 mentions
- **minimum** — 3 mentions
- **risk** — 3 mentions
- **decoding** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=281|Speech and Language Processing.pdf p. 281]]

## Liens
- Up: [[research/slp/translating-in-low-resource-situations]]
- Next: [[research/slp/multilingual-models]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
