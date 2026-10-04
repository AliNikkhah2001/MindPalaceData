---
title: "The Mention-Rank Architecture"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : CHAPTER 23 • COREFERENCE RESOLUTION AND ENTITY LINKING • a negative instance (mi,mk) for each mk between mj and mi Thus for the anaphor she, we would choose (she, her) as the positive example and no negative examples."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "542-542"
---

# The Mention-Rank Architecture

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › Architectures for Coreference Algorithms › The Mention-Rank Architecture · pp. 542–542 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 23 • COREFERENCE RESOLUTION AND ENTITY LINKING • a negative instance (mi,mk) for each mk between mj and mi Thus for the anaphor she, we would choose (she, her) as the positive example and no negative examples. Similarly, for the anaphor the company we would choose (the company, Megabucks) as the positive example and (the company, she) (the company, the 38-year-old) (the company, her pay) and (the company, her) as negative examples. Once the classifier is trained, it is applied to each test sentence in a clustering step. For each mention i in a document, the classifier considers each of the prior i−1 mentions. In closest-first clustering (Soon et al., 2001), the classifier is run right to left (from mention i−1 down to mention 1) and the first antecedent with probability > .5 is linked to i. If no antecedent has probably > 0.5, no antecedent is selected for i. In best-first clustering, the classifier is run on all i −1 antecedents and the most probable preceding mention is chosen as the antecedent for i. The transitive closure of the pairwise relation is taken as the cluster. While the mention-pair model has the advantage of simplicity, it has two main problems. First, the classifier doesn’t directly compare candidate antecedents to each other, so it’s not trained to decide, between two likely antecedents, which one is in fact better.

## Key terms
- **mention** — 16 mentions
- **antecedent** — 14 mentions
- **classifier** — 8 mentions
- **company** — 6 mentions
- **model** — 6 mentions
- **anaphor** — 4 mentions
- **candidate** — 4 mentions
- **negative** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=542|Speech and Language Processing.pdf p. 542]]

## Liens
- Up: [[research/slp/architectures-for-coreference-algorithms]]
- ← Prev: [[research/slp/the-mention-pair-architecture]]
- Next: [[research/slp/entity-based-models]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
