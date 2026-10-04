---
title: "Translating in low-resource situations"
summary: "§I Large Language Models › Machine Translation › Translating : 12.5 • TRANSLATING IN LOW-RESOURCE SITUATIONS The intuition of minimum Bayes risk is that instead of trying to choose the translation which is most probable, we choose the one that is likely to have the least error."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "281-282"
---

# Translating in low-resource situations

§I Large Language Models › Machine Translation › Translating in low-resource situations · pp. 281–282 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
12.5 • TRANSLATING IN LOW-RESOURCE SITUATIONS The intuition of minimum Bayes risk is that instead of trying to choose the translation which is most probable, we choose the one that is likely to have the least error. For example, we might want our decoding algorithm to find the translation which has the highest score on some evaluation metric. For example in Section 12.6 we will introduce metrics like chrF or BERTScore that measure the goodness-of-fit between a candidate translation and a set of reference human translations. A translation that maximizes this score, especially with a hypothetically huge set of perfect human translations is likely to be a good one (have minimum risk) even if it is not the most probable translation by our particular probability estimator. In practice, we don’t know the perfect set of translations for a given sentence. So the standard simplification used in MBR decoding algorithms is to instead choose the candidate translation which is most similar (by some measure of goodness-offit) with some set of candidate translations. We’re essentially approximating the enormous space of all possible translations U with a smaller set of possible candidate translations Y.

## Key terms
- **translation** — 24 mentions
- **language** — 20 mentions
- **data** — 17 mentions
- **bitext** — 11 mentions
- **candidate** — 8 mentions
- **english** — 7 mentions
- **backtranslation** — 7 mentions
- **target** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=281|Speech and Language Processing.pdf p. 281]]

## Liens
- Up: [[research/slp/machine-translation]]
- ← Prev: [[research/slp/decoding-in-mt-beam-search]]
- Next: [[research/slp/mt-evaluation]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
