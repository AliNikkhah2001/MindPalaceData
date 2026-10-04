---
title: "Automatic Evaluation: Embedding-Based Methods"
summary: "§I Large Language Models › Machine Translation › MT Evaluatio: CHAPTER 12 • MACHINE TRANSLATION in the candidate translation that also occur in the reference translation, and ditto for bigrams and so on, up to 4-grams."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "286-286"
---

# Automatic Evaluation: Embedding-Based Methods

§I Large Language Models › Machine Translation › MT Evaluation › Automatic Evaluation: Embedding-Based Methods · pp. 286–286 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 12 • MACHINE TRANSLATION in the candidate translation that also occur in the reference translation, and ditto for bigrams and so on, up to 4-grams. BLEU extends this unigram metric to the whole corpus by computing the numerator as the sum over all sentences of the counts of all the unigram types that also occur in the reference translation, and the denominator is the total of the counts of all unigrams in all candidate sentences. We compute this n-gram precision for unigrams, bigrams, trigrams, and 4-grams and take the geometric mean. BLEU has many further complications, including a brevity penalty for penalizing candidate translations that are too short, and it also requires the ngram counts be clipped in a particular way. Because BLEU is a word-based metric, it is very sensitive to word tokenization, making it impossible to compare different systems if they rely on different tokenization standards, and doesn’t work as well in languages with complex morphology. Nonetheless, you will sometimes still see systems evaluated by BLEU, particularly for translation into English. In such cases it’s important to use packages that enforce standardization for tokenization like SACREBLEU (Post, 2018).

## Key terms
- **chrf** — 15 mentions
- **translation** — 11 mentions
- **system** — 9 mentions
- **score** — 9 mentions
- **metric** — 8 mentions
- **bleu** — 6 mentions
- **candidate** — 5 mentions
- **test** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=286|Speech and Language Processing.pdf p. 286]]

## Liens
- Up: [[research/slp/mt-evaluation]]
- ← Prev: [[research/slp/automatic-evaluation]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
