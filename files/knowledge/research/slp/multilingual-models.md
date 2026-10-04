---
title: "Multilingual models"
summary: "§I Large Language Models › Machine Translation › Translating : CHAPTER 12 • MACHINE TRANSLATION Data augmentation is a statistical technique for dealing with insufficient training data, by adding new synthetic data that is generated from the current natural data."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "282-282"
---

# Multilingual models

§I Large Language Models › Machine Translation › Translating in low-resource situations › Multilingual models · pp. 282–282 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 12 • MACHINE TRANSLATION Data augmentation is a statistical technique for dealing with insufficient training data, by adding new synthetic data that is generated from the current natural data. The most common data augmentation technique for machine translation is called backtranslation. Backtranslation relies on the intuition that while parallel corpora backtranslation may be limited for particular languages or domains, we can often find a large (or at least larger) monolingual corpus, to add to the smaller parallel corpora that are available. The algorithm makes use of monolingual corpora in the target language by creating synthetic bitexts. In backtranslation, our goal is to improve source-to-target MT, given a small parallel text (a bitext) in the source/target languages, and some monolingual data in the target language. We first use the bitext to train a MT system in the reverse direction: a target-to-source MT system. We then use it to translate the monolingual target data to the source language. Now we can add this synthetic bitext (natural target sentences, aligned with MT-produced source sentences) to our training data, and retrain our source-to-target MT model. For example suppose we want to translate from Navajo to English but only have a small Navajo-English bitext, although of course we can find lots of monolingual English data.

## Key terms
- **data** — 15 mentions
- **language** — 15 mentions
- **bitext** — 10 mentions
- **target** — 7 mentions
- **backtranslation** — 6 mentions
- **monolingual** — 6 mentions
- **system** — 6 mentions
- **training** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=282|Speech and Language Processing.pdf p. 282]]

## Liens
- Up: [[research/slp/translating-in-low-resource-situations]]
- ← Prev: [[research/slp/data-augmentation]]
- Next: [[research/slp/sociotechnical-issues]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
