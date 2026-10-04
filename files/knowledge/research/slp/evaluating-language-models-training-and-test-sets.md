---
title: "Evaluating Language Models: Training and Test Sets"
summary: "§I Large Language Models › N-gram Language Models › Evaluatin: CHAPTER 3 • N-GRAM LANGUAGE MODELS Longer context Although for pedagogical purposes we have only described bigram models, when there is sufficient training data we use trigram models, which trigram condition on the pr"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "52-53"
---

# Evaluating Language Models: Training and Test Sets

§I Large Language Models › N-gram Language Models › Evaluating Language Models: Training and Test Sets · pp. 52–53 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 3 • N-GRAM LANGUAGE MODELS Longer context Although for pedagogical purposes we have only described bigram models, when there is sufficient training data we use trigram models, which trigram condition on the previous two words, or 4-gram or 5-gram models. For these larger 4-gram 5-gram n-grams, we’ll need to assume extra contexts to the left and right of the sentence end. For example, to compute trigram probabilities at the very beginning of the sentence, we use two pseudo-words for the first trigram (i.e., P(I|<s><s>). Some large n-gram datasets have been created, like the million most frequent n-grams drawn from the Corpus of Contemporary American English (COCA), a curated 1 billion word corpus of American English (Davies, 2020), Google’s Web 5-gram corpus from 1 trillion words of English web text (Franz and Brants, 2006), or the Google Books Ngrams corpora (800 billion tokens from Chinese, English, French, German, Hebrew, Italian, Russian, and Spanish) (Lin et al., 2012a)). It’s even possible to use extremely long-range n-gram context. The infini-gram (∞-gram) project (Liu et al., 2024) allows n-grams of any length. Their idea is to avoid the expensive (in space and time) pre-computation of huge n-gram count tables.

## Key terms
- **model** — 42 mentions
- **test** — 40 mentions
- **language** — 21 mentions
- **n-gram** — 20 mentions
- **training** — 17 mentions
- **data** — 14 mentions
- **corpus** — 8 mentions
- **want** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=52|Speech and Language Processing.pdf p. 52]]

## Liens
- Up: [[research/slp/n-gram-language-models]]
- ← Prev: [[research/slp/n-grams]]
- Next: [[research/slp/evaluating-language-models-perplexity]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
