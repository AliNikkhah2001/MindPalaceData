---
title: "Automatic Evaluation"
summary: "§I Large Language Models › Machine Translation › MT Evaluatio: CHAPTER 12 • MACHINE TRANSLATION We can do the same thing to judge the second dimension, adequacy, using raters to assign scores on a scale."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "284-285"
---

# Automatic Evaluation

§I Large Language Models › Machine Translation › MT Evaluation › Automatic Evaluation · pp. 284–285 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 12 • MACHINE TRANSLATION We can do the same thing to judge the second dimension, adequacy, using raters to assign scores on a scale. If we have bilingual raters, we can give them the source sentence and a proposed target sentence, and rate, on a 5-point or 100-point scale, how much of the information in the source was preserved in the target. If we only have monolingual raters but we have a good human translation of the source text, we can give the monolingual raters the human reference translation and a target machine translation and again rate how much information is preserved. An alternative is to do ranking: give the raters a pair of candidate translations, and ask them which one ranking they prefer. Training of human raters (who are often online crowdworkers) is essential; raters without translation expertise find it difficult to separate fluency and adequacy, and so training includes examples carefully distinguishing these. Raters often disagree (source sentences may be ambiguous, raters will have different world knowledge, raters may apply scales differently). It is therefore common to remove outlier raters, and (if we use a fine-grained enough scale) normalizing raters by subtracting the mean from their scores and dividing by the variance.

## Key terms
- **translation** — 17 mentions
- **raters** — 13 mentions
- **chrf** — 13 mentions
- **unigram** — 12 mentions
- **human** — 11 mentions
- **metric** — 10 mentions
- **bigram** — 10 mentions
- **chrp** — 10 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=284|Speech and Language Processing.pdf p. 284]]

## Liens
- Up: [[research/slp/mt-evaluation]]
- ← Prev: [[research/slp/using-human-raters-to-evaluate-mt]]
- Next: [[research/slp/automatic-evaluation-embedding-based-methods]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
