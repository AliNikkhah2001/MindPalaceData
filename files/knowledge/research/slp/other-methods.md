---
title: "Other Methods"
summary: "§II Annotating Linguistic Structure › Lexicons for Sentiment,: 22.4 • SEMI-SUPERVISED INDUCTION OF AFFECT LEXICONS then choose a node to move to with probability proportional to the edge probability."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "517-517"
---

# Other Methods

§II Annotating Linguistic Structure › Lexicons for Sentiment, Affect, and Connotation › Semi-supervised Induction of Affect Lexicons › Other Methods · pp. 517–517 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
22.4 • SEMI-SUPERVISED INDUCTION OF AFFECT LEXICONS then choose a node to move to with probability proportional to the edge probability. A word’s polarity score for a seed set is proportional to the probability of a random walk from the seed set landing on that word (Fig. 22.7). 4. Create word scores: We walk from both positive and negative seed sets, resulting in positive (rawscore+(wi)) and negative (rawscore−(wi)) raw label scores. We then combine these values into a positive-polarity score as: score+(wi) = rawscore+(wi) rawscore+(wi)+rawscore−(wi) (22.5) It’s often helpful to standardize the scores to have zero mean and unit variance within a corpus. 5. Assign confidence to each score: Because sentiment scores are influenced by the seed set, we’d like to know how much the score of a word would change if a different seed set is used. We can use bootstrap sampling to get confidence regions, by computing the propagation B times over random subsets of the positive and negative seed sets (for example using B = 50 and choosing 7 of the 10 seed words each time). The standard deviation of the bootstrap sampled polarity scores gives a confidence measure. idolize love adore appreciate li…

## Key terms
- **score** — 11 mentions
- **seed** — 11 mentions
- **word** — 9 mentions
- **positive** — 8 mentions
- **negative** — 7 mentions
- **polarity** — 5 mentions
- **rawscore** — 5 mentions
- **adjectives** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=517|Speech and Language Processing.pdf p. 517]]

## Liens
- Up: [[research/slp/semi-supervised-induction-of-affect-lexicons]]
- ← Prev: [[research/slp/label-propagation]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
