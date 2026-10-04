---
title: "Computing span representations"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : 23.6 • A NEURAL MENTION-RANKING ALGORITHM It is crucial in feature-based systems to use conjunctions of features; one experiment suggested that moving from individual features in a classifier to conjunctions of multip"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "545-545"
---

# Computing span representations

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › A neural mention-ranking algorithm › Computing span representations · pp. 545–545 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
23.6 • A NEURAL MENTION-RANKING ALGORITHM It is crucial in feature-based systems to use conjunctions of features; one experiment suggested that moving from individual features in a classifier to conjunctions of multiple features increased F1 by 4 points (Lee et al., 2017a). Specific conjunctions can be designed by hand (Durrett and Klein, 2013), all pairs of features can be conjoined (Bengtson and Roth, 2008), or feature conjunctions can be learned using decision tree or random forest classifiers (Ng and Cardie 2002a, Lee et al. 2017a). Features can also be used in neural models as well. Neural systems use contextual word embeddings so don’t benefit from shallow features like string match or or mention types. However features like mention length, distance between mentions, or genre can complement neural contextual embedding models. In this section we describe the neural e2e-coref algorithms of Lee et al. (2017b) (simplified and extended a bit, drawing on Joshi et al. (2019) and others). This is a mention-ranking algorithm that considers all possible spans of text in the document, assigns a mention-score to each span, prunes the mentions based on this score, then assigns coreference links to the remaining mentions.

## Key terms
- **span** — 17 mentions
- **feature** — 8 mentions
- **mention** — 7 mentions
- **score** — 7 mentions
- **word** — 6 mentions
- **antecedent** — 6 mentions
- **neural** — 5 mentions
- **algorithm** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=545|Speech and Language Processing.pdf p. 545]]

## Liens
- Up: [[research/slp/a-neural-mention-ranking-algorithm]]
- Next: [[research/slp/computing-the-mention-and-antecedent-scores-m-and-c]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
