---
title: "Working through an example"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES JJ NNP NNP NNP MD MD MD MD VB VB JJ JJ JJ NN NN RB RB RB RB DT DT DT DT NNP Janet will back the bill NN VB MD NN VB JJ RB NNP DT NN VB Figure 17.11"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "402-403"
---

# Working through an example

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › HMM Part-of-Speech Tagging › Working through an example · pp. 402–403 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES JJ NNP NNP NNP MD MD MD MD VB VB JJ JJ JJ NN NN RB RB RB RB DT DT DT DT NNP Janet will back the bill NN VB MD NN VB JJ RB NNP DT NN VB Figure 17.11 A sketch of the lattice for Janet will back the bill, showing the possible tags (qi) for each word and highlighting the path corresponding to the correct tag sequence through the hidden states. States (parts of speech) which have a zero probability of generating a particular word according to the B matrix (such as the probability that a determiner DT will be realized as Janet) are greyed out. vt−1(i) the previous Viterbi path probability from the previous time step ai j the transition probability from previous state qi to current state qj bj(ot) the state observation likelihood of the observation symbol ot given the current state j Let’s tag the sentence Janet will back the bill; the goal is the correct series of tags (see also Fig. 17.11): (17.20) Janet/NNP will/MD back/VB the/DT bill/NN NNP MD VB JJ NN RB DT <s> 0.2767 0.0006 0.0031 0.0453 0.0449 0.0510 0.2026 NNP 0.3777 0.0110 0.0009 0.0084 0.0584 0.0090 0.0025 MD 0.0008 0.0002 0.7968 0.0005 0.0008 0.1698 0.0041 VB…

## Key terms
- **state** — 13 mentions
- **start** — 11 mentions
- **janet** — 10 mentions
- **back** — 8 mentions
- **bill** — 7 mentions
- **word** — 7 mentions
- **probability** — 7 mentions
- **sequence** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=402|Speech and Language Processing.pdf p. 402]]

## Liens
- Up: [[research/slp/hmm-part-of-speech-tagging]]
- ← Prev: [[research/slp/the-viterbi-algorithm]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
