---
title: "Learning"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : 23.6 • A NEURAL MENTION-RANKING ALGORITHM We then compute the antecedent score for high-scoring mentions. The antecedent score c(i, j) takes as input a representation of the spans i and j, but also the elementwise sim"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "547-547"
---

# Learning

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › A neural mention-ranking algorithm › Learning · pp. 547–547 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
23.6 • A NEURAL MENTION-RANKING ALGORITHM We then compute the antecedent score for high-scoring mentions. The antecedent score c(i, j) takes as input a representation of the spans i and j, but also the elementwise similarity of the two spans to each other gi ◦gj (here ◦is element-wise multiplication). Fig. 23.6 shows the computation of the score s for the three possible antecedents of the company in the example sentence from Fig. 23.5. Figure 23.6 The computation of the score s for the three possible antecedents of the company in the example sentence from Fig. 23.5. Figure after Lee et al. (2017b). Given the set of mentions, the joint distribution of antecedents for each document is computed in a forward pass, and we can then do transitive closure on the antecedents to create a final clustering for the document. Fig. 23.7 shows example predictions from the model, showing the attention weights, which Lee et al. (2017b) find correlate with traditional semantic heads. Note that the model gets the second example wrong, presumably because attendants and pilot likely have nearby word embeddings. Figure 23.7 Sample predictions from the Lee et al. (2017b) model, with one cluster per example, showing one correct example and one mistake.

## Key terms
- **antecedent** — 10 mentions
- **mention** — 10 mentions
- **cluster** — 5 mentions
- **gold** — 5 mentions
- **score** — 4 mentions
- **spans** — 3 mentions
- **possible** — 3 mentions
- **model** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=547|Speech and Language Processing.pdf p. 547]]

## Liens
- Up: [[research/slp/a-neural-mention-ranking-algorithm]]
- ← Prev: [[research/slp/computing-the-mention-and-antecedent-scores-m-and-c]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
