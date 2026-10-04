---
title: "Semantic Axis Methods"
summary: "§II Annotating Linguistic Structure › Lexicons for Sentiment,: 22.4 • SEMI-SUPERVISED INDUCTION OF AFFECT LEXICONS melancholy / despair? Which of the four words below is associated with the LEAST happiness / pleasure / positiveness / satisfaction / contentedness / hopefulness OR "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "515-515"
---

# Semantic Axis Methods

§II Annotating Linguistic Structure › Lexicons for Sentiment, Affect, and Connotation › Semi-supervised Induction of Affect Lexicons › Semantic Axis Methods · pp. 515–515 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
22.4 • SEMI-SUPERVISED INDUCTION OF AFFECT LEXICONS melancholy / despair? (Four words listed as options.) Q2. Which of the four words below is associated with the LEAST happiness / pleasure / positiveness / satisfaction / contentedness / hopefulness OR MOST unhappiness / annoyance / negativeness / dissatisfaction / melancholy / despair? (Four words listed as options.) The score for each word in the lexicon is the proportion of times the item was chosen as the best (highest V/A/D) minus the proportion of times the item was chosen as the worst (lowest V/A/D). The agreement between annotations are evaluated by splithalf reliability: split the corpus in half and compute the correlations between the split-half reliability annotations in the two halves. Another common way to learn sentiment lexicons is to start from a set of seed words that define two poles of a semantic axis (words like good or bad), and then find ways to label each word w by its similarity to the two seed sets. Here we summarize two families of seed-based semi-supervised lexicon induction algorithms, axis-based and graph-based. One of the most well-known lexicon induction methods, the Turney and Littman (2003) algorithm, is given seed words like good or bad, and then for each word w to be labeled, measures both how similar it is to good and how different it is from bad.

## Key terms
- **word** — 14 mentions
- **seed** — 9 mentions
- **different** — 7 mentions
- **lexicon** — 6 mentions
- **induction** — 4 mentions
- **affect** — 4 mentions
- **good** — 4 mentions
- **algorithm** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=515|Speech and Language Processing.pdf p. 515]]

## Liens
- Up: [[research/slp/semi-supervised-induction-of-affect-lexicons]]
- Next: [[research/slp/label-propagation]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
